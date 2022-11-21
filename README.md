# GPC DVINCI Data Linkage Pilot Project
## Overview
As one of the contractual milestones for PCORnet Phase 3, GPC will advance Datavant tokenization of the Veterans Administration (VA) and Department of Defense (DoD) electronic health records to support linkage across PCORnet and the corresponding Governance processes. Leveraging existing inter-network resources and in support of the [brain injury data sharing (BIDS)](doc/GPC_LEC_2022_BIDS-VA-Linkage.pptx) project, we propose a demonstration linkage project between GPC EHR data and DoD/VA EHR data to advance the understanding of treatment, progression and long-term outcomes of traumatic brain injury (TBI) for Servicemembers and Veterans.  

Participating sites will need to maintain [Datavant®](https://datavant.com/) software for generating GPC-specific hash token used for linking with VA health data in support of the proposed overlapping analysis and federate modeling. Sites are expected to submit hash token tables to GPC CC following the established process of submitting their CDM datamarts onto GROUSE. 

## Scope of Work Overview
1. Administrative preparation: Datavant order form, IRB or non-human-determination, GPC DROC request
2. Hash Token Generation and Submission: Performing sites will submit GPC-specific hash token table to GROUSE following the AWS-based secure process (established GROUSE data submission process)
3. Linkage mapping generation: Coordinating site will aggregate hash token tables, perform deduplication and coordinate with leading site and VA to generate linkage mapping
4. Analysis and Result Dissemination: Authorized analysts at CS will perform overlapping analysis, federated analysis on selected topics to assess the validity and utility of the linked dataset

## Data Flow
![dataflow](res/GPC%20-%20VA%20Linkage%20%20-%20Option%201_%20GPC%20gets%20crosswalk%20FINAL.png)

## Participating Sites Workflow
**Administrative Preparations**
- As an extension of the BIDS project, a no-cost and no-signature Datavant order form has been officially executed for the linkage work. Sites can download the executed order form for local reference from: [Executed Datavant Order Form](doc/Final%20BIDS%20DaVINCI%20GPC%20Linkage%20Order%20Form_v2%20(002)%20FE.pdf)
- Non-human subject derermination letters have been obtained from IRBs of both the leading site (University of Utah) and coordination site (University of Missouri)
|Role|Site PI|Site Name|NHS letter|
|Leading|[Dr.Jacob Kean]()|University of Utah|[NHS-Kean-UU](doc/NHS-Kean-UU.pdf)|
|Coordinating|[Dr.Xing Song]()|University of Missouri|[NHS-Song-MU](doc/NHS-Song-MU.pdf)|
- GPC DROC request has been submitted

**Step 1: Data Tokenization**
*Site*


**Step 2: Token Submission and Integration**
*GPC CC*

**Step 3: Linkage and Overlap Analysis**
*VA*






