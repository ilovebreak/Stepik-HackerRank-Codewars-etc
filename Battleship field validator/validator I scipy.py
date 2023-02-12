from scipy.ndimage import label, find_objects
import numpy as np


def validate_battlefield(field):
    field = np.array(field)
    # lbl = label(field, np.ones((3, 3)))
    # print('label1', lbl)
    # lbl = label(field)
    # print('label2', lbl)
    # fo = find_objects(lbl[0])
    # for pos in fo:
    #     print(pos)
    #     ship = field[pos]
    #     print('ship', ship)
    #     print('ship.size', ship.size)
    #     print('ship.shape', ship.shape)
    #
    # return sorted(
    #     ship.size for ship in (field[pos] for pos in find_objects(label(field)[0])) if min(ship.shape) == 1
    # )

    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field)[0]))
    ) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


    # return sorted(
    #     ship.size if min(ship.shape) == 1 else 0
    #     for ship in (field[pos] for pos in find_objects(label(field, np.ones((3, 3)))[0]))
    # ) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]
# should return True

print(validate_battlefield(field))
