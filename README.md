🎯 **Customer Churn Prediction Pipeline with MLflow**

📌 **Project Overview**
This is a personal learning project where I focused on moving my Machine Learning code from Jupyter Notebooks into a structured Python pipeline. The goal is to predict customer churn while learning how to write cleaner code and track experiments properly.

I used Object-Oriented Programming (OOP) concepts to keep the pipeline steps, like data scaling, encoding, and missing value handling, separated and easier to manage.

🚀 **Things I Implemented and Learned**
* **Modular Code Structure:** Used the Strategy Design Pattern in Python to separate different data preprocessing steps.
* **LLM-Powered Data Imputation:** Integrated the Groq API (Llama-3.3) to intelligently predict missing genders based on the customer's first name instead of simple mode imputation.
* **Experiment Tracking:** Used MLflow to automatically log model hyperparameters, evaluation metrics (Accuracy, F1-Score), and artifacts like confusion matrices and learning curves.
* **Configuration Management:** All file paths, split ratios, and model parameters are managed via a central config.yaml file.
* **Automation:** Wrote a Makefile to make it easy to run the data processing and training pipelines with single commands.

🔮 **Future Roadmap (My Learning Path)**
I plan to evolve this project into a more complex architecture by learning and integrating these technologies in sequence:

* 🟡 **Phase 1: PySpark** - Migrating current Pandas preprocessing to handle distributed big data processing.
* 🔵 **Phase 2: Apache Airflow** - Automating and orchestrating the end-to-end data and training workflows.
* 🟢 **Phase 3: Apache Kafka** - Introducing real-time streaming to perform live inference on incoming data.

🛠️ **Tech Stack & Tools Used**
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn, XGBoost, RandomForest
* **Experiment Tracking:** MLflow
* **External APIs:** Groq API (Llama-3.3-70B-Versatile)

📁 **Project Structure**
* artifacts/ - Generated models, plots, and MLflow run artifacts
* data/ - Raw (ChurnModelling.csv) and processed datasets
* pipelines/ - Main execution scripts (data, training, inference)
* src/ - Core logic and OOP classes (encoding, scaling, etc.)
* utils/ - Configurations and MLflow utility functions
* config.yaml - Central configuration file
* Makefile - Automation commands

⚙️ **How to Run the Project**

**1. Setup Environment**
Clone the repository and create a .env file in the root directory to add your Groq API key:
GROQ_API_KEY=your_api_key_here

**2. Install Dependencies**
Run `make install` and activate the virtual environment (`source .venv/Scripts/activate`).

**3. Run the Pipelines**
* Data Processing: `make data-pipeline`
* Model Training: `make train-pipeline`
* Run All: `make run-all`

**4. View MLflow Dashboard**
Run `make mlflow-ui` and access the dashboard at http://localhost:5000

---
*Note: This project is part of my continuous learning journey in Data Science and Machine Learning. Feedback and suggestions on the code structure or my approach are highly appreciated!*