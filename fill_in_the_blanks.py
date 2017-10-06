

'''
Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.
'''
# VARIABLES
welcome_message = '''
*-------------------------------------------------------*
	WELCOME TO FILL IN THE BLANKS GAME by JESUARVA'''
# level_difficulty = {'easy': 1, 'medium': 2, 'hard': 3}
level = ''
lives = 0
list_of_guessed_words = []
guessed_words = 0
paragraph = []
words = []
# set_of_words = set()
level_difficulty = {'easy': ['Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.',
							 ['____1____', '____2____', '____3____', '____4____']
							],
					'medium': ['Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.',
							   ['____1____', '____2____', '____3____', '____4____', '____5____']
							  ],
		 			'hard': ['Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.',
		 					 ['____1____', '____2____', '____3____', '____4____', '____5____', '____6____']
		 					]
		 			}
# END VARIABLE

# FUNCTIONS
def select_number_words(set_of_words, words):
	count = 0
	while count < len(words):
		words[count] = set_of_words.pop() #ALWAYS RETURN THE SAME WORDS FOR A GIVEN FIXED SET ¿WHY THAT?
		count += 1
def assign_words(level, words):
	'''Select the words to guess from the paragraph'''
	split = paragraph[0].split()
	set_of_words = set(split)
	select_number_words(set_of_words, words)
	# print level_selected
	return ''
def level_selected():
	level = raw_input('''	
	Seletc a level. Please type one of the following:
	-> easy
	-> medium
	-> hard
	''')
	paragraph.append(level_difficulty[level][0])
	words = list(level_difficulty[level][1])
	list_of_guessed_words = list(level_difficulty[level][1])
	assign_words(level, words)
	return level, words, list_of_guessed_words
def print_paragraph():
	'''SET PARAGRAPH TO PRINT'''
	paragraph_to_print = paragraph[0]
	index = 0
	while index < len(words):
		split = paragraph_to_print.split(words[index])
		paragraph_to_print = list_of_guessed_words[index].join(split)
		index += 1
	print '''
*-------------------------------------------------------*
		PARAGRAPH TO FILL IN THE BLANKS
'''+paragraph_to_print
def live():
	'''Allow user to select the number of lives'''
	lives = raw_input('''
	Selec a number of lives for your game
	''')
	return int(lives)
def continue_playing(lives):
	'''while lives > 0 -> continue playing'''
	if lives > 0:
		return True
	return False
def prompt_user(lives, guessed_words, words):
	'''Get guessed word from user'''
	'''Include a message warning the number of lives left'''
	print '''
	You have '''+str(lives)+''' lives remaining'''
	print '''
	Type your guessed word for ___'''+str(guessed_words+1)+'''___ :'''
	list_of_guessed_words[guessed_words] = raw_input('''	''')
	return ''
def guessed_word_is_correct(guessed_words):
	'''To check if guessed word is correct'''
	if list_of_guessed_words[guessed_words] == words[guessed_words]:
		return True
	return False
def is_winner(guessed_words, words):
	if guessed_words == len(words):
		return True
	return False
def play_game(list_of_guessed_words, guessed_words, lives, words):
	while continue_playing(lives):
		print_paragraph()
		prompt_user(lives, guessed_words, words)
		if guessed_word_is_correct(guessed_words) == False:
			lives -= 1
		else:
			guessed_words += 1
		if is_winner(guessed_words, words):
			print_paragraph()
			return '''
*-------------------------------------------------------*
|	YOU WIN!!! Amazing, That was no easy                |
*-------------------------------------------------------*'''
	return '''
		YOU LOSE - GAME OVER
*-------------------------------------------------------*'''
#END FUNCTIONS

# PLAY GAME
import random
print welcome_message
level, words, list_of_guessed_words = level_selected()
lives = live()
print play_game(list_of_guessed_words, guessed_words, lives, words)
# END PLAY GAME


#TESTING
# print continue_playing() #OK
# level, words = level_selected()
# print paragraph
# print assign_words('easy', words) #OK
# # TEST raw_imput WITH NO ARGUMENT
# guessed_words = 0
# print 'Type your guessed word for ___'+str(guessed_words+1)+'___ :'
# raw_input('''	''')
# #
# print guessed_word_is_correct(guessed_words)
# print guessed_words
# while continue_playing(lives) == False and guessed_words == 0:
# 	print 'seems to work'
# 	continue_playing = True