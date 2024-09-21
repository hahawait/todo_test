FROM python:3.10-slim

WORKDIR /application

COPY requirements.txt .
COPY .env .
RUN pip install -r requirements.txt

COPY todo .

# Set environment variables for superuser creation
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

# Run migrations and create superuser
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py createsuperuser --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]