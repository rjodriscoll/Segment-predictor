

for speed in range(1, 40, 1):
    print('~' * 200)

    # speed = converge_on_speed_given_power(p)
    
    power = get_power_given_speed(
        grade=grade,
        rider_weight=rider_weight,
        weight_else=weight_else,
        coef_rolling_resistance=coef_rolling_resistance,
        air_density=air_density,
        frontal_area=frontal_area,
        coef_drag=coef_drag,
        drive_losses=drive_losses,
        speed=speed,
    )
   
    time = distance/speed
    time_seconds = 60 * 60 * time 
    time_mins = time_seconds /60 
    

    print(
        "power =",
        round(power),
        "wkg =",
        round(power/rider_weight , 2),
        "speed =",
        round(speed, 5),
        "cda =",
        round(coef_drag * frontal_area, 2),
        "this rider covers",
        distance,
        "km in",
        round(time_mins,2),
        "mins"
    )

    print('~' * 200)
