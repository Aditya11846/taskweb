# taskweb – Flask Task Manager Web App

## Overview
This project builds a web app version of the taskcli task manager using Flask and SQLite.

You'll:
- Serve an HTML interface for viewing and adding tasks
- Use a shared SQLite database
- Add REST-like routes to complete/delete tasks (you will implement these)
- Write secure SQL queries (parameterized)
- Deploy the app publicly
- Make a Docker container for the app, instructions at [./docker.md](./docker.md).

## Features
- ✅ List tasks
- ✅ Add a new task
- ⬜ Complete a task (you will implement)
- ⬜ Delete a task (you will implement)

## Getting Started
```bash
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

To create the database, copy the `db_schema.sql` from taskcli and initialize it:
```bash
sqlite3 tasks.db < db_schema.sql
```

## Deployment Guide (Render example)

1. Push your code to GitHub
2. Create a free Render account
3. New Web Service → connect your GitHub repo (note that you'll need
   to move this project to your own repo, best not to continue to use
   `nebhrajani-a/singh` anyway for resume reasons)
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add a `render.yaml` (optional) or configure manually
6. SQLite will be reset on each deploy unless you use a persistent disk

To test locally with gunicorn:
```bash
gunicorn app:app
```

## What You Should Build

This project is intentionally open-ended. Here are ideas:

### Minimum Completion Goals
- [ ] Implement `/complete/<id>` to mark a task done
- [ ] Implement `/delete/<id>` to remove a task
- [ ] Sanitize inputs and handle errors (example: priority ranges)
- [ ] Style the UI for clarity (CSS or framework)

### Optional Enhancements
- Filter tasks by status/priority
- Add due dates and sort logic
- User authentication (Flask-Login or sessions)
- REST API (`GET /api/tasks`, `POST /api/tasks`)
- Deploy to a second platform (Fly.io, Vercel with adapter)

## Database Schema
```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
);
```

## Tech Stack
- Flask
- SQLite
- HTML + Jinja
- Gunicorn (for deployment)

## Run Tests (Optional)
Use `curl` or Postman to test routes locally.
