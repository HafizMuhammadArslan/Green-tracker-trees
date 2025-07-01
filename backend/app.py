from flask import Flask, render_template, request
import sqlite3

#  Setup Flask app
app = Flask(__name__, template_folder='../templates')

#  My own code (which i moodify from old )of the database setup function
def setup_database():
    connection = sqlite3.connect('trees.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            date TEXT,
            status TEXT
        )
    ''')
    connection.commit()
    connection.close()

#  Main route to handle form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tree_name = request.form.get('tree_name')
        location = request.form.get('location')
        date = request.form.get('date_planted')
        status = request.form.get('status')

        print(" Received:", tree_name, location, date, status)

        connection = sqlite3.connect('trees.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO trees (name, location, date, status)
            VALUES (?, ?, ?, ?)
        ''', (tree_name, location, date, status))
        connection.commit()
        connection.close()

    return render_template('index.html')

#  Run the app
if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
