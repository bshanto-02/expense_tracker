from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "expense-tracker-decodelabs-2026"

# ---------- STATE (initialized OUTSIDE any loop/request) ----------
# LEARN: total must live here, not inside a function.
# If it were inside a route, it would reset to 0 on every request.
# This is "The Anatomy of State" — Initialization (Memory) vs Iteration (Amnesia).
expenses = []       # stores each individual transaction
total    = 0.0      # THE ACCUMULATOR — persists across all requests


# ---------- ROUTES ----------

@app.route("/")
def index():
    count = len(expenses)
    avg   = (total / count) if count > 0 else 0
    return render_template("index.html",
                           expenses=expenses,
                           total=total,
                           count=count,
                           avg=avg)


@app.route("/add", methods=["POST"])
def add_expense():
    global total

    label = request.form.get("label", "").strip() or "Expense"
    raw   = request.form.get("amount", "").strip()

    # SENTINEL CHECK (Kill Switch) — typing "done" ends the session
    if raw.lower() == "done":
        flash("Session closed. Final total locked in.", "info")
        return redirect(url_for("index"))

    # GATEKEEPER: try/except catches invalid types before they crash the engine
    # '100' + '50' = '10050' (Disaster) vs float('100') + float('50') = 150.0 (Truth)
    try:
        amount = float(raw)
        if amount <= 0:
            raise ValueError("Must be positive.")
    except ValueError:
        flash(f'"{raw}" is not valid. Enter a number like 100 or 49.99.', "error")
        return redirect(url_for("index"))

    # ACCUMULATOR PATTERN: State(new) = State(old) + Input
    total += amount    # total = total + new_expense

    expenses.append({
        "id":     len(expenses) + 1,
        "label":  label,
        "amount": amount,
    })

    flash(f'Added {amount:,.2f} for "{label}". Running total: {total:,.2f}', "success")
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    global total, expenses
    total    = 0.0
    expenses = []
    flash("Accumulator reset to zero. All records cleared.", "info")
    return redirect(url_for("index"))


@app.route("/delete/<int:expense_id>")
def delete_expense(expense_id):
    global total, expenses
    target = next((e for e in expenses if e["id"] == expense_id), None)
    if target:
        total   -= target["amount"]
        expenses = [e for e in expenses if e["id"] != expense_id]
        flash(f'Removed {target["amount"]:,.2f}. New total: {total:,.2f}', "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("\n  Expense Tracker running at http://127.0.0.1:5000\n")
    app.run(debug=True)
