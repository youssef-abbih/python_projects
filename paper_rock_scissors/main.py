import random
from art import rock, paper, scissors

user_choice = input('enter your choice ')
if user_choice == "rock":
  print(f'rock\n{rock}')
elif user_choice == "paper":
  print (f'paper\n{paper}')
elif user_choice == "scissors":
  print(f'scissors\n{scissors}')

computer_choice =[rock, paper, scissors]
computer_choice = random.choice(computer_choice)
print(f'computer choice{computer_choice}')
if computer_choice == "rock":
  print(f'rock\n{rock}')
elif computer_choice == "paper":
  print (f'paper\n{paper}')
elif computer_choice == "scissors":
  print(f'scissors\n{scissors}')



if (user_choice =="rock" and computer_choice == rock) or (user_choice == "paper" and computer_choice == paper) or (user_choice == "scissors" and computer_choice == scissors):
  print('draw')
elif (user_choice =="rock" and computer_choice == scissors) or (user_choice == "paper" and computer_choice == rock) or (user_choice == "scissors" and computer_choice == paper):
  print('you Win')
else:
  print('you Lose')
