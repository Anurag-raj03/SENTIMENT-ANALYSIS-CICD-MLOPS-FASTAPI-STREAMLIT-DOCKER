

---

### **📌 SENTIMENT ANALYSIS CICD PIPELINE 🚀**  
#### **🔗 End-to-End CI/CD Workflow with Docker, MLflow, and Model Retraining 🔥**  

---

## **🌟 Project Overview**  
This project is a fully automated **Sentiment Analysis System** powered by a **CI/CD pipeline**, ensuring **continuous integration and deployment** of the model.  

🔹 **Key Features:**  
✅ **MLflow** for model monitoring and tracking.  
✅ **Dockerized microservices** for API, monitoring, and frontend deployment.  
✅ **ETL Pipeline** that triggers **data drift detection** when new data arrives.  
✅ **Automated Model Retraining** when:  
   - More than **50 new records** are added.  
   - **Data drift is detected** using the `Script` library.  
✅ If model accuracy falls **below 75%**, retraining is automatically triggered.  
✅ **GitHub Actions** for continuous integration & deployment.  
✅ **Kaggle Profile for other ML & Data Science Projects** 👉 [My Kaggle](https://www.kaggle.com/anuragraj03)  

---

## **📂 Project Folder Structure**  
```bash
Sentiment_CICD/
│── ANALYSIS/
│   ├── api/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── database_api.py
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── fastapi.py
│   │   ├── requirement.txt
│── DATA/
│   ├── data/
│   │   ├── drift_input.csv
│   │   ├── mlflow_modified.csv
│── database/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── db_config.py
│   ├── init_db.py
│   ├── save_db.py
│   ├── sentiment.db
│   ├── update_copy/
│── logs/
│── model_making/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── model_train.py
│   ├── split_n_ux.py
│   ├── word_vec.py
│── monitoring/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── drift_detection.py
│   ├── entrypoint.sh
│   ├── mlflow_tracking.py
│   ├── model_registry.py
│   ├── monitoring.txt
│   ├── requirements.txt
│   ├── retrain_model.py
│── preprocessing/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── dropping_nay.py
│   ├── labeling.py
│   ├── making_lower_case.py
│   ├── remove_empty.py
│   ├── removing_link.py
│   ├── removing_stop.py
│   ├── removing_strip.py
│   ├── stemming.py
│   ├── tf_idf.py
│   ├── train_model/
│   ├── vc_vectorizer.pkl
│── STEPS/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── data_pipelining.py
│   ├── data_validation.py
│   ├── pipeline_main.py
│── streamlit_app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── docker-compose.yml
│   ├── after_space.co
│   ├── docker_compose.yml
│   ├── makeover
│   ├── prediction.csv
```

---

## **🔗 End-to-End Pipeline Workflow 🛠️**  

### **1️⃣ ETL Pipeline 🛠️**  
📥 **New Data Arrives** → **Stored in Database** 🗄  
🔄 **If More Than 50 Records** → **Check for Data Drift** 🚨  

### **2️⃣ Data Drift Detection 📊**  
🔍 Uses **Script Library** to compare new data with historical patterns.  
📉 **If Drift Detected:** Triggers model retraining process.  

### **3️⃣ Model Retraining 🤖**  
✅ **Check Model Accuracy** after retraining:  
   - **If Accuracy ≥ 75%:** ✅ Deploy new model  
   - **If Accuracy < 75%:** ❌ Retrain again until acceptable  

### **4️⃣ Model Deployment 🚀**  
📡 **FastAPI Backend** serves the model predictions.  
🎨 **Streamlit Frontend** provides a user-friendly interface.  

### **5️⃣ MLflow Monitoring 📊**  
🔍 Tracks **model versions, performance, and parameters**.  
📈 Logs all **training metrics, accuracy, and loss trends**.  

### **6️⃣ CI/CD with GitHub Actions ⚙️**  
🔹 Push to GitHub → **Triggers Automated Workflow**  
🔹 Builds & pushes Docker images to **Docker Hub**  
🔹 Pulls & deploys the latest version 🚀  

---

## **📦 Deployment (Run on Any Machine) 🖥️**  
💡 **Since the images are public on Docker Hub, anyone can run this project easily! First clone my git repo**  

### **1️⃣ Pull Docker Images 📥**  
```bash
docker pull anuragraj03/sentiment_repo_cicd/sentiment_api:latest
docker pull anuragraj03/sentiment_repo_cicd/streamlit_app:latest
docker pull anuragraj03/sentiment_repo_cicd/monitoring_service:latest
```

### **2️⃣ Start All Services 🚀**  
```bash
docker compose up -d
```

🟢 **Now the project is running!**  
- **Backend API:** `http://localhost:8000`  
- **Frontend (Streamlit):** `http://localhost:8501`  
- **MLflow UI:** `http://localhost:5000`  

---

## **📜 Setup Script (Bash)**
If you want to automate everything, create a `setup.sh` file and run this script:

```bash
#!/bin/bash

echo "🚀 Pulling Docker Images..."
docker pull anuragraj03/sentiment_repo_cicd/sentiment_api:latest
docker pull anuragraj03/sentiment_repo_cicd/streamlit_app:latest
docker pull anuragraj03/sentiment_repo_cicd/monitoring_service:latest

echo "✅ Images Pulled Successfully!"

echo "🔧 Starting Services..."
docker compose up -d

echo "🎉 Deployment Complete!"
echo "📡 Backend API: http://localhost:8000"
echo "🎨 Streamlit UI: http://localhost:8501"
echo "📊 MLflow Dashboard: http://localhost:5000"
```

**Run this in your terminal:**
```bash
chmod +x setup.sh
./setup.sh
```

---

## **👨‍💻 Contributing**  
🚀 Feel free to fork the repo, open issues, or submit PRs!  

---

## **🔗 More ML & Data Science Projects**  
📊 Check out my Kaggle Profile for more awesome **ML & Data Science** projects:  
👉 **[My Kaggle](https://www.kaggle.com/anuragraj03)**  

---
