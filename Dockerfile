# syntax = edrevo/dockerfile-plus

FROM python:3.8-buster

INCLUDE+ Dockerfile.common

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:8080", "api.server:create_app()", "-t", "100000"]

