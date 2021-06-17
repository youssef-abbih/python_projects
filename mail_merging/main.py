names_list = []
txt = "[name]"
with open("Input/Names/invited_names.txt") as names:
	names_list = [name.strip('\n') for name in names.readlines()]
with open('Input/Letters/starting_letter.txt',mode = "r") as letter:
	letter_content = letter.read()
	for name in names_list:
		new_letter = letter_content.replace(txt,name)
		with open(f"Output/ReadyToSend/letter_to_{name}.txt",mode = "w") as sent_letter:
			sent_letter.write(new_letter)

