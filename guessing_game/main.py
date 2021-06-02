from random import randint
from art import logo


EASY_MODE = 10
HARD_MODE = 5

def lives():
  dificulty = input("Choose a dificulty, type 'easy' or 'hard' ")
  if dificulty == 'easy':
    return EASY_MODE
  else:
    return HARD_MODE

def check_answer(guess, number, lives_number):
  if guess > number:
    print('Too high')
    return lives_number - 1
  elif guess == number:
      print(f'Correct, the number is {number}')
      return
  else:
    print('Too low')
    return lives_number - 1

def game():
  print(logo)
  number = randint(1,100)
  lives_number = lives()
  guess = 0
  while guess != number:
    print(f"You have {lives_number} attempts remaining to guess the number.")
    guess = int(input('Enter a number between 1 and 100 '))
    lives_number = check_answer(guess, number, lives_number)
    
    if lives_number == 0:
      print('you run out of lives')
      break
    elif guess != number:
      print('guess again')


game()
