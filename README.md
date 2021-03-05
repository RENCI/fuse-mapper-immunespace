[![Build Status](https://travis-ci.com/RENCI/fuse-mapper-immunescape.svg?branch=master)](https://travis-ci.com/RENCI/fuse-mapper-immunescape)

# fuse-mapper-immunescape

## prerequisites
 python 3.8 or higher

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

* Fix config/config.py (see above)
* re-brand this for FUSE immunespace, it's currently using cdm for PDS parallex
* create fuse-cdm-specs
