from jardle import Jardle

def main():
    print("Hello Jardle!")
    jardle = Jardle("えんぴつ")
    
    while True: 
        x = input("Your guess: ")
        if x == jardle.secret:
            print("Well done!")
            break
        print("Not quite.")

if __name__ == "__main__":
    main()