#Battleship 1 player game
import random
import sys
class Battleship:

    def __init__(self, boardsize, shipsizes):
        self.size = boardsize
        self.shipsizes = shipsizes
        self.counter = 0
        self.wincounter = 0
        self.board = []
        self.positions = []
        dict = {}
#creates the game board: board and another board which keeps track of the ship positions:positions. 
    def generate_board(self):
        self.board = [[0]*self.size for i in range(self.size)]
    #    for i in range(Self.size):
    #        board.append([0]*self.size)
        self.positions = [[0]*self.size for i in range(self.size)]

#displays the game board
    def print_board(self):
        for i in range(self.size):
            print("\n")
            print ("-------" * self.size)
            for j in range(self.size):
                print "|   ", self.board[i][j],
        print("\n")
        print ("-------" * self.size)

#generates board positions to place the ships
    def generate_ship_index(self):
        ship_row = random.randint(0, self.size-1)
        ship_col = random.randint(0, self.size-1)
        return ship_row, ship_col

#check if the ship of size shipsize can be placed at row, col on the board
    def validate_ship_position(self, row, col, shipsize, orientation):
        if row > self.size - 1 or col > self.size - 1:
            return False
        if orientation == 'vertical' and (row+shipsize) > self.size:
            return False
        elif orientation == 'horizontal' and (col+shipsize) > self.size:
            return False
        if orientation == 'vertical':
            for i in range(shipsize):
                if self.positions[row+i][col] != 0:
                    return False
        elif orientation == 'horizontal':
            for i in range(shipsize):
                if self.positions[row][col+i] != 0:
                    return False
        return True

#after positions are finalized, place the ships
    def place_ship(self, row, col, ship, orientation):
        if orientation == 'vertical':
            for i in range(ship):
                self.positions[row+i][col] = ship
        if orientation == 'horizontal':
            for i in range(ship):
                self.positions[row][col+i] = ship

#arranges the ships on the board after generating random ship positions
    def prepare_board(self):
        o = ['vertical', 'horizontal']
        for ship in self.shipsizes:
            orientation = random.choice(o)
            while True:
                row, col = self.generate_ship_index()
                if not self.validate_ship_position(row, col, ship, orientation):
                    continue
                else:
                    self.place_ship(row, col, ship, orientation)
                    break
#Checks if the user input is correct or out of range and if the move has not been entered before
    def check_if_valid_move(self, row, col):
        if row > self.size - 1 or row < 0 or col > self.size - 1 or col < 0:
            print "Uh oh. Enter a valid row and column"
            return 1
        elif self.board[row][col] == 'X' or self.board[row][col] == 'S':
            print "\nYou've already entered this. Enter a new row and column"
            return 1
        else:
            return 0

#Playing the move chosen by the user. The board will be updated of the player's move
    def make_move(self, row, col):
        if self.positions[row][col] > 0:
             print "\nIt's a hit!"
             self.board[row][col] = 'S'
             self.print_board()
             self.check_sunk_ship(self.positions[row][col])
        elif self.positions[row][col] == 0:
             print "\nYou missed the ship. Try again."
             self.board[row][col] = 'X'
             self.print_board()

#After each correct move when the player finds a ship index, this function is called to check if the ship is sink
    def check_sunk_ship(self, shipno):
        self.counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.positions[i][j] == shipno and self.board[i][j] == 'S':
                    self.counter += 1
        if self.counter == shipno:
            self.wincounter += 1
            print "\nGood find. This Battleship has sunk. Have a cookie."
        if self.wincounter == len(self.shipsizes):
            self.win_or_lose()

#Function to check if the player won or lost
    def win_or_lose(self):
        if self.wincounter == len(self.shipsizes):
            print "\nYay, you win!"
            sys.exit(0)
        else:
            print "\nYou missed this this time. Wanna play again?"
            sys.exit(0)


if __name__ == "__main__":
    no_of_moves = 15
    obj = Battleship(6, [2,3,4])
    obj.generate_board()
    obj.print_board()
    obj.prepare_board()
    while no_of_moves >= 0:
        print "Moves remaining: ", no_of_moves
        row = int(raw_input("\nEnter row: "))
        col = int(raw_input("\nEnter column: "))
        if obj.check_if_valid_move(row, col) == 0:
            no_of_moves -= 1
            obj.make_move(row, col)
    obj.win_or_lose()
