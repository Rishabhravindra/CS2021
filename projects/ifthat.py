def if_this_not_that(i_list, this):
	"""
	>>> original_list = [1, 2, 3, 4, 5]
 	>>> if_this_not_that(original_list, 3)
 	that
 	that
 	that
 	4
 	5
 	"""
	for e in i_list:
		if(e>this):
			print (e)
		else:
			print ("that")
def replace_all(d,x,y):
	for k in d:
		if d[k]==x:
			d[k] = y

def make_prediction(name, guess):
	return [name, guess]
def get_name(pred):
	return pred[0]
def get_guess(pred):
	return pred[1]
winningpred = min(predictions, key = lambda x: abs(get_guess-correctno))
print (get_name(winningpred))

def makeDir(secret):
	def direction(guess):
		if(guess > secret):
			return 1
		elif (guess < secret):
			return -1
		else:
			return 0
	return direction