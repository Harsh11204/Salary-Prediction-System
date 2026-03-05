# 💼 Employee Salary Prediction System

A Streamlit-based Web App that predicts the salary of employees based on factors such as age, years of experience, performance score, city, and department.
The system uses a Machine Learning Linear Regression model to estimate salary and provides an interactive interface for users to input employee details and obtain predictions instantly.

This project demonstrates a complete end-to-end machine learning workflow, including data preprocessing, model training, evaluation, and deployment using Streamlit.

## 📂 Dataset Format

The dataset used to train this model has the following structure:

| Column Name | Type | Description |
|-------------|------|-------------|
| `age` | Integer | Age of the employee |
| `years_experience` | Integer | Total years of professional experience |
| `performance_score` | Float | Performance rating of the employee |
| `city` | String | City where the employee works |
| `department` | String | Department of the employee |
| `salary` | Float | Actual salary of the employee (target variable) |

## 🚀Features & Usage
### 1. Employee Input Panel

Users can manually enter employee details:

* Age

* Years of Experience

* Performance Score

* City

* Department

After entering the details, the system predicts the expected salary using the trained machine learning model.

### 2. Salary Prediction

The system processes the input data using the same preprocessing steps used during training:

* Feature scaling

* One-hot encoding of categorical variables

* Column alignment with training data

Then, the model predicts the estimated salary.

### 3. Model Evaluation

The model performance is evaluated using multiple metrics:

* 📈 R² Score – Measures how well the model explains salary variation

* 📉 RMSE (Root Mean Squared Error) – Measures prediction error magnitude

* 📊 MAE (Mean Absolute Error) – Measures average prediction error

### 4. Data Visualization

The project also includes some visualizations during model development:

* Experience vs Salary relationship

* Actual vs Predicted salary comparison plots

These visualizations help understand how different features influence salary predictions.

## ⚙️ Technologies Used

* **Python 3.13.0**
* **Streamlit** (for mlodel deployment)
* **Scikit-learn**
* **Pandas, NumPy**
* **Matplotlib, Seaborn**
* **Joblib** (for model persistence)

Joblib (for saving and loading trained models)

## 📧 Contact

**Developed by:** Harsh Verma ||
**Email:** [harshverma11204@gmail.com](mailto:harshverma11204@gmail.com) ||
**LinkedIn:** [https://www.linkedin.com/in/harsh-verma-1b3857287](https://www.linkedin.com/in/harsh-verma-1b3857287)
