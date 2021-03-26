from pprint import pprint
import json
import math

pprint.sorted = lambda x, key=None: x

CAR_INPUTS = {
    "weight": 3800,
    "front_percent": 55,
    "front_arb": 20,
    "rear_arb": 20,
    "front_aero": 80,
    "power_hp": 330,
    "hp_per_ton": 0
}

MAIN_CALC = {
    "front_camber_results": 2.0,
    "front_camber_fine_tune_results": 2.0,
    "rear_camber_results": 1.6,
    "rear_camber_fine_tune_results": 1.6,
    "front_toe_results": 0.0,
    "front_toe_fine_tune_results": 0.0,
    "rear_toe_results": 0.0,
    "rear_toe_fine_tune_results": 0.0,
    "front_caster_results": 6.0,
    "front_caster_fine_tune_results": 6.0,
    "front_arb_results": 0.0,
    "front_arb_fine_tune_results": 0.0,
    "rear_arb_results": 0.0,
    "rear_arb_fine_tune_results": 0.0,
    "front_springs_results": 0.0,
    "front_springs_fine_tune_results": 0.0,
    "rear_springs_results": 0.0,
    "rear_springs_fine_tune_results": 0.0,
    "front_rebound_results": 0.0,
    "front_rebound_fine_tune_results": 0.0,
    "rear_rebound_results": 0.0,
    "rear_rebound_fine_tune_results": 0.0,
    "front_bump_results": 0.0,
    "front_bump_fine_tune_results": 0.0,
    "rear_bump_results": 0.0,
    "rear_bump_fine_tune_results": 0.0,
    "front_aero_results": 0.0,
    "front_aero_fine_tune_results": 0.0,
    "rear_aero_results": 0.0,
    "rear_aero_fine_tune_results": 0.0,
    "overall_balance": 0.0,
    "overall_balance2": 0.0,
    "spring_stiffness": 0.0,
    "front_bias": 0.0,
    "rear_bias": 0.0,
    "rear_rebound2": 0.0,
    "damper_stiffness_front": 0.0,
    "damper_stiffness_rear": 0.0,
    "anti_roll_bar_only": 0.0,
    "new_percentage_front": 0.0,
    "new_percentage_front_neg": 0.0,
    "spring_stiffness_cal_front": 0.0,
    "spring_stiffness_cal_front2": 0.0,
    "weight_cal_kg": 0.0,
    "spring_stiffness_cal_rear": 0.0,
    "spring_stiffness_cal_rear2": 0.0,
    "front_rebound": 0.0,
    "per_change_damper": 0.0,
    "front_bump": 0.0,
    "rear_bump2": 0.0,
    "front_rebound_damper": 0.0,
    "rear_rebound_damper": 0.0,
    "front_bump_damper": 0.0,
    "rear_bump_damper2": 0.0,
    "total_front_damping": 0.0,
    "total_rear_damping2": 0.0,
    "bias_rear_rebound_damper": 0.0,
    "bias_front_rebound_damper": 0.0,
    "bias_front_bump_damper": 0.0,
    "bias_rear_bump_damper2": 0.0,
    "per_rebound": 0.0,
    "front_roll_bar": 0.0,
    "rear_roll_bar": 0.0,
    "front_rear": 0.0,
    "front_rear2": 0.0,
    "result_front_rear": 0.0,
    "result_front_rear2": 0.0,
    "front_roll_bar_less": 0.0,
    "final_adjusted_ratio_top": 0.0,
    "final_adjusted_ratio_bottom": 0.0,
    "adjusted_split_rebound": 0.0,
    "adjusted_split_bump": 0.0,
    "adjusted_ratio_top_left": 0.0,
    "adjusted_ratio_top_right": 0.0,
    "adjusted_ratio_bottom_left": 0.0,
    "adjusted_ratio_bottom_right": 0.0,
    "increase_rear_damping_ratio_understeer_input2": 0.0,
    "increase_rear_damping_ratio_understeer_input2_res": 0.0,
    "decrease_rear_damping_ratio_oversteer_input2": 0.0,
    "decrease_rear_damping_ratio_oversteer_input2_res": 0.0,
    "per_rear_adjustment": 0.0,
    "rear_aero_calculations": 0.0,
    "front_aero_calculations": 0.0,
    "front_springs_calculations": 0.0,
    "rear_springs_calculations": 0.0,
    "spring_stiff_cal_front": 0.0,
    "spring_stiff_cal_rear": 0.0,
    "spring_stiff_cal_front2": 0.0,
    "spring_stiff_cal_rear2": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
}

