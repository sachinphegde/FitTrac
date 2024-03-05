import sqlite3

# Step 1: Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('FitTrac')

# Step 2: Create a cursor object to interact with the database
cur = conn.cursor()

# Step 3: Execute SQL commands to create tables, insert data, etc.
# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS strava_user_data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL)''')

# Insert some data
cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Jane Doe', 'jane@example.com'))

# Step 4: Commit changes
conn.commit()

# Step 5: Query the database
cur.execute("SELECT * FROM users")
print("Users:")
for row in cur.fetchall():
    print(row)

# Step 6: Close the connection
conn.close()