#!/bin/bash

set -a
source .env
set +a

docker-compose -f docker-compose.yml up --build -V -d