ADJUSTMENTS = {
    "arbonlyslider": 0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
    "": 0.0,
}

UI_TEXT = {
    "arbfr": "",
    "front_rear": "",
    "front_rear2": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
}

def display_tune():
    # CAR_INPUTS['hp_per_ton'] = int(CAR_INPUTS['power_hp']/(CAR_INPUTS['weight']/2240))
    sum()
    pprint(CAR_INPUTS)
    pprint(MAIN_CALC, sort_dicts=False)

def __set_var(dest_dict, key, ftn, default):
    try:
        dest_dict[key] = ftn()
        # print(f'dest_dict: {dest_dict}, key: {key}, set value: {dest_dict[key]}, default: {default}')
    except Exception:
        dest_dict[key] = default

    return dest_dict[key]

def sum():
    num1 = CAR_INPUTS['power_hp']
    num2 = CAR_INPUTS['weight']
    num3 = CAR_INPUTS['front_percent']
    num4 = MAIN_CALC['overall_balance2']
    num5 = CAR_INPUTS['front_arb']
    num6 = CAR_INPUTS['front_aero']
    num7 = MAIN_CALC['spring_stiffness']
    num8 = MAIN_CALC['front_bias']
    num9 = MAIN_CALC['rear_bias']
    num11 = MAIN_CALC['damper_stiffness_front']
    num12 = MAIN_CALC['damper_stiffness_rear']
    num14 = MAIN_CALC['overall_balance']
    num15 = MAIN_CALC['anti_roll_bar_only']
    num16 = MAIN_CALC['new_percentage_front']
    num17 = MAIN_CALC['spring_stiffness_cal_front']
    num18 = MAIN_CALC['spring_stiffness_cal_front2']
    num19 = MAIN_CALC['weight_cal_kg']
    num20 = MAIN_CALC['spring_stiffness_cal_rear']
    num21 = MAIN_CALC['spring_stiffness_cal_rear2']
    num22 = MAIN_CALC['front_rebound']
    num23 = MAIN_CALC['per_change_damper']
    num24 = MAIN_CALC['rear_rebound2']
    num25 = MAIN_CALC['front_bump']
    num26 = MAIN_CALC['rear_bump2']
    num27 = MAIN_CALC['front_rebound_damper']
    num28 = MAIN_CALC['new_percentage_front_neg']
    num29 = MAIN_CALC['rear_rebound_damper']
    num30 = MAIN_CALC['front_bump_damper']
    num31 = MAIN_CALC['rear_bump_damper2']
    num32 = MAIN_CALC['total_front_damping']
    num33 = MAIN_CALC['total_rear_damping2']
    num34 = MAIN_CALC['bias_rear_rebound_damper']
    num35 = MAIN_CALC['bias_front_rebound_damper']
    num36 = MAIN_CALC['bias_front_bump_damper']
    num37 = MAIN_CALC['bias_rear_bump_damper2']
    num40 = MAIN_CALC['result_front_rear2']
    num41 = MAIN_CALC['result_front_rear']
    num42 = MAIN_CALC['per_rebound']

    unit = 'English'
    word2 = UI_TEXT['front_rear']
    word3 = UI_TEXT['front_rear2']

    num43nw = MAIN_CALC['final_adjusted_ratio_top']
    num44nw = MAIN_CALC['final_adjusted_ratio_bottom']
    num45nw = MAIN_CALC['adjusted_split_rebound']
    num46nw = MAIN_CALC['adjusted_split_bump']
    num47nw = MAIN_CALC['adjusted_ratio_top_left']
    num48nw = MAIN_CALC['adjusted_ratio_top_right']
    num49nw = MAIN_CALC['adjusted_ratio_bottom_left']
    num50nw = MAIN_CALC['adjusted_ratio_bottom_right']
    num51nw = MAIN_CALC['increase_rear_damping_ratio_understeer_input2']
    num52nw = MAIN_CALC['increase_rear_damping_ratio_understeer_input2_res']
    num53nw = MAIN_CALC['decrease_rear_damping_ratio_oversteer_input2']
    num54nw = MAIN_CALC['decrease_rear_damping_ratio_oversteer_input2_res']
    num55nw = MAIN_CALC['total_rear_damping2']
    num56nw = MAIN_CALC['per_rear_adjustment']

    result7_l = lambda: num16 + num15
    result7 = __set_var(ADJUSTMENTS, 'arbonlyslider', result7_l, 0) # new_percentage_front + anti_roll_bar_only

    hp_per_ton_l = lambda: int(CAR_INPUTS['power_hp']/(CAR_INPUTS['weight']/2240))
    hp_per_ton = __set_var(CAR_INPUTS, 'hp_per_ton', hp_per_ton_l, 0)

    result2_l = num3 + num4 # front_percent + overall_balance2
    result2 = __set_var(MAIN_CALC, 'new_percentage_front', result2_l, 0)
    
    result3_l = lambda: num3 + (num14 * -1) # front_percent + -overall_balance
    result3 = __set_var(MAIN_CALC, 'new_percentage_front_neg', result3_l, 0)

    result4_l = lambda: round((result7 / (100 - result7) * num5), 2) # spring_stiffness% x arb%
    result4 = __set_var(MAIN_CALC, 'rear_roll_bar', result4_l, 0)

    result5 = num5 # front_arb
    MAIN_CALC['front_roll_bar'] = result5
    MAIN_CALC['result_front_rear2'] = result5

    result6_l = lambda: round(pow(result7 / (100 - result7), -2) * num5, 2)
    result6 = __set_var(MAIN_CALC, 'front_roll_bar_less', result6_l, 0)
    
    result8 = 'Front'
    result9 = 'Rear'
    if (num16 > 50.0): # if new_percentage_front > 50
        UI_TEXT['front_rear'] = result8
    else:
        UI_TEXT['front_rear'] = result9

    if (num16 <= 50.0): # if new_percentage_front < 50
        UI_TEXT['front_rear2'] = result8
    else:
        UI_TEXT['front_rear2'] = result9

    if (num16 > 50.0):
        MAIN_CALC['result_front_rear'] = result6
    else:
        MAIN_CALC['result_front_rear'] = result4

    if (word2 == 'Front'):
        MAIN_CALC['front_arb_results'] = round(num41, 2) # result_front_rear
    else:
        MAIN_CALC['front_arb_results'] = round(num40, 2) # result_front_rear2

    if (word3 == 'Rear'):
        MAIN_CALC['rear_arb_results'] = round(num40, 2) # result_front_rear2
    else:
        MAIN_CALC['rear_arb_results'] = round(num41, 2) # result_front_rear

    result10_l = lambda: round(num22 + ((num22/100) * num23), 2)
    result10 = __set_var(MAIN_CALC, 'front_rebound_damper', result10_l, 0)

    result11_l = lambda: round(num24 + ((num24/100) * num23), 2)
    result11 = __set_var(MAIN_CALC, 'rear_rebound_damper', result11_l, 0)
    
    result12_l = lambda: round(num25 + ((num25/100) * num23), 2)
    result12 = __set_var(MAIN_CALC, 'front_bump_damper', result12_l, 0)

    result13_l = lambda: round(num26 + ((num26/100) * num23), 2)
    result13 = __set_var(MAIN_CALC, 'rear_bump_damper2', result13_l, 0)

    result14_l = lambda: round((num27/100) * num11 + num27, 2)
    result14 = __set_var(MAIN_CALC, 'bias_front_rebound_damper', result14_l, 0)
    
    result15_l = lambda: round((num29/ 100) * num12 + num29, 2)
    result15 = __set_var(MAIN_CALC, 'bias_rear_rebound_damper', result15_l, 0)

    result16_l = lambda: round((num30/100) * num11 + num30, 2)
    result16 = __set_var(MAIN_CALC, 'bias_front_bump_damper', result16_l, 0)

    result17_l = lambda: round((num31/100) * num12 + num31, 2)
    result17 = __set_var(MAIN_CALC, 'bias_rear_bump_damper2', result17_l, 0)

    result18_l = lambda: round((math.log(0.667) * (num19) * ((num28)/100) / 32 / 1.5 * -1), 2)
    result18 = __set_var(MAIN_CALC, 'total_front_damping', result18_l, 0)

    result19_l = lambda: round((math.log(0.667) * (num19) * ((100 - (num28)) / 100) / 32 / 1.5 * -1), 2)
    result19 = __set_var(MAIN_CALC, 'total_rear_damping2', result19_l, 0)

    result20_l = lambda: round(num32 / ((num42 / 100) + 1), 2)
    result20 = __set_var(MAIN_CALC, 'front_rebound', result20_l, 0)

    result21_l = lambda: round((num33 / ((num42 / 100) + 1)), 2)
    result21 = __set_var(MAIN_CALC, 'rear_rebound2', result21_l, 0)

    result22_l = lambda: round(((num42 / 100) * num22), 2)
    result22 = __set_var(MAIN_CALC, 'front_bump', result22_l, 0)
    
    result23_l = lambda: round(((num42 / 100) * num24), 2)
    result23 = __set_var(MAIN_CALC, 'rear_bump2', result23_l, 0)

    result24_l = lambda: round(num34, 1)
    result24 = __set_var(MAIN_CALC, 'rear_rebound_results', result24_l, 0)

    result25_l = lambda: round(num35, 1)
    result25 = __set_var(MAIN_CALC, 'front_rebound_results', result25_l, 0)

    result26_l = lambda: round(num36, 1)
    result26 = __set_var(MAIN_CALC, 'front_bump_results', result26_l, 0)

    result27_l = lambda: round(num37, 1)
    result27 = __set_var(MAIN_CALC, 'rear_bump_results', result27_l, 0)

    result30 = num6
    MAIN_CALC['front_aero_calculations'] = result30
   
    result28 = round(((100 - num16) / num16) * num6, 2)
    try:
        result28 = round(((100 - num16) / num16) * num6, 2)
    except Exception:
        pass

    if (num16 == 0.0):
        MAIN_CALC['rear_aero_calculations'] = 0.0
    else:
        MAIN_CALC['rear_aero_calculations'] = result28

    MAIN_CALC['front_aero_results'] = round(result30, 0)
    
    if (num16 == 0.0):
        MAIN_CALC['rear_aero_results'] = 0
    else:
        MAIN_CALC['rear_aero_results'] =round(result28, 0)

    springresult1_l = lambda: round((num19 * (result3 / 100) / 64 * 31.193), 1)
    springresult1 = __set_var(MAIN_CALC, 'front_springs_calculations', springresult1_l, 0)

    springresult2_l = lambda: round((num19 * ((100 - result3) / 100) / 64 * 31.193), 1)
    springresult2 = __set_var(MAIN_CALC, 'rear_springs_calculations', springresult2_l, 0)

    springresult3_l = lambda: ((springresult1 / 100) * num7) + springresult1
    springresult3 = __set_var(MAIN_CALC, 'spring_stiff_cal_front', springresult3_l, 0)

    springresult4_l = lambda: (num17 / 100) * num8 + num17
    springresult4 = __set_var(MAIN_CALC, 'spring_stiff_cal_rear', springresult4_l, 0)
    
    springresult5_l = lambda: (springresult2 / 100) * num7 + springresult2
    springresult5 = __set_var(MAIN_CALC, 'spring_stiff_cal_front2', springresult5_l, 0)

    springresult6_l = lambda: (num18 / 100) * num9 + num18
    springresult6 = __set_var(MAIN_CALC, 'spring_stiff_cal_rear2', springresult6_l, 0)

    if (unit == 'English'):
        MAIN_CALC['front_springs_results'] = round(num20, 1)
    elif (unit == 'Metric'):
        springresult7_l = lambda: round((springresult4) * 0.17858, 1)
        springresult7 = __set_var(MAIN_CALC, 'front_springs_results', springresult7_l, 0)

    if (unit == 'English'):
        MAIN_CALC['rear_springs_results'] = round(num21, 1)
    elif (unit == 'Metric'):
        springresult8_l = lambda: round((springresult6) * 0.17858, 1)
        springresult8 = __set_var(MAIN_CALC, 'rear_springs_results', springresult8_l, 0)

    if (num16 > 50.0):
        UI_TEXT['arbfr'] = "Rear ARB"
    else:
        UI_TEXT['arbfr'] = "Front ARB"

if __name__ == "__main__":
    print('Running manual Forza_Tune')
    display_tune()