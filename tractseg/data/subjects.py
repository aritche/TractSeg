
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os.path import join

from tractseg.libs.system_config import SystemConfig as C


# HCP_105
# (bad subjects removed: 994273, 937160, 885975, 788876, 713239)
# (no CA: 885975, 788876, 713239)
all_subjects_FINAL = ["992774", "991267", "987983", "984472", "983773", "979984", "978578", "965771", "965367", "959574",
                    "958976", "957974", "951457", "932554", "930449", "922854", "917255", "912447", "910241", "907656",
                    "904044", "901442", "901139", "901038", "899885", "898176", "896879", "896778", "894673", "889579",
                    "887373", "877269", "877168", "872764", "872158", "871964", "871762", "865363", "861456", "859671",
                    "857263", "856766", "849971", "845458", "837964", "837560", "833249", "833148", "826454", "826353",
                    "816653", "814649", "802844", "792766", "792564", "789373", "786569", "784565", "782561", "779370",
                    "771354", "770352", "765056", "761957", "759869", "756055", "753251", "751348", "749361", "748662",
                    "748258", "742549", "734045", "732243", "729557", "729254", "715647", "715041", "709551", "705341",
                    "704238", "702133", "695768", "690152", "687163", "685058", "683256", "680957", "679568", "677968",
                    "673455", "672756", "665254", "654754", "645551", "644044", "638049", "627549", "623844", "622236",
                    "620434", "613538", "601127", "599671", "599469"]

