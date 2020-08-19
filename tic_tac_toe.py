import math, random

class Game:

    def __init__(self, players=1):
        self.players = players
        # board variables
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.turn_counter = 0

    def end(self):
        ### class method to end the game and ask the user for a new game ###
        play_again = input('Play again? (Y/N)')

        if play_again == 'Y' or play_again == 'y' or play_again == 'Yes' or play_again == 'yes':
            # Starts a new game
            return 'start'
        elif play_again == 'N' or play_again == 'n' or play_again == 'No' or play_again == 'no':
            print('Thank you for playing!')
            return 'end'
        else: 
            return False

    def print_board(self):
        ### prints the game board ###
           
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('- - - - -')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('- - - - -')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')
    
    def player_move(self):
        ### asks the user for a choice ###
        print('Player Turn')
        picked = False
        
        while not picked:
            space_choice = input('Pick a space:(1-9)')

            if space_choice in self.board:
                picked = True
                self.update('X',int(space_choice))
                return
            elif type(space_choice) == int and space_choice >= 1 and space_choice <= 9:
                print('Space already taken, please choose again.')
            else: 
                print('Make sure to pick a valid number')
    
    def update(self, player, space_choice):
        ### places the player option on the board ###
        self.board[space_choice-1] = player

    def possible_wins(self):
        return [
            [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
        ]

    def determine_win(self):
        ### checks to see if a winner has been picked ###
        wins = self.possible_wins()

        moves = 0
        for s in self.board:
            if s == 'O' or s == 'X':
                moves += 1
        
        for win in wins:
            count_x = 0
            count_o = 0
            # checks to see if either player has 3 in a row
            for space in win:
                if self.board[space] == 'X':
                    count_x += 1
                elif self.board[space] == 'O':
                    count_o += 1
                
            if count_x == 3:
                print('X wins!!')
                return 'end'
            elif count_o == 3:
                print('O wins!!')
                return 'end'
                
        if moves == 9:
            print("It's a tie")
            return 'end'

    def comp_move(self):
        ### method for the computer to make a move ### 
        print('Computer Turn')

        # Conner opening moves
        if self.turn_counter == 1:
            print('Possible corner move!')
            if self.board[0] == 'X':
                self.update('O',9)
                return
            elif self.board[2] == 'X':
                self.update('O',7)
                return
            elif self.board[6] == 'X':
                self.update('O',3)
                return
            elif self.board[8] == 'X':
                self.update('O',1)
                return
        
        for win in self.possible_wins():
            count_x = 0
            count_o = 0
            for space in win:
                if self.board[space] == 'X':
                    count_x += 1
                elif self.board[space] == 'O':
                    count_o += 1
                
            if (count_x == 2 and count_o == 0) or (count_o == 2 and count_x == 0):
                for space in win:
                    if self.board[space] != 'X' and self.board[space] != 'O':
                        self.update('O',space+1)
                        return
        
        # Takes the center if it is open
        if self.board[4] != 'X' and self.board[4] != 'O':
            print('Center space!')
            self.update('O',5)
            return
        
        comp_pick = False

        while not comp_pick:
            choice = random.randint(1,9)
            if self.board[choice-1] != 'X' and self.board[choice-1] != 'O':
                self.update('O',choice)
                return

    def start_game(self):
        print('Wecome to Command Line Tic-Tac-Toe!!')

        # resets to initial game settings
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.turn_counter = 0

        self.print_board()
        
        self.take_turn()

    def take_turn(self):
        # switches between computer and player turn
        if self.turn_counter % 2 == 0:
            self.player_move()
        else:
            self.comp_move()

        # prints updated board after move
        self.print_board()
        win = self.determine_win()

        print(f'win = {win}')
        
        if win == 'end':
            end = self.end()
            if end == 'start': # starts a new game
                self.start_game()
            elif end == 'end':
                print('End game')
                return
        
        # increases the turn counter to change the score
        self.turn_counter += 1

        self.take_turn()


# creates an instance of the game
my_game = Game()

my_game.start_game()
