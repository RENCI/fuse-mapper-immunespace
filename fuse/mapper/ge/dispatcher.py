# xxx implement a cache like this:
# import fuse.server.cache as cache

import docker


# library API
# from fuse.server.immunespace.dispatcher import GetObject
def GetMapping(query):
    resc = _get_mapping(query)

    if resc is not None:
        return resc
    else:
        return "not found", 404

# internal methods

def _get_mapping(query):


    # kludge, works for this query:
    # curl -X POST -H "Content-Type: application/json" --data '{"objectIds":["1", "2"], "timestamp":"2020-07-01T14:29:15.453Z", "data":{"foo":"bar"} }' http://localhost:8082/mapping
    ret_response = []
    ret_response.append(
         {
                "objectId": "1",
                "values": [
                    {
                        "title": "Age",
                        "id": "LOINC:30525-0",
                        "certitude": 2,
                        "group": "Object variable",
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
                        "why": "Age is used to compare the gene expression of same-age objects"
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
            })
    ret_response.append(
            {
                "objectId": "2",
                "values": [
                    {
                        "title": "Age",
                        "id": "LOINC:30525-0",
                        "certitude": 2,
                        "group": "Object variable",
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
                        "why": "Age is used to compare the gene expression of same-age objects"
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
   )
    
    return ret_response

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
# can ask for a record by object id
# object id list,
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

