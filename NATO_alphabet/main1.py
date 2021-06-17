import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

NATO = {row.letter:row.code for index,row in df.iterrows()}

name = input("Enter your name ").upper()
phonetic = [NATO[key] for key in name if key in NATO]
print(phonetic)

