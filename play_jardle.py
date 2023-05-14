from typing import List
from letter_state import LetterState
from jardle import Jardle
from colorama import Fore
import random

def main():
    print("Hello Jardle!")
    jardle = Jardle("えんぴつ")
    
    while jardle.can_attempt: 
        x = input("Your guess: ")

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
    for word in jardle.attempts:    
        result = jardle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    pass

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

if __name__ == "__main__":
    main()