# Expense Tracker
## Setup & Run

```bash
pip install -r requirements.txt
python app.py
# → http://127.0.0.1:5000
```

---

## Project Structure

```
expense_tracker/
├── app.py                ← Backend logic (accumulator, gatekeeper, sentinel)
├── requirements.txt
├── templates/
│   └── index.html        ← Jinja2 template (output / display)
└── static/
    └── style.css
```

---

## Quality Standard Checklist (from DecodeLabs)

- [x] **Stability** — handles 5+ transactions without crashing
- [x] **State** — `total` initialized OUTSIDE the loop/request
- [x] **Defense** — `try/except ValueError` on every input
- [x] **Control** — sentinel value `"done"` ends session gracefully
- [x] **Output** — Final total displayed clearly (FINAL TOTAL row)

---

## Key Concepts

| Concept | Code Location | DecodeLabs Term |
|---|---|---|
| Accumulator | `total += amount` in `add_expense()` | The Heartbeat of the Ledger |
| Type casting | `float(raw)` | Phase 1: The Gatekeeper |
| Defensive coding | `try/except ValueError` | Digital Poka-Yoke |
| Sentinel value | `if raw == "done"` | The Kill Switch |
| State outside loop | `total = 0.0` at module level | Anatomy of State |

---

## Stretch Challenges

1. Add **categories** (Food, Transport, Bills) with a dropdown
2. **Export** the ledger to a `.csv` file
3. Set a **budget limit** and show a warning when exceeded
4. Save data to **JSON** so it survives restarts
