FROM python:3.8.10-slim-buster
WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt \
    && mkdir resources

COPY . /app

ENTRYPOINT [ "python" ]
CMD ["main.py"]