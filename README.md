[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/fuse-mapper-immunespace?style=plastic)](https://hub.docker.com/repository/docker/txscience/fuse-mapper-immunescape/builds)

# fuse-mapper-immunescape

## prerequisites:
* python 3.8 or higher
* Docker 20.10 or higher
* docker-compose v1.28 and 3.8 in the yml
* cargo 1.49.0 or higher (for installing dockerfile-plus)

Install dockerfile-plus:
`cargo build`

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

edit `tests/docker.env`

Put your spec under `config`. Put your custom python functions under a sub dir in that dir. Any python module under the sub dir can be imported in your spec. Your spec should output the format that the api specifies.

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

* create fuse-cdm-specs
