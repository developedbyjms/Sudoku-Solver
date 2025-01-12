# -*- coding:utf8;-*-
import random  # For generating random numbers
import os      # For file and directory operations
import json    # For reading and parsing JSON data

class Sudoku:
    def __init__(self):
        # Constructor: No specific initialization needed for this class
        pass

    def generateProblem(self, level="Easy"):
        """
        Generates a Sudoku problem grid based on the specified difficulty level.
        Args:
            level (str): Difficulty level of the Sudoku problem (e.g., "Easy").
        Returns:
            list: A 9x9 grid representing the Sudoku puzzle.
        """
        # Change the working directory to the current script's location
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Path to the file containing Sudoku problems
        path = os.getcwd() + "/problems.txt"

        # Read problems from the file
        with open(path, "r") as f:
            content = f.read()

        # Parse the JSON content to retrieve problems
        problems = json.loads(content)

        # Select a random problem from the specified difficulty level
        point = random.randint(0, 9)
        problem = problems[level][point]

        # Convert the problem string into a 9x9 grid
        l1 = [int(n) for n in problem[0:9]]
        l2 = [int(n) for n in problem[9:18]]
        l3 = [int(n) for n in problem[18:27]]
        l4 = [int(n) for n in problem[27:36]]
        l5 = [int(n) for n in problem[36:45]]
        l6 = [int(n) for n in problem[45:54]]
        l7 = [int(n) for n in problem[54:63]]
        l8 = [int(n) for n in problem[63:72]]
        l9 = [int(n) for n in problem[72:81]]
        return [l1, l2, l3, l4, l5, l6, l7, l8, l9]

    def solve(self, problem):
        """
        Solves a given Sudoku problem using a backtracking algorithm.
        Args:
            problem (list of lists): A 9x9 grid representing the Sudoku puzzle.
        """
        for y in range(9):
            for x in range(9):
                # Check for empty cells (denoted by 0)
                if problem[y][x] == 0:
                    # Try placing numbers 1 through 9
                    for n in range(1, 10):
                        if self.possible(problem, y, x, n):
                            problem[y][x] = n
                            self.solve(problem)  # Recursive call to solve the rest of the grid
                            problem[y][x] = 0  # Backtrack if the solution fails
                    return  # Exit if no solution is found

        # Print the solved Sudoku grid
        print("[ " + "=" * 23 + " ]")
        for row in problem:
            print(row)
        print("[ " + "=" * 23 + " ]\n")

    def possible(self, grid, y, x, n):
        """
        Checks if a number can be placed in a specific cell of the grid.
        Args:
            grid (list of lists): The 9x9 Sudoku grid.
            y (int): Row index.
            x (int): Column index.
            n (int): Number to check.
        Returns:
            bool: True if the number can be placed, False otherwise.
        """
        # Check if the number is already in the row
        for i in range(9):
            if grid[y][i] == n:
                return False

        # Check if the number is already in the column
        for i in range(9):
            if grid[i][x] == n:
                return False

        # Check if the number is in the 3x3 subgrid
        x0 = (x // 3) * 3  # Top-left corner of the subgrid (x-axis)
        y0 = (y // 3) * 3  # Top-left corner of the subgrid (y-axis)
        for i in range(3):
            for j in range(3):
                if grid[y0 + i][x0 + j] == n:
                    return False

        # If all checks pass, the number can be placed
        return True


"""
=> DevelopedByJMS™
=> José Sixpenze
=> 12/01/2015
"""