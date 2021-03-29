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
    "arbonlyslider": 0,
    "increase-front-toe-out-input2": 0.0,
    "adjust_increase_front_toe_out_input2": 0.0,
    "increase_front_bump_damping_input": 0.0,
    "increase_front_toe_out_input2": 0.0,
    "adjust_increase_front_bump_damping_input2": 0.0,
    "increase_front_bump_damping_ft_res": 0.0,
    "increase_caster_angle_input2": 0.0,
    "adjust_increase_caster_angle_input2": 0.0,
    "increase_caster_angle_ft_res": 0.0,
    "increase_front_downforce_input2": 0.0,
    "adjust_increase_front_downforce_input2": 0.0,
    "increase_front_downforce_ft_res": 0.0,
    "stiffen_front_arb_input2": 0.0,
    "adjust_stiffen_front_arb_input2": 0.0,
    "stiffen_front_arb_ft_res": 0.0,
    "increase_front_spring_rate_input2": 0.0,
    "adjust_increase_front_spring_rate_input2": 0.0,
    "increase_front_spring_rate_ft_res": 0.0,
    "increase_front_bump_damping2_input2": 0.0,
    "adjust_increase_front_bump_damping2_input2": 0.0,
    "increase_front_bump_damping2_ft_res": 0.0,
    "soften_front_arb_input2": 0.0,
    "adjust_soften_front_arb_input2": 0.0,
    "soften_front_arb_ft_res": 0.0,
    "soften_front_spring_rate_input2": 0.0,
    "adjust_soften_front_spring_rate_input2": 0.0,
    "soften_front_spring_rate_ft_res": 0.0,
    "increase_front_shock_stiffness_input2": 0.0,
    "increase_front_shock_stiffness_input": 0.0,
    "adjust_increase_front_shock_stiffness_input2": 0.0,
    "increase_front_shock_stiffness_ft_res": 0.0,
    "front_bump_slider_input2": 0.0,
    "adjust_front_bump_slider_input2": 0.0,
    "front_bump_slider_input_ft_res": 0.0,
    "adjust_increase_negative_front_wheel_camber_input2": 0.0,
    "increase_negative_front_wheel_camber_input2": 0.0,
    "increase_negative_front_wheel_camber_ft_res": 0.0,
    "reduce_front_rebound_damping_input2": 0.0,
    "adjust_reduce_front_rebound_damping_input2": 0.0,
    "reduce_front_rebound_damping_ft_res": 0.0,
    "os_increase_rear_downforce_input2": 0.0,
    "adjust_os_increase_rear_downforce_input2": 0.0,
    "os_increase_rear_rebound_damping_input2": 0.0,
    "adjust_os_increase_rear_rebound_damping_input2": 0.0,
    "os_increase_rear_rebound_damping_ft_res": 0.0,
    "os_increase_rear_downforce_ft_res": 0.0,
    "os_reduce_rear_shock_stiffness_ft_res": 0.0,
    "os_reduce_rear_shock_stiffness_input": 0.0,
    "front_bump_slider2_input2": 0.0,
    "adjust_front_bump_slider2_input2": 0.0,
    "front_bump_slider2_input2_ft_res": 0.0,
    "os_increase_negative_rear_wheel_camber_input2": 0.0,
    "os_increase_negative_rear_wheel_camber_ft_res": 0.0,
    "os_increase_rear_toe_in_input2": 0.0,
    "os_increase_rear_toe_in_ft_res": 0.0,
    "os_reduce_rear_bump_damping_input2": 0.0,
    "adjust_os_reduce_rear_bump_damping_input2": 0.0,
    "os_reduce_rear_bump_damping_ft_res": 0.0,
    "adjust_increase_rear_damping_ratio_understeer_input2": 0.0,
    "adjust_decrease_rear_damping_ratio_oversteer_input2": 0.0,
    "os_increase_rear_spring_rate_input2": 0.0,
    "os_soften_rear_arb_input2": 0.0,
    "os_soften_rear_spring_rate_input2": 0.0,
    "os_reduce_rear_shock_stiffness_input2": 0.0
}

