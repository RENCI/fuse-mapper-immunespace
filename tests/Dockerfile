FROM python:3.8-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY config.json  /usr/src/app
COPY tx-utils/src /usr/src/app
COPY api          /usr/src/app/api

COPY tests/test_*.py /usr/src/app/

# testing-specfic:
RUN pip3 install --no-cache-dir pytest requests
ENTRYPOINT ["pytest"]
CMD ["-s"]
