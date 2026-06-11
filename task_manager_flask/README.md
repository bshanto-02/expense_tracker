# TaskFlow — Flask Task Manager
### Intern Python Project

A simple task manager built with **Flask**, teaching lists, routes and Jinja2 templates.

## Project Structure

task_manager_flask/
├── app.py                  ← Flask routes & list logic
├── requirements.txt        ← Dependencies
├── templates/
│   └── index.html          ← Jinja2 HTML template
└── static/
    └── style.css           ← Stylesheet

## Setup & Run

bash
# 1. Install Flask
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open your browser
# → http://127.0.0.1:5000

## Key Concepts Covered

| Concept              | Where                          |
|----------------------|--------------------------------|
| `list` + `append()`  | `add_task()` in app.py         |
| `for` loop           | `{% for task in tasks %}` HTML |
| List comprehension   | `delete_task()` in app.py      |
| Flask `@app.route`   | Every function in app.py       |
| Jinja2 templating    | `templates/index.html`         |
| Flash messages       | `flash()` + `get_flashed_messages()` |

## Challenge Extensions

1. **Persist data** — Save tasks to a JSON file so they survive restarts.
2. **Edit tasks** — Add a `/edit/<id>` route with a pre-filled form.
3. **Due dates** — Store tasks as dicts with a `due` field.
4. **SQLite database** — Replace the list with Flask-SQLAlchemy.
