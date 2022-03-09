import numpy as np

# we need to be able to calculate the power required for a speed. This is hard because velovity is needed for f_drag
distance = 10
time_mins = 55
rider_weight = 75
frontal_area = 0.609
coef_drag = 0.7
grade = 7
weight_else = 8
coef_rolling_resistance = 0.005
air_density = 0.076537
coef_drag = 0.7
drive_losses = 4


def get_power_given_speed(
    grade: float,
    rider_weight: float,
    weight_else: float,
    coef_rolling_resistance: float,
    air_density: float,
    frontal_area: float,
    coef_drag: float,
    drive_losses: float,
    speed: float,
):

    weight_total = rider_weight + weight_else
    velocity = speed / 3.6

    f_gravity = 9.8067 * np.sinh(np.arctan(grade / 100)) * weight_total
    f_rolling = (
        9.8067
        * np.cosh(np.arctan(grade / 100))
        * weight_total
        * coef_rolling_resistance
    )
    f_drag = 0.5 * coef_drag * frontal_area * air_density * velocity**2
    f_resist = f_gravity + f_rolling + f_drag

    power = (1 - drive_losses / 100) * f_resist * velocity
    return power


# the below function is needed to calculate the power required for a speed or a particular segment. This is becuase the user will provide one power and we will calculate the speed for that segment
def converge_on_speed_given_power(target_power):

    lower, upper = target_power * 0.99, target_power * 1.01
    speed_min, speed_max = 1, 100
    speed = 1
    power = 1

    while not (power > lower and power < upper):

        if power <= lower:
            speed_min = speed
            speed = np.mean([speed, speed_max])
        if power >= upper:
            speed_max = speed
            speed = np.mean([speed, speed_min])

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

        if power >= lower and power <= upper:
            return speed


for p in range(200, 600, 5):
    print('~' * 200)
    print(p)
    speed = converge_on_speed_given_power(p)
    
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
        "speed =",
        round(speed, 2),
        "cda =",
        round(coef_drag * frontal_area, 2),
        "this rider covers",
        distance,
        "km in",
        time_mins,
        "mins"
    )

    print('~' * 200)
