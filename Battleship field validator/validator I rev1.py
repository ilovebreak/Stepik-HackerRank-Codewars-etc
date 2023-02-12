'''
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
'''

field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def add_frame(field):
    for line in field:
        line.insert(0, 0)
        line.append(0)
    field.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    return field


def check_neighbours(field, *ship):
    neighbours = []
    for coordinates in ship:
        for i, j in coordinates:
            neighbours.extend(
                [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                 (i + 1, j + 1)])
    neighbours = set(neighbours) - set(*ship)
    # print(neighbours)

    return all(field[i][j] == 0 for i, j in neighbours)


def find_battleship(field):
    battleship = []
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] == 1 and field[i + 1][j] == 1 and field[i + 2][j] == 1 and field[i + 3][j] == 1:
                battleship = [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]
            if field[i][j] == 1 and field[i][j + 1] == 1 and field[i][j + 2] == 1 and field[i][j + 3] == 1:
                battleship = [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]
    return battleship


def find_cruiser(field):
    cruiser = []
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] == 1 and field[i + 1][j] == 1 and field[i + 2][j] == 1:
                cruiser = [(i, j), (i + 1, j), (i + 2, j)]
            if field[i][j] == 1 and field[i][j + 1] == 1 and field[i][j + 2] == 1:
                cruiser = [(i, j), (i, j + 1), (i, j + 2)]
    return cruiser


def find_destroyer(field):
    destroyer = []
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] == 1 and field[i + 1][j] == 1:
                destroyer = [(i, j), (i + 1, j)]
            if field[i][j] == 1 and field[i][j + 1] == 1:
                destroyer = [(i, j), (i, j + 1)]
    return destroyer


def find_submarine(field):
    submarine = []
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] == 1:
                submarine = [(i, j)]
            if field[i][j] == 1 and field[i][j + 1] == 1:
                submarine = [(i, j)]
    return submarine


def validate_battlefield(field):
    add_frame(field)

    battleship1 = find_battleship(field)
    if not battleship1 or not check_neighbours(field, battleship1):
        return False
    for i, j in battleship1:
        field[i][j] = 0
    battleship2 = find_battleship(field)
    if battleship2:
        return False

    cruiser1 = find_cruiser(field)
    valid_cruiser1 = check_neighbours(field, cruiser1)
    for i, j in cruiser1:
        field[i][j] = 0
    cruiser2 = find_cruiser(field)
    valid_cruiser2 = check_neighbours(field, cruiser2)
    if not (cruiser1 and cruiser2) or not (valid_cruiser1 and valid_cruiser2):
        return False
    for i, j in cruiser2:
        field[i][j] = 0
    cruiser3 = find_cruiser(field)
    if cruiser3:
        return False

    destroyer1 = find_destroyer(field)
    valid_destroyer1 = check_neighbours(field, destroyer1)
    for i, j in destroyer1:
        field[i][j] = 0
    destroyer2 = find_destroyer(field)
    valid_destroyer2 = check_neighbours(field, destroyer2)
    for i, j in destroyer2:
        field[i][j] = 0
    destroyer3 = find_destroyer(field)
    valid_destroyer3 = check_neighbours(field, destroyer3)
    for i, j in destroyer3:
        field[i][j] = 0
    if not (destroyer1 and destroyer2 and destroyer3) or not (
            valid_destroyer1 and valid_destroyer2 and valid_destroyer3):
        return False
    destroyer4 = find_destroyer(field)
    if destroyer4:
        return False

    submarine1 = find_submarine(field)
    valid_submarine1 = check_neighbours(field, submarine1)
    for i, j in submarine1:
        field[i][j] = 0
    submarine2 = find_submarine(field)
    valid_submarine2 = check_neighbours(field, submarine2)
    for i, j in submarine2:
        field[i][j] = 0
    submarine3 = find_submarine(field)
    valid_submarine3 = check_neighbours(field, submarine3)
    for i, j in submarine3:
        field[i][j] = 0
    submarine4 = find_submarine(field)
    valid_submarine4 = check_neighbours(field, submarine4)
    for i, j in submarine4:
        field[i][j] = 0
    if not (submarine1 and submarine2 and submarine3 and submarine4) or not (
            valid_submarine1 and valid_submarine2 and valid_submarine3 and valid_submarine4):
        return False
    submarine5 = find_submarine(field)
    if submarine5:
        return False

    return True


# battleship = [(1, 1), (2, 1), (3, 1), (4, 1)]
# print(find_battleship(field))
# print(check_neighbours(add_frame(field), battleship))
print(validate_battlefield(field))
