import pandas as pd

file =pd.read_csv("nato_phonetic_alphabet.csv", index_col=0, squeeze=True).to_dict()

NATO_alphabet = {alphabet : names for alphabet,names in file.items()}



name = input("Enter your name ").upper()

phonetic = [NAto_alphabet[key] for key in name if key in file]

print(phonetic)
