from art import logo
from caesar import caesar

print(logo)

end = False
while not end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction = direction, text = text, shift = shift)
  restart = input('Type\'yes\' if you want to go again, otherwise \'no\' ')
  if restart == "no":
    end = True
    print("Goodbye")
