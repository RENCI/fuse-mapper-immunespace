import requests
from pathlib import Path
import logging
import os
import json
import pytest

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

appliance="http://fuse-mapper-immunespace:8080"
log.info(f"starting on port ("+appliance+")")

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test_config():
    if os.getenv('TEST_LIBRARY') == "1":
        pytest.skip("Only testing docker lib")

    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config=json.load(f)
    resp = requests.get(f"{appliance}/config")
    assert resp.json() == config


json_headers = {
    "Accept": "application/json"
}

# other endpoint tests, start with "test_"

def test_mapping():

    if os.getenv('TEST_LIBRARY') == "1":
        pytest.skip("Only testing docker lib")

    with open("tests/input/test_2.json", 'r', encoding='utf-8') as f:
        query = json.load(f)

    log.info(f"Asking for mapping")

    mapping = requests.post(f"{appliance}/mapping", headers=json_headers, json=query)

    with open("tests/expected/test_2.json", 'r', encoding='utf-8') as f:
        expected = json.load(f)

    mappings = json.dumps(mapping, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)

    if(g_debug):
        print("mapping:")
        print(mappings)

    assert mappings == expecteds

