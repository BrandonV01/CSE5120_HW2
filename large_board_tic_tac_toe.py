"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
																				 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
	def __init__(self, size = (600, 600)):

		self.size = self.width, self.height = size
		# Define some colors
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 255)

		# Grid Size
		self.GRID_SIZE = 3
		self.OFFSET = 5

		self.CIRCLE_COLOR = (140, 146, 172)
		self.CROSS_COLOR = (140, 146, 172)

		# This sets the WIDTH and HEIGHT of each grid location
		self.WIDTH = (self.size[0] - self.OFFSET*2) /self.GRID_SIZE 
		self.HEIGHT = (self.size[1] - self.OFFSET*2) /self.GRID_SIZE

		# This sets the margin between each cell
		self.MARGIN = 5

		# This creates initial gamestate class
		board = [[0 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
		self.game_state = GameStatus(board, False)


		# Initialize pygame
		pygame.init()
		self.game_reset()


	def draw_game(self):
		# Create a 2 dimensional array using the column and row variables
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Tic Tac Toe Random Grid")
		self.screen.fill(self.WHITE)
		
		"""
		YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
		"""
		# Draw box the grid will be within
		pygame.draw.line(self.screen, self.BLACK, (self.OFFSET, self.OFFSET), (self.size[0]-self.OFFSET, self.OFFSET), self.MARGIN)
		pygame.draw.line(self.screen, self.BLACK, (self.OFFSET, self.OFFSET + (self.GRID_SIZE * self.HEIGHT)), (self.size[0]-self.OFFSET, self.OFFSET + (self.GRID_SIZE * self.HEIGHT)), self.MARGIN)
		pygame.draw.line(self.screen, self.BLACK, (self.OFFSET, self.OFFSET), (self.OFFSET, self.OFFSET + (self.GRID_SIZE * self.HEIGHT)), self.MARGIN)
		pygame.draw.line(self.screen, self.BLACK, (self.size[0]-self.OFFSET, self.OFFSET), (self.size[0]-self.OFFSET, self.OFFSET + (self.GRID_SIZE * self.HEIGHT)), self.MARGIN)

		# Draw the grid
		for x in range(1, self.GRID_SIZE):
			pygame.draw.line(self.screen, self.BLACK, (self.OFFSET, self.OFFSET + self.HEIGHT * x), (self.size[0]-self.OFFSET, self.OFFSET + self.HEIGHT * x), self.MARGIN)
			pygame.draw.line(self.screen, self.BLACK, (self.OFFSET + self.WIDTH * x, self.OFFSET), (self.OFFSET + self.WIDTH * x, self.size[0]-self.OFFSET), self.MARGIN)
		
		self.change_turn()

		pygame.display.update()


	def change_turn(self):

		if(self.game_state.turn_O):
			pygame.display.set_caption("Tic Tac Toe - O's turn")
		else:
			pygame.display.set_caption("Tic Tac Toe - X's turn")


	def draw_circle(self, x, y):
		"""
		YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
		"""
		pygame.draw.circle(self.screen, self.BLUE, (self.OFFSET + (self.WIDTH * (x))+ self.WIDTH/2, self.OFFSET + (self.HEIGHT * (y)) + self.HEIGHT/2), self.WIDTH / 3, self.MARGIN)
		

	def draw_cross(self, x, y):
		"""
		YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
		"""
		pygame.draw.line(self.screen, self.RED, (self.OFFSET + self.WIDTH * x + self.WIDTH / 4, self.OFFSET + self.HEIGHT * y + self.HEIGHT / 4), (self.OFFSET + self.WIDTH * x + (self.HEIGHT * 3 / 4), self.OFFSET + self.HEIGHT * y + (self.HEIGHT * 3 / 4)), self.MARGIN)
		pygame.draw.line(self.screen, self.RED, (self.OFFSET + self.WIDTH * x + (self.HEIGHT * 3 / 4), self.OFFSET + self.HEIGHT * y + self.HEIGHT / 4), (self.OFFSET + self.WIDTH * x + self.WIDTH / 4, self.OFFSET + self.HEIGHT * y + (self.HEIGHT * 3 / 4)), self.MARGIN)
		
		
	def is_game_over_standard(self):

		"""
		YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
		FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
		
		YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
		"""
		return self.game_state.is_terminal()
	

	def is_game_over_big_board(self):
		# Second game over function for when baord isn't 3x3 hence uses different ruling
		return self.game_state.is_terminal_big_board()
	

	def move(self, move):
		self.game_state = self.game_state.get_new_state(move)


	def play_ai(self):
		"""
		YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
		ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
		ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
		
		THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
		NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
		"""

		value, best_move = minimax(self.game_state, 10, 1)

		self.draw_circle(best_move[0], best_move[1])
		self.move(best_move)

		self.change_turn()
		pygame.display.update()
		""" USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """


	def game_reset(self):
		"""
		YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
		BOARD STATE
		"""
		self.draw_game()

		# Fill game_state with board state filled with 0
		board = [[0 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
		self.game_state = GameStatus(board, False)

		
		pygame.display.update()


	def play_game(self, mode = "player_vs_ai"):
		done = False

		clock = pygame.time.Clock()


		while not done:
			for event in pygame.event.get():  # User did something
				"""
				YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
				"""

				"""
				YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
				THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
				"""
					
				"""
				YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
				IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
				DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
				PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
				"""
				
				if event.type == pygame.QUIT:
					done = True
					
				if event.type == pygame.MOUSEBUTTONUP:
					# Get the position
					mouse_pos = pygame.mouse.get_pos()

					# Change the x/y screen coordinates to grid coordinates
					if self.OFFSET < mouse_pos[0] <= self.size[1] - self.OFFSET and self.OFFSET < mouse_pos[1] <= self.size[0] - self.OFFSET:
						grid_x = int((mouse_pos[0] - self.OFFSET) // self.WIDTH)
						grid_y = int((mouse_pos[1] - self.OFFSET) // self.HEIGHT)
						coordinates = [grid_x, grid_y]

						# Checks if the grid is empty and if so fills it in with appropriate symbol and makes the move
						if self.game_state.board_state[grid_y][grid_x] == 0:
							if mode == "player_vs_player":
								if self.game_state.turn_O == True:
									self.draw_circle(grid_x, grid_y)
								else:
									self.draw_cross(grid_x, grid_y)
								
								self.move(coordinates)

								if self.GRID_SIZE == 3:
									done = self.is_game_over_standard()
								else:
									done = self.is_game_over_big_board()
								
								self.change_turn()

							elif mode == "player_vs_ai":

								self.draw_cross(grid_x, grid_y)
								self.move(coordinates)

								self.change_turn()

								if self.GRID_SIZE == 3:
									done = self.is_game_over_standard()
								else:
									done = self.is_game_over_big_board()
								
								
								pygame.display.update()
								
								if not done:
									self.play_ai()

									if self.GRID_SIZE == 3:
										done = self.is_game_over_standard()
									else:
										done = self.is_game_over_big_board()

					# Check if the game is human vs human or human vs AI player from the GUI. 
					# If it is human vs human then your opponent should have the value of the selected cell set to -1
					# Then draw the symbol for your opponent in the selected cell
					# Within this code portion, continue checking if the game has ended by using is_terminal function
					
			# Update the screen with what was drawn.
			pygame.display.update()

		pygame.quit()

tictactoegame = RandomBoardTicTacToe()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
#mode = "player_vs_player"
tictactoegame.play_game(mode)
