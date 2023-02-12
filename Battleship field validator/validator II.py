'''
https://www.codewars.com/kata/571ec81d7e8954ce1400014f
разница между классической задачей и этой - корабли могут примыкать друг к другу
'''

import numpy as np
import re



def find_ship(field, n):
    for i, row in enumerate(field):
        for k in range(len(row) - n + 1):
            section = row[k: k + n]
            if all(el == 1 for el in section):
                for j in range(k, k + n):
                    field[i][j] = 0
                return n
    trans_field = np.transpose(field)
    for i, row in enumerate(trans_field):
        for k in range(len(row) - n + 1):
            section = row[k: k + n]
            if all(el == 1 for el in section):
                for j in range(k, k + n):
                    field[j][i] = 0
                return n

    return 0


    #
    # if not ship:
    #     field = np.transpose(field)
    #     return horizontal_seek(field, n)[1]
    #
    # return ship


def count_ships(field):
    # ships = []
    ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    # for size in ship_sizes:
    #     ships.append(find_ship(field, size))
    ships = [find_ship(field, size) for size in ship_sizes]
    print(ships)
    return ships == ship_sizes and sum(sum(field)) == 0
    # return ships

def validate_battlefield(field):
    field1 = np.array(field)
    field2 = np.rot90(field1.copy())
    field3 = np.rot90(field2.copy())
    field4 = np.rot90(field3.copy())

    return any(func for func in
        [count_ships(field1), count_ships(field2), count_ships(field3), count_ships(field4)]
    )


	# print(field)
	# trans_field = np.transpose(field)
	# horizontals = ','.join([''.join(map(str, row)) for row in field])
	# verticals = ','.join([''.join(map(str, row)) for row in trans_field])
	# text_field = horizontals + verticals
	# battleships = re.findall('1{4}', text_field)
	# # text_field = text_field.replace(battleships[0], '4444')
	# cruisers = re.findall('1{3}', text_field)
	# destroyers = re.findall('1{2}', text_field)
	# if len(re.findall('1{4}', text_field)) < 1:
	# 	return False
	# if len(re.findall('1{3}', text_field)) < 2:
	# 	return False
	# if len(re.findall('1{2}', text_field)) < 3:
	# 	return False
	#
	# return text_field.count('1') == 40


# verticals = [str(field[])]


# battleship = [(1, 1), (2, 1), (3, 1), (4, 1)]
# print(find_battleship(field))
# print(check_neighbours(add_frame(field), battleship))
# print(find_ship(add_frame(field), 4))

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
# # should return True

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
# should return True

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

# field = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#          [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#          [1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
#          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
# should return False

field = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
# should equal True

# print(find_ship(field, 3))
print(validate_battlefield(field))
