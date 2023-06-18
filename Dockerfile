# current python stable version
FROM python:3.11.4

WORKDIR /app

COPY . .

# install python requirements to run the project
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]