class Score(object):
	name = 'player'
	score = 0
	dif = 0
	gen_score = 0

	# initializes score and players name
	def __init__(self, name, score, dif):
		self.name = name
		self.score = score
		self.dif = dif
		self.gen_score = 1000*dif +score

	# returns the name associated with score
	def get_name(self):
		return self.name

	# returns score of player
	def get_score(self):
		return self.score

	def get_dif(self):
		return self.dif

	def get_gen(self):
		return self.gen_score