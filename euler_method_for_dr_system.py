from constants import constants
from equation_system import system
import matplotlib.pylab as plt
from math import sin, pi


def get_input_voltage(timestamp):
    return constants.U_MAX_IN_VOLTS * sin(2 * pi * constants.FREQUENCY_IN_HERTZ * timestamp)


def get_output_voltage(values, timestamp):
    input_voltage = get_input_voltage(timestamp)
    return (constants.R2_IN_OMS * (input_voltage - values[0] - values[1] * constants.R1_IN_OMS) / (
            constants.R1_IN_OMS + constants.R2_IN_OMS)) - values[2] - values[1] * constants.R3_IN_OMS


def get_next_values(timestamp, next_timestamp, values):
    end_interval_values = [values[i] + constants.STEP * system.functions[i](timestamp, values) for i in
                           range(len(values))]
    medium_interval_values = [values[i] + 0.5 * constants.STEP * (
            system.functions[i](timestamp, values) + system.functions[i](next_timestamp, end_interval_values))
                              for i in range(len(values))]

    return medium_interval_values


def modified_euler_method(timestamp, values):
    timestamps = []
    output_voltage_values = []

    while timestamp < constants.TIME_INTERVAL_IN_SECONDS:
        next_timestamp = timestamp + constants.STEP
        next_values = get_next_values(timestamp, next_timestamp, values)

        timestamp = next_timestamp
        values = next_values

        timestamps.append(timestamp)
        output_voltage_values.append(get_output_voltage(values, timestamp))
    return timestamps, output_voltage_values


def main():
    initial_values = [0, 0, 0]
    initial_timestamp_in_seconds = 0

    timestamps, output_voltage_values = modified_euler_method(initial_timestamp_in_seconds, initial_values)

    plt.plot(timestamps, output_voltage_values)
    plt.show()


if __name__ == '__main__':
    main()
