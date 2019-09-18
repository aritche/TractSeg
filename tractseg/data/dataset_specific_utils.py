
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from tractseg.libs import img_utils


def get_correct_input_dim(Config):
    if Config.DIM == "2D":
        if Config.RESOLUTION == "1.25mm":
            input_dim = (144, 144)
        elif Config.RESOLUTION == "2mm":
            input_dim = (96, 96)
        elif Config.RESOLUTION == "2.5mm":
            input_dim = (80, 80)
    else:  # 3D
        if Config.RESOLUTION == "1.25mm":
            input_dim = (144, 144, 144)
        elif Config.RESOLUTION == "2mm":
            input_dim = (96, 96, 96)
        elif Config.RESOLUTION == "2.5mm":
            input_dim = (80, 80, 80)
    return input_dim


def get_dwi_affine(dataset, resolution):

    if dataset == "HCP" and resolution == "1.25mm":
        # shape (145,174,145)
        return np.array([[-1.25, 0.,  0.,   90.],
                         [0., 1.25,   0.,  -126.],
                         [0.,    0., 1.25, -72.],
                         [0.,    0.,  0.,   1.]])

    elif dataset == "HCP_32g" and resolution == "1.25mm":
        # shape (145,174,145)
        return np.array([[-1.25, 0.,  0.,   90.],
                         [0., 1.25,   0.,  -126.],
                         [0.,    0., 1.25, -72.],
                         [0.,    0.,  0.,   1.]])

    elif (dataset == "HCP_32g" or dataset == "HCP_2mm") and resolution == "2mm":
        # shape (90,108,90)
        return np.array([[-2., 0.,  0.,   90.],
                         [0.,  2.,  0.,  -126.],
                         [0.,  0.,  2.,  -72.],
                         [0.,  0.,  0.,   1.]])

    elif (dataset == "HCP" or dataset == "HCP_32g" or dataset == "HCP_2.5mm") and resolution == "2.5mm":
        # shape (73,87,73)
        return np.array([[-2.5, 0.,  0.,   90.],
                         [0.,  2.5,  0.,  -126.],
                         [0.,  0.,  2.5,  -72.],
                         [0.,  0.,  0.,    1.]])

    else:
        raise ValueError("No Affine defined for this dataset and resolution")


def scale_input_to_unet_shape(img4d, dataset, resolution="1.25mm"):
    """
    Scale input image to right isotropic resolution and pad/cut image to make it square to fit UNet input shape.
    This is not generic but optimised for some specific datasets.

    Args:
        img4d: (x, y, z, classes)
        dataset: HCP|HCP_32g|TRACED|Schizo
        resolution: 1.25mm|2mm|2.5mm

    Returns:
        img with dim 1mm: (144,144,144,none) or 2mm: (80,80,80,none) or 2.5mm: (80,80,80,none)
        (note: 2.5mm padded with more zeros to reach 80,80,80)
    """
    if resolution == "1.25mm":
        if dataset == "HCP":  # (145,174,145)
            # no resize needed
            return img4d[1:, 15:159, 1:]  # (144,144,144)
        elif dataset == "HCP_32g":  # (73,87,73)
            img4d = img_utils.resize_first_three_dims(img4d, zoom=2)  # (146,174,146,none)
            img4d = img4d[:-1,:,:-1]  # remove one voxel that came from upsampling   # (145,174,145)
            return img4d[1:, 15:159, 1:]  # (144,144,144)
        elif dataset == "TRACED":  # (78,93,75)
            raise ValueError("resolution '1.25mm' not supported for dataset 'TRACED'")
        elif dataset == "Schizo":  # (91,109,91)
            img4d = img_utils.resize_first_three_dims(img4d, zoom=1.60)  # (146,174,146)
            return img4d[1:145, 15:159, 1:145]                                # (144,144,144)

    elif resolution == "2mm":
        if dataset == "HCP":  # (145,174,145)
            img4d = img_utils.resize_first_three_dims(img4d, zoom=0.62)  # (90,108,90)
            return img4d[5:85, 14:94, 5:85, :]  # (80,80,80)
        elif dataset == "HCP_32g":  # (145,174,145)
            img4d = img_utils.resize_first_three_dims(img4d, zoom=0.62)  # (90,108,90)
            return img4d[5:85, 14:94, 5:85, :]  # (80,80,80)
        elif dataset == "HCP_2mm":  # (90,108,90)
            # no resize needed
            return img4d[5:85, 14:94, 5:85, :]  # (80,80,80)
        elif dataset == "TRACED":  # (78,93,75)
            raise ValueError("resolution '2mm' not supported for dataset 'TRACED'")
        elif dataset == "Schizo":  # (91,109,91)
            return img4d[:, 9:100, :]                                # (91,91,91)

    elif resolution == "2.5mm":
        if dataset == "HCP":  # (145,174,145)
            img4d = img_utils.resize_first_three_dims(img4d, zoom=0.5)  # (73,87,73,none)
            bg = np.zeros((80, 80, 80, img4d.shape[3])).astype(img4d.dtype)
            # make bg have same value as bg from original img  (this adds last dim of img4d to last dim of bg)
            bg = bg + img4d[0,0,0,:]
            bg[4:77, :, 4:77] = img4d[:, 4:84, :, :]
            return bg  # (80,80,80)
        elif dataset == "HCP_2.5mm":  # (73,87,73,none)
            # no resize needed
            bg = np.zeros((80, 80, 80, img4d.shape[3])).astype(img4d.dtype)
            # make bg have same value as bg from original img  (this adds last dim of img4d to last dim of bg)
            bg = bg + img4d[0,0,0,:]
            bg[4:77, :, 4:77] = img4d[:, 4:84, :, :]
            return bg  # (80,80,80)
        elif dataset == "HCP_32g":  # (73,87,73,none)
            bg = np.zeros((80, 80, 80, img4d.shape[3])).astype(img4d.dtype)
            # make bg have same value as bg from original img  (this adds last dim of img4d to last dim of bg)
            bg = bg + img4d[0, 0, 0, :]
            bg[4:77, :, 4:77] = img4d[:, 4:84, :, :]
            return bg  # (80,80,80)
        elif dataset == "TRACED":  # (78,93,75)
            # no resize needed
            bg = np.zeros((80, 80, 80, img4d.shape[3])).astype(img4d.dtype)
            bg = bg + img4d[0, 0, 0, :]  # make bg have same value as bg from original img
            bg[1:79, :, 3:78, :] = img4d[:, 7:87, :, :]
            return bg  # (80,80,80)


