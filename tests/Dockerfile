# syntax = edrevo/dockerfile-plus

FROM python:3.8-buster

INCLUDE+ Dockerfile.common

RUN mkdir -p /usr/src/app/expected
COPY tests/expected  /usr/src/app/expected
COPY tests/test_*.py /usr/src/app/

RUN pip3 install --no-cache-dir pytest requests

ENTRYPOINT ["pytest"]

CMD ["-s"]
