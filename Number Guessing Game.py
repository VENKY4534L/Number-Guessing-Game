import random

def number_guessing_game():
    print("\n🎮 Welcome to the Number Guessing Game! 🎮")
    best_score = None

    while True:
        # Difficulty Selection
        print("\nSelect Difficulty Level:")
        print("1. Easy (1–10)")
        print("2. Medium (1–50)")
        print("3. Hard (1–100)")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            max_range = 10
        elif choice == '2':
            max_range = 50
        elif choice == '3':
            max_range = 100
        else:
            print("Invalid choice. Defaulting to Easy level.")
            max_range = 10

        secret_number = random.randint(1, max_range)
        attempts = 0

        print(f"\nI have selected a number between 1 and {max_range}. Try to guess it!")

        # Game Loop
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter only numbers!")
                continue

            attempts += 1

            if guess < secret_number:
                print("🔼 Higher!")
            elif guess > secret_number:
                print("🔽 Lower!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break

        # Track best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"🏆 New Best Score: {best_score} attempts!")

        # Replay Option
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Goodbye 👋")
            break


# Run the game
number_guessing_game()