def scale_input_to_original_shape(img4d, dataset, resolution="1.25mm"):
    """
    Scale input image to original resolution and pad/cut image to make it original size.
    This is not generic but optimised for some specific datasets.

    Args:
        img4d:  (x, y, z, classes)
        dataset: HCP|HCP_32g|TRACED|Schizo
        resolution: 1.25mm|2mm|2.5mm

    Returns:
        (x_original, y_original, z_original, classes)
    """

    if resolution == "1.25mm":
        if dataset == "HCP":  # (144,144,144)
            # no resize needed
            return img_utils.pad_4d_image_left(img4d, np.array([1, 15, 1, 0]),
                                               [146, 174, 146, img4d.shape[3]], pad_value=0)  # (146, 174, 146, none)
        elif dataset == "HCP_32g":  # (144,144,144)
            # no resize needed
            return img_utils.pad_4d_image_left(img4d, np.array([1, 15, 1, 0]),
                                               [146, 174, 146, img4d.shape[3]], pad_value=0)  # (146, 174, 146, none)
        elif dataset == "TRACED":  # (78,93,75)
            raise ValueError("resolution '1.25mm' not supported for dataset 'TRACED'")
        elif dataset == "Schizo":  # (144,144,144)
            img4d = img_utils.pad_4d_image_left(img4d, np.array([1, 15, 1, 0]),
                                                [145, 174, 145, img4d.shape[3]], pad_value=0)  # (145, 174, 145, none)
            return img_utils.resize_first_three_dims(img4d, zoom=0.62)  # (91,109,91)

    elif resolution == "2mm":
        if dataset == "HCP":  # (80,80,80)
            return img_utils.pad_4d_image_left(img4d, np.array([5, 14, 5, 0]),
                                               [90, 108, 90, img4d.shape[3]], pad_value=0)  # (90, 108, 90, none)
        elif dataset == "HCP_32g":  # (80,80,80)
            return img_utils.pad_4d_image_left(img4d, np.array([5, 14, 5, 0]),
                                               [90, 108, 90, img4d.shape[3]], pad_value=0)  # (90, 108, 90, none)
        elif dataset == "HCP_2mm":  # (80,80,80)
            return img_utils.pad_4d_image_left(img4d, np.array([5, 14, 5, 0]),
                                               [90, 108, 90, img4d.shape[3]], pad_value=0)  # (90, 108, 90, none)
        elif dataset == "TRACED":  # (78,93,75)
            raise ValueError("resolution '2mm' not supported for dataset 'TRACED'")

    elif resolution == "2.5mm":
        if dataset == "HCP":  # (80,80,80)
            img4d = img_utils.pad_4d_image_left(img4d, np.array([0, 4, 0, 0]),
                                                [80, 87, 80, img4d.shape[3]], pad_value=0) # (80,87,80,none)
            return img4d[4:77,:,4:77, :] # (73, 87, 73, none)
        elif dataset == "HCP_2.5mm":  # (80,80,80)
            img4d = img_utils.pad_4d_image_left(img4d, np.array([0, 4, 0, 0]),
                                                [80, 87, 80, img4d.shape[3]], pad_value=0)  # (80,87,80,none)
            return img4d[4:77,:,4:77,:]  # (73, 87, 73, none)
        elif dataset == "HCP_32g":  # ((80,80,80)
            img4d = img_utils.pad_4d_image_left(img4d, np.array([0, 4, 0, 0]),
                                                [80, 87, 80, img4d.shape[3]], pad_value=0)  # (80,87,80,none)
            return img4d[4:77, :, 4:77, :]  # (73, 87, 73, none)
        elif dataset == "TRACED":  # (80,80,80)
            img4d = img_utils.pad_4d_image_left(img4d, np.array([0, 7, 0, 0]),
                                                [80, 93, 80, img4d.shape[3]], pad_value=0)  # (80,93,80,none)
            return img4d[1:79, :, 3:78, :]  # (78,93,75,none)
