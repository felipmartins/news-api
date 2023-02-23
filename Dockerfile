FROM python:3.9-slim-buster

WORKDIR /

COPY requirements.txt ./
COPY dev-requirements.txt ./
RUN pip install -r dev-requirements.txt

COPY ./news ./news/
RUN mkdir /news/media

RUN chown 65534:65534 /app/media

USER 65534:65534

ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]
