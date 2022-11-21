# GPC DVINCI Data Linkage Pilot Project
## Overview
As one of the contractual milestones for PCORnet Phase 3, GPC will advance Datavant tokenization of the Veterans Administration (VA) and Department of Defense (DoD) electronic health records to support linkage across PCORnet and the corresponding Governance processes. Leveraging existing inter-network resources and in support of the [brain injury data sharing (BIDS)](doc/GPC_LEC_2022_BIDS-VA-Linkage.pptx) project, we propose a demonstration linkage project between GPC EHR data and DoD/VA EHR data to advance the understanding of treatment, progression and long-term outcomes of traumatic brain injury (TBI) for Servicemembers and Veterans.

Participating sites will need to maintain [Datavant®](https://datavant.com/) software for generating GPC-specific hash token used for linking with VA health data in support of the proposed overlapping analysis and federate modeling. 

****************************************************************************

## Scope of Work Overview
1. Administrative preparation: Datavant order form, IRB or non-human-determination, GPC DROC request
2. Hash Token Generation and Submission: Performing sites will submit GPC-specific hash token table to GROUSE following the AWS-based secure process (established GROUSE data submission process)
3. Linkage mapping generation: Coordinating site will aggregate hash token tables, perform deduplication and coordinate with leading site and VA to generate linkage mapping
4. Analysis and Result Dissemination: Authorized analysts at CS will perform overlapping analysis, federated analysis on selected topics to assess the validity and utility of the linked dataset

****************************************************************************

## Administrative Preparations
- As an extension of the BIDS project, a no-cost and no-signature Datavant order form has been officially executed for the linkage work. Sites can download the executed order form for local reference from: [Executed Datavant Order Form](doc/Final%20BIDS%20DaVINCI%20GPC%20Linkage%20Order%20Form_v2%20(002)%20FE.pdf)
- Non-human subject derermination letters have been obtained from IRBs of both the leading site (University of Utah) and coordination site (University of Missouri)

|Site Role|Site PI|Site Name|NHS letter|
|---------|-------|---------|----------|
|Leading site|[Dr.Jacob Kean](https://medicine.utah.edu/faculty/mddetail/u6002766)|University of Utah|[NHS-Kean-UU](doc/NHS-Kean-UU.pdf)|
|Coordinating site|[Dr.Xing Song](https://medicine.missouri.edu/faculty/xing-song-phd)|University of Missouri|[NHS-Song-MU](doc/NHS-Song-MU.pdf)|
- A GPC DROC request has been submitted: [DROC Request Submission](doc/GPCDROCOversightRequest_GPCDRO_2022-11-21_1051.pdf)

************************************************************************

## Participating Sites Workflow

![dataflow](res/GPC%20-%20VA%20Linkage%20%20-%20Option%201_%20GPC%20gets%20crosswalk%20FINAL.png)

As entailed in the data flow figure above, sites are only required to complete Step 1. For full transparency and document completion, we will describe the entire workflow below: 

### Step 1: Data Tokenization and Submission (*at GPC-Site*)
#### Step 1.1 (Tokenization)         
Assume that sites have all generated the [site-specific token](https://datavant.com/wp-content/uploads/dlm_uploads/2018/09/WhitePaper_-De-Identifying-and-Linking-Structured-Data.pdf) based on the same configuration as PCORnet hash tokens (tokens 1,2,3,4,5,16). Please ensure that these site-specific tokens are not outdated and a **local mapping to CDM PATID submitted to GROUSE** is preserved. 

PCORnet site-specific tokens generated previously can be further converted to `gpc_va` study-specific transit tokens, by running the following command in cooresponding operation system where datavant executable is installed. You will need to specify the following parameter before running the command: 
- \<yoursitedvkey\>: is the name key of your site specified in the Datavant portal. Please note that site-specific tokens are not the transit tokens sent to PCORnet. PCORnet transit tokens cannot be converted to `gpc_va` transit tokens.   
- \<credentials\> or \<credentials.txt\> file: is your user-specific credentials, retrieved from the Datavant portal and stored in a plain text file in the required location
- \<yoursitenameabbr\>: is your site-specific abbreviation (e.g., 'UMO' for 'University of Missouri', this is in line with PCORnet abbreviations) to separate your hash token file form the others. 

*Windows*
```bash
cat credentials.txt | .\Datavant_Win.exe transform-tokens --to gpc_va -s <yoursitedvkey> -i tokenization_input.csv -o tokenization_output_<yoursitenameabbr>.csv --credentials
```

*Mac*
```bash
cat credentials | .\Datavant_Mac transform-tokens --to gpc_va -s <yoursite> -i tokenization_input.csv -o tokenization_output_<yoursitenameabbr>.csv --credentials
```

*Linux*
```bash
cat credentials | .\Datavant_Linux transform-tokens --to gpc_va -s <yoursite> -i tokenization_input.csv -o tokenization_output_<yoursitenameabbr>.csv --credentials
```

#### Step 1.2 (Submission)       
Participating sites are expected to submit hash token files to GPC CC following the established process of submitting their CDM datamarts onto [GROUSE*](https://github.com/gpcnetwork/GROUSE). Sites can choose to: 
a) either submit to their site-specific upload buckets via your site-specific submission url: 

| **GPC Site** | **S3 Bucket URL**                                                  |
|--------------|--------------------------------------------------------------------|
| Allina       | https://s3.console.aws.amazon.com/s3/buckets/gpc-allina-upload/    |
| IHC          | https://s3.console.aws.amazon.com/s3/buckets/gpc-ihc-upload/       |
| KUMC         | https://s3.console.aws.amazon.com/s3/buckets/gpc-kumc-upload/      |
| MCRI         | https://s3.console.aws.amazon.com/s3/buckets/gpc-mcri-upload/      |
| MCW          | https://s3.console.aws.amazon.com/s3/buckets/gpc-mcw-upload/       |
| UTHSCSA      | https://s3.console.aws.amazon.com/s3/buckets/gpc-uthscsa-upload/   |
| UTSW         | https://s3.console.aws.amazon.com/s3/buckets/gpc-utsw-upload/      |
| UNMC         | https://s3.console.aws.amazon.com/s3/buckets/gpc-unmc-upload/      |
| UU           | https://s3.console.aws.amazon.com/s3/buckets/gpc-uu-upload/        |
| UIOWA        | https://s3.console.aws.amazon.com/s3/buckets/gpc-uiowa-upload/     |
| UTHouston    | https://s3.console.aws.amazon.com/s3/buckets/gpc-uthouston-upload/ |
| WashU        | https://s3.console.aws.amazon.com/s3/buckets/gpc-washu-upload/     |

OR 

b) using `aws s3 ls` or `aws s3 sync` commands to upload data to site-specific bucket: 

| **GPC Site** | **<upload-bucket-name>**  |
|--------------|---------------------------|
| Allina       | `gpc-allina-upload`       |
| IHC          | `gpc-ihc-upload`          |
| KUMC         | `gpc-kumc-upload`         |
| MCRI         | `gpc-mcri-upload`         |
| MCW          | `gpc-mcw-upload`          |
| UTHSCSA      | `gpc-uthscsa-upload`      |
| UTSW         | `gpc-utsw-upload`         |
| UNMC         | `gpc-unmc-upload`         |
| UU           | `gpc-uu-upload`           |
| UIOWA        | `gpc-uiowa-upload`        |
| UTHouston    | `gpc-uthouston-upload`    |
| WashU        | `gpc-washu-upload`        |

More technical details can be found from the [GROUSE Instruction Page](https://github.com/gpcnetwork/GROUSE#readme). Note that GROUSE gpcnetwork repo is private for security and privacy reasons. If you can't access the GROUSE gpcnetwork repo, please reach out to ask-umbmi@umsystem.edu or create an issue at https://github.com/gpcnetwork/gpc-va-linkage/issues 


### Step 2: Token Integration and Transfer (*at GPC-CC*)
#### Step 2.1 (Extraction): 
#### Step 2.2 (Integration): 
#### Step 2.3 (Transfer): 


#### Step 3: Linkage and Overlap Analysis** (*at VA*)
#### Step 3.1 (Linkage): 
#### Step 3.2 (Analysis): 
#### Step 3.3 (Retention): 


************************************************************************
*Copyright (c) 2022 The Curators of University of Missouri*</br>
*Share and Enjoy according to the terms of the MIT Open Source License*</br>
*Repo structure style follows [GitHub Repository Structure Best Practices](https://soulaimanghanem.medium.com/github-repository-structure-best-practices-248e6effc405) (Ghanem, 2021)*



