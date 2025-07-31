# 🛠️ WorkWatch: Smart Workstation Analytics Platform

WorkWatch is a machine learning-powered platform designed to monitor, analyze, and predict hardware reliability in workstations using SMART log data. It detects potential hard drive failures early, alerts users, and logs analytics into a PostgreSQL database — all through an interactive Streamlit dashboard.

## 🚀 Features

- 📊 **SMART Data Ingestion**: Upload `.csv` logs to analyze workstation health.
- 🤖 **Failure Prediction**: Trained models detect early signs of hard drive failure.
- 🔍 **Feature Importance Visualization**: Understand key SMART attributes impacting model predictions.
- 📝 **PostgreSQL Logging**: Every prediction is securely logged into a PostgreSQL database for auditing.
- ⚠️ **Alert System**: Automatically displays warnings for risky drives based on model output.
- 🌐 **Streamlit Frontend**: Simple, browser-based UI for non-technical users.

## 🧠 Tech Stack

- **Languages**: Python
- **Libraries**: pandas, scikit-learn, joblib, psycopg2, streamlit
- **Database**: PostgreSQL
- **Modeling**: Logistic Regression, Random Forest
- **Deployment**: Local Streamlit App

## 📁 Folder Structure
