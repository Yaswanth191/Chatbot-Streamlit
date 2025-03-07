import sqlite3

def fetch_all_data():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    print("\n--- Chat History ---")
    cursor.execute("SELECT id, user_message, bot_response, timestamp FROM chats ORDER BY timestamp DESC")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Stored User Names ---")
    cursor.execute("SELECT id, user_name, timestamp FROM user_data ORDER BY timestamp DESC")
    for row in cursor.fetchall():
        print(row)

    conn.close()

# Run the function to fetch data
fetch_all_data()
