# syntax = edrevo/dockerfile-plus

FROM python:3.8-buster

INCLUDE+ Dockerfile.common

COPY tests/test_*.py /usr/src/app/

RUN pip3 install --no-cache-dir pytest requests

ENTRYPOINT ["pytest"]

CMD ["-s"]
