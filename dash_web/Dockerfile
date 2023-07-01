FROM python:latest

ENV DASH_DEBUG_MODE True

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN set -ex && pip install -r requirements.txt

EXPOSE 8050

CMD ["python3", "app.py"]
