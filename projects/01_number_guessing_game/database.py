import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        database='python_games'
    )

# Save scores
def save_score(player_name, score, difficulty_name):
    conn = connect_to_database() # Create a new connection to database
    cursor = conn.cursor() # Create a cursor - think of it as a pointer that will execute our SQL commands

    query = " INSERT INTO high_scores (player_name, score, difficulty) VALUES (%s, %s, %s)"# SQL query with placeholders (%s) for safety against SQL injection
    cursor.execute(query, (player_name, score, difficulty_name)) # Execute query, replacing %s with actual values from the parameters

    conn.commit() # Save changes to database (like Git commit)
    cursor.close() # Clean up by closing cursor and connection
    conn.close()

# Get top scores
def get_top_scores(difficulty_name):
    conn = connect_to_database() # Create a new connection to database
    cursor = conn.cursor() # Create a cursor - think of it as a pointer that will execute our SQL commands

    # SQL query to get top 5 scores for specific difficulty
    # ORDER BY score (ascending, fewer guesses = better)
    query = "SELECT player_name, score FROM high_scores WHERE difficulty = %s ORDER BY score LIMIT 5"
    cursor.execute(query, (difficulty_name,))

    # Fetch all results from query
    scores = cursor.fetchall()
    cursor.close()
    conn.close()
    # Return the scores to use in our game
    return scores



# Test connection
if __name__ == "__main__":
    try:
        conn = connect_to_database()
        print('Successfully connected to database!')
        conn.close()
    except:
        print(f"Error: {err}")


    