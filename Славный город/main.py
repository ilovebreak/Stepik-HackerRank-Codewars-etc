from pprint import pprint

def deikstra(rows, matrix):
    '''
    Функция перезаписывает заданную матрицу значениями, равными расстоянию от левой верхней ячейки,
    при этом в соответствии с условием задачи (0 - это стражник) нули не перезаписываются. Все ячейки справа и
    снизу от стражника также заполняются нулями, поскольку через них искомый путь пролегать не может.
    '''
    for j in range(rows - 1):  # перезаписываем верхний ряд
        if matrix[0][j] == 0:
            matrix[0][j + 1] = 0
        elif not matrix[0][j +1] == 0:
            matrix[0][j + 1] += matrix[0][j]

    for i in range(1, rows - 1):  # перезаписываем матрицу от второго до предпоследнего ряда
        if matrix[i][0] == 0:
            matrix[i + 1][0] = 0
        elif not matrix[i][0] == 0:
            matrix[i][0] += matrix[i - 1][0]
        for j in range(1, rows):
            aim_cell = matrix[i][j]
            up_cell = matrix[i - 1][j]
            left_cell = matrix[i][j - 1]
            if not aim_cell == 0:
                if not up_cell == 0 and not left_cell == 0:
                    matrix[i][j] += min(up_cell, left_cell)
                elif up_cell == 0 and left_cell == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = aim_cell + up_cell + left_cell

    if not matrix[-1][0] == 0:
        matrix[-1][0] += matrix[-2][0]  # перезаписываем левую нижнюю ячейку

    for j in range(1, rows): # перезаписываем последний ряд
        aim_cell = matrix[-1][j]
        up_cell = matrix[-2][j]
        left_cell = matrix[-1][j - 1]
        if not aim_cell == 0:
            if not up_cell == 0 and not left_cell == 0:
                matrix[-1][j] += min(up_cell, left_cell)
            elif up_cell == 0 and left_cell == 0:
                matrix[-1][j] = 0
            else:
                matrix[-1][j] = aim_cell + up_cell + left_cell
    #
    # for j in range(rows - 1):
    #     matrix[-1][j + 1] += matrix[-1][j]
    return matrix


def next_step(rows, matrix, result):
    '''
    Функция принимает на вход result (список кортежей с координатами предыдущих ходов) и выбирает следующий ход
    по минимальному расстоянию от начала пути и записывает координаты следующего хода в result.
    Если упираемся в стражника, функция возвращает Impossible
    '''

    y, x = result[-1][0], result[-1][1]

    if y > - rows and x == -rows:
        up = matrix[y - 1][x]
        left = 0
    elif x > - rows and y == -rows:
        left = matrix[y][x - 1]
        up = 0
    else:
        up = matrix[y - 1][x]
        left = matrix[y][x - 1]

    if left == 0 and up != 0:
        result.append((y - 1, x))
    elif left != 0 and up == 0:
        result.append((y, x - 1))
    elif left == 0 and up == 0:
        return 'Impossible'
    # elif left == up:
    #     options.append(result.copy())
    #     options[-1].append((y - 1, x, up))
    #     result.append((y, x - 1, left))
    elif left > up:
        result.append((y - 1, x))
    else:
        result.append((y, x - 1))

    if result[-1][0] == -rows and result[-1][1] == -rows:
        return result


def print_way(rows, result):
    '''
    Функция принимает на вход окончательный result (список кортежей с координатами всех ходов либо Impossible) и выдает
    на печать искомую схему движения либо Impossible
    '''
    if result == 'Impossible':
        city = [['I', 'm', 'p', 'o', 's', 's', 'i', 'b', 'l', 'e']]
        print(result)
    else:
        city = [['-'] * rows for _ in range(rows)]

        for x, y in result:
                city[x][y] = '#'

        # [print(*[elem for elem in row], sep='') for row in city]
    return city

def main(rows, matrix, result):
    if matrix[-1][-1] == 0 or matrix[0][0] == 0:
        return 'Impossible'
    for _ in range(rows * 2 - 2):
        next_step(rows, matrix, result)
    return result


if __name__ == '__main__':
    rows = int(input())
    city = [[int(i) for i in list(input())] for j in range(rows)]

    result = [(-1, -1)]
    deikstra_matrix = deikstra(rows, city)
    [print(*[str(elem).ljust(3) for elem in row]) for row in deikstra_matrix]
    # print_way(main(deikstra_matrix, result))
    print(print_way(rows, main(deikstra(rows, city), result)))

