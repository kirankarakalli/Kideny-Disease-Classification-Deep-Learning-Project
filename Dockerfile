FROM python:3.13-alpine

RUN apk add --no-cache aws-cli

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
