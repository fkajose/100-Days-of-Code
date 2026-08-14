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
    morse_or_text = input("Morse Code or Regular Text? Type 'm' or 'r':").upper()

    if morse_or_text == "R":
        source = input("Enter your text here:").upper()
        translated = source.strip()
        unique_chars = set(source)
        for char in unique_chars:
            if char in dictionary.keys():
                translated = translated.replace(char, f"{dictionary[char]} ")
        break
    elif morse_or_text == "M":
        source = input("Enter your text here:").upper()
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
