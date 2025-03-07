import sqlite3

def get_db_connection():
    return sqlite3.connect("chat_history.db", check_same_thread=False)

def initialize_database():
    """ Create the tables if they don’t exist """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

def save_chat(user_message, bot_response):
    """ Save chat history to the database """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chats (user_message, bot_response) VALUES (?, ?)", (user_message, bot_response))
    conn.commit()
    conn.close()

def fetch_chat_history(limit=10):
    """ Retrieve chat history from the database """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chats ORDER BY timestamp DESC LIMIT ?", (limit,))
    data = cursor.fetchall()
    conn.close()
    return data

def save_user_name(user_name):
    """ Save user name in the database """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_data (user_name) VALUES (?)", (user_name,))
    conn.commit()
    conn.close()

def fetch_last_user_name():
    """ Retrieve the most recent user name from the database """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM user_data ORDER BY timestamp DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

initialize_database()  # Ensure database is initialized
