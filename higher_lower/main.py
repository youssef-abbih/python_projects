from art import logo, vs
from game_data import data
from random import choice


def check_answer(guess,a,b):
  if a['follower_count'] > b['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'

def play():
  score = 0
  gameOver = False
  print(logo)
  a= choice(data)
  b= choice(data)
  while not gameOver:
    a = b
    b = choice(data)
    while a == b:
      b = choice()
    print(f"Compare A: {a['name']},a {a['description']}, from {a['country']}")

    print(vs)
    print(f"Against B: {b['name']},a {b['description']}, from {b['country']}")

    guess = input('Who has more followers? Type \'A\' or \'B\':').lower()
    is_correct = check_answer(guess,a,b)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      gameOver = True
      print(f"Sorry, that's wrong. Final score: {score}")

play()  
