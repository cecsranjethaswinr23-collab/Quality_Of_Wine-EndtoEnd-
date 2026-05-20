# Quality of Wine Prediction Pipeline (End-to-End)

An enterprise-grade, production-ready machine learning pipeline that predicts wine quality based on content of chemical properties. This project demonstrates a fully modular architecture, robust MLOps tracking with MLflow, and automated deployment pipelines targeting AWS cloud infrastructure.

## Tech Stack & Tools

**Language:** Python, HTML, CSS
**ML Frameworks:** Scikit-Learn, NumPy, Pandas
**MLOps & Tracking:** MLflow, DagsHub
**Cloud & Deployment:** AWS (EC2 / ECR / App Runner), Docker, Flask
**Orchestration:** Custom Modular Pipeline Architecture


## Key Features

**Modular Architecture:** Stages: Data Ingestion, Data Validation,  Data Transformation, Model Training, and Model Evaluation.
**Experiment Tracking:** Fully integrated with **MLflow** and hosted on **DagsHub** to track parameters, metrics, and version models.
**Production ML Model:** Utilizes an **ElasticNet Regression** model, optimized via hyperparameter tuning to balance L1 (Lasso) and L2 (Ridge) regularization.
**CI/CD Deployment:** Automatically builds and deploys the prediction service to **AWS** services for real-time inference.


## Project Structure

```text
├── .github/workflows/     # CI/CD pipelines for AWS deployment
├── config/
│   └── config.yaml        # Centralized configuration file
├── src/
│   └── wineQuality/
│       ├── components/    # Data Ingestion, Validation, Transformation, Model Trainer
│       ├── config/        # Configuration Manager
│       ├── constants/     # Global constant definitions
│       ├── entity/        # Custom artifacts & configuration data types
│       └── pipeline/      # Orchestrated training and prediction pipelines
├── app.py                 # Flask application for web interface/REST API
├── main.py                # Main execution script to trigger pipelines
├── requirements.txt       # Project dependencies
└── README.md


## Quality_Of_Wine-EndtoEnd- ##

# Workflows of thos project
1.First creating template.py
-to create a template for the whole project

2.Making requirements.txt
-to install/import all neccessary packages needed for the ML project

3.Setting up setup.py
-settingup with the author name, project name, versions, etc....

4.Setting logger
-logging.info() for knowing the custom exception type of message to track the workflow

5.utils/common.py
-the backbone of the project where the conversion and reading data occurs through pipeline

# main workflows

## --data ingestion,validation,tansformation and model trainer (follows same steps)-- ##
## --Model trainer is little different but similiar ##
1.update config.yaml(# update it first )
2.update schema.yaml()
3.update params.yaml()
4.update entity()
5.update configuration manager in src config.()
6.update components()
7.update pipelines()
8.update main.py()
9.update dvc.yaml()



## model evaluation ##

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='cecsranjethaswinr23-collab', repo_name='Quality_Of_Wine-EndtoEnd-', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Launch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model