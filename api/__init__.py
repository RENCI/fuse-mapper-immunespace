import os
import logging
from pathlib import Path
from tx.functional.maybe import Just, Nothing
from tx.functional.either import Left
from tx.functional.utils import identity
from pathvalidate import validate_filename
from tx.requests.utils import get
import yappi
import json

yappi.set_clock_type(os.environ.get("CLOCK_TYPE", "wall"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config_url = os.environ.get("CONFIG_URL")

def mappend(a, b):
    if isinstance(a, list) and isinstance(b, list):
        obj = a + b
    elif isinstance(a, dict) and isinstance(b, dict):
        obj = {}
        for k, v in a.items():
            if k in b:
                obj[k] = mappend(v, b[k])
            else:
                obj[k] = v
        for kb, vb in b.items():
            if kb not in a:
                obj[kb] = vb
    else:
        obj = b

    return obj
    
def assign(array, keys, value):
    if len(keys) == 0:
        return mappend(array, value)
    else:
        key, *the_keys = keys
        if array is None:
            array = []

        if isinstance(key, int):
            if isinstance(array, list):
                if len(array) <= key:
                    array = array + [{}] * (key + 1 - len(array))
            else:
                if key not in array:
                    array[key] = {}
        else:
            if isinstance(array, list):
                obj = {}
                for i, elem in enumerate(array):
                    obj[i] = elem
                array = obj
            if key not in array:
                array[key] = {}
                
        array[key] = assign(array[key], the_keys, value)
        
        return array

    
def getModelParameter(modelParameters, modelParameterId, proc, default):
    specNames = [modelParameter for modelParameter in modelParameters if modelParameter["id"] == modelParameterId]
    if len(specNames) == 0 or specNames[0].get("parameterValue", {}).get("value") is None:
        specName = default()
    else:
        specName = proc(specNames[0]["parameterValue"]["value"])
    return specName


def jsonify(obj):
    if isinstance(obj, dict):
        return {k: json.dumps(jsonify(v), sort_keys=True) if k == "how" else jsonify(v) for k, v in obj.items()}
    elif isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        return [jsonify(elem) for elem in obj]
    elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, bool) or isinstance(obj, str) or obj is None:
        return obj
    else:
        return str(obj)


output_dir = os.environ.get("OUTPUT_DIR")

def mappingClinicalFromData(body):
    if "settingsRequested" not in body:
        body["settingsRequested"] = config['settingsDefaults']
    patient_ids = body["patientIds"]
    timestamp = body["timestamp"]

    ret_response = []
    for i, patient_id in enumerate(patient_ids):
        val = pdsphenotypemapping.dispatcher.lookupClinicalsFromData(patient_id, i, timestamp, body)
        if isinstance(val, tuple):
            # mapping failed since a (error_message, status_code) tuple is returned
            return val
        else:
            ret_response.append({
                "patientId": patient_id,
                "values": val
            })
    return ret_response

def get_default_config(default):

    if config_url is None:
        return default
    obj = get(config_url)
    if isinstance(obj, Left):
        return objl.value

    else:
        settingsDefault = None if config_url is None else obj.value.get("settingsDefaults", None)

        return {
            "title": "fuse immunespace mapper",
            'piid': "fuse-mapper-immunespace",
            "pluginType": "m",
            **({
                "settingsDefaults": settingsDefault,
            } if settingsDefault is not None else {}),
            "pluginTypeTitle": "Mapping"
        }


config = {
    "pluginDependencies": ["pdspi-fhir-example"],
    "title": "tx-parallex variable mapper",
    "pluginType": "m",
    "pluginTypeTitle": "Mapping",
    "pluginSelectors": [],
    "settingsDefaults": {
        "pluginSelectors": [],
        "patientVariables": [
            {
                "id": "LOINC:2160-0",
                "legalValues": {
                    "type": "number"
                },
                "title": "Serum creatinine"
            },
            {
                "id": "LOINC:82810-3",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Pregnancy"
            },
            {
                "id": "HP:0001892",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Bleeding"
            },
            {
                "id": "HP:0000077",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Kidney dysfunction"
            },
            {
                "id": "LOINC:45701-0",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Fever"
            },
            {
                "id": "LOINC:LP212175-6",
                "legalValues": {
                    "type": "string"
                },
                "title": "Date of fever onset"
            },
            {
                "id": "LOINC:64145-6",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Cough"
            },
            {
                "id": "LOINC:85932-2",
                "legalValues": {
                    "type": "string"
                },
                "title": "Date of cough onset"
            },
            {
                "id": "LOINC:54564-0",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Shortness of breath"
            },
            {
                "id": "LOINC:LP172921-1",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Cardiovascular disease"
            },
            {
                "id": "LOINC:54542-6",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Pulmonary disease"
            },
            {
                "id": "LOINC:LP128504-0",
                "legalValues": {
                    "type": "boolean"
                },
                "title": "Autoimmune disease"
            },
            {
                "id": "LOINC:LP21258-6",
                "legalValues": {
                    "type": "number"
                },
                "title": "Oxygen saturation"
            },
            {
                "id": "LOINC:30525-0",
                "legalValues": {
                    "type": "integer"
                },
                "title": "Age"
            },
            {
                "id": "LOINC:54134-2",
                "legalValues": {
                    "type": "string"
                },
                "title": "Race"
            },
            {
                "id": "LOINC:54120-1",
                "legalValues": {
                    "type": "string"
                },
                "title": "Ethnicity"
            },
            {
                "id": "LOINC:21840-4",
                "legalValues": {
                    "type": "string"
                },
                "title": "Sex"
            },
            {
                "id": "LOINC:8302-2",
                "legalValues": {
                    "type": "number"
                },
                "title": "Height"
            },
            {
                "id": "LOINC:29463-7",
                "legalValues": {
                    "type": "number"
                },
                "title": "Weight"
            },
            {
                "id": "LOINC:56799-0",
                "legalValues": {
                    "type": "string"
                },
                "title": "Address"
            },
            {
                "id": "LOINC:39156-5",
                "legalValues": {
                    "type": "number"
                },
                "title": "BMI"
            }
        ],
        "modelParameters": [
            {
                "id": "nthreads",
                "title": "number of threads",
                "legalValues": {"type": "integer"},
                "parameterValue": {
                    "value": 3
                }
            }, {
                "id": "level",
                "title": "nested for paralleization level",
                "legalValues": {"type": "integer"},
                "parameterValue": {
                    "value": 0
                }
            }, {
                "id": "specName",
                "title": "spec name",
                "legalValues": {"type": "string"},
                "parameterValue": {
                    "value": "spec.py"
                }
            }, {
                "id": "libraryPath",
                "title": "Python load module path",
                "legalValues": {"type": "string"},
                "parameterValue": {
                    "value": None
                }
            }
        ]
    }
}

config = {
    "title": "FUSE immunespace mapper data provider",
    "pluginType": "m",
    "pluginTypeTitle": "mapper",
}
def get_config():
    return config
