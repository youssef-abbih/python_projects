from random import choice
from art import logo

def deal_card():
  """Retourn a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def blackjack():
  print(logo)
  gameOver = False
  user_cards =[]
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not gameOver:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    string = f"""Your cards: {user_cards}, current score: {user_score} 
Computer's first card: {computer_cards[0]}"""
    final = f"""Your final hand: {user_cards}, final score: {user_score} 
Computer's final hand: {computer_cards}, final score: {computer_score} 
  """
    print(string)
    if user_score == 0 or computer_score == 0 or user_score > 21:
      gameOver = True
    else:
      continu = input("Type 'y' to get another card, type 'n' to pass:")
      if continu == 'y':
        user_cards.append(deal_card())
      else:
        gameOver = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(final)
  print(compare(user_score, computer_score))

  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()

blackjack()
