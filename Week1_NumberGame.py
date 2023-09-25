from random import randint

answer = randint(1, 10)
print('Guess the number game')
print()
print('I have thought of a number between one and ten. You must guess what it is')

guess = input('Enter your guess > ')
if int(guess) == answer:
    print('Well done! Your guessed number was ' + str(answer))
    
if int(guess) < answer:
    print('Sorry your guess was too low. The answer was ' + str(answer))
    
if int(guess) > answer:
    print('Sorry, your guess was too high. The answer was ' + str(answer))