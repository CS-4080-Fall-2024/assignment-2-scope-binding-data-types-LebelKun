import random

class RubiksCube:
    def __init__(self, size=3):
        self.size = size
        self.faces = ['W', 'Y', 'G', 'B', 'R', 'O']  # Colors for each face: Up, Down, Left, Right, Front, Back
        # Create a cube with each face being a solid color
        self.cube = [[[color for _ in range(size)] for _ in range(size)] for color in self.faces]

    def display(self):
        # Display the cube state
        print("Cube State:")
        for i in range(6):
            print(f"Face {i} ({self.faces[i]}):")
            for row in self.cube[i]:
                print(' '.join(row))
            print()

    def rotate_face_clockwise(self, face):
        # Rotate a face 90 degrees clockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def rotate_face_counter_clockwise(self, face):
        # Rotate a face 90 degrees counterclockwise
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

    def rotate_u(self, inverse=False):
        """Rotate the Up (U) face clockwise or counterclockwise."""
        self.rotate_face_clockwise(4) if not inverse else self.rotate_face_counter_clockwise(4)

        if not inverse:
            # Rotate the adjacent sides: F (0), R (1), B (2), L (3)
            top_row = self.cube[0][0][:]
            self.cube[0][0] = self.cube[1][0]
            self.cube[1][0] = self.cube[2][0]
            self.cube[2][0] = self.cube[3][0]
            self.cube[3][0] = top_row
        else:
            top_row = self.cube[0][0][:]
            self.cube[0][0] = self.cube[3][0]
            self.cube[3][0] = self.cube[2][0]
            self.cube[2][0] = self.cube[1][0]
            self.cube[1][0] = top_row

    def rotate_d(self, inverse=False):
        """Rotate the Down (D) face clockwise or counterclockwise."""
        self.rotate_face_clockwise(5) if not inverse else self.rotate_face_counter_clockwise(5)

        if not inverse:
            # Rotate the adjacent sides: F (0), R (1), B (2), L (3)
            bottom_row = self.cube[0][2][:]
            self.cube[0][2] = self.cube[3][2]
            self.cube[3][2] = self.cube[2][2]
            self.cube[2][2] = self.cube[1][2]
            self.cube[1][2] = bottom_row
        else:
            bottom_row = self.cube[0][2][:]
            self.cube[0][2] = self.cube[1][2]
            self.cube[1][2] = self.cube[2][2]
            self.cube[2][2] = self.cube[3][2]
            self.cube[3][2] = bottom_row

    def rotate_l(self, inverse=False):
        """Rotate the Left (L) face clockwise or counterclockwise."""
        self.rotate_face_clockwise(3) if not inverse else self.rotate_face_counter_clockwise(3)

        if not inverse:
            # Rotate the adjacent sides: U (4), F (0), D (5), B (2)
            left_column_u = [self.cube[4][i][0] for i in range(self.size)]
            for i in range(self.size):
                self.cube[4][i][0] = self.cube[2][self.size - 1 - i][2]
                self.cube[2][self.size - 1 - i][2] = self.cube[5][i][0]
                self.cube[5][i][0] = self.cube[0][i][0]
                self.cube[0][i][0] = left_column_u[i]
        else:
            left_column_u = [self.cube[4][i][0] for i in range(self.size)]
            for i in range(self.size):
                self.cube[4][i][0] = self.cube[0][i][0]
                self.cube[0][i][0] = self.cube[5][i][0]
                self.cube[5][i][0] = self.cube[2][self.size - 1 - i][2]
                self.cube[2][self.size - 1 - i][2] = left_column_u[i]

    def rotate_r(self, inverse=False):
        """Rotate the Right (R) face clockwise or counterclockwise."""
        self.rotate_face_clockwise(1) if not inverse else self.rotate_face_counter_clockwise(1)

        if not inverse:
            # Rotate the adjacent sides: U (4), F (0), D (5), B (2)
            right_column_u = [self.cube[4][i][self.size - 1] for i in range(self.size)]
            for i in range(self.size):
                self.cube[4][i][self.size - 1] = self.cube[0][i][self.size - 1]
                self.cube[0][i][self.size - 1] = self.cube[5][i][0]
                self.cube[5][i][0] = self.cube[2][self.size - 1 - i][0]
                self.cube[2][self.size - 1 - i][0] = right_column_u[i]
        else:
            right_column_u = [self.cube[4][i][self.size - 1] for i in range(self.size)]
            for i in range(self.size):
                self.cube[4][i][self.size - 1] = self.cube[2][self.size - 1 - i][0]
                self.cube[2][self.size - 1 - i][0] = self.cube[5][i][0]
                self.cube[5][i][0] = self.cube[0][i][self.size - 1]
                self.cube[0][i][self.size - 1] = right_column_u[i]

    def rotate_f(self, inverse=False):
        """Rotate the Front (F) face clockwise or counterclockwise."""
        self.rotate_face_clockwise(0) if not inverse else self.rotate_face_counter_clockwise(0)

        if not inverse:
            # Rotate the adjacent sides: U (4), R (1), D (5), L (3)
            front_row = self.cube[0][self.size - 1][:]
            for i in range(self.size):
                self.cube[0][self.size - 1][i] = self.cube[4][self.size - 1][i]
                self.cube[4][self.size - 1][i] = self.cube[1][0][i]
                self.cube[1][0][i] = self.cube[5][0][self.size - 1 - i]
                self.cube[5][0][self.size - 1 - i] = front_row[i]
        else:
            front_row = self.cube[0][self.size - 1][:]
            for i in range(self.size):
                self.cube[0][self.size - 1][i] = self.cube[5][0][self.size - 1 - i]
                self.cube[5][0][self.size - 1 - i] = self.cube[1][0][i]
                self.cube[1][0][i] = self.cube[4][self.size - 1][i]
                self.cube[4][self.size - 1][i] = front_row[i]

    def perform_move(self, move):
        """Perform a move based on standard Rubik's Cube notation."""
        if move == 'U':
            self.rotate_u()
        elif move == "U'":
            self.rotate_u(inverse=True)
        elif move == 'D':
            self.rotate_d()
        elif move == "D'":
            self.rotate_d(inverse=True)
        elif move == 'L':
            self.rotate_l()
        elif move == "L'":
            self.rotate_l(inverse=True)
        elif move == 'R':
            self.rotate_r()
        elif move == "R'":
            self.rotate_r(inverse=True)
        elif move == 'F':
            self.rotate_f()
        elif move == "F'":
            self.rotate_f(inverse=True)
        elif move == 'B':
            self.rotate_face_clockwise(2)
        elif move == "B'":
            self.rotate_face_counter_clockwise(2)
        else:
            raise ValueError(f"Invalid move: {move}")

        self.display()

    def scramble(self, moves=20):
        """Randomly scramble the cube by performing random moves."""
        possible_moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
        for _ in range(moves):
            move = random.choice(possible_moves)
            self.perform_move(move)

    def solve(self):
        """Solve the cube by resetting it to the solved state."""
        self.cube = [[[color for _ in range(self.size)] for _ in range(self.size)] for color in self.faces]
        print("Cube has been reset to solved state.")

    def is_solved(self):
        # Check if the cube is solved
        return all(all(all(tile == self.cube[face][0][0] for tile in row) for row in self.cube[face]) for face in range(6))

    def command_line_interface(self):
        while True:
            print("\nEnter a move (U, D, L, R, F, B, and their inverses with '):")
            print("Type 'scramble' to scramble the cube or 'solve' to reset it.")
            print("Type 'exit' to quit.")
            move = input("Your move: ").strip()

            if move.lower() == 'exit':
                break
            elif move.lower() == 'scramble':
                self.scramble()
                print("Cube scrambled.")
            elif move.lower() == 'solve':
                self.solve()
                print("Cube reset to solved state.")
            else:
                try:
                    self.perform_move(move)
                    print(f"Performed move: {move}")
                except ValueError as e:
                    print(e)

            self.display()

# Example Usage
if __name__ == "__main__":
    cube = RubiksCube(3)
    print("Initial Cube State:")
    cube.display()

    # Start command line interface
    cube.command_line_interface()
