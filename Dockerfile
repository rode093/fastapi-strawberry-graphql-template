from python:3

WORKDIR /app

COPY . /app 

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
