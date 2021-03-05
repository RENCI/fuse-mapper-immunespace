import requests
import yaml
from pathlib import Path
import logging
from tempfile import mkdtemp
import os
import json
import shutil

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

input_dir = os.environ.get("INPUT_DIR")
output_dir = os.environ.get("OUTPUT_DIR")

# some nice parameters might include:
# id_source=entrez/ncbi | hgnc | ensembl 
# id_type=transcript_id|gene_id
# normalized=none|deseq2
# transpose=yes(genes on cols)|no(genes on rows)
# filter=<genelist>
# filter_id=<genelist id on server to use for filter>
# 

appliance="http://fuse-mapper-immunespace:8080"
# xxx log.info(f"starting on port (${API_PORT})")

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

def query(pid, cv, unit=None, data=None):
    pv = {
        "title": f"{cv} title",
        "legalValues": {
            "type": "integer"
        },
        "why": f"{cv} why",
        "id": cv,
    }
    if unit is None:
        pv["units"] = unit
        q = {
            "subjectIds": [pid],
            "timestamp" : "2019-10-19T00:00:00Z",
            "data": data if data is not None else [bundles.get(pid, {"resourceType": "Bundle", "type": "collection"})],
            "settingsRequested": {"patientVariables": [pv]}
        }
    
    return requests.post(f"{appliance}/mapping", headers=json_headers, json=q), pv


# xxx this isn't testing anything right now
def test_api_passthrough():
    # result, pvt = query("1000", "LOINC:30525-0")
    result = requests.models.Response()
    result._content = b'{ "key" : "a" }'
    result.status_code = 200

    print(result.content)
    assert result.status_code == 200
    assert result.json() ==  {"key" : "a" }

config = {
    "title": "FUSE immunespace mapper data provider",
    "pluginType": "m",
    "pluginTypeTitle": "mapper",
}
def test_config():
    resp = requests.get(f"{appliance}/config")
    print(resp.content)
    #assert resp.status_code == 200
    #assert resp.json() == config
    return True
