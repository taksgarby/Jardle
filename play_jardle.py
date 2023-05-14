from jardle import Jardle

def main():
    print("Hello Jardle!")
    jardle = Jardle("えんぴつ")
    
    while jardle.can_attempt: 
        x = input("Your guess: ")

        if len(x) != jardle.WORD_LENGTH:
            print(f"Word must be {jardle.WORD_LENGTH} characters long.")
            continue
        jardle.attempt(x)
        result = jardle.guess(x)
        print(*result, sep="\n")
    # the asterisk splits the texts

    if jardle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("Sorry, you did not solve the puzzle.")

if __name__ == "__main__":
    main()