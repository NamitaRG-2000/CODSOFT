import random

print("=== Rock Paper Scissors ===")

options = ['rock', 'paper', 'scissors']

while True:
    user = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user == 'exit':
        print("Thanks for playing!")
        break

    if user not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")
