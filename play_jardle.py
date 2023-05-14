from typing import List
from letter_state import LetterState
from jardle import Jardle
from colorama import Fore
import random

def main():
    print("Hello Jardle!")
    jardle = Jardle("えんぴつ")
    
    while jardle.can_attempt: 
        x = input("\nType Your guess: ")

        if len(x) != jardle.WORD_LENGTH:
            print(Fore.RED 
                  + f"Word must be {jardle.WORD_LENGTH} characters long." 
                  + Fore.RESET)
            continue
        jardle.attempt(x)
        display_results(jardle)
        # result = jardle.guess(x)
        # print(*result, sep="\n")
    # the asterisk splits the texts

    if jardle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("Sorry, you did not solve the puzzle.")

def display_results(jardle: Jardle):
    print("\nYour results so far..\n")
    print(f"You have {jardle.remaining_attempts} attempts remaining.")

    lines = []

    for word in jardle.attempts:    
        result = jardle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(jardle.remaining_attempts):
        lines.append(" ".join(["_"] * jardle.WORD_LENGTH))
    
    draw_border_around(lines)

def convert_result_to_color(result: List[LetterState]):
    result_with_color =[]
    for letter in result: 
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else: 
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return "".join(result_with_color)

def draw_border_around(lines: List[str], size: int=9, pad: int=1):
    
    content_length= size + pad * 2 
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + " │ ")
    
    print(bottom_border)

if __name__ == "__main__":
    main()