import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cur = conn.cursor()

# Create BakingContestPeople table if it doesn't exist (empty for now)
cur.execute("""
    CREATE TABLE IF NOT EXISTS BakingContestPeople (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL CHECK (age > 0 AND age < 121),
        phone_number TEXT NOT NULL,
        security_level INTEGER NOT NULL CHECK (security_level BETWEEN 1 AND 3),
        password TEXT NOT NULL
    )
""")

# Create BakingContestEntry table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS BakingContestEntry (
        entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        baking_item TEXT NOT NULL,
        num_excellent_votes INTEGER DEFAULT 0,
        num_ok_votes INTEGER DEFAULT 0,
        num_bad_votes INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES BakingContestPeople (id)
    )
""")

# Sample data to insert into the BakingContestEntry table (no actual users)
sample_entries = [
    (1, "Whoot Whoot Cookies", 1, 2, 4),  
    (2, "Chocolate Chip Cookies", 4, 1, 2),  
    (3, "Chocolate Cake", 2, 4, 1),  
    (1, "Sugar Cookies", 2, 2, 1)   
]

# Insert sample data into BakingContestEntry table
cur.executemany("""
    INSERT INTO BakingContestEntry (user_id, baking_item, num_excellent_votes, num_ok_votes, num_bad_votes)
    VALUES (?, ?, ?, ?, ?)
""", sample_entries)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Database initialized with sample contest entries.")
