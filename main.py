#-*-coding:utf8;-*-
from Sudoku import Sudoku

def show(grid):
	print("[ "+"="*23+" ]")
	print("[     BEFORE SOLUTION:    ]")
	print("[ "+"="*23+" ]")
	for row in grid:
		print(row)
	print("[ "+"="*23+" ]")
	print("[     AFTER SOLUTION:     ]")

def sample():
	return [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6], [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]

sudoku = Sudoku()

#SAMPLE
sample = sample()
show(sample)
sudoku.solve(sample)


#EASY PROBLEM
easy_problem = sudoku.generateProblem("Easy")
show(easy_problem)
sudoku.solve(easy_problem)

#MEDIUM PROBLEM
medium_problem = sudoku.generateProblem("Medium")
show(medium_problem)
sudoku.solve(medium_problem)

#HARD PROBLEM
hard_problem = sudoku.generateProblem("Hard")
show(hard_problem)
sudoku.solve(hard_problem)

#EXPERT PROBLEM
expert_problem = sudoku.generateProblem("Expert")
show(expert_problem)
sudoku.solve(expert_problem)


"""
=> DevelopedByJMS™
=> José Sixpenze
=> 12/01/2025
"""
