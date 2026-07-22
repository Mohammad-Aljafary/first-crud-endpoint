# First CRUD Endpoints

This is a small FastAPI CRUD API for managing tasks. It runs with Docker Compose, uses PostgreSQL for persistence, and exposes a simple set of endpoints for creating, reading, updating, and deleting tasks.

## What This Is

It is a learning project for FastAPI, SQLAlchemy, and basic API design. The application starts with one command, loads its configuration from an env file, and includes a seeded tasks table so you can inspect real data immediately.

## Run Everything

From the repository root:

```bash
docker compose up
```

## Environment Variables

Copy [server/.env.example](server/.env.example) to [server/.env](server/.env) and set these values:

- `DATABASE_URL`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

Example:

```env
DATABASE_URL=postgresql+psycopg2://postgres:db_password@postgres:5432/db_name
POSTGRES_PASSWORD=db_password
POSTGRES_DB=db_name
```

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Health-style welcome message |
| `GET` | `/health` | Returns API status |
| `GET` | `/tasks` | Returns all tasks |
| `GET` | `/tasks/{task_id}` | Returns one task by ID |
| `POST` | `/tasks` | Creates a task |
| `PUT` | `/tasks/{task_id}` | Updates a task |
| `DELETE` | `/tasks/{task_id}` | Deletes a task |

## Curl Example

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","done":false}'
```

## Database Screenshot

The data in the database can be inspected in a GUI client such as DB Browser, DBeaver, pgAdmin, or TablePlus.

![Tasks table in the database](docs/Screenshot%20from%202026-07-21%2001-28-20.png)

## Project Structure

- `server/main.py` - application setup and base routes
- `server/tasks_route.py` - task endpoints and request models
- `server/db.py` - database connection, table creation, and seed data
- `server/.env.example` - template for local environment variables
- `docker-compose.yaml` - starts the API and PostgreSQL together

## Notes

- The tasks table is seeded when it is empty, so you can view example data right away.
- If you change the env file, restart Compose so the containers pick up the new values.

