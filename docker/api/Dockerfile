ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

RUN apt-get update

WORKDIR /app

COPY . .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ARG API_PORT
ENV API_PORT ${API_PORT}
EXPOSE ${API_PORT}


