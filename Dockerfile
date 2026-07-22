FROM python:3.12

WORKDIR /app

COPY server/ .

RUN pip install uv

RUN uv pip install --system -r pyproject.toml

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]