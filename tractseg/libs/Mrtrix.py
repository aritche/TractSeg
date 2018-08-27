# Copyright 2017 Division of Medical Image Computing, German Cancer Research Center (DKFZ)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from os.path import join
from tractseg.libs.FiberUtils import FiberUtils
import nibabel as nib

class Mrtrix():

    @staticmethod
    def create_brain_mask(input_file, output_dir):
        print("Creating brain mask...")

        # os.system("export FSLDIR=/usr/local/fsl")
        # os.system("export PATH=$FSLDIR/bin:$PATH")
        os.system("export PATH=/usr/local/fsl/bin:$PATH")

        input_dir = os.path.dirname(input_file)
        input_file_without_ending = os.path.basename(input_file).split(".")[0]
        os.system("bet " + join(input_dir, input_file_without_ending) + " " + output_dir + "/nodif_brain_mask.nii.gz  -f 0.3 -g 0 -m")
        os.system("rm " + output_dir + "/nodif_brain_mask.nii.gz")           #masked brain
        os.system("mv " + output_dir + "/nodif_brain_mask_mask.nii.gz " + output_dir + "/nodif_brain_mask.nii.gz")
        return join(output_dir, "nodif_brain_mask.nii.gz")

    @staticmethod
    def create_fods(input_file, output_dir, bvals, bvecs, brain_mask, csd_type):
        os.system("export PATH=/code/mrtrix3/bin:$PATH")

        if csd_type == "csd_msmt_5tt":
            # MSMT 5TT
            print("Creating peaks (1 of 4)...")
            t1_file = join(os.path.dirname(input_file), "T1w_acpc_dc_restore_brain.nii.gz")
            os.system("5ttgen fsl " + t1_file + " " + output_dir + "/5TT.mif -premasked")
            print("Creating peaks (2 of 4)...")
            os.system("dwi2response msmt_5tt " + input_file + " " + output_dir + "/5TT.mif " + output_dir + "/RF_WM.txt " +
                      output_dir + "/RF_GM.txt " + output_dir + "/RF_CSF.txt -voxels " + output_dir + "/RF_voxels.mif -fslgrad " +
                      bvecs + " " + bvals)         # multi-shell, multi-tissue
            print("Creating peaks (3 of 4)...")
            os.system("dwi2fod msmt_csd " + input_file + " " + output_dir + "/RF_WM.txt " + output_dir +
                      "/WM_FODs.mif " + output_dir + "/RF_GM.txt " + output_dir + "/GM.mif " + output_dir +
                      "/RF_CSF.txt " + output_dir + "/CSF.mif -mask " + brain_mask + " -fslgrad " + bvecs + " " + bvals)       # multi-shell, multi-tissue
            print("Creating peaks (4 of 4)...")
            os.system("sh2peaks " + output_dir + "/WM_FODs.mif " + output_dir + "/peaks.nii.gz -quiet")
        elif csd_type == "csd_msmt":
            # MSMT DHollander    (only works with msmt_csd, not with csd)
            # dhollander does not need a T1 image to estimate the response function (more recent (2016) than tournier (2013))
            print("Creating peaks (1 of 3)...")
            os.system("dwi2response dhollander -mask " + brain_mask + " " + input_file + " " + output_dir + "/RF_WM.txt " +
                      output_dir + "/RF_GM.txt " + output_dir + "/RF_CSF.txt -fslgrad " + bvecs + " " + bvals)
            print("Creating peaks (2 of 3)...")
            os.system("dwi2fod msmt_csd " + input_file + " " + output_dir + "/RF_WM.txt " + output_dir +
                      "/WM_FODs.mif -fslgrad " + bvecs + " " + bvals + " -mask " + brain_mask + "")
            print("Creating peaks (3 of 3)...")
            os.system("sh2peaks " + output_dir + "/WM_FODs.mif " + output_dir + "/peaks.nii.gz -quiet")
        elif csd_type == "csd":
            # CSD Tournier
            print("Creating peaks (1 of 3)...")
            os.system("dwi2response tournier " + input_file + " " + output_dir + "/response.txt -mask " + brain_mask +
                      " -fslgrad " + bvecs + " " + bvals + " -quiet")
            print("Creating peaks (2 of 3)...")
            os.system("dwi2fod csd " + input_file + " " + output_dir + "/response.txt " + output_dir +
                      "/WM_FODs.mif -mask " + brain_mask + " -fslgrad " + bvecs + " " + bvals + " -quiet")
            print("Creating peaks (3 of 3)...")
            os.system("sh2peaks " + output_dir + "/WM_FODs.mif " + output_dir + "/peaks.nii.gz -quiet")
        else:
            raise ValueError("'csd_type' contains invalid String")

    @staticmethod
    def track(bundle, output_dir, brain_mask, filter_by_endpoints=False):
        '''

        :param bundle:   Bundle name
        :param output_dir:
        :param brain_mask:
        :param filter_by_endpoints:     use results of endings_segmentation to filter out all fibers not endings in those regions
        :return:
        '''
        os.system("export PATH=/code/mrtrix3/bin:$PATH")
        os.system("mkdir -p " + output_dir + "/TOM_trackings")

        if filter_by_endpoints:
            beginnings_mask_ok = nib.load(output_dir + "/endings_segmentations/" + bundle + "_b.nii.gz").get_data().max() > 0
            endings_mask_ok = nib.load(output_dir + "/endings_segmentations/" + bundle + "_e.nii.gz").get_data().max() > 0

            if not beginnings_mask_ok:
                print("WARNING: tract beginnings mask of {} empty".format(bundle))

            if not endings_mask_ok:
                print("WARNING: tract endings mask of {} empty".format(bundle))

        if filter_by_endpoints and beginnings_mask_ok and endings_mask_ok:
            os.system("tckgen -algorithm FACT " +
                      output_dir + "/TOM/" + bundle + ".nii.gz " +
                      output_dir + "/TOM_trackings/" + bundle + ".tck" +
                      " -seed_image " + brain_mask +
                      " -include " + output_dir + "/endings_segmentations/" + bundle + "_b.nii.gz" +
                      " -include " + output_dir + "/endings_segmentations/" + bundle + "_e.nii.gz" +
                      " -minlength 40 -select 2000 -force -quiet")
        else:
            os.system("tckgen -algorithm FACT " +
                      output_dir + "/TOM/" + bundle + ".nii.gz " +
                      output_dir + "/TOM_trackings/" + bundle + ".tck" +
                      " -seed_image " + brain_mask +
                      " -minlength 40 -select 2000 -force -quiet")

        reference_affine  = nib.load(brain_mask).get_affine()
        FiberUtils.convert_tck_to_trk(output_dir + "/TOM_trackings/" + bundle + ".tck",
                                      output_dir + "/TOM_trackings/" + bundle + ".trk", reference_affine)
        os.system("rm -f " + output_dir + "/TOM_trackings/" + bundle + ".tck")

    @staticmethod
    def clean_up(HP):
        if not HP.KEEP_INTERMEDIATE_FILES:
            os.chdir(HP.PREDICT_IMG_OUTPUT)

            os.system("rm -f nodif_brain_mask.nii.gz")
            os.system("rm -f WM_FODs.mif")
            os.system("rm -f peaks.nii.gz")

            if HP.CSD_TYPE == "csd_msmt" or HP.CSD_TYPE == "csd_msmt_5tt":
                os.system("rm -f 5TT.mif")
                os.system("rm -f RF_WM.txt")
                os.system("rm -f RF_GM.txt")
                os.system("rm -f RF_CSF.txt")
                os.system("rm -f RF_voxels.mif")
                os.system("rm -f CSF.mif")
                os.system("rm -f GM.mif")
            else:
                os.system("rm -f response.txt")
