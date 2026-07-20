# First CRUD Endpoints

Simple FastAPI project for learning CRUD API design with a task management example backed by SQLite.

## Project Overview

This repository contains a small REST API built with FastAPI. It exposes a set of task endpoints for creating, reading, updating, and deleting tasks.

Tasks are stored in SQLite, so the data survives server restarts. The project is intentionally lightweight and is a good starting point for practicing API structure, request validation, and route organization.

## Why SQLite?

- It lives in a single file, which keeps the project easy to move around.
- It needs zero setup for local development.
- It survives restarts, so your data does not disappear every time the app stops.

## Database Location

- The database file lives at `server/db/tasks.db`.
- It is created automatically the first time the app starts.
- It is usually git-ignored, so each new clone starts with a fresh database file.

## Features

- FastAPI application with automatic validation and OpenAPI docs
- CRUD endpoints for tasks
- Basic health check endpoint
- SQLite persistence for simple experimentation

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLite
- SQLAlchemy

## Project Structure

- `server/main.py` - application setup and basic routes
- `server/tasks_route.py` - task models and CRUD endpoints
- `server/pyproject.toml` - project dependencies and metadata

## API Endpoints

### Root

- `GET /` - returns a welcome message

Example:

```bash
curl http://localhost:8000/
```

### Health

- `GET /health` - returns API status

Example:

```bash
curl http://localhost:8000/health
```

### Tasks

- `GET /tasks` - list all tasks
- `GET /tasks/{task_id}` - get a task by ID
- `POST /tasks` - create a new task
- `PUT /tasks/{task_id}` - update an existing task
- `DELETE /tasks/{task_id}` - delete a task

Example: list all tasks

```bash
curl http://localhost:8000/tasks
```

Example: get a task by ID

```bash
curl http://localhost:8000/tasks/1
```

Example: create a task

```bash
curl -X POST http://localhost:8000/tasks \
	-H "Content-Type: application/json" \
	-d '{"title":"Learn FastAPI"}'
```

Example: update a task

```bash
curl -X PUT http://localhost:8000/tasks/1 \
	-H "Content-Type: application/json" \
	-d '{"id":1,"title":"Learn FastAPI","done":true}'
```

Example: delete a task

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## Task Payloads

Create task request:

```json
{
	"title": "Buy groceries"
}
```

Create and update responses include:

```json
{
	"id": 1,
	"title": "Buy groceries",
	"done": false
}
```

## Getting Started

### Install dependencies

From the `server` directory:

```bash
uv sync
```

### Start the project

```bash
uv run uvicorn main:app --reload
```

### Open the docs

Once the server is running, open:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database Screenshot

![SQLite database open in DB Browser](docs/db-browser-snapshot.svg)

## Example SQL Query

One query used in Stage 4 was:

```sql
SELECT COUNT(*) FROM tasks;
```

On this copy of the database, it returned `4`.

## Example Requests

Create a task:

```bash
curl -X POST http://localhost:8000/tasks \
	-H "Content-Type: application/json" \
	-d '{"title":"Learn FastAPI"}'
```

List tasks:

```bash
curl http://localhost:8000/tasks
```

## Notes

- Task IDs are assigned automatically by SQLite.
- Empty task titles are rejected with a validation error.
- Example tasks are seeded only when the table is empty, so they do not multiply on restart.

