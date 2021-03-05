FROM python:3.8-buster

RUN pip3 install --no-cache-dir pytest requests pyyaml python-dateutil==2.8.1 tx-functional>=0.0.16 tx-parallex[arrow]>=0.1.2 pint

RUN mkdir /test

WORKDIR /test

COPY api /test/api
COPY tx-utils/src /test
COPY tests/test_*.py /test/

ENV PYTHONPATH=/test

ENTRYPOINT ["pytest"]
CMD ["-s"]
