# Genoxus Annotation

Genoxus Labs Team: genoxuslabs@gmail.com


Version 1.0   
April 8, 2026



## Introduction

Genoxus Annotation is a harmonized and curated collection of human genetic variant databases designed to support accurate and salable variant annotation. Variant annotation following genetic testing such as whole genome sequencing (WGS) or whole exome sequencing (WES) is a critical step in identifying and interpreting disease-associated genetic factors. As sequencing technologies continue to generate large volumes of genomic data, robust and well-structured annotation resources are essential for translating raw variant calls into clinically meaningful insights.

Genoxus Annotation v1.0 integrates data from [NCBI ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/). ClinVar provides curated information on the clinical significance of a broad spectrum of genetic variants, including single nucleotide variants (SNVs), insertions (INS), deletions (DEL), INDELs, copy number variations (CNVs), and structural variants (SVs), along with their associated diseases and traits.  

GWAS catalog complements ClinVar by focusing primarily on SNVs identified through genome-wide association studies, linking common variants to complex diseases and phenotype traits. (GWAS data is planned in a future release.)

By harmonizing variant representations, standardizing disease terminology, and consolidating evidence across sources, Genoxus Annotation provides a unified framework that streamlines variant interpretation for research and clinical applications.

## Data Organization 

Genoxus Annotation as [Open Data on AWS](https://aws.amazon.com/opendata/) is hosted in a S3 bucket. Files are organized by the following layers: 

Top level directories: **GRCh=37** and **GRCh=38**.

Within each of these folders, multiple folders are created here, each mapping to one chromosome, for example **chr=1**, or **chr=10**, etc. Within each chromosome folder, there are multiple folders mapped to that chromosome’s base pairs(bp) locations. For example, **bp=1-1000000** is mapped to the first 1 million bp, and subsequent folders are mapped with 1 million bp increments. 

This folder naming convention supports data partition by chromosome and bp locations. 

In each of these folders there is a file called **clinvar.parquet**. This file contains all variants documented by ClinVar for the given chromosome's specific bp range. These variants are synchronized with update from NCBI ClinVar.

There is a **misc** folder inside folder **GRCh=37**. A parquet file here contains all variants with unexpected chromosome coordinates.


## Variant Schema

The following example illustrates a variant's schema:

```
{
  "Variant_Identifications": {
    "VariationID": "12578",
    "VariationName": "NM_004985.5(KRAS):c.34G>T (p.Gly12Cys)",
    "VCV_Accession": "VCV000012578"
  },
  "Variant_Type": {
    "VariationType": "single nucleotide variant"
  },
  "Timeline": {
    "DateCreated": "2016-07-26",
    "DateLastUpdated": "2020-06-25",
    "MostRecentSubmission": "",
    "RecordStatus": "current"
  },
  "Variant_Location": [
    {
      "Chromosome": "12",
      "CytogeneticLocation": "",
      "Start": 25398285,
      "Stop": 25398285,
      "TargetLength": 1,
      "Strand": ""
    }
  ],
  "Variant_referenceAllele": "",
  "Variant_alternateAllele": "",
  "GeneList": [
    {
      "Symbol": "KRAS",
      "FullName": "KRAS proto-oncogene, GTPase",
      "ID": "3845",
      "OMIM": "190070",
      "Location": [
        {
          "GRCh38_assembly": {
            "Chromosome": "12",
            "CytogeneticLocation": "12p12.1",
            "Start": 25205246,
            "Stop": 25250929,
            "TargetLength": 45684,
            "Strand": "-"
          }
        },
        {
          "GRCh37_assembly": {
            "Chromosome": "12",
            "CytogeneticLocation": "12p12.1",
            "Start": 25358179,
            "Stop": 25403853,
            "TargetLength": 45675,
            "Strand": "-"
          }
        }
      ]
    }
  ],
  "ProteinChange": [
    "G12C"
  ],
  "Classifications": {
    "GermlineClassification": [
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2019-02-02",
        "DateCreated": "2017-09-29",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-12-16",
        "DateCreated": "2016-07-26",
        "MostRecentSubmission": "2019-04-02",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-03-01",
        "DateCreated": "2016-10-14",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": {
          "DateLastUpdated": "2019-03-31",
          "ReviewStatus": "reviewed by expert panel",
          "Classification": [
            "OncogenicityClassification",
            "Oncogenic"
          ],
          "AssertionMethodList": [
            "ACMG Guidelines, 2015"
          ],
          "Citations": [
            {
              "ID": "25741868",
              "Type": "",
              "Source": "PubMed"
            }
          ],
          "AssertedTraitList": []
        }
      }
    ],
    "SomaticClinicalImpact": [
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2019-02-02",
        "DateCreated": "2017-09-29",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-12-16",
        "DateCreated": "2016-07-26",
        "MostRecentSubmission": "2019-04-02",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-03-01",
        "DateCreated": "2016-10-14",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": {
          "DateLastUpdated": "2019-03-31",
          "ReviewStatus": "reviewed by expert panel",
          "Classification": [
            "OncogenicityClassification",
            "Oncogenic"
          ],
          "AssertionMethodList": [
            "ACMG Guidelines, 2015"
          ],
          "Citations": [
            {
              "ID": "25741868",
              "Type": "",
              "Source": "PubMed"
            }
          ],
          "AssertedTraitList": []
        }
      }
    ],
    "OncogenicityClassification": [
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2019-02-02",
        "DateCreated": "2017-09-29",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-12-16",
        "DateCreated": "2016-07-26",
        "MostRecentSubmission": "2019-04-02",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": ""
      },
      {
        "ConditionList": [
          {
            "Type": "Disease",
            "Names": [
              {
                "Prostate cancer, hereditary, 1": "Preferred"
              }
            ],
            "Affected_Genes": [
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              },
              {
                "Preferred": {
                  "Symbol": "Prostate cancer, hereditary, 1",
                  "OMIM": ""
                }
              }
            ],
            "Citations": [
              {
                "ID": "25394175",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "URL": "https://www.nccn.org/professionals/physician_gls/pdf/prostate.pdf",
                "CitationText": "NCCN Clinical Practice Guidelines in Oncology,\n                                    Prostate Cancer, Version 4.2022",
                "Type": "practice guideline"
              },
              {
                "ID": "31829902",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "35924163",
                "Type": "general",
                "Source": "PubMed"
              },
              {
                "ID": "9339641",
                "Type": "general",
                "Source": "pmc"
              }
            ]
          }
        ],
        "DateLastEvaluated": "2016-03-01",
        "DateCreated": "2016-10-14",
        "MostRecentSubmission": "2019-03-31",
        "ReviewStatus": "",
        "Description": "",
        "ClinicalAssertion": {
          "DateLastUpdated": "2019-03-31",
          "ReviewStatus": "reviewed by expert panel",
          "Classification": [
            "OncogenicityClassification",
            "Oncogenic"
          ],
          "AssertionMethodList": [
            "ACMG Guidelines, 2015"
          ],
          "Citations": [
            {
              "ID": "25741868",
              "Type": "",
              "Source": "PubMed"
            }
          ],
          "AssertedTraitList": []
        }
      }
    ]
  }
}
```

## DDL
File TableDDL.json is produced with AWS Glue scanning our data, and provided in this project for your reference. Schema may change in future releases. 

## Roadmap

The following datasets are planned in future releases:

[GWAS](https://www.ebi.ac.uk/gwas/) data is planned to be included in v2 release.


[GnomAD](https://gnomad.broadinstitute.org/) data is planned to be included in v3 release.


