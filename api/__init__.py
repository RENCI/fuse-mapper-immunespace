import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_mapping(body):
    # kludge, works for this query:
    # curl -X POST -H "Content-Type: application/json" --data '{"subjectIds":["1", "2"], "timestamp":"2020-07-01T14:29:15.453Z", "data":{"foo":"bar"} }' http://localhost:8082/mapping
    ret_response = []
    ret_response.append(
        [
            {
                "subjectId": "1",
                "values": [
                    {
                        "title": "Age",
                        "id": "LOINC:30525-0",
                        "certitude": 2,
                        "group": "Subject variable",
                        "how": "The value was specified by the end user.",
                        "legalValues": {
                            "minimum": "0",
                            "type": "number"
                        },
                        "timestamp": "2020-07-01T14:29:15.453Z",
                        "variableDescription": "The age is determined by subtracting the birthdate from the current time. Also known as 'chronological age' or 'Post Natal Age' (PNA). Specified as somen fraction of years, convention.",
                        "variableValue": {
                            "units": "years",
                            "value": "0.5"
                        },
                        "why": "Age is used to compare the gene expression of same-age subjects"
                    },
                    {
                        "title": "Gene expression",
                        "id": "FUSE:expression",
                        "certititude": 2,
                        "how": "From Immunescape microarrays",
                        "variableValue": {
                            "sampleId":"SAMP:1", 
                            "aliquotId":"SAMP:1",
                            "system": "ensembl",
                            "value": {"6005":0.5, "622":0.4, "6120":0.3, "22934":0.2}
                        }
                    }
                ]
            },
            {
                "subjectId": "2",
                "values": [
                    {
                        "title": "Age",
                        "id": "LOINC:30525-0",
                        "certitude": 2,
                        "group": "Subject variable",
                        "how": "The value was specified by the end user.",
                        "legalValues": {
                            "minimum": "0",
                            "type": "number"
                        },
                        "timestamp": "2020-08-01T14:29:15.453Z",
                        "variableDescription": "The age is determined by subtracting the birthdate from the current time. Also known as 'chronological age' or 'Post Natal Age' (PNA). Specified as somen fraction of years, convention.",
                        "variableValue": {
                            "units": "years",
                            "value": "10.7"
                        },
                        "why": "Age is used to compare the gene expression of same-age subjects"
                    },
                    {
                        "title": "Gene expression",
                        "id": "FUSE:expression",
                        "certititude": 2,
                        "how": "From Immunescape microarrays",
                        "variableValue": {
                            "sampleId":"SAMP:1", 
                            "aliquotId":"SAMP:1",
                            "system": "ensembl",
                            "value": {"6005":1.5, "622":0.74, "6120":0.33, "22934":1.2}
                        }
                    }
                ]
            }

        ]
   )

    return ret_response

import json
def get_config():
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)
        
