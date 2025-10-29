from CoolProp.CoolProp import PropsSI
import numpy as np
import time
from multiprocessing import Pool

def main(par):
    initial_pressure = par[0]
    final_pressure = par[1]
    initial_enthalpy = par[2]
    initial_entropy = par[3]
    efficiency = par[4]
    max_turbines = par[5]
    final_results = []

    intermediate_pressures = np.linspace(final_pressure, initial_pressure, max_turbines + 1)
    intermediate_pressures = intermediate_pressures[::-1]

    h = []
    S = [initial_entropy]
    h_real = []
    index_2 = 0
    for pressure in intermediate_pressures:
        h.append(PropsSI('H', 'P', pressure, 'S',S[-1] , 'Water'))
        if index_2 == 0:
            h_real.append(initial_enthalpy)
            index_2 = 67
            continue
        h_real.append(h_real[-1] * (1 - efficiency) + efficiency * h[-1])
        S.append(PropsSI('S', 'P', pressure, 'H', h_real[-1], 'Water'))

    final_results.append(initial_enthalpy - h_real[-1])

    return final_results

def convert_atm_pascal(pressure_in_pascal):
    return pressure_in_pascal * 101_325

def convert_celsius_kelvin(temperature_in_celsius):
    return temperature_in_celsius + 273.15

if __name__ == '__main__':
    starting_time = time.time()
    p_i = convert_atm_pascal(50)
    p_f = convert_atm_pascal(0.05)
    t_i = convert_celsius_kelvin(500)
    h_i = PropsSI('H', 'P', p_i, 'T', t_i, 'Water')
    s_i = PropsSI('S', 'P', p_i, 'H', h_i , 'Water')
    eff = 0.7
    turbines = 500
    params = [(p_i, p_f, h_i, s_i, eff, m_t) for m_t in range(1, turbines + 2)]
    final_results = Pool().map(main,params)
    max_result = np.max(final_results)
    min_result = np.min(final_results)
    print(f'The difference is: {round((max_result - min_result) / 4186, 2)} kcal/kg')


    print(f'It took {time.time() - starting_time} seconds')