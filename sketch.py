paragraph = {
			 '1': 'Loren Ipsum',
			 '2': 'Loren Ipsum',
			 '3': 'Loren Ipsum',
			 }
print paragraph['1']

words = [{'easy': ['hola', 'caracola'], '2': 'hola caracola 2', '3': '', '4': ''},
		 {'1': '', '2': '', '3': '', '4': '', '5': ''},
		 {'1': '', '2': '', '3': '', '4': '', '5': '', '6': ''}]

print words[0]['easy']
print words[0]['2']
if 1 in words[0]:
	print 'Ole'
else:
	print 'uhu, ahi no esta'
if '1' in words[0]:
	print 'Ole'
else:
	print 'uhu, ahi no esta'

def play_game():
	while continue_playing():
		print_paragraph()
		prompt_user()
		guessed_word_is_correct()

# print_paragraph()
# prompt_user()
def play_game():
	while continue_playing():
		if guessed_word_is_correct() == False:
			lives -= 1
		else:
			count_of_guessed_words += 1

	return 'Game Over'

def play_game():
	while continue_playing():
		if count_of_guessed_words == len(words):
			print_paragraph()
			return 'You win!! Great'
		else:
			if guessed_word_is_correct() == False:
				lives -= 1
			else:
				count_of_guessed_words += 1
		print_paragraph()
		prompt_user()

	return 'Game Over'

listi = []
listi.append('algo')
print listi[0]

testing_set = set('Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.'.split())
print 'testing_set'
print testing_set.pop()
testing_set = set('Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.')
print 'testing_set'
print testing_set.pop()



'''
Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.
'''
# VARIABLES
welcome_message = '''
*-------------------------------------------------------*
	WELCOME TO FILL IN THE BLANKS GAME by JESUARVA'''
# level_difficulty = {'easy': 1, 'medium': 2, 'hard': 3}
level_selected = ''
lives = 0
count_of_guessed_words = 0
guessed_word = ''
paragraph = []
words = []
set_of_words = set()
level_difficulty = {'easy': ['Spicy jalapeno bacon ipsum dolor amet ball tip capicola meatloaf beef ribs, ham hock biltong shank pork filet mignon sirloin turducken bacon ground round. T-bone jerky pork loin capicola ground round rump salami tri-tip filet mignon tongue pancetta pork chop. Venison flank swine ham hock landjaeger, doner meatloaf jowl ribeye salami t-bone. Pork burgdoggen strip steak turkey, pancetta tongue meatloaf brisket cupim chuck filet mignon pastrami flank bacon beef ribs. Pancetta salami tri-tip, meatball t-bone prosciutto burgdoggen jowl leberkas kevin.',
							 ['____1____', '____2____', '____3____', '____4____']
							],
					'medium': ['Loren Ipsum-2',['____1____', '____2____', '____3____', '____4____', '____5____']],
		 			'hard': ['Loren Ipsum-3',['____1____', '____2____', '____3____', '____4____', '____5____', '____6____']]
		 			}
# END VARIABLE
print 'TESTING 2'
print level_difficulty['easy'][1]
words = level_difficulty['easy'][1]
print len(words)

# TEST raw_imput WITH NO ARGUMENT
guessed_words = 0
print 'Type your guessed word for ___'+str(guessed_words+1)+'___ :'

ho = -1
print ho