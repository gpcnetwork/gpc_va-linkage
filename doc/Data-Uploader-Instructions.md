# NAACCR Data Upload to designated AWS S3 bucket

The following parameter table provides a quick overview of the recurrent NAACCR data upload task. Please read through the document for step-by-step instructions of data upload.

| **Parameter**    | **Value**                                                                     |
|------------------|-------------------------------------------------------------------------------|
| Upload Frequency | *Monthly*                                                                     |
| Upload Mechanism | *Full extract since inception of the registry*                                |
| Data I/O flow    | *Oncolog -> Common Drive -> S3 bucket*                                        |
| Source File Path | *\\\\umh.edu\\data\\EF_Cancer_Registry\\Common\\Tiger Institute Folder\\2021* |


## Account Initialization

After your AWS account being created using organizational email (e.g.
user@umsystem.edu), you will receive an invitation email from AWS for
setting up password, Multifactor Authentication (MFA) as well as initial
access to the AWS Single-Sign-On (SSO) portal. Please contact
[<u>umbmiaws-prod@umsystem.edu</u>](mailto:umbmiaws-prod@umsystem.edu)
if you have any questions or technical issues.

## Recurrent Data Upload

First please identify and confirm the local path to the data to be
uploaded. For NAACCR registry data, we have been informed that the
source file is saved in the “**Source File Path**“ referred in the
parameter table above. Then follow these steps to upload the required
data file to the designated secured S3 bucket:

1.  Go to <https://umbmi.awsapps.com/start#/> (Single-Sign-On page), and
    log in to the AWS Management Console by selecting the “Management
    Console” next to your pre-defined role
    (“NAACCR-Cancer-Registry-Data-Load”). Note that you will be required
    to put in MFA codes every time log into the AWS account.

<img src="attachments/359399441/359399493.png" class="image-center" loading="lazy" data-image-src="attachments/359399441/359399493.png" data-height="109" data-width="640" data-unresolved-comment-count="0" data-linked-resource-id="359399493" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210616-192815.png" data-base-url="https://nextgenbmi.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="359399441" data-linked-resource-container-version="2" data-media-id="c70910d8-4c0d-41b8-adea-1f8783f98ee6" data-media-type="file" />

2\. Within your AWS management console, double check on the right upper
corner of the page that your Role is correct and make sure that you are
in the **us-east-2 ohio** region:

<img src="attachments/359399441/359399490.png?width=544" class="image-center" loading="lazy" data-image-src="attachments/359399441/359399490.png" data-height="347" data-width="693" data-unresolved-comment-count="0" data-linked-resource-id="359399490" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210616-193409.png" data-base-url="https://nextgenbmi.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="359399441" data-linked-resource-container-version="2" data-media-id="9b63b0fa-4cc4-458c-af29-95249b70bc4f" data-media-type="file" width="544" />

3\. Open another web browser tab and enter the following URL which will
directly prompt you to the S3 console for data upload

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` java
https://s3.console.aws.amazon.com/s3/buckets/nextgenbmi-upload-naaccr/
```

</div>

</div>

<img src="attachments/359399441/359399457.png?width=544" class="image-center" loading="lazy" data-image-src="attachments/359399441/359399457.png" data-height="153" data-width="407" data-unresolved-comment-count="0" data-linked-resource-id="359399457" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210616-212011.png" data-base-url="https://nextgenbmi.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="359399441" data-linked-resource-container-version="2" data-media-id="7d97f90b-a715-4b35-b3b6-a88a719d02f5" data-media-type="file" width="544" />

4\. Use the “Upload” and “Add Files” buttons to upload requested files

<img src="attachments/359399441/359399469.png?width=544" class="image-center" loading="lazy" data-image-src="attachments/359399441/359399469.png" data-height="718" data-width="612" data-unresolved-comment-count="0" data-linked-resource-id="359399469" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20210616-200222.png" data-base-url="https://nextgenbmi.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="359399441" data-linked-resource-container-version="2" data-media-id="1da429e6-b7c5-41ac-ad4e-9e65a97e15a0" data-media-type="file" width="544" />

5\. A banner will appear if the upload is successful, and the file
status will be shown as “Succeeded”

<img src="attachments/359399441/359399460.png?width=544" class="image-center" loading="lazy" data-image-src="attachments/359399441/359399460.png" data-height="216" data-width="432" data-unresolved-comment-count="0" data-linked-resource-id="359399460" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Picture1.png" data-base-url="https://nextgenbmi.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="359399441" data-linked-resource-container-version="2" data-media-id="b948e525-6d97-46c9-b531-5f6b4baa18cf" data-media-type="file" width="544" />

6\. Please note that a new file of existing name may overwrite the old
one of the same name. Although S3 bucket kept at most 3 versions, we
would still recommend the following naming convention to separate
different upload:

> **naaccr-\<data extraction date, yyyymmdd>-\<version number, e.g.,
> v1>**

For example, “naaccr-20210823-v1” means “it is the first upload of
naaccr data extracted on 08/23/2021”. If you this is the third uplod of
naaccr data extract on 09/01/2021, the file name will be
“naaccr-20210901-v3”.

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-212011.png](attachments/359399441/359399457.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Picture1.png](attachments/359399441/359399460.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-200422.png](attachments/359399441/359399463.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-200316.png](attachments/359399441/359399466.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-200222.png](attachments/359399441/359399469.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-200127.png](attachments/359399441/359399472.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-194134.png](attachments/359399441/359399475.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-194120.png](attachments/359399441/359399478.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-194105.png](attachments/359399441/359399481.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-193804.png](attachments/359399441/359399484.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-193752.png](attachments/359399441/359399487.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-193409.png](attachments/359399441/359399490.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-192815.png](attachments/359399441/359399493.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-192547.png](attachments/359399441/359399496.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210616-192503.png](attachments/359399441/359399499.png)
(image/png)  

</div>
