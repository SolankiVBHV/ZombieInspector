from datetime import datetime
from teamsbot import WebExActions
from smartsheetFunction import ssActions
from clusterDataFetch import runner
# static stuff 
tag_column_mapping = {
"Time": 1946804609673092,
"C1-CM": 7236520691165060,
"C1-IMP1": 6450404237043588,
"C1-UC1": 4198604423358340,
"C1-UC2": 8702204050728836,
"CL1-CCX1": 539429726119812,
"C2-CM": 5043029353490308,
"C2-UC1": 2791229539805060,
"C3-CM": 7294829167175556,
"C3-IMP1": 1665329632962436,
"C3-UC1": 6168929260332932,
"C4-CM": 3917129446647684,
"C4-UC1": 8420729074018180,
"C5-CM": 1102379679541124,
"C5-UC1": 5605979306911620,
"C6-CM": 3354179493226372,
"C6-UC1": 7857779120596868,
"C7-CM": 2228279586383748,
"C7-UC1": 6731879213754244,
"C10-CM": 4480079400068996,
"C10-IMP1": 8983679027439492,
"C10-UC1": 29256330831748,
"SME-APAC": 4532855958202244,
"3C1-CM": 2281056144516996,
"3C2-CM": 6784655771887492,
"3C2-IMP": 1155156237674372,
"IN1-CM": 5658755865044868,
"IN2-CM": 3406956051359620,
"2DZ-CM": 7910555678730116,
"2DZ-IMP": 592206284253060,
"2MT-CM": 5095805911623556,
"2MT-UC": 2844006097938308,
"2OM-UC": 7347605725308804,
"2OM-CM": 1718106191095684,
"2TR-UC": 6221705818466180,
"2TR-CM": 3969906004780932,
"2ZA-CM": 8473505632151428,
"2ZA-UC": 310731307542404,
"BR2-CM": 4814330934912900,
"BR2-UC": 2562531121227652,
"EU3-UC": 7066130748598148,
"EU3-CM": 1436631214385028,
"EU3-IMP": 5940230841755524,
"HO1-IMP": 3688431028070276,
"HO1-UC": 8192030655440772,
"HO1-CM": 873681260963716,
"HO1-UC2": 5377280888334212,
"HO8-IMP": 3125481074648964,
"HO8-UC": 7629080702019460,
"HO8-CM": 1999581167806340,
"ME7-CM": 6503180795176836,
"ME7-UC": 4251380981491588,
"SM4-CM": 8754980608862084,
"SM9-CM": 169993819187076,
"2LU-UC": 4673593446557572,
"2LU-IMP": 2421793632872324,
"2LU-CM": 6925393260242820,
"2LU-UC1": 1295893726029700,
"2LU-IMP1": 5799493353400196,
"SME-US": 3547693539714948,
"MX1-CM": 8051293167085444,
"MX2-CM1": 732943772608388,
"CUC-MX1": 5236543399978884,
"CUC-MX2": 2984743586293636,
"CENT-CM-US": 7488343213664132,
"CENT-IMP-US": 1858843679451012,
"US1-CM": 6362443306821508,
"Unity-US1": 4110643493136260,
"CER-US1-US2": 8614243120506756,
"US1-CCX": 451468795897732,
"US2-CM": 4955068423268228,
"Unity-US2": 2703268609582980,
"UCCX-US2": 7206868236953476,
"US3-CM": 1577368702740356,
"Unity-US3": 6080968330110852,
"CER-US3": 3829168516425604,
"UCCX-US3": 8332768143796100,
"2BM-CM": 1014418749319044,
"CUC-2BM": 5518018376689540,
"CENT-CM-NA": 3266218563004292,
"CENT-IMP-NA": 7769818190374788
}

cluster_zombie_result = {
    "Time" : datetime.now(),
    "C1-CM" : 1,
    "C1-IMP1" : 0,
    "C1-UC1" : 0,
    "C1-UC2" : 0,
    "CL1-CCX1" : 0
}

def check_zombies_for_teams(cluster_zombie_result):
    effected_cluster = []
    for k,v in cluster_zombie_result.items():
        if k == 'Time':
            continue
        elif v > 0:
            effected_cluster.append(k)
    
    if len(effected_cluster) == 0:
        teamsObj.send_no_zombie_message()
    else:
        teamsObj.send_zombie_message(effected_cluster)

#main function called 
cluster_zombie_result_return = runner()
print(cluster_zombie_result_return)
ssObject = ssActions()
cluster_zombie_result_return['Time'] = datetime.now()
# hard coding failure for testing
# cluster_zombie_result_return['US1'] = 3
ssObject.add_row(tag_column_mapping, cluster_zombie_result_return)
teamsObj = WebExActions()
check_zombies_for_teams(cluster_zombie_result=cluster_zombie_result_return)
