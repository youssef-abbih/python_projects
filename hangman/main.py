from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
end_of_game = True
display = []
print(logo)
word = choice(word_list)
for _ in range(len(word)):
  display+=("_")
prev_letter = ""


while end_of_game:
  letter = input("choose a letter: ")
  if(prev_letter == letter):
    print("you already guessed this letter")
    prev_letter = ""
  prev_letter = letter
  for position in range(len(word)):
    if word[position] == letter:
      display[position] = letter
  print(''.join(display))
  if letter not in word:
    print(f"{letter} is not in this word")
    print(stages[lives])
    lives-=1
    if lives == 0:
      print(stages[lives])
      print(f'Game Over, the word is {word}')
      end_of_game = False
  elif '_' not in display:
    print('You Win')
    end_of_game = False
