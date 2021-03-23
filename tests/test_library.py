from fuse.mapper.ge.dispatcher import GetMapping
import json
import os
import pytest

g_debug = True
#g_debug = False

def test_GetMapping():

    if os.getenv('TEST_LIBRARY') == "0":
        pytest.skip("Only testing docker container")


    with open("tests/input/test_2.json", 'r', encoding='utf-8') as f:
        query = json.load(f)

    mapping = GetMapping(query)

    with open('tests/expected/test_2.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)

    # Uncomment this to capture output:
    #with open('tests/test_2.out.json', 'w', encoding='utf-8') as f:
    #     json.dump(obj, f, ensure_ascii=False, indent=4, sort_keys=True)

    mappings = json.dumps(mapping, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)

    if(g_debug):
        print("mapping:")
        print(mappings)
        print("expected:")
        print(expecteds)
        
    assert mappings == expecteds

