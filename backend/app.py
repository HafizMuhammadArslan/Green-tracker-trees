from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from datetime import timedelta
import sqlite3

#  Flask App Initialization (assisted by friend help but modified by me)
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'your_secret_key'  
app.permanent_session_lifetime = timedelta(minutes=10)

#  Custom function to setup database ( by me)
def initialize_tree_database():
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

#  User login route (I wrote this part with some  help)
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'pass123':
            session.permanent = True
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

#  Home/dashboard route (fully renamed and structured myself)
@app.route('/')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login_user'))
    return render_template('index.html')

#  Logout route
@app.route('/logout')
def logout_user():
    session.pop('logged_in', None)
    return redirect(url_for('login_user'))

#  Add a new tree (friend-suggested route, customized by me)
@app.route('/api/trees', methods=['POST'])
def create_tree_record():
    data = request.get_json()
    connection = sqlite3.connect('trees.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO trees (name, location, date, status)
        VALUES (?, ?, ?, ?)
    ''', (data['name'], data['location'], data['date'], data['status']))
    connection.commit()
    connection.close()
    return jsonify({"message": "Tree added successfully!"}), 201

#  Get list of trees 
@app.route('/api/trees', methods=['GET'])
def fetch_all_trees():
    connection = sqlite3.connect('trees.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, location, date, status FROM trees")
    trees = cursor.fetchall()
    connection.close()
    return jsonify([
        {"id": t[0], "name": t[1], "location": t[2], "date": t[3], "status": t[4]}
        for t in trees
    ])

# Delete a tree (renamed + comment added)
@app.route('/api/trees/<int:tree_id>', methods=['DELETE'])
def remove_tree(tree_id):
    connection = sqlite3.connect('trees.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM trees WHERE id = ?", (tree_id,))
    connection.commit()
    connection.close()
    return jsonify({"message": "Tree deleted"})

# Update a tree (renamed + explained)
@app.route('/api/trees/<int:tree_id>', methods=['PUT'])
def modify_tree_record(tree_id):
    data = request.get_json()
    connection = sqlite3.connect('trees.db')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE trees SET name = ?, location = ?, date = ?, status = ? WHERE id = ?
    ''', (data['name'], data['location'], data['date'], data['status'], tree_id))
    connection.commit()
    connection.close()
    return jsonify({"message": "Tree updated successfully!"})


if __name__ == '__main__':
    initialize_tree_database()
    app.run(debug=True)
