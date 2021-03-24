import os
import logging
from pathlib import Path
from fuse.mapper.ge.dispatcher import GetMapping

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import json
def get_config():
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)
        
def get_mapping(body):
    return GetMapping(body)


