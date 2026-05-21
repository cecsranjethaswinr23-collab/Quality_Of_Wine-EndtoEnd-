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


## Architecture & Pipeline Flow

1. **Local Development:** Code updated and pushed to GitHub.
2. **CI/CD Automation:** GitHub Actions triggers a workflow using a self-hosted runner.
3. **Containerization:** The application is packaged into a lightweight Docker image.
4. **Cloud Deployment:** The updated container is deployed live to an AWS EC2 instance.



## Project Structure

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

---


## Project Links & Author

**Repository:** [GitHub](https://github.com/cecsranjethaswinr23-collab/Quality_Of_Wine-EndtoEnd-)
**Author:** Ranjeth Aswin Ravindran
**Connect with me:** 👋 [LinkedIn](www.linkedin.com/in/ranjeth-aswin-ravindran-018277253)
                         [GitHub](https://github.com/cecsranjethaswinr23-collab)