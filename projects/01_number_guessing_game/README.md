# Number Guessing Game

A command-line number guessing game built with Python and MySQL for score tracking.

## Features

- Multiple difficulty levels:
- Easy (1-50, 15 guesses)
- Medium (1-100, 10 guesses)
- Hard (1-200, 7 guesses)
- High score system using MySQL database
- Error handling for invalid inputs
- Player feedback (too high/too low)
- Score tracking by difficulty level
- Play again option

## Setup

1. Create MySQL database and table:

````sql
CREATE DATABASE python_games;
USE python_games;

CREATE TABLE high_scores (
   id INT AUTO_INCREMENT PRIMARY KEY,
   player_name VARCHAR(100),
   score INT,
   difficulty VARCHAR(10),
   played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

2. Install dependencies:

``` bash
pip install mysql-connector-python
````

## How To Play

1. Run the game:
   python number_game.py

2. Choose difficulty (1-3)
3. Try to guess the number with provided feedback
4. Your score will be saved if you win
5. View top scores for each difficulty level

## Technologies Used

- Python
- MySQL
- mysql-connector-python
