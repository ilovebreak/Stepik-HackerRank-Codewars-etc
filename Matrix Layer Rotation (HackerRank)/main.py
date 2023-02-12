'''
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
'''

from pprint import pprint

'''
Итоговое решение
'''


# функция поворачивает всю матрицу против часовой стрелки
def rotate_anticlockwise(matrix):
    m, n = len(matrix), len(matrix[0])
    new_matrix = [[0] * m for _ in range(n)]
    coordinates = list(zip(list(range(n)[::-1]), list(range(n))))
    for j in range(m):
        for x, y in coordinates:
            new_matrix[x][j] = matrix[j][y]
    return new_matrix


# функция разбирает матрицу по слоям (1 слой - внешний контур, 2 - на один ближе к центру и т.д.)
def matrix_to_layers(matrix):
    m, n = len(matrix), len(matrix[0])
    number_of_layers = min(m, n) // 2
    layers = [[] for _ in range(number_of_layers)]
    for _ in range(4):
        x, y = 0, len(matrix[0]) - 1
        for i, layer in enumerate(layers):
            layer += matrix[i][x:y]
            x += 1
            y -= 1
        matrix = rotate_anticlockwise(matrix)
    return layers


# функция собирает матрицу из слоев
def layers_to_matrix(layers, m, n):
    matrix = [[0] * n for _ in range(m)]
    for _ in range(4):
        x, y, z = 0, len(matrix[0]) - 1, len(matrix[0]) - 1
        for i, layer in enumerate(layers):
            matrix[i][x:y] = layer[:z]
            layers[i] = layer[z:]
            x += 1
            y -= 1
            z -= 2
        matrix = rotate_anticlockwise(matrix)
    return matrix


# функция сдвигает слои на заданное количество символов r
def move_symbols_inside_layers_r_times(layers, r):
    new_layers = []
    for layer in layers:
        moves = r % len(layer)
        new_layers.append(layer[moves:] + layer[:moves])
    return new_layers


# основная функция решения задачи
def move_left_by_symbol_r_times(matrix, m, n, r):
    layers = matrix_to_layers(matrix)
    new_layers = move_symbols_inside_layers_r_times(layers, r)
    # new_list = sum(new_layers, [])
    # new_matrix = list_to_matrix_by_spiral(new_list, m, n)
    new_matrix = layers_to_matrix(new_layers, m, n)
    return new_matrix


# m, n, r = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# print(matrix)

# m, n, r = 300, 300, 999999999
#
# # заполняем матрицу числами от 1 до m*n
# lst = list(range(1, m * n + 1))
# matrix = []
# while lst:
#     matrix.append(lst[:n])
#     lst = lst[n:]
# pprint(matrix)

m, n, r = 10, 8, 40
# matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
#           [9, 10, 11, 12, 13, 14, 15, 16],
#           [17, 18, 19, 20, 21, 22, 23, 24],
#           [25, 26, 27, 28, 29, 30, 31, 32],
#           [33, 34, 35, 36, 37, 38, 39, 40],
#           [41, 42, 43, 44, 45, 46, 47, 48],
#           [49, 50, 51, 52, 53, 54, 55, 56],
#           [57, 58, 59, 60, 61, 62, 63, 64],
#           [65, 66, 67, 68, 69, 70, 71, 72],
#           [73, 74, 75, 76, 77, 78, 79, 80]]
#
matrix = [[9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
          [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371],
          [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748],
          [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864],
          [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840],
          [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798],
          [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547],
          [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362],
          [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021],
          [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]]
# expected:
# 93754371 53195748 90198864 91644840 32720798 35319547 89653362 50410021
# 31785927 25289229 10844931 97945481 5270000 69622764 27762534 43779176
# 73470430 90786953 42430633 96642353 88915819 85669747 26629304 86544343
# 38021292 22590518 90502426 67042516 54688734 32589026 75398396 61983443
# 21884498 54702481 17112485 5932542 29446517 2218936 71783860 7071172
# 85388216 71197978 15654690 58592832 49558405 6331115 10329789 56239301
# 5103628 47265349 54630910 56425665 23544383 86523163 96382322 27353496
# 60013003 63729346 51189 1408833 34699742 38446081 71055337 31297360
# 9718805 38615864 92837327 6967117 17741775 96087879 30247265 9392211
# 69999937 79943507 79354991 84146680 58623600 49469904 20888810 55349226


# вывод результата
for line in move_left_by_symbol_r_times(matrix, m, n, r):
    print(*line)

'''
Функции, которые родились в процессе решения и в итоге не пригодились
'''


# функция "разворачивает" матрицу по спирали
def matrix_to_list_by_spiral(matrix):
    result = matrix.pop(0)
    while matrix:
        matrix = rotate_anticlockwise(matrix)
        result += matrix.pop(0)

    return result


# функция "сворачивает" список в матрицу размером m * n по спирали
def list_to_matrix_by_spiral(lst, m, n):
    matrix = [['*'] * n for _ in range(m)]
    row = 0
    rotate_count = 0
    while lst:
        for i in range(len(matrix[0])):
            if matrix[row][i] == '*':
                matrix[row][i] = lst.pop(0)
        matrix = rotate_anticlockwise(matrix)
        rotate_count += 1
        if rotate_count % 4 == 0:
            row += 1
    if rotate_count % 4 != 0:
        matrix = rotate_anticlockwise(matrix)
    return matrix
