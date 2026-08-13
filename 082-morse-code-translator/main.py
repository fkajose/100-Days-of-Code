import json

with open("082-morse-code-translator/dictionary.json", "r") as file:
    dictionary = json.load(file)
    revd_dictionary = dict()
    for idx, key in enumerate(dictionary):
        revd_dictionary[dictionary[key]] = key


print("Welcome to the Morse Code Translator!")
print(
    "You can translate any text to Morse code or translate Morse code back to regular text."
)
print("To translate from Morse Code to text, enter 'm'")
print("To translate from regular text to Morse Code, enter 'r'")

while True:
    morse_or_text = input("Morse Code or Regular Text? Type 'm' or 'r':").lower()

    if morse_or_text == "r":
        source = input("Enter your text here:").lower()
        translated = source.replace(" ", "/ ")
        for idx, letter in enumerate(dictionary):
            if letter in source:
                translated = translated.replace(letter, f"{dictionary[letter]} ")
        break
    elif morse_or_text == "m":
        source = input("Enter your text here:").lower()
        words = source.strip().split(" / ")
        text_words = []
        for word in words:
            letters = []
            for code in word.split(" "):
                if not code:
                    continue
                letter = revd_dictionary.get(code)
                if letter:
                    letters.append(letter)
                else:
                    print(f"Warning: unrecognized Morse code '{code}', skipping.")
            text_words.append("".join(letters))
            translated = " ".join(text_words)
        break
    else:
        print("Invalid input, please enter a valid input")
        continue


print(translated)
