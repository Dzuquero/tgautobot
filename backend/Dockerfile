FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD alembic -c alembic.ini upgrade head && python alembic/seed.py && uvicorn app.main:app --host 0.0.0.0 --port 8000