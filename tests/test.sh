#!/bin/bash

export $(cat tests/test.env)
export TEST_LIBRARY=0

docker-compose -f docker-compose.yml -f tests/docker-compose.yml up --build -V --exit-code-from fuse-mapper-immunespace
