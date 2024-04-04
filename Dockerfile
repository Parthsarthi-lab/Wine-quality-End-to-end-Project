FROM python:3.12.2-slim-bookworm

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY ./app /app
RUN pip install -r requirements.txt

CMD ["python3","app.py"]
