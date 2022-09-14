FROM openjdk:slim
COPY --from=python:3.9 / /

WORKDIR /workdir


COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

RUN apt-get update

COPY . .

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "80"]
