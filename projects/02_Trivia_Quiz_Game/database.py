import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        database='python_games'
    )

# Save scores
def save_score(player_name, category_name, difficulty_name):
    conn = connect_to_database() 
    cursor = conn.cursor() 
    score_type = f"{difficulty_name}_score"

    check_query = "SELECT * FROM scores WHERE player_name = %s AND category = %s"
    cursor.execute(check_query, (player_name, category_name)) 

    if cursor.fetchone():
    #Player exists - update score
        update_query = f"UPDATE scores SET {score_type} = {score_type} + 1 WHERE player_name = %s AND category = %s"
        cursor.execute(update_query, (player_name, category_name))
    else:
        query = f"INSERT INTO scores (player_name, {score_type}, category) VALUES(%s, 1, %s)"
        cursor.execute(query,(player_name, category_name))

    conn.commit() 
    cursor.close() 
    conn.close()