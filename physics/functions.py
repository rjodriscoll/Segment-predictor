import numpy as np



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


def converge_on_speed_given_power(target_power:float, grade: float,
    rider_weight: float,
    weight_else: float,
    coef_rolling_resistance: float,
    air_density: float,
    frontal_area: float,
    coef_drag: float,
    drive_losses: float):

    lower, upper = target_power * 0.99, target_power * 1.01
    speed_min, speed_max = 1, 60
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

        if speed > 59 or speed < 2: 
            return speed
