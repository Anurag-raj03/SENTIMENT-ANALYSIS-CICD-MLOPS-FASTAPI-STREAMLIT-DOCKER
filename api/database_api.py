import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from databases.db_config import get_connection

def save_text_to_db(sentence,sentiment):
    conn=get_connection()
    cursor=conn.cursor()
    
    cursor.execute("INSERT INTO sentiment_data (Sentence, Sentiment) VALUES (?, ?)", (sentence, sentiment))
    
    conn.commit()
    conn.close()
    print("✅ Data saved to database!")
    
    