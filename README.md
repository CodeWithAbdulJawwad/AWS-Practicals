# AWS Practical Tasks Repository

This repository contains practical exercises and examples related to AWS services, including IAM, EC2, S3, Athena, Lambda, and DMS. Each section includes code snippets and step-by-step instructions for performing common tasks in AWS.

## Table of Contents

- [IAM (Identity and Access Management)](#iam-identity-and-access-management)
- [EC2 (Elastic Compute Cloud)](#ec2-elastic-compute-cloud)
- [S3 (Simple Storage Service)](#s3-simple-storage-service)
- [Athena](#athena)
- [Lambda](#lambda)
- [DMS (Database Migration Service)](#dms-database-migration-service)

---

## IAM (Identity and Access Management)

### 1. Create Two IAM User Accounts
Steps for creating two IAM user accounts using the root account.

### 2. Create an Admin Group and Assign Roles
- Create an IAM user and assign them to an Admin group.
- Allocate admin roles and policies to the group.

---

## EC2 (Elastic Compute Cloud)

### 1. Launch an EC2 Instance
- Launch an EC2 instance of type `t2.micro` using the web UI in the AWS Console.

### 2. Execute 5 Linux Commands on AWS EC2
- After launching the EC2 instance, execute the following 5 Linux commands on AWS Linux EC2 instance:
  - Example commands: `ls`, `cd`, `pwd`, `mkdir`, `touch`.

### 3. Connect to EC2 Using AWS CLI
- Use AWS CLI to connect to the EC2 instance.

### 4. Use PuTTY to Connect to EC2
- Instructions to connect to the EC2 instance using PuTTY.
- Create a sample S3 bucket after connecting.

### 5. Upload a Sample Text File to S3
- Insert a sample text file into the S3 bucket using the AWS CLI.

---

## S3 (Simple Storage Service)

### 1. Create an S3 Bucket Using `boto3`
- Using `boto3`, create an S3 bucket programmatically.

### 2. Host the S3 Bucket on the Web
- Steps to configure the S3 bucket for static website hosting.

### 3. Enable Versioning on S3 Bucket
- Instructions to enable versioning on the S3 bucket and view object versions.

### 4. Use KMS with S3 Bucket
- Steps to use AWS KMS with an S3 bucket for encryption.

### 5. PySpark: Transform Data in S3
- Write a PySpark code that:
  - Connects to an S3 bucket.
  - Performs transformations and adds a new column.
  - Writes the transformed data back to S3.

### 6. PySpark Session Code to Read and Write from S3
- PySpark session code to read data, perform transformations, and write it back to an S3 bucket.

### 7. Sample Spark Code to Connect to AWS S3
- Sample Spark code to connect to S3 and perform operations.

---

## Athena

### 1. Query Data in S3 Using Athena
- Create sample data in S3 and use Athena to query it.

---

## Lambda

### 1. Lambda to Read Data from S3 and Load to Redshift
- Write a Lambda function to:
  - Read data from an S3 bucket.
  - Load the data into a Redshift table.

---

## DMS (Database Migration Service)

### 1. Transfer MySQL Table to S3 Using DMS
- Steps to use DMS to transfer a MySQL table to an S3 bucket.

---

## Setup Instructions

To run the above tasks, ensure that you have:
- AWS CLI configured with the necessary permissions.
- Access to AWS Console for creating and managing resources.
- Python 3.x installed with `boto3` and `PySpark` libraries for S3 and Lambda tasks.

## Author
Abdul Jawwad

This `README.md` provides an overview of the tasks, including setup instructions and the required tools. You can adjust or expand on it based on your specific repository details.
