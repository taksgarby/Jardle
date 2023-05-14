from jardle import Jardle

def main():
    print("Hello Jardle!")
    jardle = Jardle("えんぴつ")
    
    while jardle.can_attempt: 
        x = input("Your guess: ")
        jardle.attempt(x)
        result = jardle.guess(x)
        print(result)
    
    if jardle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("Sorry, you did not solve the puzzle.")

if __name__ == "__main__":
    main()