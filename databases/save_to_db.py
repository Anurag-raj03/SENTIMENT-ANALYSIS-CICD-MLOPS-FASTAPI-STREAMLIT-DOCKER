import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from databases.db_config import get_connection  

def save_text_to_db(Sentence: str, Sentiment: int):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sentiment_data (Sentence, Sentiment) VALUES (?, ?)", (Sentence, Sentiment))
    
    conn.commit()
    conn.close()
    print("Data saved to database.")
