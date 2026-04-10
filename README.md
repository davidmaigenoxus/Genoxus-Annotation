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
   "Variant_Identifications":{
      "ID":"144791",
      "Name":"GRCh38/hg38 1p36.33(chr1:904070-978251)x1",
      "VCV_accession":null
   },
   "Variant_Type":"copy number loss",
   "Record_Timeline":{
      "Date_Created":1436745600000,
      "Date_Last_Updated":1697328000000,
      "Date_Most_Recent_Submission":1436745600000,
      "Current_Status":"current"
   },
   "Genomic_Location":{
      "Chromosome":"1",
      "Cytogenetic_Location":"1p36.33",
      "Start":839450,
      "Stop":913631,
      "Strand":null,
      "Target_Length":74182
   },
   "Reference_Allele":null,
   "Alternate_Allele":null,
   "Host_Genes":[
      {
         "Symbol":"KLHL17",
         "Full_Name":"kelch like family member 17",
         "ID":"339451",
         "OMIM":"619262",
         "Location":{
            "Chromosome":"1",
            "Cytogenetic_Location":"1p36.33",
            "Start":895966,
            "Stop":901098,
            "Strand":"+",
            "Target_Length":5133
         },
         "Haploinsufficiency_Assertion":null,
         "Triplosensitivity_Assertion":null
      },
      {
         "Symbol":"NOC2L",
         "Full_Name":"NOC2 like nucleolar associated transcriptional repressor",
         "ID":"26155",
         "OMIM":"610770",
         "Location":{
            "Chromosome":"1",
            "Cytogenetic_Location":"1p36.33",
            "Start":879582,
            "Stop":894678,
            "Strand":"-",
            "Target_Length":15097
         },
         "Haploinsufficiency_Assertion":null,
         "Triplosensitivity_Assertion":null
      },
      {
         "Symbol":"PLEKHN1",
         "Full_Name":"pleckstrin homology domain containing N1",
         "ID":"84069",
         "OMIM":null,
         "Location":{
            "Chromosome":"1",
            "Cytogenetic_Location":"1p36.33",
            "Start":901876,
            "Stop":910487,
            "Strand":"+",
            "Target_Length":8612
         },
         "Haploinsufficiency_Assertion":null,
         "Triplosensitivity_Assertion":null
      },
      {
         "Symbol":"SAMD11",
         "Full_Name":"sterile alpha motif domain containing 11",
         "ID":"148398",
         "OMIM":"616765",
         "Location":{
            "Chromosome":"1",
            "Cytogenetic_Location":"1p36.33",
            "Start":861120,
            "Stop":879960,
            "Strand":"+",
            "Target_Length":18841
         },
         "Haploinsufficiency_Assertion":null,
         "Triplosensitivity_Assertion":null
      }
   ],
   "Protein_Changes":null,
   "HGVSs":[
      {
         "Assembly":"GRCh38",
         "Type":"genomic, top-level",
         "Nucleotide_Expression":"NC_000001.11:g.(?_904070)_(978251_?)del",
         "Protein_Expression":null,
         "Molecular_Consequence":null
      },
      {
         "Assembly":"NCBI36",
         "Type":"genomic, top-level",
         "Nucleotide_Expression":"NC_000001.9:g.(?_829313)_(903494_?)del",
         "Protein_Expression":null,
         "Molecular_Consequence":null
      },
      {
         "Assembly":"GRCh37",
         "Type":"genomic, top-level",
         "Nucleotide_Expression":"NC_000001.10:g.(?_839450)_(913631_?)del",
         "Protein_Expression":null,
         "Molecular_Consequence":null
      }
   ],
   "XRefs":[
      {
         "Database":"dbVar",
         "Accession":"nssv583288",
         "Type":null
      },
      {
         "Database":"dbVar",
         "Accession":"nsv497257",
         "Type":null
      }
   ],
   "RCVs":[
      {
         "Accession":"RCV000134195",
         "Title":"GRCh38/hg38 1p36.33(chr1:904070-978251)x1 AND See cases",
         "Description":null,
         "Classified_Conditions":null,
         "Classifications":[
            {
               "Name":"GermlineClassification",
               "Review_Status":null,
               "Descriptions":[
                  {
                     "Description":"Benign",
                     "Clinical_Impact_Assertion_Type":null,
                     "Clinical_Impact_Clinical_Significance":null,
                     "Submission_Count":1,
                     "Date_Last_Evaluated":1291075200000
                  }
               ]
            }
         ]
      }
   ],
   "Classifications":[
      {
         "Name":"GermlineClassification",
         "Date_Last_Evaluated":1291075200000,
         "Date_Created":1436745600000,
         "Date_Most_Recent_Submission":1436745600000,
         "Number_Of_Submissions":1,
         "Review_Status":null,
         "Description":null,
         "Conditions":[
            {
               "Type":"PhenotypeInstruction",
               "Contributes_To_Aggregate_Classification":true,
               "Traits":[
                  {
                     "Name":"See cases",
                     "Label":"Preferred",
                     "XRefs":null
                  }
               ],
               "Symbolic_Trait":null,
               "Attributes":null,
               "Citations":null
            }
         ]
      }
   ],
   "Clinical_Assertions":[
      {
         "Asserted_Classification":{
            "Name":"GermlineClassification",
            "Description":"Benign",
            "Review_Status":"no assertion criteria provided",
            "Date_Last_Evaluated":1291075200000,
            "Clinical_Impact_Assertion_Type":null,
            "Clinical_Impact_Clinical_Significance":null,
            "Comment":null,
            "Citations":null
         },
         "Assertion":"variation to disease",
         "Attributes":null,
         "ID":"313157",
         "Date_Submission":1403308800000,
         "Date_Last_Updated":1436745600000,
         "Date_Created":1409356800000,
         "Contributes_To_Aggregate_Classification":true,
         "ClinVar_Accession":"SCV000173719",
         "ClinVar_Submitter":"GeneDx",
         "Record_Status":"current",
         "Observed_Ins":[
            {
               "Sample":null,
               "Is_Affected":true,
               "Method":"clinical testing",
               "Observed_Data":""
            }
         ],
         "Conditions":null
      }
   ],
   "Trait_Mappings":[
      {
         "TraitType":"Finding",
         "MedGen_CUI":"CN218420",
         "MedGen_Name":"Developmental delay AND/OR other significant developmental or morphological phenotypes"
      },
      {
         "TraitType":"PhenotypeInstruction",
         "MedGen_CUI":"None",
         "MedGen_Name":"See cases"
      }
   ]
}
```

## DDL
File TableDDL.json is produced with AWS Glue scanning our data, and provided in this project for your reference. Schema may change in future releases. 

## Roadmap

The following datasets are planned in future releases:

[GWAS](https://www.ebi.ac.uk/gwas/) data is planned to be included in v2 release.


[GnomAD](https://gnomad.broadinstitute.org/) data is planned to be included in v3 release.


