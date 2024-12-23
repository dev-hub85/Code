# Helper function to check constraints
def is_valid(board, row, col):
    for r, c in enumerate(board):
        # Check if the row or diagonal is attacked
        if r == row or abs(r - row) == abs(c - col):
            return False

    return True

# Backtracking function to solve the CSP
def solve_queens(n):
    board = [-1] * n  # Initialize an empty board with n columns

    def backtrack(col):
        # If all queens are placed
        if col == n:
            print_solution(board)
            return True

        # Try placing the queen in each row for the current column
        for row in range(n):
            if is_valid(board, row, col):
                board[col] = row  # Place queen
                if backtrack(col + 1):  # Recur to place the next queen
                    return True
                board[col] = -1  # Backtrack if no solution

        return False

    backtrack(0)  # Start backtracking from the first column

# Function to print the solution in a readable format
def print_solution(board):
    for row in board:
        line = ['.'] * len(board)  # Create an empty row
        line[row] = 'Q'  # Place the queen
        print(' '.join(line))
    print("\n")

# Solve the 4-Queens problem
solve_queens(4)
