# Trivia Quiz Game

A command-line trivia game that tests your knowledge across multiple categories with varying difficulty levels.

## Features

- Multiple knowledge categories:
  - Geography
  - Science
  - Technology
  - Mathematics
- Three difficulty levels:
  - Easy
  - Medium
  - Hard
- Score tracking system
- Persistent high scores using MySQL
- Case-insensitive answer checking

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages:
  - mysql-connector-python

## Setup

1. Clone the repository
2. Create a MySQL database and run the setup script:

```sql
CREATE DATABASE quiz_game;
USE quiz_game;
CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    easy_score INT DEFAULT 0,
    medium_score INT DEFAULT 0,
    hard_score INT DEFAULT 0,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

3. Configure database connection in database.py

4. Run the game:

```
python quiz_game.py
```

## How to Play

1. Select a category
2. Choose difficulty level
3. Answer questions
4. Your scores will be automatically saved to the database

## Project Structure

- quiz_game.py: Main game logic
- database.py: Database operations
- Questions.txt: Question bank
