import random
while True:

    random_num = random.randint(1, 100)
    number_of_guesses = 0
    user_guess = None
    max_guesses = 10

    while user_guess != random_num and number_of_guesses < max_guesses:
        remaining_guesses = max_guesses - number_of_guesses
        print('You have '+ str(remaining_guesses) + ' guesses left')

        try:
            user_guess = int(input('Guess a number between 1 and 100:'))
        except ValueError:    
            print('Insert a valid number!') 
            continue

        number_of_guesses = number_of_guesses + 1
            
        if user_guess == random_num:
            print('Nice guess! ' + str(user_guess) + ' is true!')
            print(str('You took ' + str(number_of_guesses) + ' guesses!'))
            
        elif user_guess < random_num:
            print('Too low! Try again!')
        else:
            print('Too high! try again!')

    if number_of_guesses >= max_guesses and user_guess != random_num:
        print('Game Over! The number was ' + str(random_num))

    play_again = input('Want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        print('Thanks for playing!')
        break   