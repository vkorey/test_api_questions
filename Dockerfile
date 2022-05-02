FROM python:3.8.1-alpine
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /app/requirements.txt --no-cache-dir
COPY . .

ENTRYPOINT uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --workers 1
