import os
import logging
from pathlib import Path
from tx.functional.maybe import Just, Nothing
from tx.functional.either import Left
from tx.functional.utils import identity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_mapping(body):
    # kludge, works for this query:
    # curl -X POST -H "Content-Type: application/json" --data '{"patientIds":["1"], "timestamp":"2020-07-01T14:29:15.453Z", "data":{"foo":"bar"} }' http://localhost:8082/mapping
    ret_response = []
    ret_response.append(
        [
            {
                "patientId": "string",
                "values": [
                    {
                        "certitude": 2,
                        "group": "Patient variable",
                        "how": "The value was specified by the end user.",
                        "id": "LOINC:30525-0",
                        "legalValues": {
                            "minimum": "0",
                            "type": "number"
                        },
                        "timestamp": "2020-07-01T14:29:15.453Z",
                        "title": "Age",
                        "variableDescription": "The age is determined by subtracting the birthdate from the current time. Also known as 'chronological age' or 'Post Natal Age' (PNA). Specified as somen fraction of years, convention.",
                        "variableValue": {
                            "units": "years",
                            "value": "0.5"
                        },
                        "why": "Age is used to calculate the creatinine clearance. Dosing is lower for geriatric patient and contraindicated for pediatric patients"
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
        
