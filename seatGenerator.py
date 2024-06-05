seat10_chair = [['#seat_e0p7jes0g7_0_10'],
                ['#seat_e0p7jes0g7_1_8'],
                ['#seat_e0p7jes0g7_2_8'],
                ['#seat_e0p7jes0g7_3_7'],
                ['#seat_e0p7jes0g7_4_6'],
                ['#seat_e0p7jes0g7_5_6'],
                ['#seat_e0p7jes0g7_6_5'],
                ['#seat_e0p7jes0g7_7_5'],
                ['#seat_e0p7jes0g7_8_4'],
                ['#seat_e0p7jes0g7_9_4'],
                ['#seat_e0p7jes0g7_10_3'],
                ['#seat_e0p7jes0g7_11_3'],
                ['#seat_e0p7jes0g7_12_2'],
                ['#seat_e0p7jes0g7_13_1'],
                ['#seat_e0p7jes0g7_14_1'],
                ['#seat_e0p7jes0g7_15_0']
                ]

seat11_chair = [['#seat_e4eimo2z0t_0_20'],
                ['#seat_e4eimo2z0t_1_18'],
                ['#seat_e4eimo2z0t_2_15'],
                ['#seat_e4eimo2z0t_3_12'],
                ['#seat_e4eimo2z0t_4_6'],
                ['#seat_e4eimo2z0t_5_5'],
                ['#seat_e4eimo2z0t_6_4'],
                ['#seat_e4eimo2z0t_7_4'],
                ['#seat_e4eimo2z0t_8_3'],
                ['#seat_e4eimo2z0t_9_3'],
                ['#seat_e4eimo2z0t_10_2'],
                ['#seat_e4eimo2z0t_11_2'],
                ['#seat_e4eimo2z0t_12_1'],
                ['#seat_e4eimo2z0t_13_0'],
                ]
seat12_chair = [['#seat_e55d9cxhbb_0_0'],
                ['#seat_e55d9cxhbb_1_0'],
                ['#seat_e55d9cxhbb_2_0'],
                ['#seat_e55d9cxhbb_3_0'],
                ['#seat_e55d9cxhbb_4_0'],
                ['#seat_e55d9cxhbb_5_0'],
                ['#seat_e55d9cxhbb_6_0'],
                ['#seat_e55d9cxhbb_7_0'],
                ['#seat_e55d9cxhbb_8_0'],
                ['#seat_e55d9cxhbb_9_0'],
                ['#seat_e55d9cxhbb_10_0']
                ]
seat28_chair = [['#seat_enq24gga74_3_3','#seat_enq24gga74_3_4','#seat_enq24gga74_3_5','#seat_enq24gga74_3_6','#seat_enq24gga74_3_7','#seat_enq24gga74_3_8',
                 '#seat_enq24gga74_3_9','#seat_enq24gga74_3_10','#seat_enq24gga74_3_11','#seat_enq24gga74_3_12','#seat_enq24gga74_3_13','#seat_enq24gga74_3_14',
                 '#seat_enq24gga74_3_15','#seat_enq24gga74_3_16','#seat_enq24gga74_3_17','#seat_enq24gga74_3_18','#seat_enq24gga74_3_19','#seat_enq24gga74_3_20',
                 '#seat_enq24gga74_3_21','#seat_enq24gga74_3_22','#seat_enq24gga74_3_23']]
seatB_chair = [['#seat_e9vlphh5bt_16_0'],
               ['#seat_e9vlphh5bt_17_0']
               ]

import re
#seat10_chair = [12,14,14,15,16,16,17,17,18,18,19,19,20,21,21,22] #공란이 있으면 수동추가할 것
seat10_chair_cnt = [11,13,13,14,15,15,16,16,17,17,18,18,19,20,20,21]
    
for i in range(len(seat10_chair_cnt)):
    text = seat10_chair[i][0]
    pattern = r'#seat_e0p7jes0g7_(\d+)_(\d+)'
    match = re.match(pattern, text)
    if match:
        start_num = int(match.group(1))
        end_num = int(match.group(2))
    for seatCnt in range(seat10_chair_cnt[i]):
        end_num += 1
        seat10_chair[i].append(f'#seat_e0p7jes0g7_{start_num}_{end_num}')
##########################################################################
seat11_chair_cnt = [1,3,6,9,13,16,17,17,18,18,19,19,20,21]
for i in range(len(seat11_chair_cnt)):
    text = seat11_chair[i][0]
    pattern = r'#seat_e4eimo2z0t_(\d+)_(\d+)'
    match = re.match(pattern, text)
    if match:
        start_num = int(match.group(1))
        end_num = int(match.group(2))
    for seatCnt in range(seat11_chair_cnt[i]):
        end_num += 1
        seat11_chair[i].append(f'#seat_e4eimo2z0t_{start_num}_{end_num}')
##########################################################################
seat12_chair_cnt = [4,9,16,17,17,18,19,19,20,20,21]
for i in range(len(seat12_chair_cnt)):
    text = seat12_chair[i][0]
    pattern = r'#seat_e55d9cxhbb_(\d+)_(\d+)'
    match = re.match(pattern, text)
    if match:
        start_num = int(match.group(1))
        end_num = int(match.group(2))
    for seatCnt in range(seat12_chair_cnt[i]):
        end_num += 1
        seat12_chair[i].append(f'#seat_e55d9cxhbb_{start_num}_{end_num}')

##########################################################################
seatB_chair_cnt = [48,48]
for i in range(len(seatB_chair_cnt)):
    text = seatB_chair[i][0]
    pattern = r'#seat_e9vlphh5bt_(\d+)_(\d+)'
    match = re.match(pattern, text)
    if match:
        start_num = int(match.group(1))
        end_num = int(match.group(2))
    for seatCnt in range(seatB_chair_cnt[i]):
        end_num += 1
        seatB_chair[i].append(f'#seat_e9vlphh5bt_{start_num}_{end_num}')

def chair10():
    return seat10_chair
def chair11():
    return seat11_chair
def chair12():
    return seat12_chair
def chairB():
    return seatB_chair 