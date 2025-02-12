from colorama import Fore, Style
import time

# logo
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def display_logo_with_animation():
    """Prints the logo with a typewriter animation and color."""
    # Print your custom name/version at the top
    title = "Caesar Cipher v1.0 by [Your Name]"
    print(Fore.CYAN + title.center(80) + Style.RESET_ALL)

    # Display the logo with typewriter animation
    for char in logo:
        print(Fore.GREEN + char + Style.RESET_ALL, end="", flush=True)
        time.sleep(0.005)  # Delay for animation effect

    print("\n")  # Add space after the logo

def caesar(start_text, shift_amount, caesar_direction):
    """Encodes or decodes text using the Caesar Cipher."""
    new_text = ""
    if caesar_direction == "decode":
        shift_amount *= -1  # Reverse shift for decoding

    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            new_text += alphabet[new_position]
        else:
            new_text += char  # Leave non-alphabet characters as is

    print(f"\nThe {caesar_direction}d text is: {Fore.YELLOW}{new_text}{Style.RESET_ALL}\n")

# Main program
def main():
    display_logo_with_animation()

    should_continue = True
    while should_continue:
        # User input
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ["encode", "decode"]:
            print(Fore.RED + "Invalid option. Please type 'encode' or 'decode'.\n" + Style.RESET_ALL)
            continue

        text = input("Type your message:\n")
        shift = input("Type the shift number:\n")

        # Validate shift input
        if not shift.isdigit():
            print(Fore.RED + "Shift must be a number. Please try again.\n" + Style.RESET_ALL)
            continue

        shift = int(shift) % 26  # Ensure shift wraps around alphabet
        caesar(text, shift, direction)

        # Check if user wants to continue
        result = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
        if result == "no":
            should_continue = False
            print(Fore.CYAN + "Goodbye! Thanks for using the Caesar Cipher tool." + Style.RESET_ALL)

# Run the program
if __name__ == "__main__":
    main()
