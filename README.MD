# First CRUD Endpoints

Simple FastAPI project for learning CRUD API design with a task management example.

## Project Overview

This repository contains a small REST API built with FastAPI. It exposes a set of task endpoints for creating, reading, updating, and deleting tasks.

Tasks are stored in memory, so the data is reset whenever the server restarts. The project is intentionally lightweight and is a good starting point for practicing API structure, request validation, and route organization.

## Features

- FastAPI application with automatic validation and OpenAPI docs
- CRUD endpoints for tasks
- Basic health check endpoint
- In-memory data storage for simple experimentation

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

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

### 1. Install dependencies

From the `server` directory:

```bash
uv sync
```

### 2. Run the app

```bash
uvicorn main:app --reload
```

### 3. Open the docs

Once the server is running, open:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

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

- Task IDs are assigned automatically in the current in-memory list.
- Empty task titles are rejected with a validation error.
- The API is designed for local development and learning, not persistent storage.

