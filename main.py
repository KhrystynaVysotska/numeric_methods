from math import ceil
from constants import *
from chart import show_cart
from inductance_coefficients import coefficients

equations = [
    lambda time_stamp, values: (values[1] - values[2]) / C1,
    lambda time_stamp, values: (input_voltage(time_stamp) - values[0] - values[1] * R1) / inductance(
        values[1]),
    lambda time_stamp, values: (values[0] - values[2] * (R3 + R2)) / L2]


def input_voltage(time_stamp):
    number_of_half_periods = ceil(time_stamp / half_period)

    if number_of_half_periods % 2:
        return 10 / half_period * (time_stamp - (number_of_half_periods - 1) * half_period)

    return -10 * ((time_stamp - ((number_of_half_periods - 1) * half_period)) / half_period)


def output_voltage(values):
    return values[0]


def inductance(current_value):
    if abs(current_value) <= i_min:
        return L_max

    if abs(current_value) >= i_max:
        return L_min

    return coefficients[0] + coefficients[1] * abs(current_value) + coefficients[2] * (abs(current_value) ** 2) + \
           coefficients[3] * (abs(current_value) ** 3)


def get_next_values_by_runge_kutta_method(time_stamp, values, step):
    next_values = values
    for i in range(len(values)):
        value = values[i]
        K1 = step * equations[i](time_stamp, values)
        values[i] = value + 0.5 * K1
        K2 = step * equations[i](time_stamp + 0.5 * step, values)
        values[i] = value + 0.5 * K2
        K3 = step * equations[i](time_stamp + 0.5 * step, values)
        values[i] = value + K3
        K4 = step * equations[i](time_stamp + step, values)
        values[i] = value
        next_values[i] = values[i] + (K1 + 2 * (K2 + K3) + K4) / 6
    return next_values


def get_results(time_stamp, time_interval, values, step):
    time_value_pairs = dict()

    while time_stamp < time_interval:
        values = get_next_values_by_runge_kutta_method(time_stamp, values, step)
        time_stamp += step

        time_value_pairs[time_stamp] = [values[0], values[1], values[2], input_voltage(time_stamp),
                                        output_voltage(values)]
    return time_value_pairs


def main():
    time_stamp = 0
    values = [0, 0, 0]
    time_interval = number_of_periods * T
    step = T / 400

    time_value_pairs = get_results(time_stamp, time_interval, values, step)

    time_points = []
    values_u_c1 = []
    values_i_l1 = []
    values_i_l2 = []
    values_u1 = []
    values_u2 = []
    values_of_inductance = []

    i_interval = []
    i = 0
    while i <= i_max + 1:
        i_interval.append(i)
        values_of_inductance.append(inductance(i))
        i += step

    for t, v in time_value_pairs.items():
        time_points.append(t)
        values_u_c1.append(v[0])
        values_i_l1.append(v[1])
        values_i_l2.append(v[2])
        values_u1.append(v[3])
        values_u2.append(v[4])

    show_cart(time_points, values_u1, "U1", "t", "u")
    show_cart(i_interval, values_of_inductance, "L1", "i", "L")
    show_cart(time_points, values_i_l1, "i_l1", "t", "i_l1")
    show_cart(time_points, values_i_l2, "i_l2", "t", "i_l2")
    show_cart(time_points, values_u_c1, "U_C1", "t", "u")
    show_cart(time_points, values_u2, "U2", "t", "u")


if __name__ == '__main__':
    main()
