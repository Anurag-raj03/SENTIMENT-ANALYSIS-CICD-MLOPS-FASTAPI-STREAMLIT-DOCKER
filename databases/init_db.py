import sqlite3 as sq

DB_PATH = "databases/sentiment.db"

def init_db():
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_data (
            Sentence TEXT NOT NULL,
            Sentiment TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("DATABASE INITIALIZED SUCCESSFULLY")