# HCP all (1061) (679568, 917255, 191235 removed because xtract missing)
all_subjects_HCP_all = ["100206", "130922", "147030", "162228", "177746", "196144", "211821", "305830", "413934", "558960", "654552", "763557", "882161", "100307", "116221", "131217", "147636", "162329", "178142", "196346", "211922", "307127", "414229", "559053", "654754", "765056", "884064", "100408", "116423", "131419", "147737", "162733", "178243", "196750", "212015", "308129", "415837", "559457", "656253", "765864", "885975", "100610", "116524", "148032", "162935", "178647", "196851", "212116", "308331", "419239", "561242", "656657", "766563", "886674", "101006", "116726", "131722", "148133", "163129", "178748", "196952", "212217", "309636", "421226", "561444", "657659", "767464", "887373", "101107", "117021", "131823", "148335", "163331", "178849", "197348", "212318", "310621", "422632", "561949", "660951", "769064", "888678", "101309", "117122", "131924", "148436", "163432", "178950", "212419", "311320", "424939", "562345", "770352", "889579", "101410", "117324", "132017", "148840", "163836", "179245", "197550", "212823", "314225", "429040", "562446", "663755", "771354", "891667", "101915", "132118", "148941", "164030", "179346", "197651", "213017", "316633", "432332", "565452", "664757", "773257", "894067", "102008", "117930", "133019", "149236", "164131", "198047", "213421", "316835", "433839", "566454", "665254", "774663", "894673", "102109", "118023", "133625", "149337", "164636", "179952", "198249", "213522", "317332", "436239", "567052", "667056", "779370", "894774", "102311", "118124", "133827", "149539", "164939", "180129", "198350", "214019", "318637", "436845", "567759", "668361", "896778", "102513", "118225", "133928", "149741", "165032", "180230", "198451", "214221", "320826", "441939", "567961", "671855", "782561", "896879", "102614", "118528", "134021", "149842", "180432", "198653", "214423", "321323", "445543", "568963", "672756", "783462", "898176", "102715", "118730", "134223", "150019", "165436", "180533", "198855", "214524", "322224", "448347", "569965", "673455", "784565", "899885", "102816", "118831", "134324", "165638", "180735", "199150", "214625", "325129", "449753", "570243", "675661", "786569", "901038", "103010", "118932", "134425", "150524", "165840", "180836", "199251", "214726", "329440", "453441", "571144", "677766", "788674", "901139", "103111", "119025", "134627", "150625", "165941", "180937", "199352", "217126", "329844", "453542", "571548", "677968", "788876", "901442", "103212", "119126", "134728", "150726", "166438", "181131", "199453", "217429", "330324", "454140", "572045", "789373", "902242", "103414", "119732", "134829", "150928", "166640", "181232", "199655", "219231", "333330", "456346", "573249", "679770", "792564", "904044", "103515", "119833", "135124", "151021", "167036", "181636", "199958", "220721", "334635", "459453", "573451", "680250", "792766", "905147", "103818", "120010", "135225", "151223", "167238", "182032", "200008", "336841", "461743", "576255", "680452", "792867", "907656", "104012", "120111", "135528", "151324", "167440", "182436", "200109", "221319", "339847", "462139", "578057", "680957", "793465", "908860", "104416", "120212", "135629", "151425", "167743", "182739", "200210", "223929", "341834", "463040", "578158", "683256", "800941", "910241", "104820", "120414", "135730", "151526", "182840", "200311", "224022", "342129", "465852", "579665", "685058", "802844", "910443", "105014", "120515", "135932", "151627", "168139", "183034", "200513", "227432", "346137", "467351", "579867", "686969", "803240", "911849", "105115", "120717", "136126", "151728", "168240", "183337", "200614", "227533", "346945", "468050", "580044", "687163", "804646", "912447", "105216", "136227", "151829", "168341", "183741", "200917", "228434", "348545", "469961", "580347", "688569", "809252", "105620", "121416", "136631", "151930", "168745", "185038", "201111", "231928", "349244", "473952", "580650", "810439", "917558", "105923", "121618", "136732", "152225", "168947", "185139", "201414", "233326", "350330", "475855", "580751", "690152", "810843", "919966", "106016", "121719", "136833", "152427", "169040", "185341", "201515", "236130", "351938", "479762", "581349", "692964", "812746", "922854", "106319", "137027", "152831", "185442", "237334", "352132", "480141", "581450", "693461", "814548", "923755", "106521", "121921", "137128", "153025", "169343", "185846", "201818", "238033", "352738", "481042", "583858", "693764", "814649", "926862", "106824", "122317", "137229", "153126", "169444", "185947", "202113", "353740", "481951", "694362", "815247", "927359", "107018", "122418", "137431", "153227", "169545", "186040", "202719", "239944", "355239", "485757", "585256", "695768", "816653", "929464", "122620", "137532", "153429", "169747", "186141", "202820", "245333", "486759", "585862", "698168", "818455", "930449", "107321", "122822", "137633", "153631", "169949", "186444", "203418", "246133", "492754", "586460", "700634", "818859", "932554", "107422", "123117", "137936", "153732", "170631", "186545", "248238", "356948", "495255", "587664", "701535", "820745", "933253", "107725", "123420", "138130", "153833", "170934", "186848", "203923", "248339", "358144", "497865", "588565", "702133", "937160", "108020", "123521", "138231", "153934", "204016", "249947", "360030", "499566", "589567", "704238", "825048", "942658", "108121", "123723", "138332", "154229", "171330", "187143", "204218", "250427", "361234", "500222", "590047", "705341", "825553", "943862", "108222", "123824", "138534", "154330", "171431", "187345", "204319", "250932", "361941", "506234", "592455", "706040", "825654", "947668", "108323", "123925", "138837", "154431", "171532", "187547", "204420", "251833", "362034", "510225", "594156", "707749", "826353", "951457", "108525", "124220", "139233", "154532", "171633", "187850", "204521", "255639", "365343", "510326", "597869", "709551", "826454", "952863", "108828", "124422", "139435", "154734", "188145", "204622", "255740", "366042", "512835", "598568", "713239", "827052", "109123", "124624", "139637", "154835", "172029", "188347", "205119", "256540", "366446", "513130", "599065", "715041", "828862", "955465", "124826", "139839", "154936", "172130", "188448", "205220", "257542", "368551", "513736", "599469", "715647", "832651", "957974", "109830", "125222", "140117", "155231", "172332", "188549", "205725", "257845", "368753", "516742", "599671", "715950", "833148", "958976", "110007", "125424", "140319", "155635", "172433", "188751", "205826", "257946", "371843", "517239", "601127", "720337", "833249", "959574", "110411", "125525", "140420", "155938", "172534", "189349", "206222", "263436", "376247", "518746", "604537", "723141", "835657", "962058", "110613", "126325", "140824", "156031", "172635", "189450", "206323", "268749", "377451", "519647", "609143", "724446", "837560", "965367", "111009", "126426", "140925", "156233", "172938", "189652", "206525", "268850", "378756", "519950", "725751", "837964", "965771", "111211", "126628", "141119", "156334", "173132", "190031", "206727", "270332", "378857", "520228", "611938", "727553", "841349", "966975", "111312", "141422", "156435", "173233", "206828", "274542", "379657", "521331", "727654", "843151", "969476", "111413", "127226", "141826", "156536", "173334", "191033", "206929", "275645", "380036", "522434", "613538", "728454", "844961", "970764", "111514", "127327", "156637", "173435", "207123", "280739", "381038", "523032", "614439", "729254", "845458", "971160", "111716", "127630", "142828", "157336", "173536", "191336", "207426", "280941", "381543", "524135", "615441", "729557", "849264", "972566", "112112", "127731", "143224", "157437", "173637", "191437", "281135", "382242", "525541", "615744", "731140", "849971", "973770", "112314", "127832", "143325", "157942", "173738", "191841", "208024", "283543", "385046", "529549", "616645", "732243", "852455", "978578", "112516", "127933", "143426", "158035", "173839", "191942", "208125", "284646", "385450", "529953", "617748", "856463", "979984", "112819", "128026", "158136", "173940", "192035", "208226", "285345", "386250", "530635", "618952", "734045", "856766", "983773", "112920", "128127", "143830", "158338", "174437", "192136", "208327", "285446", "387959", "531536", "620434", "856968", "984472", "113215", "144125", "158540", "174841", "192237", "208428", "286347", "389357", "531940", "622236", "735148", "857263", "987074", "113316", "128632", "144226", "158843", "175035", "192439", "208630", "286650", "390645", "536647", "737960", "859671", "987983", "128935", "144428", "159138", "175136", "192540", "209127", "287248", "391748", "540436", "623844", "742549", "861456", "989987", "113619", "129028", "144731", "159239", "175237", "192641", "209228", "289555", "392447", "541640", "626648", "744553", "865363", "990366", "113821", "129129", "144832", "159340", "175338", "192843", "209329", "290136", "392750", "541943", "627549", "867468", "991267", "113922", "129331", "144933", "159441", "175439", "193239", "293748", "393247", "545345", "627852", "748258", "869472", "992673", "114116", "145127", "159744", "175540", "193441", "209834", "295146", "393550", "547046", "628248", "748662", "870861", "992774", "114217", "175742", "193845", "209935", "297655", "394956", "548250", "633847", "749058", "871762", "993675", "114318", "129634", "145632", "159946", "176037", "194140", "210011", "298051", "395251", "549757", "634748", "749361", "871964", "994273", "114419", "129937", "145834", "160123", "176239", "194443", "210112", "298455", "395756", "550439", "635245", "751348", "872158", "995174", "114621", "130013", "146129", "160729", "176441", "194645", "210415", "299154", "395958", "552241", "638049", "751550", "872562", "996782", "114823", "130114", "146331", "160830", "176542", "194746", "210617", "299760", "397154", "644044", "753150", "872764", "130316", "146432", "160931", "176744", "194847", "211114", "300618", "397760", "553344", "644246", "753251", "873968", "115017", "130417", "146533", "161327", "176845", "195041", "211215", "300719", "397861", "555348", "645450", "756055", "877168", "115219", "130518", "146634", "161630", "177140", "195445", "211316", "303119", "401422", "555651", "645551", "757764", "877269", "115320", "130619", "146735", "161731", "177241", "195647", "211417", "303624", "406432", "555954", "647858", "759869", "878776", "115724", "130720", "146836", "161832", "177342", "195849", "211619", "304020", "406836", "557857", "760551", "878877", "115825", "130821", "146937", "162026", "177645", "195950", "211720", "304727", "412528", "558657", "654350", "761957", "880157"]

