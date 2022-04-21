import random
from words import words
import string 
import time




nicemsg = ["You guessed right! Nice :)", "Wow. It was correct. :)", "Great job :>"]
meanmsg = ["That was incorrect. :(", "Try to get it with 6 lives.", "Meh. :<"]
nice = random.choice(nicemsg)
mean = random.choice(meanmsg)




#My own addition: Fake loading screen for 10 seconds before game starts. I call on this function down below before game starts.

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Loading...')

    


def get_valid_word(words):
    word = random.choice(words)
    while '-' or ' ' or 'Rai' or 'Zimmerman' in word:
        word = random.choice(words)
        return word.upper

def hangman():
    word = get_valid_word(words)
    word_letters = set(word())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6




    while len(word_letters) > 0 and lives > 0:
        time.sleep(1)
        print('You have' , lives, ' lives left.' 'You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word()]
        print('Current word: ', ' '.join(word_list)) 
        #
        #
        #
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
        elif user_letter in used_letters:
            time.sleep(1)
            print('You already guess this! :|')
        else:
            time.sleep(1)
            print("Invalid character. Try again. :< ")
    if lives == 0:
        print( ''' 
   +---+
       |
       |
       |
     ===''') 
    elif lives == 1:
        print('''
   +---+
   O   |
       |
       |
      ===''')
    elif lives == 2:
        print('''
   +---+
   O   |
   |   |
       |
     ===''')
    elif lives == 3:
        print('''
   +---+
    O   |
   /|   |
        |
      ===''')
    elif lives == 4:
        print('''
   +---+
   O   |
  /|\  |
       |
      ===''')
    elif lives == 5:
        print('''
   +---+
   O   |
  /|\  |
  /    |
      ===''')
    else:
        print('''
   +---+
   O   |
  /|\  |
  / \  |
      ===''')
        
    if lives < 6:
        print(mean)
    elif lives == 0:
        print(nice)




if __name__ == '__main__':
    countdown(10)
    hangman()


