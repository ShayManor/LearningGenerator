FROM python:3.13-slim

WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app/main.py .
COPY src/ ./src/

EXPOSE 8080
ENTRYPOINT ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:$PORT"]