UI_TEXT = {
    "arbfr": "",
    "front_rear": "",
    "front_rear2": "",
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
    num1 = CAR_INPUTS['power_hp'] #pylint: disable=unused-variable
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
    result7 = __set_var(MAIN_CALC, 'arbonlyslider', result7_l, 0) # new_percentage_front + anti_roll_bar_only

    hp_per_ton_l = lambda: int(CAR_INPUTS['power_hp']/(CAR_INPUTS['weight']/2240))
    hp_per_ton = __set_var(CAR_INPUTS, 'hp_per_ton', hp_per_ton_l, 0) #pylint: disable=unused-variable

    result2_l = num3 + num4 # front_percent + overall_balance2
    result2 = __set_var(MAIN_CALC, 'new_percentage_front', result2_l, 0) #pylint: disable=unused-variable
    
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
    result10 = __set_var(MAIN_CALC, 'front_rebound_damper', result10_l, 0) #pylint: disable=unused-variable

    result11_l = lambda: round(num24 + ((num24/100) * num23), 2)
    result11 = __set_var(MAIN_CALC, 'rear_rebound_damper', result11_l, 0) #pylint: disable=unused-variable
    
    result12_l = lambda: round(num25 + ((num25/100) * num23), 2)
    result12 = __set_var(MAIN_CALC, 'front_bump_damper', result12_l, 0) #pylint: disable=unused-variable

    result13_l = lambda: round(num26 + ((num26/100) * num23), 2)
    result13 = __set_var(MAIN_CALC, 'rear_bump_damper2', result13_l, 0) #pylint: disable=unused-variable

    result14_l = lambda: round((num27/100) * num11 + num27, 2)
    result14 = __set_var(MAIN_CALC, 'bias_front_rebound_damper', result14_l, 0) #pylint: disable=unused-variable
    
    result15_l = lambda: round((num29/ 100) * num12 + num29, 2)
    result15 = __set_var(MAIN_CALC, 'bias_rear_rebound_damper', result15_l, 0) #pylint: disable=unused-variable

    result16_l = lambda: round((num30/100) * num11 + num30, 2)
    result16 = __set_var(MAIN_CALC, 'bias_front_bump_damper', result16_l, 0) #pylint: disable=unused-variable

    result17_l = lambda: round((num31/100) * num12 + num31, 2)
    result17 = __set_var(MAIN_CALC, 'bias_rear_bump_damper2', result17_l, 0) #pylint: disable=unused-variable

    result18_l = lambda: round((math.log(0.667) * (num19) * ((num28)/100) / 32 / 1.5 * -1), 2)
    result18 = __set_var(MAIN_CALC, 'total_front_damping', result18_l, 0) #pylint: disable=unused-variable

    result19_l = lambda: round((math.log(0.667) * (num19) * ((100 - (num28)) / 100) / 32 / 1.5 * -1), 2)
    result19 = __set_var(MAIN_CALC, 'total_rear_damping2', result19_l, 0) #pylint: disable=unused-variable

    result20_l = lambda: round(num32 / ((num42 / 100) + 1), 2)
    result20 = __set_var(MAIN_CALC, 'front_rebound', result20_l, 0) #pylint: disable=unused-variable

    result21_l = lambda: round((num33 / ((num42 / 100) + 1)), 2)
    result21 = __set_var(MAIN_CALC, 'rear_rebound2', result21_l, 0) #pylint: disable=unused-variable

    result22_l = lambda: round(((num42 / 100) * num22), 2)
    result22 = __set_var(MAIN_CALC, 'front_bump', result22_l, 0) #pylint: disable=unused-variable
    
    result23_l = lambda: round(((num42 / 100) * num24), 2)
    result23 = __set_var(MAIN_CALC, 'rear_bump2', result23_l, 0) #pylint: disable=unused-variable

    result24_l = lambda: round(num34, 1)
    result24 = __set_var(MAIN_CALC, 'rear_rebound_results', result24_l, 0) #pylint: disable=unused-variable

    result25_l = lambda: round(num35, 1)
    result25 = __set_var(MAIN_CALC, 'front_rebound_results', result25_l, 0) #pylint: disable=unused-variable

    result26_l = lambda: round(num36, 1)
    result26 = __set_var(MAIN_CALC, 'front_bump_results', result26_l, 0) #pylint: disable=unused-variable

    result27_l = lambda: round(num37, 1)
    result27 = __set_var(MAIN_CALC, 'rear_bump_results', result27_l, 0) #pylint: disable=unused-variable

    result30 = num6
    MAIN_CALC['front_aero_calculations'] = result30
   
    result28_l = lambda: round(((100 - num16) / num16) * num6, 2)
    result28 = __set_var(MAIN_CALC, 'result28', result28_l, 0)

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
    springresult3 = __set_var(MAIN_CALC, 'spring_stiff_cal_front', springresult3_l, 0) #pylint: disable=unused-variable

    springresult4_l = lambda: (num17 / 100) * num8 + num17
    springresult4 = __set_var(MAIN_CALC, 'spring_stiff_cal_rear', springresult4_l, 0)
    
    springresult5_l = lambda: (springresult2 / 100) * num7 + springresult2
    springresult5 = __set_var(MAIN_CALC, 'spring_stiff_cal_front2', springresult5_l, 0) #pylint: disable=unused-variable

    springresult6_l = lambda: (num18 / 100) * num9 + num18
    springresult6 = __set_var(MAIN_CALC, 'spring_stiff_cal_rear2', springresult6_l, 0)

    if (unit == 'English'):
        MAIN_CALC['front_springs_results'] = round(num20, 1)
    elif (unit == 'Metric'):
        springresult7_l = lambda: round((springresult4) * 0.17858, 1)
        springresult7 = __set_var(MAIN_CALC, 'front_springs_results', springresult7_l, 0) #pylint: disable=unused-variable

    if (unit == 'English'):
        MAIN_CALC['rear_springs_results'] = round(num21, 1)
    elif (unit == 'Metric'):
        springresult8_l = lambda: round((springresult6) * 0.17858, 1)
        springresult8 = __set_var(MAIN_CALC, 'rear_springs_results', springresult8_l, 0) #pylint: disable=unused-variable

    if (num16 > 50.0):
        UI_TEXT['arbfr'] = "Rear ARB"
    else:
        UI_TEXT['arbfr'] = "Front ARB"

    weightcal1 = num2
    weightcal = num2 * 2.20462

    if (unit == 'English'):
        MAIN_CALC['weight_cal_kg'] = weightcal1
    elif (unit == 'Metric'):
        MAIN_CALC['weight_cal_kg'] = weightcal
    
    if (unit == 'English'):
        UI_TEXT['weightkg'] = "LB"
        UI_TEXT['frontaerokg'] = "LB"
        UI_TEXT['frontareoreskg'] = "LB"
        UI_TEXT['frontareokgresfine'] = "LB"
        UI_TEXT['rearareoreskg'] = "LB"
        UI_TEXT['rearareokgresfine'] = "LB"
    
    if(unit == 'Metric'):
        UI_TEXT['weightkg'] = "KG"
        UI_TEXT['frontaerokg'] = "KG"
        UI_TEXT['frontareoreskg'] = "KG"
        UI_TEXT['frontareokgresfine'] = "KG"
        UI_TEXT['rearareoreskg'] = "KG"
        UI_TEXT['rearareokgresfine'] = "KG"
    
    LBIN = "LB/IN"
    kgfcm = "kgf/cm"

    if(unit == 'English'):
        UI_TEXT['frontspringskg'] = LBIN
        UI_TEXT['frontspringskgfine'] = LBIN
        UI_TEXT['rearspringskg'] = LBIN
        UI_TEXT['rearspringskgfine'] = LBIN
    
    if(unit == 'Metric'):
        UI_TEXT['rearspringskgfine'] = kgfcm
        UI_TEXT['rearspringskg'] = kgfcm
        UI_TEXT['frontspringskgfine'] = kgfcm
        UI_TEXT['frontspringskg'] = kgfcm
    
    fronttoe = MAIN_CALC['increase_front_toe_out_input2']
    finetuneunder1_l = lambda: round(fronttoe * 0.1, 1)
    finetuneunder1 = __set_var(MAIN_CALC, 'adjust_increase_front_toe_out_input2', finetuneunder1_l, 0.0)
    
    fronttoe3 = MAIN_CALC['front_toe_results']
    fronttoe4_l = lambda: round(fronttoe3 + finetuneunder1, 1)
    fronttoe4 = __set_var(MAIN_CALC, 'front_toe_fine_tune_results', fronttoe4_l, 0.0)
    MAIN_CALC['increase_front_toe_ft_res'] = fronttoe4

    frontbump = MAIN_CALC['front_bump_results']
    frontbump2 = MAIN_CALC['increase_front_bump_damping_input']
    frontbumpadj_l = lambda: round((frontbump / 20) * frontbump2, 1)
    frontbumpadj = __set_var(MAIN_CALC, 'adjust_increase_front_bump_damping_input2', frontbumpadj_l, 0.0) #pylint: disable=unused-variable

    frontbumpres = MAIN_CALC['front_rebound_results']
    finetuneentry = MAIN_CALC['adjust_increase_front_bump_damping_input2']
    finetuneentry_1 = lambda: frontbumpres + finetuneentry
    finetuneentry = __set_var(MAIN_CALC, 'increase_front_bump_damping_ft_res', finetuneentry_1, 0.0)

    casterang = MAIN_CALC['increase_caster_angle_input2']
    casterangadj_l = lambda: round(casterang * 0.2, 1)
    casterangadj = __set_var(MAIN_CALC, 'adjust_increase_caster_angle_input2', casterangadj_l, 0.0)

    caster2 = MAIN_CALC['front_caster_results']
    casterangres_l = lambda: round(caster2 + casterangadj, 1)
    casterangres = __set_var(MAIN_CALC, 'front_caster_fine_tune_results', casterangres_l, 0.0)
    MAIN_CALC['increase_caster_angle_ft_res'] = casterangres

    frontaer = MAIN_CALC['front_aero_results']
    frontaersl = MAIN_CALC['increase_front_downforce_input2']
    frontaerres_l = lambda: round((frontaer / 20) * frontaersl, 0)
    frontaerres = __set_var(MAIN_CALC, 'adjust_increase_front_downforce_input2', frontaerres_l, 0.0)

    frontaerres1_l = lambda: round((frontaerres + frontaer), 0)
    frontaerres1 = __set_var(MAIN_CALC, 'front_aero_fine_tune_results', frontaerres1_l, 0)
    MAIN_CALC['increase_front_downforce_ft_res'] = frontaerres1

    frontarb = MAIN_CALC['front_arb_results']
    frontarb1 = MAIN_CALC['stiffen_front_arb_input2']
    frontarbres_l = lambda: round(((frontarb / 10) * frontarb1), 1)
    frontarbres = __set_var(MAIN_CALC, 'adjust_stiffen_front_arb_input2', frontarbres_l, 0.0) #pylint: disable=unused-variable

    undermidarb1 = MAIN_CALC['adjust_stiffen_front_arb_input2']
    frontarbres1_l = lambda: round((frontarb + undermidarb1), 1)
    frontarbres1 = __set_var(MAIN_CALC, 'stiffen_front_arb_ft_res', frontarbres1_l, 0.0) #pylint: disable=unused-variable

    frontsp = MAIN_CALC['front_springs_results']
    frontsp1 = MAIN_CALC['increase_front_spring_rate_input2']
    frontspres_l = lambda: round(((frontsp / 20) * frontsp1), 1)
    frontspres = __set_var(MAIN_CALC, 'adjust_increase_front_spring_rate_input2', frontspres_l, 0.0)

    frontspres1_l = lambda: round((frontsp + frontspres), 1)
    frontspres1 = __set_var(MAIN_CALC, 'increase_front_spring_rate_ft_res', frontspres1_l, 0.0) #pylint: disable=unused-variable

    frontbm = MAIN_CALC['front_bump_results']
    frontbm1 = MAIN_CALC['increase_front_bump_damping2_input2']
    frontbmres_l = lambda: round((frontbm / 20) * frontbm1, 1)
    frontbmres = __set_var(MAIN_CALC, 'adjust_increase_front_bump_damping2_input2', frontbmres_l, 0.0) #pylint: disable=unused-variable

    frontbmres1 = MAIN_CALC['adjust_increase_front_bump_damping2_input2']
    frontbmres3 = MAIN_CALC['front_bump_results']
    frontbmres2_l = lambda: round(frontbmres1 + frontbmres3, 1)
    frontbmres2 = __set_var(MAIN_CALC, 'increase_front_bump_damping2_ft_res', frontbmres2_l, 0.0) #pylint: disable=unused-variable

    frontsft = MAIN_CALC['front_arb_results']
    frontsft1 = MAIN_CALC['soften_front_arb_input2']
    frontsftres_l = lambda: round((frontsft / 10) * frontsft1, 1)
    frontsftres = __set_var(MAIN_CALC, 'adjust_soften_front_arb_input2', frontsftres_l, 0.0) #pylint: disable=unused-variable

    frontsftres1 = MAIN_CALC['stiffen_front_arb_ft_res']
    frontsftres3 = MAIN_CALC['adjust_soften_front_arb_input2']
    frontsftres2_l = lambda: round(frontsftres1 + frontsftres3, 2)
    frontsftres2 = __set_var(MAIN_CALC, 'soften_front_arb_ft_res', frontsftres2_l, 0.0)
    front_arb_fine_tune_results = frontsftres2 #pylint: disable=unused-variable

    frontsftsp = MAIN_CALC['front_springs_results']
    frontsftsp1 = MAIN_CALC['soften_front_spring_rate_input2']
    frontsftspres_l = lambda: round((frontsftsp / 20) * frontsftsp1, 1)
    frontsftspres = __set_var(MAIN_CALC, 'adjust_soften_front_spring_rate_input2', frontsftspres_l, 0.0)

    frontsftspres1 = MAIN_CALC['increase_front_spring_rate_ft_res']
    frontsftspres2_l = lambda: round(frontsftspres1 + frontsftspres, 1)
    frontsftspres2 = __set_var(MAIN_CALC, 'soften_front_spring_rate_ft_res', frontsftspres2_l, 0.0)
    MAIN_CALC['front_springs_fine_tune_results'] = frontsftspres2

    frontshst = MAIN_CALC['front_rebound_results']
    frontshst1 = MAIN_CALC['increase_front_shock_stiffness_input2']
    frontshstres_l = lambda: round((frontshst / 20) * frontshst1, 1)
    frontshstres = __set_var(MAIN_CALC, 'adjust_increase_front_shock_stiffness_input2', frontshstres_l, 0.0) #pylint: disable=unused-variable

    undermid1 = MAIN_CALC['adjust_increase_front_shock_stiffness_input2']
    undermid2 = MAIN_CALC['increase_front_bump_damping_ft_res']
    frontshstres1_l = lambda: round(undermid1 + undermid2, 1)
    frontshstres1 = __set_var(MAIN_CALC, 'increase_front_shock_stiffness_ft_res', frontshstres1_l, 0.0) #pylint: disable=unused-variable

    sliderfrbm = MAIN_CALC['increase_front_shock_stiffness_input']
    sliderfrbm2_l = lambda: sliderfrbm * 2
    sliderfrbm2 = __set_var(MAIN_CALC, 'front_bump_slider_input2', sliderfrbm2_l, 0.0) #pylint: disable=unused-variable

    underst1 = MAIN_CALC['front_bump_results']
    underst2 = MAIN_CALC['front_bump_slider_input2']
    underst3_l = lambda: round((underst1 / 20) * underst2, 1)
    underst3 = __set_var(MAIN_CALC, 'adjust_front_bump_slider_input2', underst3_l, 0.0) #pylint: disable=unused-variable

    underst4 = MAIN_CALC['adjust_front_bump_slider_input2']
    underst46 = MAIN_CALC['increase_front_bump_damping2_ft_res']
    underst5_l = lambda: round(underst4 + underst46, 1)
    underst5 = __set_var(MAIN_CALC, 'front_bump_slider_input_ft_res', underst5_l, 0.0)
    MAIN_CALC['front_bump_fine_tune_results'] = underst5

    frontcamres_l = lambda: (underst9 / 5) * underst7
    frontcamres = __set_var(MAIN_CALC, 'adjust_increase_negative_front_wheel_camber_input2', frontcamres_l, 0.0)

    underst7 = MAIN_CALC['increase_negative_front_wheel_camber_input2']
    underst9 = MAIN_CALC['front_camber_results']
    frontcamres_l = lambda: (underst9 / 5) * underst7
    frontcamres = __set_var(MAIN_CALC, 'adjust_increase_negative_front_wheel_camber_input2', frontcamres_l, 0.0)

    underst8_l = lambda round:(frontcamres + underst9, 1)
    underst8 = __set_var(MAIN_CALC, 'increase_negative_front_wheel_camber_ft_res', underst8_l, 0.0)
    MAIN_CALC['front_camber_fine_tune_results'] = underst8

    underst10 = MAIN_CALC['front_rebound_results']
    underst11 = MAIN_CALC['reduce_front_rebound_damping_input2']
    underst12_l = lambda: round((underst10 / 20) * underst11, 1)
    underst12 = __set_var(MAIN_CALC, 'adjust_reduce_front_rebound_damping_input2', underst12_l, 0.0)

    underst13 = MAIN_CALC['increase_front_shock_stiffness_ft_res']
    underst14_l = lambda: round(underst13 + underst12, 1)
    underst14 = __set_var(MAIN_CALC, 'reduce_front_rebound_damping_ft_res', underst14_l, 0.0)
    MAIN_CALC['front_rebound_fine_tune_results'] = underst14

    ovrstr1 = MAIN_CALC['rear_aero_results']
    ovrstr2 = MAIN_CALC['os_increase_rear_downforce_input2']
    ovrstr3_l = lambda: round((ovrstr1 / 20) * ovrstr2, 1)
    ovrstr3 = __set_var(MAIN_CALC, 'adjust_os_increase_rear_downforce_input2', ovrstr3_l, 0.0) #pylint: disable=unused-variable

    ovrstr5 = MAIN_CALC['rear_rebound_results']
    ovrstr6 = MAIN_CALC['os_increase_rear_rebound_damping_input2']
    ovrstr7_l = lambda: round((ovrstr5 / 20) * ovrstr6, 2)
    ovrstr7 = __set_var(MAIN_CALC, 'adjust_os_increase_rear_rebound_damping_input2', ovrstr7_l, 0.0) #pylint: disable=unused-variable

    osincreasedf = MAIN_CALC['adjust_os_increase_rear_rebound_damping_input2']
    ovrstr4_l = lambda: round(osincreasedf + num43nw, 2)
    ovrstr4 = __set_var(MAIN_CALC, 'os_increase_rear_rebound_damping_ft_res', ovrstr4_l, 0.0) #pylint: disable=unused-variable

    ovrstr9 = MAIN_CALC['rear_springs_results']
    ovrstr10 = MAIN_CALC['os_increase_rear_spring_rate_input2']
    ovrstr11_l = lambda: round((ovrstr9 / 20) * ovrstr10, 1)
    ovrstr11 = __set_var(MAIN_CALC, 'adjust_os_increase_rear_spring_rate_input2', ovrstr11_l, 0.0)

    ovrstr12_l = lambda: round(ovrstr9 + ovrstr11, 1)
    ovrstr12 = __set_var(MAIN_CALC, 'os_increase_rear_spring_rate_ft_res', ovrstr12_l, 0.0) #pylint: disable=unused-variable

    ovrstr13 = MAIN_CALC['rear_arb_results']
    ovrstr14 = MAIN_CALC['os_soften_rear_arb_input2']
    ovrstr15_l = lambda: round((ovrstr13 / 10) * ovrstr14, 1)
    ovrstr15 = __set_var(MAIN_CALC, 'adjust_os_soften_rear_arb_input2', ovrstr15_l, 0.0)

    ovrstr16_l = lambda: round(ovrstr13 + ovrstr15, 2)
    ovrstr16 = __set_var(MAIN_CALC, 'os_soften_rear_arb_ft_res', ovrstr16_l, 0.0)
    MAIN_CALC['rear_arb_fine_tune_results'] = ovrstr16

    ovrstr17 = MAIN_CALC['rear_springs_results']
    ovrstr18 = MAIN_CALC['os_soften_rear_spring_rate_input2']
    ovrstr19_l = lambda: round((ovrstr17 / 20) * ovrstr18, 1)
    ovrstr19 = __set_var(MAIN_CALC, 'adjust_os_soften_rear_spring_rate_input2', ovrstr19_l, 0.0)

    ovrstr20 = MAIN_CALC['os_increase_rear_spring_rate_ft_res']
    ovrstr21_l = lambda: round(ovrstr20 + ovrstr19, 1)
    ovrstr21 = __set_var(MAIN_CALC, 'os_soften_rear_spring_rate_ft_res', ovrstr21_l, 0.0)
    MAIN_CALC['rear_springs_fine_tune_results'] = ovrstr21

    ovrstr22 = MAIN_CALC['rear_rebound_results']
    ovrstr23 = MAIN_CALC['os_reduce_rear_shock_stiffness_input2']
    ovrstr24_l = lambda: round((ovrstr22 / 20) * ovrstr23, 1)
    ovrstr24 = __set_var(MAIN_CALC, 'adjust_os_reduce_rear_shock_stiffness_input2', ovrstr24_l, 0.0) #pylint: disable=unused-variable

    downforceadj_l = lambda: round((ovrstr1 / 20) * ovrstr2, 1)
    downforceadj = __set_var(MAIN_CALC, 'adjust_os_increase_rear_downforce_input2', downforceadj_l, 0.0) #pylint: disable=unused-variable

    rearaero = MAIN_CALC['rear_aero_results']
    downadjust = MAIN_CALC['adjust_os_increase_rear_downforce_input2']
    downforceres_l = lambda: round(rearaero + downadjust, 0)
    downforceres = __set_var(MAIN_CALC, 'os_increase_rear_downforce_ft_res', downforceres_l, 0.0)
    MAIN_CALC['rear_aero_fine_tune_results'] = downforceres

    ovrstr25 = MAIN_CALC['os_increase_rear_rebound_damping_ft_res']
    ovrstr26_l = lambda: round(ovrstr25 + ovrstr24, 1)
    ovrstr26 = __set_var(MAIN_CALC, 'os_reduce_rear_shock_stiffness_ft_res', ovrstr26_l, 0.0)
    MAIN_CALC['rear_rebound_fine_tune_results'] = ovrstr26

    ovrstr27 = MAIN_CALC['os_reduce_rear_shock_stiffness_input']
    ovrstr28_l = lambda: ovrstr27 * 2
    ovrstr28 = __set_var(MAIN_CALC, 'front_bump_slider2_input2', ovrstr28_l, 0.0) #pylint: disable=unused-variable

    ovrstr29 = MAIN_CALC['rear_bump_results']
    ovrstr30 = MAIN_CALC['front_bump_slider2_input2']
    ovrstr31_l = lambda: round((ovrstr29 / 20) * ovrstr30, 1)
    ovrstr31 = __set_var(MAIN_CALC, 'adjust_front_bump_slider2_input2', ovrstr31_l, 0.0)

    ovrstr33_l = lambda: round(num44nw + ovrstr31, 1)
    ovrstr33 = __set_var(MAIN_CALC, 'front_bump_slider2_input2_ft_res', ovrstr33_l, 0.0)
    MAIN_CALC['rear_bump_fine_tune_results'] = ovrstr33

    ovrstr34 = MAIN_CALC['rear_camber_results']
    ovrstr35 = MAIN_CALC['os_increase_negative_rear_wheel_camber_input2']
    ovrstr36_l = lambda: round(ovrstr34 + ((ovrstr35 / 10) * -1), 1)
    ovrstr36 = __set_var(MAIN_CALC, 'os_increase_negative_rear_wheel_camber_ft_res', ovrstr36_l, 0.0)
    MAIN_CALC['rear_camber_fine_tune_results'] = ovrstr36

    ovrstr38 = MAIN_CALC['os_increase_rear_toe_in_input2']
    ovrstr39_l = lambda: round(ovrstr38 * 0.1, 1)
    ovrstr39 = __set_var(MAIN_CALC, 'os_increase_negative_rear_wheel_camber_ft_res', ovrstr39_l, 0.0)

    ovrstr40 = MAIN_CALC['rear_toe_results']
    ovrstr41_l = lambda: round(ovrstr40 - ovrstr39, 1)
    ovrstr41 = __set_var(MAIN_CALC, 'os_increase_rear_toe_in_ft_res', ovrstr41_l, 0.0)
    MAIN_CALC['rear_toe_fine_tune_results'] = ovrstr41

    ovrstr42 = MAIN_CALC['front_bump_results']
    ovrstr43 = MAIN_CALC['os_reduce_rear_bump_damping_input2']
    ovrstr44_l = lambda: round((ovrstr42 / 20) * ovrstr43, 1)
    ovrstr44 = __set_var(MAIN_CALC, 'adjust_os_reduce_rear_bump_damping_input2', ovrstr44_l, 0.0) #pylint: disable=unused-variable

    ovrstr45 = MAIN_CALC['front_bump_slider2_input2_ft_res']
    theotherone = MAIN_CALC['adjust_os_reduce_rear_bump_damping_input2']
    kmn = MAIN_CALC['rear_bump_results'] #pylint: disable=unused-variable
    ovrstr46_l = lambda: round(ovrstr45 + theotherone, 1)
    ovrstr46 = __set_var(MAIN_CALC, 'os_reduce_rear_bump_damping_ft_res', ovrstr46_l, 0.0)
    MAIN_CALC['rear_bump_fine_tune_results'] = ovrstr46
    
    adjustedratiotop_l = lambda: num48nw
    adjustedratiotop = __set_var(MAIN_CALC, 'final_adjusted_ratio_top', adjustedratiotop_l, 0) #pylint: disable=unused-variable

    adjustedratiobottom_l = lambda: num50nw
    adjustedratiobottom = __set_var(MAIN_CALC, 'final_adjusted_ratio_bottom', adjustedratiobottom_l, 0) #pylint: disable=unused-variable

    adjustedratiotopleft_l = lambda: round((num45nw + ((num45nw / 100) * num23)), 2)
    adjustedratiotopleft = __set_var(MAIN_CALC, 'adjusted_ratio_top_left', adjustedratiotopleft_l, 0) #pylint: disable=unused-variable

    adjustedratiotopright_l = lambda: round(((num47nw / 100) * num12 + num47nw), 2)
    adjustedratiotopright = __set_var(MAIN_CALC, 'adjusted_ratio_top_right', adjustedratiotopright_l, 0) #pylint: disable=unused-variable

    adjustedratiobottomleft_l = lambda: round((num46nw + ((num46nw / 100) * num23)), 2)
    adjustedratiobottomleft = __set_var(MAIN_CALC, 'adjusted_ratio_bottom_left', adjustedratiobottomleft_l, 0) #pylint: disable=unused-variable

    adjustedratiobottomright_l = lambda: round(((num49nw / 100) * num12 + num49nw), 2)
    adjustedratiobottomright = __set_var(MAIN_CALC, 'adjusted_ratio_bottom_right', adjustedratiobottomright_l, 0) #pylint: disable=unused-variable

    divideit = (num56nw / 100)
    addtheone = divideit + 1
    adjustedsplitrebound_l = lambda: num55nw / addtheone
    adjustedsplitrebound = __set_var(MAIN_CALC, 'adjusted_split_rebound', adjustedsplitrebound_l, 0) #pylint: disable=unused-variable

    adjustedsplitbump_l = lambda: (num56nw / 100) * num45nw
    adjustedsplitbump = __set_var(MAIN_CALC, 'adjusted_split_bump', adjustedsplitbump_l, 0) #pylint: disable=unused-variable

    rearadjustedper_l = lambda: num42 + num52nw + num54nw
    rearadjustedper = __set_var(MAIN_CALC, 'per_rear_adjustment', rearadjustedper_l, 0) #pylint: disable=unused-variable

    usreardampratio_l = lambda: num51nw * 5
    usreardampratio = __set_var(MAIN_CALC, 'adjust_increase_rear_damping_ratio_understeer_input2', usreardampratio_l, 0)
    MAIN_CALC['increase_rear_damping_ratio_understeer_input2_res'] = usreardampratio

    osreardampratio_l = lambda: num53nw * 5
    osreardampratio = __set_var(MAIN_CALC, 'adjust_decrease_rear_damping_ratio_oversteer_input2', osreardampratio_l, 0)
    MAIN_CALC['decrease_rear_damping_ratio_oversteer_input2_res'] = osreardampratio


if __name__ == "__main__":
    print('Running manual Forza_Tune')
    display_tune()