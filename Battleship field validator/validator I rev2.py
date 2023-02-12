'''
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
'''

'''
function adds to battlefield frame filled by zeroes to avoid IndexError while seeking a ship
'''


def add_frame(field):
	for line in field:
		line.insert(0, 0)
		line.append(0)
	field.insert(0, [0] * 12)
	field.append([0] * 12)
	return field


def check_neighbours(field, *ship):
	neighbours = []
	for coordinates in ship:
		for i, j in coordinates:
			neighbours.extend(
				[(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
				 (i + 1, j + 1)])
	neighbours = set(neighbours) - set(*ship)
	# print('neighbours', neighbours)
	# print(len(ship), [field[i][j] for i, j in neighbours], all(field[i][j] == 0 for i, j in neighbours))

	return all(field[i][j] == 0 for i, j in neighbours)


'''
function returns list of tuples with coordinates of ship of size n 
if ship is found all its cells on battlefield are replaced by zeroes to make it possible to find next ship
'''


def find_ship(field, n):
	for i in range(1, 11):
		for j in range(1, 12 - n):
			if sum([field[i][j + k] for k in range(n)]) == n:
				ship = [(i, j + k) for k in range(n)]
				for i, j in ship:
					field[i][j] = 0
				return ship if check_neighbours(field, ship) else []
	for i in range(1, 12 - n):
		for j in range(1, 11):
			if sum([field[i + k][j] for k in range(n)]) == n:
				ship = [(i + k, j) for k in range(n)]
				for i, j in ship:
					field[i][j] = 0
				return ship if check_neighbours(field, ship) else []
	return []


def validate_battlefield(field):
	print(field)
	add_frame(field)
	ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
	ships = [find_ship(field, size) for size in ship_sizes]
	# return ships, sum(sum(field, []))
	return all(len(x) == y for x, y in zip(ships, ship_sizes)) and sum(sum(field, [])) == 0


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
## should return False

field = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]
## should return True

# field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 		[1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 		[1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 		[0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
# 		[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]
# # should return True


# battleship = [(1, 1), (2, 1), (3, 1), (4, 1)]
# print(find_battleship(field))
# print(check_neighbours(add_frame(field), battleship))
# print(find_ship(add_frame(field), 4))
print(validate_battlefield(field))
