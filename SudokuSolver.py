class Solution:
    def solveSudoku(self, board):
        self.solve(board)
        self.printBoard(board)  # Add this line to print the solved board

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # Empty cell found
                    for num in map(str, range(1, 10)):  # Try numbers '1' to '9'
                        if self.isValid(board, row, col, num):
                            board[row][col] = num  # Place the number
                            
                            if self.solve(board):
                                return True  # If solved, return True
                            else:
                                board[row][col] = '.'  # Backtrack if no solution found
                    return False  # Trigger backtracking if no valid number is found
        return True  # Board is completely solved

    def isValid(self, board, row, col, num):
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 sub-box
        startRow = 3 * (row // 3)
        startCol = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True

    def printBoard(self, board):
        for row in board:
            print(" ".join(row))

# Example Usage
if __name__ == "__main__":
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]

    solution = Solution()
    solution.solveSudoku(board)
