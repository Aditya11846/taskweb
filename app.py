from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = 'tasks.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

@app.route('/')
def index():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, priority, status FROM tasks")
        tasks = cur.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    priority = request.form['priority']
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (name, priority) VALUES (?, ?)", (name, priority))
        conn.commit()
    return redirect(url_for('index'))

# TODO: Implement a route to mark a task as complete
# @app.route('/complete/<int:task_id>')
# def complete_task(task_id):
#     ...

# TODO: Implement a route to delete a task
# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     ...

if __name__ == '__main__':
    app.run(debug=True)
