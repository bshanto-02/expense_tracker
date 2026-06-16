from py_compile import main 
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "taskmanager-secret-key" 

tasks = []

@app.route("/")
def index():
    """Home page — shows all tasks."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Receive the form, append a new task, redirect back."""
    task_text = request.form.get("task", "").strip()
    if task_text:
        tasks.append({"id": len(tasks), "text": task_text, "done": False})
        flash(f'"{task_text}" added!', "success")
    else:
        flash("Task cannot be empty.", "error")
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    """Mark a task done / not done."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Remove a task by its id."""
    global tasks
    removed = next((t for t in tasks if t["id"] == task_id), None)
    tasks = [t for t in tasks if t["id"] != task_id] 
    if removed:
        flash(f'"{removed["text"]}" deleted.', "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    print("\n  Task Manager is running!")
    print("  Open http://127.0.0.1:5000 in your browser.\n")
    app.run(debug=True)
if __name__ == "__main__":
    main()