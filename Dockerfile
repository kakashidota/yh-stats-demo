FROM python:3.9-slim
WORKDIR /dash_app
ENV PYTHONPATH=/dash_app
COPY requirements.txt requirements.txt
COPY data data
COPY src src

RUN pip install -r requirements.txt

WORKDIR /dash_app/src

EXPOSE 80
EXPOSE 443
CMD ["gunicorn", "app:server", "--bind", ":80"]
