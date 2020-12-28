from constants import *
from gauze_method import gauze_method_by_column


def get_row_of_matrix_from_function(i):
    return [1, i, i * i, i * i * i]


def get_row_of_matrix_from_derivative_function(i):
    return [0, 1, 2 * i, 3 * i * i]


def get_inductance_coefficients():
    matrix = [get_row_of_matrix_from_function(i_min),
              get_row_of_matrix_from_function(i_max),
              get_row_of_matrix_from_derivative_function(i_min),
              get_row_of_matrix_from_derivative_function(i_max)]
    result = [L_max, L_min, 0, 0]
    return gauze_method_by_column(matrix, result)


coefficients = get_inductance_coefficients()