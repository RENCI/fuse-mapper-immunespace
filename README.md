[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/fuse-mapper-immunespace?style=plastic)](https://hub.docker.com/repository/docker/txscience/fuse-mapper-immunescape/builds)

# fuse-mapper-immunescape

Maps the input gene expression to the requested format. Also returns certainty of the computed value (certitude); e.g., if a gene doesn't map, a default value will be set and the certitude will be set to 0 (uncertain); 2 (certain) otherwise).

Can be run as a stand-alone appliance (see `up.sh` below) or as a plugin to a FUSE deployment (e.g., (fuse-immcellfie)[http://github/RENCI/fuse-immcellfie]).

## prerequisites:
* python 3.8 or higher
* Docker 20.10 or higher
* docker-compose v1.28 and 3.8 in the yml
* cargo 1.49.0 or higher (for installing dockerfile-plus)

Tips for updating docker-compose on Centos:

```
sudo yum install jq
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | jq .name -r)
sudo mv /usr/local/bin/docker-compose /usr/local/bin/docker-compose.old-version
DESTINATION=/usr/local/bin/docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
sudo chmod 755 $DESTINATION
```

## configuration

1. Install dockerfile-plus:
`cargo build`

2. Copy `sample.env` to `.env` and edit to suit your server:
* __API_PORT__ pick a unique port to avoid the `up.sh` and `./tests/test.sh` commands from colliding with other installations on the same server

Don't change these:
* __DOCKER_BUILDKIT__ required for dockerfile-plus (INCLUDE+ instruction)
* COMPOSE_DOCKER_CLI_BUILD required for dockerfile-plus (INCLUDE+ instruction)


## start
```
./up.sh
```

## validate installation
```
curl -X GET http://localhost:8082/config
```
WARNING: This only works because `config/config.py` hardcodes the config. Please fix this ASAP and remove this comment.

## stop
```
./down.sh
```

## TO DO:

* implement /mapping endpoint
* create fuse-cdm-specs
