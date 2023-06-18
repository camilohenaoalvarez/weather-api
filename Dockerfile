FROM python:3.11.4

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# CMD /bin/bash -c 'python test.py'
# CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]

# COPY ./api ./api