from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Initialize the database and create table if not exists
def init_db():
    conn = sqlite3.connect('zeeshan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS People(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Route for handling both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            conn = sqlite3.connect('zeeshan.db')
            c = conn.cursor()
            c.execute('INSERT INTO People(name) VALUES(?)', (name,))
            conn.commit()
            conn.close()
    
    # Fetch all people from the database
    conn = sqlite3.connect("zeeshan.db")
    c = conn.cursor()
    c.execute('SELECT * FROM People')
    rows = c.fetchall()
    conn.close()

    # HTML page construction
    page = "<h1>People list</h1><ul>"
    for row in rows:
        page += f"<li>{row[1]}</li>"
    page += "</ul><h2>Add person</h2>"
    page += "<form method='post'>"
    page += "Name: <input name='name'><input type='submit'>"
    page += "</form>"

    return page

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
