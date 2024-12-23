def is_valid(board, row, col):
    # Check for column conflict or diagonal conflicts
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    result = []  # To store solutions
    
    def backtrack(row):
        if row == n:  # All queens are placed
            result.append(list(board))  # Add the current board configuration to results
            return
        
        for col in range(n):  # Try all columns for the current row
            if is_valid(board, row, col):
                board[row] = col  # Place queen in the current column
                backtrack(row + 1)  # Recur to place the next queen
                board[row] = -1  # Remove the queen (backtrack)
    
    backtrack(0)  # Start backtracking from the first row
    
    # Display the solutions
    for i, solution in enumerate(result):
        print(f"Solution {i + 1}:")
        for row in solution:
            line = ['.'] * n  # Create an empty row with '.' representing empty cells
            line[row] = 'Q'  # Place the queen
            print(' '.join(line))
        print("\n")

# Solve the 8-Queens problem
solve_n_queens(8)
