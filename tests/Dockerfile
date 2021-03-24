# syntax = edrevo/dockerfile-plus

FROM python:3.8-buster

INCLUDE+ Dockerfile.common

COPY tests/test_*.py /usr/src/app/
COPY config.json /usr/src/app/
RUN mkdir -p /usr/src/app/tests/expected
COPY tests/expected/test_2.json /usr/src/app/tests/expected
RUN mkdir -p /usr/src/app/tests/input
COPY tests/input/test_2.json /usr/src/app/tests/input
RUN pip3 install --no-cache-dir pytest requests

ENTRYPOINT ["pytest"]

CMD ["-s"]
