FROM python:3.10-slim

WORKDIR /application

COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt

COPY src .

CMD ["python", "bot.py"]