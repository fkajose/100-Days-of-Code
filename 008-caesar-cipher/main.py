alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"""
    Here's the {cipher_direction}d result: {end_text}
    """)

import art
print(art.logo)
print("""
Ceaser Cipher is an encryption method that substitues letters in a text with other letters at fixed positions down the alphabet. 
For example:
    encoding 'blue' by a shift of 3 would give 'eoxh'
    decoding 'eoxh' by a shift of 3 would give 'blue'
    """)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26 #prevents error when shift is greater than 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Would you like to rerun? Type 'yes' or 'no'.\n")
    if restart == "no":
        end = True
        print("Goodbye!")
