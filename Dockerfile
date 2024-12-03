FROM python:3.11-slim AS builder

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]