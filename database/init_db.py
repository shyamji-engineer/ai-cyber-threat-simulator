import sqlite3
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATABASE_PATH

def init_db():
    """Initialize the SQLite database with the required schema."""
    
    # Ensure database directory exists
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    print(f"Initializing database at {DATABASE_PATH}...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create attacks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attack_type TEXT NOT NULL,
            content TEXT NOT NULL,
            rule_risk TEXT,
            openai_risk TEXT,
            gemini_risk TEXT,
            final_risk TEXT,
            ai_reason TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
