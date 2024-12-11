from database import save_score
import random

while True: # Main game loop

    # Set up category first
        while True: # Category selection loop
            print("\n1. Geography ")
            print("2. Science ")
            print("3. Technology ")
            print("4. Mathematics ")

            try:
                category = int(input("Choose a category (1-4): "))
                if category in [1,2,3,4]: 
                    break 
                else:
                    print('please choose 1,2,3, or 4')
            except ValueError:
                print("Please enter a number!")

        # Set game parameters based on category and difficulty
        if category == 1:
            category_name = 'Geography'
            print(f'Category is set to {category_name}')
        elif category == 2:
            category_name = 'Science'
            print(f'Category is set to {category_name}')
        elif category == 3:
            category_name = 'Technology'
            print(f'Category is set to {category_name}')    
        elif category == 4:
            category_name = 'Mathematics'
            print(f'Category is set to {category_name}')     
    
        # Set up difficulty after
        while True: # Difficulty selection loop
            print("\n1. Easy ")
            print("2. Medium ")
            print("3. Hard ")

            try:
                difficulty = int(input("Choose difficulty (1-3): "))
                if difficulty in [1,2,3]: 
                    break 
                else:
                    print('please choose 1,2, or 3')
            except ValueError:
                print("Please enter a number!")
        # Set game parameters based on difficulty
        if difficulty == 1:
            difficulty_name = 'easy'
            print(f'Difficulty set to {difficulty_name}')
        elif difficulty == 2:
            difficulty_name = 'medium'
            print(f'Difficulty set to {difficulty_name}')
        elif difficulty == 3:
            difficulty_name = 'hard'
            print(f'Difficulty set to {difficulty_name}')

    
        #The Main game loop
        fhand = open('Questions.txt')

        questions_lines = {}

        for line in fhand:
            words = line.split() 

            if len(words) > 0:
                key = line[:1]
                value = line[3:].strip()
                questions_lines[key] = value
                
                if len(questions_lines) == 4 and questions_lines['T'] == category_name and questions_lines['D'] == difficulty_name:
                    break
                else:
                    continue
                    
        while True:
            apple = str(input(f'{questions_lines['Q']}'))
            user_answer = apple.lower()
            if user_answer == questions_lines['A']:
                print('Thats the right answer Bitch!')
                break
            else:
                print(f'{user_answer} is not the right answer, try again!')
              

        player_name = str(input("Enter your name for high score: "))
        save_score(player_name, category_name, difficulty_name)

        scores = dict()
        if player_name not in scores:
            scores[player_name] = {}
            scores[player_name][category_name] = {}
            scores[player_name][category_name][difficulty_name] = 0
            scores[player_name][category_name][difficulty_name] += 1
        else:
            scores[player_name][category_name][difficulty_name] + 1
        
        print(scores)