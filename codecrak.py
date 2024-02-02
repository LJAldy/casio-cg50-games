import random

def generate_secret_code(mode):
    if mode == 1:
        return unique_random_sample(range(6), 4)
    elif mode == 2:
        return unique_random_sample(range(8), 4)
    elif mode == 3:
        return unique_random_sample(range(10), 5)

def unique_random_sample(population, k):
    indices = list(range(len(population)))
    selected_indices = []
    for _ in range(k):
        selected_index = random.randint(0, len(indices) - 1)
        selected_indices.append(indices[selected_index])
        indices.remove(indices[selected_index])
    return [population[i] for i in selected_indices]

def evaluate_guess(secret_code, guess):
    correct_color_and_position = sum(1 for i, j in zip(secret_code, guess) if i == j)
    correct_color_only = sum(min(secret_code.count(color), guess.count(color)) for color in set(guess)) - correct_color_and_position
    return correct_color_and_position, correct_color_only

def print_guess_feedback(list_of_guesses):
    index = 0
    print(9*"\n")
    for guess, correct_position, correct_color_only in list_of_guesses:
        index += 1
        formatted_guess = "".join(map(str, guess))
        if index % 2 == 1:
            guess_line = formatted_guess +" "+ str(correct_position) +" "+ str(correct_color_only+correct_position)
        else:
            print(guess_line+" | "+formatted_guess +" "+ str(correct_position) +" "+ str(correct_color_only+correct_position))
    if index % 2 == 1:
        print(guess_line)
    for i in range(6-((index+1)//2)):
        print("")

def is_valid_input(guess, mode):
    guess_len = 4
    if mode == 1:
        range_check = all(x in range(6) for x in guess)
    elif mode == 2:
        range_check = all(x in range(8) for x in guess)
    elif mode == 3:
        range_check = all(x in range(10) for x in guess)
        guess_len = 5
    return len(guess) == guess_len and range_check and len(set(guess)) == len(guess)

def select_game_mode():
    while True:
        print("\n\n\n[1] 4-Digit, 0-5\n[2] 4-Digit, 0-7\n[3] 5-Digit, 0-9")
        mode = input("Mode: ")
        if mode in ["1","2","3"]:
            return int(mode)

def play_codecrak():
    mode = select_game_mode()
    secret_code = generate_secret_code(mode)
    attempts = 1
    list_of_guesses = []
    message = "Guess 1"
    while True:
        print_guess_feedback(list_of_guesses)
        try:
            guess = [int(x) for x in input(message + (10-len(message))*" " + ": ")]
        except:
            message = "Invalid"
            continue
        if not is_valid_input(guess, mode):
            message = "Invalid."
            continue
        attempts += 1
        message = "Guess " + str(attempts)
        feedback = evaluate_guess(secret_code, guess)
        list_of_guesses.append([guess, feedback[0], feedback[1]])

        if feedback[0] == len(secret_code):
            print_guess_feedback(list_of_guesses)
            message = "Cracked in " + str(attempts-1) + "!"
            return message

        if attempts == 13:
            print_guess_feedback(list_of_guesses)
            message = "Max tries: " + "".join(map(str, secret_code))
            return message

print("\n\n\n\n\n\nWelcome to CodeCrak!")
input()
print("For each guess\nyou will see:")
input()
print("\n- The guessed code\n- Number of digits\nin correct position\n- Number of digits\nin the final code")
input()
while True:
    x=input(play_codecrak())
