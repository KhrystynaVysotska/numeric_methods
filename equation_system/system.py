from constants import constants
from euler_method_for_dr_system import get_input_voltage

functions = [
    lambda timestamp, values: constants.C1_IN_FARADS * (
            get_input_voltage(timestamp) - values[2] + values[1] * constants.R2_IN_OMS) / (
                                      constants.R1_IN_OMS + constants.R2_IN_OMS),
    lambda timestamp, values: (((constants.R2_IN_OMS * (
            get_input_voltage(timestamp) - values[0] - values[1] * constants.R1_IN_OMS)) / (
                                        constants.R1_IN_OMS + constants.R2_IN_OMS)) - values[2] - values[
                                   1] * constants.R3_IN_OMS) / constants.L1_IN_HENRI,
    lambda timestamp, values: values[1] / constants.C2_IN_FARADS]
