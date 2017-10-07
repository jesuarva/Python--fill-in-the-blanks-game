def live():
	'''Randomly asign number of lives
		Number no greater than the number of words to guess'''
	lives = random.randint(1,maximum+1)
	return lives
# def live():
# 	'''Allow user to select the number of lives'''
# 	lives = 0
# 	maximum = len(words)
# 	print '''	Selec a number of lives for level "'''+level+'''""
# 	MAXIMIM ALLOWED LIVES: '''+str(maximum)
# 	lives = raw_input('''	''')
# 	if int(lives) not in range(1,maximum+1):
# 		print '''
# 	Oops, it seems you are so ambitious...
# 	Fit in the allowed maximum lives to continue...'''
# 		lives = live()
# 		return int(lives)
# 	return int(lives)
# def live():
# 	'''Allow user to select the number of lives'''
# 	lives = 0
# 	maximum = len(words)
# 	while  int(lives) not in range(1,maximum):
# 		print '''
# 	Selec a number of lives for level "'''+level+'''""
# 	NUMBER NO GREATER THAN '''+str(maximum)
# 		lives = raw_input('''	''')
# 		print lives
# 	return int(lives)
