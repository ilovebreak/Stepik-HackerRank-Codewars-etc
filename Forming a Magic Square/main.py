'''
https://www.hackerrank.com/challenges/magic-square-forming/problem
'''


def formingMagicSquare(s):
	ls_possible_square = [
		[[2, 9, 4], [7, 5, 3], [6, 1, 8]],
		[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
		[[6, 7, 2], [1, 5, 9], [8, 3, 4]],
		[[6, 1, 8], [7, 5, 3], [2, 9, 4]],
		[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
		[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
		[[4, 3, 8], [9, 5, 1], [2, 7, 6]],
		[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
	]  # 8 magic squares in case 3x3
	cost = 0
	min_cost = 72
	for x in ls_possible_square:  # x has length 8
		for i in range(3):
			for j in range(3):
				cost += abs(x[i][j] - s[i][j])
		if cost < min_cost:
			min_cost = cost
		cost = 0
	return min_cost


print(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))


'''
Possible magic square
Center: 5
Corners: even
Edges: odd

ROTATE THEN FLIP, AN EDGE FOLLOW 2 CORRESPONDING CORNERS

Num_way to put 2: 4
Num_way to put 8: 1
Num_way to put 4: 2
Num_way to put 6: 1

WE GET TOTAL 8 CASES

2 9 4 2 7 6
7 5 3 9 5 1
6 1 8 4 3 8

##
6 7 2 6 1 8
1 5 9 7 5 3
8 3 4 2 9 4

#
8 1 6 8 3 4
3 5 7 1 5 9
4 9 2 6 7 2

##
4 3 8 4 9 2
9 5 1 3 5 7
2 7 6 8 1 6
'''
