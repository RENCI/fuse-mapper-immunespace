FROM python:3.8-buster

RUN mkdir /test
WORKDIR /test

RUN pip3 install --no-cache-dir pytest requests pyyaml python-dateutil==2.8.1 tx-functional>=0.0.16 pint

COPY config.json    /test
COPY tx-utils/src /test
COPY api          /test/api

COPY tests/test_*.py /test/

ENV PYTHONPATH=/test

ENTRYPOINT ["pytest"]
CMD ["-s"]
