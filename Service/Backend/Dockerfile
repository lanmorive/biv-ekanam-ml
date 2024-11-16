FROM python:3.11-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]
