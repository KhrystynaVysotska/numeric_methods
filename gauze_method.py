def gauze_method_by_column(matrix, result):
    initial_matrix = [row[:] for row in matrix]
    initial_result = result[:]
    final_matrix, final_result = direct_way(initial_matrix, initial_result)
    return reverse_way(final_matrix, final_result)


def direct_way(initial_matrix, initial_result):
    length = len(initial_result)
    final_result = [0 for _ in range(length)]
    final_matrix = [[0 for _ in range(length)] for _ in range(length)]
    for k in range(length):
        column_sort(initial_matrix, initial_result, k)
        final_result[k] = initial_result[k] / initial_matrix[k][k]
        for row in range(k + 1, length):
            initial_result[row] = initial_result[row] - initial_matrix[row][k] * final_result[k]
            for column in range(k + 1, length):
                final_matrix[k][column] = initial_matrix[k][column] / initial_matrix[k][k]
                initial_matrix[row][column] = initial_matrix[row][column] - initial_matrix[row][k] * final_matrix[k][
                    column]
    return final_matrix, final_result


def column_sort(initial_matrix, initial_result, k):
    length = len(initial_result)
    max_column_value = initial_matrix[k][k]
    position = k
    for column in range(k + 1, length):
        if max_column_value < abs(initial_matrix[column][k]):
            max_column_value = abs(initial_matrix[column][k])
            position = column
    initial_result[k], initial_result[position] = initial_result[position], initial_result[k]
    for d in range(length):
        initial_matrix[k][d], initial_matrix[position][d] = initial_matrix[position][d], initial_matrix[k][d]


def reverse_way(final_matrix, final_result):
    length = len(final_result)
    arguments = [0] * length
    arguments[length - 1] = final_result[length - 1]
    for i in range(length - 2, -1, -1):
        terms_sum = sum([c * x for c, x in zip(final_matrix[i][i + 1:], arguments[i + 1:])])
        arguments[i] = final_result[i] - terms_sum
    return arguments
