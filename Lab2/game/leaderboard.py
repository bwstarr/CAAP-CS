
from scores import Score

class Leaderboard(object):
	board = []

	def __init__(self):
		for i in range(1):
			self.board.append(Score("Dummy Chickens On Strike", 500, 500))

	def print_board(self, num):
		leaderboard_num = []
		board_copy = self.board.copy()
		comp = ''
		for i in range(min(num, len(self.board))):
			comp = board_copy[0]
			k = 1
			while k<len(board_copy):
				if comp.get_gen()>(board_copy[k].get_gen()):
					comp = board_copy[k]
				k += 1
			leaderboard_num.append(comp)
			board_copy.remove(comp)
		for i in range(len(leaderboard_num)):
			rank = i+1
			print(str(rank) + " Name: " + str(leaderboard_num[i].get_name()) + " Difficulty (# of lives): " + str(leaderboard_num[i].get_dif()) + " Score: " + str(leaderboard_num[i].get_score()))
			

	#checks if given score should be in the leaderboard
	def update(self, score):
		if len(self.board)<100:
			self.board.append(score)
		else:
			comp = self.board[0]
			k = 1
			while k<len(self.board):
				if comp.get_gen()<(self.board[k].get_gen()):
					comp = self.board[k]
				k += 1
			if comp.get_gen()>=score.get_gen():
				self.board.append(score)
				self.board.remove(comp)