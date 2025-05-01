FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY muriel.py .
COPY matematica.py .
COPY test_matematica.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "muriel.py"]
