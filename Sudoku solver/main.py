'''
https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
'''


def sudoku(puzzle):
	"""return the solved puzzle as a 2d array of 9 x 9"""
	# puzzle = np.array(puzzle)

	counter = 0
	while True:
		counter += 1
		solved = [counter]
		flag = False
		for i, row in enumerate(puzzle):
			for j, n in enumerate(row):
				if n == 0 or isinstance(n, list):
					vertical = [puzzle[c][j] for c in range(0, 9)]
					if 0 <= i <= 2 and 0 <= j <= 2:
						quadrant = puzzle[0][:3] + puzzle[1][:3] + puzzle[2][:3]
					elif 0 <= i <= 2 and 3 <= j <= 5:
						quadrant = puzzle[0][3:6] + puzzle[1][3:6] + puzzle[2][3:6]
					elif 0 <= i <= 2 and 6 <= j <= 8:
						quadrant = puzzle[0][6:9] + puzzle[1][6:9] + puzzle[2][6:9]
					elif 3 <= i <= 5 and 0 <= j <= 2:
						quadrant = puzzle[3][:3] + puzzle[4][:3] + puzzle[5][:3]
					elif 3 <= i <= 5 and 3 <= j <= 5:
						quadrant = puzzle[3][3:6] + puzzle[4][3:6] + puzzle[5][3:6]
					elif 3 <= i <= 5 and 6 <= j <= 8:
						quadrant = puzzle[3][6:9] + puzzle[4][6:9] + puzzle[5][6:9]
					elif 6 <= i <= 8 and 0 <= j <= 2:
						quadrant = puzzle[6][:3] + puzzle[7][:3] + puzzle[8][:3]
					elif 6 <= i <= 8 and 3 <= j <= 5:
						quadrant = puzzle[6][3:6] + puzzle[7][3:6] + puzzle[8][3:6]
					elif 6 <= i <= 8 and 6 <= j <= 8:
						quadrant = puzzle[6][6:9] + puzzle[7][6:9] + puzzle[8][6:9]

					vars = [k for k in range(1, 10) if k not in row and k not in vertical and k not in quadrant]
					if len(vars) == 1:
						vars = vars[0]
						solved.append((vars, i, j))
						print(solved)
						flag = True
					row[j] = vars
		if not flag:
			break

	return puzzle


'''
 не мое
 '''


def sudoku1(P):
	for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:

		rr, cc = (row // 3) * 3, (col // 3) * 3

		use = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (
				{P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr + r][cc + c] for r in range(3)
				                                                                 for c in range(3)})

		if len(use) == 1:
			P[row][col] = use.pop()
			return sudoku(P)
	return P


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(sudoku(puzzle))
print(sudoku1(puzzle))
# Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]
