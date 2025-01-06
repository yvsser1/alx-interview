#!/usr/bin/python3
"""Program to solve the N Queens puzzle"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col].

    Args:
        board (list): Current board state
        row (int): Row to check
        col (int): Column to check
        n (int): Size of the board

    Returns:
        bool: True if queen can be placed, False otherwise
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N queens puzzle and print all solutions.

    Args:
        n (int): Size of the board and number of queens
    """
    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve_util(board, col):
        """
        Utility function to solve N Queens problem using backtracking.

        Args:
            board (list): Current board state
            col (int): Current column being processed
        """
        # Base case: If all queens are placed, print the solution
        if col >= n:
            print_solution(board)
            return

        # Consider this column and try placing this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col, n):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # Recur to place rest of the queens
                solve_util(board, col + 1)

                # If placing queen in board[i][col] doesn't lead to a solution,
                # remove queen from board[i][col]
                board[i][col] = 0

    def print_solution(board):
        """
        Print the solution in the required format.

        Args:
            board (list): Current board state with a valid solution
        """
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)

    # Start solving from first column
    solve_util(board, 0)


def main():
    """Main function to handle input and start solving"""
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
