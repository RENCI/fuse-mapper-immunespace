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
            "participants": [
                {
                    "participantId": "test_empty",
                    "values": [
                        {
                            "title": "Study Time Collected",
                            "id": "study_time_collected",
                            "certitude": 2,
                            "group": "pData",
                            "how": "The value was provided by the digital object server.",
                            "timestamp": "2020-08-01T14:29:15.453Z",
                            "variableValue": { "value":0, "units": "Days" }
                        },
                        { 
                            "title": "Gene expression",
                            "id": "FUSE:expression",
                            "certititude": 2,
                            "how": "From Immunescape microarrays",
                            "variableValue": {
                                "value": {
                                    "system": "entrez",
                                    "aliquots": [ 
                                        {
                                            "aliquotId":"test_empty_aliquot1",
                                            "value": {
                                                "1": "1.0",
                                                "503538": "2.0",
                                                "29974": "3.0"
                                            }
                                        },
                                        {
                                            "aliquotId":"test_empty_aliquot2",
                                            "value": {
                                                "1": "1.5",
                                                "503538": "2.5",
                                                "29974": "3.5"
                                            }
                                        } 
                                    ]
                                }
                            }
                        }
                    ]
                }
            ]
        }
    )

    ret_response.append(
        {
            "objectId": "cellfie_group2",
            "participants": [ 
                {
                    "participantId": "SUB112834.269",
                    "values": [
                        {
                            "title": "Study Time Collected",
                            "id": "study_time_collected",
                            "certitude": 2,
                            "group": "pData",
                            "how": "The value was provided by the digital object server.",
                            "timestamp": "2020-08-01T14:29:15.453Z",
                            "variableValue": { "value":0, "units": "Days" }
                        },
                        {
                            "title": "Gene expression",
                            "id": "FUSE:expression",
                            "certititude": 2,
                            "how": "From Immunescape microarrays",
                            "variableValue": {
                                "value": {
                                    "system": "entrez",
                                    "aliquots": [ {
                                        "aliquotId":"BS586128",
                                        "value": {
                                            "1": "3.78615018912845",
                                            "503538": "3.68295613722495",
                                            "29974": "3.82804625098162"
                                        }
                                    } ]
                                }
                            }
                        }
                    ]
                },
                {
                    "participantId": "SUB112834.269",
                    "values": [
                        {
                            "title": "Study Time Collected",
                            "id": "study_time_collected",
                            "certitude": 2,
                            "group": "pData",
                            "how": "The value was provided by the digital object server.",
                            "timestamp": "2020-08-01T14:29:15.453Z",
                            "variableValue": { "value": 7, "units": "Days" }
                        },
                        {
                            "title": "Gene expression",
                            "id": "FUSE:expression",
                            "certititude": 2,
                            "how": "From Immunescape microarrays",
                            "variableValue": {
                                "system": "entrez",
                                "aliquots": [ {
                                    "aliquotId":"BS586240",
                                    "value": {
                                        "1": "3.15087086107396",
                                        "503538": "3.22078940893019",
                                        "29974": "3.06783937011117"
                                    }
                                } ]
                            }
                        }
                    ]
                },
                {
                    "participantId": "SUB112832.269",
                    "values": [
                        {
                            "title": "Study Time Collected",
                            "id": "study_time_collected",
                            "certitude": 2,
                            "group": "pData",
                            "how": "The value was provided by the digital object server.",
                            "timestamp": "2020-08-01T14:29:15.453Z",
                            "variableValue": { "value": 0, "units": "Days" }
                        },
                        {
                            "title": "Gene expression",
                            "id": "FUSE:expression",
                            "certititude": 2,
                            "how": "From Immunescape microarrays",
                            "variableValue": {
                                "system": "entrez",
                                "aliquots": [ {
                                    "aliquotId":"BS586131",
                                    "value": {
                                        "1": "3.68940264786164",
                                        "503538": "3.51391883064394",
                                        "29974": "3.50394031553657"
                                    }
                                } ]
                            }
                        }
                    ]
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

