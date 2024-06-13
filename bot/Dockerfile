FROM python:3.8.10-slim-buster
WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt \
    && apt-get update \
    && apt-get install libpq-dev -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir resources

COPY . /app

ENTRYPOINT [ "python" ]
CMD ["main.py"]