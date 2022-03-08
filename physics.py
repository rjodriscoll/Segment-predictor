import numpy as np

grade = 9.2
weight_rider = 75
weight_else = 9
weight_total = weight_rider + weight_else
crr = 0.005 # rolling resistance
rho = 0.076537 # air density
a = 0.609 # frontal area
cd = 0.8 # coef of drag
loss_dt = 4 # drive train loss



distance = 1.78 # km 
time = (7/60)
speed = distance /time

v_kmh = speed 
v =  v_kmh / 3.6 # velocity parameter, in m/s


f_gravity = 9.8067 * np.sinh(np.arctan(grade/100)) * weight_total
f_rolling = 9.8067 * np.cosh(np.arctan(grade/100)) * weight_total * crr
f_drag = 0.5 * cd  * a * rho * v**2
f_resist = f_gravity + f_rolling + f_drag 
p_wheel = f_resist * v 
p_legs = (1 - (loss_dt/100))**-1 * (f_resist) * v

print('power =', p_legs, 'speed =', v_kmh, 'cda =', cd * a )
