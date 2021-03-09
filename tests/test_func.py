import requests
from pathlib import Path
import logging
import os
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

appliance="http://fuse-mapper-immunespace:8080"
# xxx log.info(f"starting on port (${API_PORT})")

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test_config():
    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config=json.load(f)
    resp = requests.get(f"{appliance}/config")
    assert resp.json() == config


json_headers = {
    "Accept": "application/json"
}

def test_mapping():
    test_file="expected/1_mapping.json"
    expected_path = Path(__file__).parent /  test_file
    with open(expected_path) as f:
        expected=json.load(f)

    pv =  {
        "title": f"subj var title",
        "legalValues": {
            "type": "integer"
        },
        "why": f"subj var why",
        "id": "subj var",
    }
    q = {"subjectIds":["1"], "timestamp":"2020-07-01T14:29:15.453Z", "data":{"foo":"bar"} }
    
    resp = requests.post(f"{appliance}/mapping", headers=json_headers, json=q)
    print(json.dumps(resp.json(), indent=4))
    #assert resp.json() == expected
    return True

# ----NOTES FOLLOW ----

# some nice parameters might include:
# id_source=entrez/ncbi | hgnc | ensembl 
# id_type=transcript_id|gene_id
# normalized=none|deseq2
# transpose=yes(genes on cols)|no(genes on rows)
# filter=<genelist>
# filter_id=<genelist id on server to use for filter>
# 


# xxx
# change this to be per-person:
# can ask for a record by subject id
# subject id list,
# or by cohort id, to get a 
examplar_return={
    "mappings": {
        "txid": "xyz1", 
        "values": [
            {
                "variable_id": "eset:array.1",
                "certitude": 2,
                "how": "retrieved from Immunescape",
                "group": "PatientVariables",
                "title": "Gene Expression array",
                "variableValue": {
                    "geneExpression":[{"id":"1000", "system":"HGNC", "value":1.00}, {"id":"100", "system":"HGNC", "value":1.50}],
                    "type": "array",
                    "units": "counts"
                },
                "why": "Required for many phenotype models"
            },
            {
                "variable_id": "eset:site.1",
                "certitude": 2,
                "how": "retrieved from Immunescape",
                "group": "PatientVariables",
                "title": "Anatomical Site from which gene expression was taken",
                "variableValue": {
                    "anatomicSite": "Bladder",
                    "type": "string"
                }
            },
            {
                "variable_id": "eset:class.1",
                "certitude": 2,
                "how": "retrieved from Immunescape",
                "group": "PatientVariables",
                "title": "Tissue class",
                "variableValue": {
                    "tissueClass": "normal",
                    "type": "string"
                }
            },
            {
                "variable_id": "person:disease.1",
                "certitude": 2,
                "how": "retrieved from Immunescape",
                "group": "PatientVariables",
                "title": "Disease status of person",
                "variableValue": {
                    "diseaseStatus": "BLCA",
                    "type": "string"
                }
            },
            {
                "variable_id": "person:gender.1",
                "certitude": 2,
                "how": "retrieved from Immunescape",
                "group": "PatientVariables",
                "title": "Gender",
                "variableValue": {
                    "gender": "M",
                    "type": "string"
                }
            }
        ]
    },
    "message":[
        {
            "action": "Arbitrarily setting gender to M with certitude 0 (not certain) for aliquot xyz",
            "event": "Error mapping [Gender] for [fuse-mapper-immunespace].",
            "level": 1,
            "source": "fuse-mapper-immunespace:test_func()",
            "timestamp": "2019-09-20T00:00:01Z"
        },
        {
            "action": "Returning only a subset of mapped variables and aborting.",
            "event": "Cannot respond in [500]ms, [fuse-mapper-immunespace].",
            "level": 1,
            "source": "fuse-mapper-immunespace:test_func()",
            "timestamp": "2019-09-20T00:00:01Z"
        }
    ]
}

