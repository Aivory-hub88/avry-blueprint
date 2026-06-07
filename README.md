# avry-blueprint

AI System Blueprint generator for the Aivory platform — generates architecture designs from diagnostic results.

## Tech Stack

- Python 3.11+
- FastAPI + Uvicorn
- PostgreSQL
- OpenAI / LLM integration
- Docker

## Directory Structure

```
avry-blueprint/
├── app/            # Application source code
├── blueprints/     # Generated blueprint outputs
├── data/           # Static data / templates
├── migrations/     # Database migrations
├── main.py         # Entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run Locally

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --host 0.0.0.0 --port 8083 --reload
```

## Docker

```bash
docker compose up --build
```

## VPS Deployment

```bash
docker compose -f docker-compose.yml up -d --build
```

Ensure `.env` is configured on the server with production credentials.

## Part of Aivory

This service is part of the [Aivory platform](https://github.com/ClementHansel/aivory).
