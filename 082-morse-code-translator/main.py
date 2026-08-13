import json

with open("082-morse-code-translator/dictionary.json", "r") as file:
    dictionary = json.load(file)


print("Welcome to the Morse Code Translator!")

source = input("Enter your text here:").lower()

translated = source.replace(" ", "/ ")
for idx, letter in enumerate(dictionary):
    if letter in source:
        translated = translated.replace(letter, f"{dictionary[letter]} ")


print(translated)
