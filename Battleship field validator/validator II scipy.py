from scipy.ndimage import label, find_objects, convolve
import numpy as np


def find_ship(field, n):
    ships = []
    # seek horizontal ships
    h_field = field.tolist()
    ship = [1 for _ in range(n)]
    for k, row in enumerate(h_field):
        for i in range(len(row)):
            if row[i:n] == ship:
                for j in range(i, n):
                    h_field[k][j] = 0
                    ships.append(n)
    # seek vertical ships
    v_field = np.transpose(np.array(h_field)).tolist()
    ship = [1 for _ in range(n)]
    for k, row in enumerate(v_field):
        for i in range(len(row)):
            if row[i:n] == ship:
                for j in range(i, n):
                    h_field[k][j] = 0
                    ships.append(n)
    return n if ships else 0

    # # seek horizontal ships
    # a = len(field[0]) - 2
    # if len(field[0]) - 2 >= n:
    #     for i in range(1, len(field) - 1):
    #         for j in range(1, len(field[0] - 1 - n)):
    #             if sum([field[i][j + k] for k in range(n)]) == n:
    #                 ship = [(i, j + k) for k in range(n)]
    #                 for i, j in ship:
    #                     field[i][j] = 0
    #                 return len(ship)
    # # seek vertical ships
    # if len(field) - 2 >= n:
    #     for i in range(1, len(field) - 1 - n):
    #         for j in range(1, len(field[0])):
    #             if sum([field[i + k][j] for k in range(n)]) == n:
    #                 ship = [(i + k, j) for k in range(n)]
    #                 for i, j in ship:
    #                     field[i][j] = 0
    #                 return len(ship)
    # return 0

def validate_battlefield(field):
    field = np.array(field)
    # lbl = label(field, np.ones((3, 3)))
    # print('label1', lbl)
    # lbl = label(field)
    # print('label', lbl)
    # fo = find_objects(lbl[0])
    # for pos in fo:
    #     print(pos)
    #     ship = field[pos]
    #     print('ship', ship)
    #     print('ship.size', ship.size)
    #     print('ship.shape', ship.shape)

    ship_sizes = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    single_ships = sorted(
        ship.size for ship in (field[pos] for pos in find_objects(label(field)[0])) if min(ship.shape) == 1
    )

    not_found_sizes = sorted([size for size in ship_sizes if size not in single_ships], reverse=True)
    print(not_found_sizes)
    combined_ships = [
        ship for ship in (field[pos] for pos in find_objects(label(field)[0])) if min(ship.shape) != 1
    ]
    for array in combined_ships:
        if max(array.shape) <= max(not_found_sizes):
            # array = np.pad(array, pad_width=1, mode='constant', constant_values=0) # добавляем рамку с нулями
            for size in not_found_sizes:
                ship = find_ship(array, size)
                if ship:
                    not_found_sizes.remove(ship)
                print('ship', ship)




    return combined_ships

    # return sorted(
    #     ship.size for ship in (field[pos] for pos in find_objects(label(field)[0])) if min(ship.shape) == 1
    # )

    # return sorted(
    #     ship.size if min(ship.shape) == 1 else 0
    #     for ship in (field[pos] for pos in find_objects(label(field)[0]))
    # ) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


# field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
#          [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
## should return True

# field = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#          [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
#          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
## should return True

# field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
#          [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
#          [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# # should return False

field = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
# should return False


print(validate_battlefield(field))