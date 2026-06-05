# Github Actions Django

A minimal Django project built with the sole purpose of learning and testing GitHub Actions CI pipelines.

---

## Why This Exists

This is not a production app. It is a sandbox — a simple Django REST API used as a vehicle to understand how GitHub Actions workflows behave: how they trigger, how they fail, and how to fix them.

The workflow history tells the real story:

| Run | What happened |
|-----|--------------|
| `Primer commit API Django` | First working pipeline — 17s |
| `Pequeño cambio` | Something slowed it down — 9m 28s |
| `Sin requirements` | Removed the requirements file, pipeline hung — 2m 43s |
| `Sin requirements bien` | Fixed the approach, back to normal — 16s |
| `mal codigo` | Intentionally pushed bad code to see the pipeline fail |

---

## Project Structure

```
Github-Actions-Django/
├── .github/
│   └── workflows/       # CI pipeline definitions
├── members/             # Django app
├── my_tennis_club/      # Django project settings
├── db.sqlite3           # Local SQLite database
└── manage.py            # Django entry point
```

---

## Tech Stack

- Python 3
- Django
- SQLite (local development)
- GitHub Actions (CI)

---

## CI Pipeline

The workflow is defined in `.github/workflows/` and triggers on every push to `main`.

It runs the Django test suite automatically on each commit, giving immediate feedback on whether the code is healthy or broken.

```yaml
# Example of what the workflow does
- Install dependencies from requirements.txt
- Run Django tests with manage.py test
```

---

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ElRicky17/Github-Actions-Django.git
   cd Github-Actions-Django
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Run tests:
   ```bash
   python manage.py test
   ```

---

## Key Takeaways

- A missing `requirements.txt` does not immediately crash the pipeline — it just makes it hang.
- GitHub Actions gives you a full audit trail of every run, making debugging straightforward.
- Keeping CI runs under 30 seconds is very achievable for small Django projects.
