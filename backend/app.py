from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, template_folder='../templates', static_folder='../static')

#here  is  Database setup
def setup_database():
    conn = sqlite3.connect('trees.db')
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

# for  HTML page
@app.route('/')
def home():
    return render_template('index.html')

# i am using this for Add new tree (POST)
@app.route('/api/trees', methods=['POST'])
def add_tree():
    data = request.get_json()
    conn = sqlite3.connect('trees.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO trees (name, location, date, status)
        VALUES (?, ?, ?, ?)
    ''', (data['name'], data['location'], data['date'], data['status']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tree added successfully!"}), 201

#for  Get all trees (GET)
@app.route('/api/trees', methods=['GET'])
def get_trees():
    conn = sqlite3.connect('trees.db')
    c = conn.cursor()
    c.execute("SELECT id, name, location, date, status FROM trees")
    trees = c.fetchall()
    conn.close()
    return jsonify([
        {"id": t[0], "name": t[1], "location": t[2], "date": t[3], "status": t[4]}
        for t in trees
    ])

# i am using it for Delete a tree 
@app.route('/api/trees/<int:tree_id>', methods=['DELETE'])
def delete_tree(tree_id):
    conn = sqlite3.connect('trees.db')
    c = conn.cursor()
    c.execute("DELETE FROM trees WHERE id = ?", (tree_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tree deleted"})
#for update a tree
@app.route('/api/trees/<int:tree_id>', methods=['PUT'])
def update_tree(tree_id):
    data = request.get_json()
    conn = sqlite3.connect('trees.db')
    c = conn.cursor()
    c.execute('''
        UPDATE trees SET name = ?, location = ?, date = ?, status = ? WHERE id = ?
    ''', (data['name'], data['location'], data['date'], data['status'], tree_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tree updated successfully!"})


if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