# 410 subjects - random order
all_subjects_Schizo = ['CH7912a', 'A00014804', 'A00020805', 'A00010684', 'CH8301a', 'A00014522', 'A00022915',
                       'A00001530', 'A00036451', 'A00022490', 'A00019803', 'A00020895', 'A00031788', 'A00023143',
                       'A00027787', 'A00015581', 'A00036256', 'A00019293', 'A00017294', 'CH7546a', 'A00013059',
                       'A00005037', 'A00021058', 'A00001181', 'A00009357', 'A00036403', 'A00012986', 'A00027434',
                       'CH8665b', 'A00018335', 'CH7131b', 'A00006931', 'A00017368', 'CH8853b', 'A00031429', 'A00037628',
                       'A00036330', 'A00036654', 'CH7684a', 'CH8914b', 'A00037871', 'A00021598', 'A00036405',
                       'A00019217', 'A00035915', 'CH7852a', 'A00027537', 'A00029045', 'A00003754', 'A00028189',
                       'A00024198', 'A00036238', 'CH7098a', 'A00036847', 'A00005153', 'A00012995', 'A00011655',
                       'CH1840', 'A00034092', 'CH8883a', 'A00023095', 'A00036232', 'A00037139', 'A00007745',
                       'A00030933', 'A00023243', 'A00036136', 'A00013816', 'A00035552', 'A00027978', 'CH8461a',
                       'A00024301', 'A00028404', 'A00024684', 'CH8335b', 'A00003684', 'A00025493', 'A00022592',
                       'A00014898', 'A00023800', 'A00024113', 'A00000909', 'A00019819', 'A00023246', 'A00024546',
                       'A00022509', 'A00037792', 'A00036133', 'A00016806', 'A00032885', 'A00006754', 'CH7259b',
                       'A00011115', 'A00020787', 'A00018235', 'A00017005', 'CH8701a', 'A00011415', 'A00023131',
                       'A00005936', 'A00017500', 'A00036248', 'A00036653', 'A00011739', 'A00001452', 'A00038770',
                       'A00002405', 'A00036429', 'A00003413', 'A00007401', 'A00036326', 'A00021081', 'A00022500',
                       'CH7316a', 'A00014120', 'A00036188', 'A00036657', 'CH3183', 'A00023366', 'CH8402b', 'CH5994',
                       'A00038122', 'A00018979', 'CH7668a', 'A00018145', 'A00024955', 'CH8698b', 'A00014225',
                       'A00036304', 'A00018150', 'A00000860', 'A00020630', 'A00026945', 'A00037200', 'A00019324',
                       'A00036107', 'A00015826', 'A00002198', 'A00003150', 'A00009949', 'A00018140', 'A00022729',
                       'CH7877a', 'A00015518', 'CH7496a', 'A00001243', 'A00024228', 'CH8413a', 'A00034378', 'A00028052',
                       'CH7718b', 'A00003158', 'CH7831a', 'CH8476a', 'CH7683a', 'A00022727', 'CH7193b', 'A00036458',
                       'A00037754', 'CH7781a', 'A00001271', 'CH8508a', 'A00014719', 'A00039430', 'CH7674b', 'A00018553',
                       'A00000368', 'A00035022', 'A00008015', 'A00036390', 'A00009948', 'A00016346', 'A00014887',
                       'A00023848', 'A00036366', 'A00000541', 'A00037847', 'A00019613', 'A00015272', 'A00023337',
                       'A00022837', 'CH7724b', 'A00019128', 'A00028139', 'CH8284b', 'CH8876b', 'A00024820', 'CH8926b',
                       'A00021676', 'A00021072', 'A00010443', 'CH7616b', 'A00024535', 'A00018872', 'A00028134',
                       'A00003880', 'A00019349', 'CH7317b', 'A00020883', 'A00019942', 'A00007343', 'A00027520',
                       'A00028507', 'A00027969', 'A00007946', 'A00019900', 'A00023750', 'A00036213', 'A00014636',
                       'A00037140', 'A00018370', 'A00036230', 'A00001251', 'A00020414', 'A00000865', 'CH7779b',
                       'A00028324', 'A00003162', 'A00036067', 'A00027755', 'A00036359', 'A00001048', 'A00038436',
                       'A00027616', 'A00017937', 'A00022773', 'CH7272b', 'A00018253', 'A00016646', 'CH8959a',
                       'A00013216', 'A00020984', 'A00018129', 'A00000838', 'CH8266b', 'A00036192', 'A00023120',
                       'CH8860b', 'CH8095a', 'A00015328', 'A00024663', 'A00017726', 'A00017691', 'A00039491',
                       'A00018434', 'A00022515', 'A00006942', 'A00036369', 'A00013446', 'A00004289', 'A00027839',
                       'A00036668', 'CH7562b', 'CH7814b', 'A00009160', 'A00012180', 'A00024568', 'CH7202b', 'A00028685',
                       'A00007470', 'CH8941a', 'A00010150', 'A00019612', 'A00018174', 'A00033766', 'A00036388',
                       'A00022835', 'A00036299', 'A00017147', 'A00036436', 'A00036216', 'A00009946', 'A00013663',
                       'A00009280', 'A00008203', 'A00019365', 'A00017896', 'A00017910', 'CH7353a', 'A00007409',
                       'A00018514', 'A00037145', 'A00036293', 'A00027498', 'CH7172a', 'A00025969', 'CH7510b',
                       'A00019941', 'CH8593b', 'A00034392', 'A00016723', 'A00005231', 'A00021145', 'A00036128',
                       'A00023132', 'A00036472', 'A00019139', 'A00036157', 'A00000984', 'A00000844', 'A00014590',
                       'CH8357', 'A00002480', 'A00020968', 'A00038585', 'CH7539a', 'CH7930a', 'CH8639a', 'A00015648',
                       'A00036652', 'A00036292', 'CH2917', 'CH8539b', 'A00008965', 'A00037141', 'A00014509',
                       'A00013140', 'A00008608', 'CH7059b', 'A00027827', 'CH7875b', 'A00000385', 'A00010600', 'CH7458a',
                       'CH8541b', 'A00022619', 'CH7614b', 'A00037177', 'A00022400', 'CH7264b', 'A00036247', 'A00037812',
                       'A00019343', 'A00034096', 'A00018851', 'A00021591', 'A00022687', 'CH8043b', 'A00036473',
                       'A00024953', 'A00036314', 'A00036351', 'A00026996', 'A00024372', 'A00031831', 'A00039384',
                       'A00018288', 'CH8937a', 'A00022810', 'A00037613', 'A00039190', 'A00037136', 'A00023158',
                       'CH7307a', 'A00023590', 'A00007883', 'A00036236', 'A00001853', 'A00031888', 'A00019750',
                       'A00036269', 'A00013363', 'A00024926', 'A00036276', 'CH7869b', 'A00020416', 'A00016197',
                       'A00036249', 'CH8930a', 'CH8577b', 'A00027838', 'CH8041b', 'A00021085', 'CH8559b', 'A00000828',
                       'CH8288a', 'CH8350b', 'A00028349', 'A00024959', 'A00018716', 'CH8001a', 'CH7567b', 'A00036358',
                       'A00009642', 'A00018317', 'A00018451', 'CH3098', 'A00019018', 'A00011725', 'CH8126b',
                       'A00019877', 'A00031279', 'A00026907', 'CH8033a', 'A00023330', 'A00002191', 'A00011265',
                       'A00028885', 'CH7957', 'A00018403', 'CH7944a', 'A00036455', 'A00031249', 'A00000159', 'CH7692a',
                       'A00000300', 'A00000456', 'A00014830', 'A00012767', 'A00014607']


def all_subjects_biobank_20k():
    base_path = join(C.DATA_PATH, "biobank_preproc")
    with open(join(base_path, "biobank_all_subjects_with_DWI_shuffled_xtract_complete.txt"), "r") as f:
        lines = f.read().splitlines()
    return lines


all_subjects_biobank_10 = ["1000013", "1000024", "1000036", "1000048", "1000055", "1000067", "1000072", "1000080",
                           "1000099", "1000106"]


def get_all_subjects(dataset="HCP"):
    if dataset == "HCP" or dataset == "HCP_final" or dataset == "HCP_32g":
        return all_subjects_FINAL
    elif dataset == "HCP_all":
        return all_subjects_HCP_all
    elif dataset.startswith("Schizo"):
        return all_subjects_Schizo
    elif dataset.startswith("biobank_20k"):
        return all_subjects_biobank_20k()
    elif dataset.startswith("biobank_10"):
        return all_subjects_biobank_10 * 10
    else:
        raise ValueError("Invalid dataset name")