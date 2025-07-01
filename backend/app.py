from flask import Flask, request, render_template
import sqlite3

# Create the Flask app
app = Flask(__name__, template_folder='../templates')

# 🔧 Step 1: Create database table (if not already created)
def init_db():
    conn = sqlite3.connect('trees.db')  # creates a file called trees.db
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            date TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()
    # 🔁 Step 2: Handle form and insert data into database
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('tree_name')
        location = request.form.get('location')
        date = request.form.get('date_planted')
        status = request.form.get('status')

        # Print for testing
        print("✅ Received:", name, location, date, status)

        # Save to database
        conn = sqlite3.connect('trees.db')
        c = conn.cursor()
        c.execute("INSERT INTO trees (name, location, date, status) VALUES (?, ?, ?, ?)",
                  (name, location, date, status))
        conn.commit()
        conn.close()

    return render_template('index.html')

# 🚀 Step 3: Start Flask and initialize database
if __name__ == '__main__':
    init_db()  # run this once when app starts
    app.run(debug=True)