import random

def number_guessing_game():
    while True:
        print("\nNumber Guessing Game Menu")
        print("1. Start New Game")
        print("2. Exit")
        
        choice = input("Select an option (1-2): ")
        
        if choice == '2':
            print("Exiting game. Goodbye!")
            break
        
        if choice == '1':
            number = random.randint(1, 100)
            attempts = 0
            
            while True:
                guess = int(input("Guess the number (between 1 and 100): "))
                attempts += 1
                
                if guess < number:
                    print("Too low! Try again.")
                elif guess > number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
        else:
            print("Invalid choice. Please select a valid option.")

number_guessing_game()
