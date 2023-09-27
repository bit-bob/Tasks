FROM python:3.9-alpine3.13

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "./backend/main.py"]
