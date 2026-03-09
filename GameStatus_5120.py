# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		"""
		terminal check for standard 3x3 tic tac toe
      """
		col_index = 0
		for x in self.board_state:
			# Starting off with checking if a row has 3 of the same symbol
			if abs(sum(x)) == 3:
				return True

			# Now checking each col
			if abs(self.board_state[0][col_index] + self.board_state[1][col_index] + self.board_state[2][col_index]) == 3:
				return True

			col_index += 1
		
		# Checking for a diagnal win
		if abs(self.board_state[0][0] + self.board_state[1][1] + self.board_state[2][2]) == 3 or abs(self.board_state[0][2] + self.board_state[1][1] + self.board_state[2][0]) == 3: 
			return True
		
		# Checking for tie case
		return (not any(0 in row for row in self.board_state))
	
	def is_terminal_big_board(self):
		"""
		YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
		THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
      """
		
		return (not any(0 in row for row in self.board_state))
		

	def get_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		score = 0
		check_point = 3 if terminal else 2
		
		# return the line closest to creating
		col_index = 0
		for x in self.board_state:
			# Starting off with checking if a row has 3 of the same symbol
			if sum(x) == 3:
				score = 1
			elif sum(x) == -3:
				score = -1

			# Now checking each col
			if self.board_state[0][col_index] + self.board_state[1][col_index] + self.board_state[2][col_index] == 3:
				score = 1
			elif self.board_state[0][col_index] + self.board_state[1][col_index] + self.board_state[2][col_index] == -3:
				score = -1

			col_index += 1
		
		# Checking for a diagnal win
		if self.board_state[0][0] + self.board_state[1][1] + self.board_state[2][2] == 3 or self.board_state[0][2] + self.board_state[1][1] + self.board_state[2][0] == 3: 
			score = 1
		elif self.board_state[0][0] + self.board_state[1][1] + self.board_state[2][2] == -3 or self.board_state[0][2] + self.board_state[1][1] + self.board_state[2][0] == -3: 
			score = -1

		return score
		
	    

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	    

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		for row in range(rows):
			for col in range(cols):
				if self.board_state[row][col] == 0:
					moves.append([col, row])

		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[y][x] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
