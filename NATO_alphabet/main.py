import pandas as pd

file =pd.read_csv("nato_phonetic_alphabet.csv", index_col=0, squeeze=True).to_dict()

NATO_alphabet = {alphabet : names for alphabet,names in file.items()}
print(file)

name = input("Enter your name ").upper()
phonetic = []
for letter  in name:
    if letter in file:
        phonetic.append(file[letter])
print(phonetic)
