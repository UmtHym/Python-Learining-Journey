from database import save_score, get_top_scores
import random

while True: # Main game loop
    # Set up difficulty first
    while True: # Difficulty selection loop
        print("\n1. Easy (1-50, 15 guesses)")
        print("2. Medium (1-100, 10 guesses)")
        print("3. Hard (1-200, 7 guesses)")

        try:
            difficulty = int(input("Choose difficulty (1-3): "))
            if difficulty in [1,2,3]: # Check valid choice
                break # Exit difficulty section loop
            else:
                print('please choose 1,2, or 3')
        except ValueError:
            print("Please enter a number!")
    # Set game parameters based on difficulty
    if difficulty == 1:
        difficulty_name = 'easy'
        max_number = 50
        max_guesses = 15
        print(f'Difficulty set to {difficulty_name}')
    elif difficulty == 2:
        difficulty_name = 'medium'
        max_number = 100
        max_guesses = 10
        print(f'Difficulty set to {difficulty_name}')
    elif difficulty == 3:
        difficulty_name = 'hard'
        max_number = 200
        max_guesses = 7
        print(f'Difficulty set to {difficulty_name}')

    #initialise game variables
    random_num = random.randint(1, max_number)
    number_of_guesses = 0
    user_guess = None

    # Main game loop
    while user_guess != random_num and number_of_guesses < max_guesses:
        remaining_guesses = max_guesses - number_of_guesses
        print('You have ' + str(remaining_guesses) + ' guesses left')

        try:
            user_guess = int(input('Guess a number betweeen 1 and ' + str(max_number) + ':'))
        except ValueError:
            print('Please enter a valid number!')
            continue

        number_of_guesses = number_of_guesses + 1

        if user_guess == random_num:
            print('Nice guess ' + str(user_guess) + ' is true!')
            print('You took ' + str(number_of_guesses) + ' guesses!')

            player_name = str(input("Enter your name for high score: "))
            save_score(player_name, number_of_guesses, difficulty_name)
            
            print("\nTop Scores for this difficulty: ")
            top_scores = get_top_scores(difficulty_name)
            for name, score in top_scores:
                print(f"{name}: {score} guesses")

        elif user_guess < random_num:
            print('Too low! Try again!')
        else: 
            print('Too high! Try again!')

    if number_of_guesses >= max_guesses and user_guess != random_num:
        print('Game Over! The number was ' + str(random_num))

    play_again = input('Want to play again? (yes/no): ').lower()
    if play_again != 'yes' :
        print('Thanks for playing!')
        break