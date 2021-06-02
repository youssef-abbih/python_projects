alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  empty_text = ""
  if shift > 26:
    shift %= 26
  for letter in text:
    if letter in alphabet:
      if direction == 'encode':
        new_position = alphabet.index(letter) + shift
        if new_position >= len(alphabet):
          new_position -= len(alphabet)
      elif direction =='decode':
        new_position = alphabet.index(letter) - shift
      empty_text += alphabet[new_position]
    else:
      empty_text += letter
  print(empty_text)
