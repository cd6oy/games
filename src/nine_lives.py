import random


lives = 9

words = ['happy', 'pizza', 'otter', 'sixty', 'truck', 'teeth', 'night', 'light', 'fight', 'hight']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol =u'♥ '

guessed_word_correctly = False

def find_question_mark(clue):
    has_question_mark = False
    index = 0
    while index < len(clue):
        if '?' == clue[index]:
            has_question_mark = True
            break
        else:
            index = index + 1
    return has_question_mark
 
def update_clue(guessed_letter, seceret_word, clue):
    index = 0
    
    while index < len(seceret_word):
        if guessed_letter == seceret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

# this is main function
while lives > 0:
        print(clue)
        print('lives left: ' + heart_symbol * lives)
        
        guess = input('guess a letter or the whole word: ')


        if guess == secret_word:
            guessed_word_correctly = True
            break

        if guess in secret_word:
            update_clue(guess, secret_word, clue)
            if find_question_mark(clue) == False:
                guessed_word_correctly =  True
                break
        else:
            print('Incorrect. You lose a life')
            lives = lives - 1


if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('you lost! The secret word was ' + secret_word)
