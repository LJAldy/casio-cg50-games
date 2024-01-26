import random

def generate_secret_code():
    return [random.randint(1, 6) for _ in range(4)]

def evaluate_guess(secret_code, guess):
    correct_color_and_position = sum(1 for i, j in zip(secret_code, guess) if i == j)
    correct_color_only = sum(min(secret_code.count(color), guess.count(color)) for color in set(guess)) - correct_color_and_position
    return correct_color_and_position, correct_color_only

def print_feedback(correct_color_and_position, correct_color_only):
    print(f"Correct position: {correct_color_and_position}, Correct color: {correct_color_only}")

def is_winner(correct_color_and_position):
    return correct_color_and_position == 4

def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 0

    print("Welcome to Mastermind!")

    while True:
        guess = [int(x) for x in input("Enter your guess (4 digits): ")]
        
        if len(guess) != 4 or not all(1 <= x <= 6 for x in guess):
            print("Invalid input. Please enter 4 digits between 1 and 6.")
            continue

        attempts += 1
        feedback = evaluate_guess(secret_code, guess)
        print_feedback(*feedback)

        if is_winner(feedback[0]):
            print(f"Congratulations! You've guessed the code in {attempts} attempts.")
            break

        if attempts == 10:
            print(f"Sorry, you've reached the maximum attempts. The secret code was: {secret_code}")
            break

if __name__ == "__main__":
    while True:
        print("NOT WORKING RIGHT NOW")
        input()
    play_mastermind()
