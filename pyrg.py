import random
#function for the guess
def guess_game(guessLim,number):
    randomNumber = random.randint(1,number)
    try:
        while guessLim >0:
            guess= int(input('what is your guess? '))
            guessLim -=1
            if randomNumber == guess:
                print('congrats, you got the correct number! ')
                break
            elif guess > number:
                print('your guess is higher than the random number! ')
                print(f'you have {guessLim} guess(es) left ')
            else:
                print('sorry, wong guess! ')
                print(f'you have {guessLim} guess(es) left ')
        print('Game Over!')
        print(f'The Random number was {randomNumber} ')
    except ValueError:
        print('please use only integer values ')

def easy():
    print('Guess a number between 1 and 10, you have 5 guesses ')
    guess_game(5,10)

def medium():
    print('Guess a number between 1 and 20, you have 4 guesses ')
    guess_game(4,20)
def hard():
    print('Guess a number between 1 and 20, you have 3 guesses ')
    guess_game(3,20)
def tryAgain():
    again = input('Do you want to try agian? Y/N ')
    if again.upper()=='Y':
        welcome()
    elif agian.upper()=='N':
        print('Thank you for playing ')
    else:
        print('wrong input ')
        tryAgain()
def welcome():
    print('Welcome to the guessing number game! ')
    gameDifficulty = input('chose you level between easy (E), medium(M) and hard(H) ')
    if gameDifficulty.upper() =='E':
        easy()
        tryAgain()
    elif gameDifficulty.upper() =='M':
        medium()
        tryAgain()
    elif gameDifficulty.upper() =='H':
        hard()
        tryAgain()
    else:
        print('This is wrong input try again ')
        welcome()

welcome()
        

