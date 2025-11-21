# Flight Price Prediction using Machine Learning

This project predicts **flight ticket prices** for Indian domestic airlines using **machine learning**.  
It includes data cleaning, EDA, feature engineering, model building, hyperparameter tuning, evaluation, feature importance analysis, and deployment using **Streamlit**.

---

## Problem Statement

Flight ticket prices vary based on several factors such as airline, route, class, number of stops, duration, booking time, and time of travel.  
The goal is to create a machine learning model that **predicts the price of a flight** using these attributes.

---

## Approach

### **1. Data Understanding & Cleaning**

- Loaded dataset and inspected missing values, duplicates, and outliers.
- Cleaned inconsistent values and converted categorical fields.
- Processed date/time fields into meaningful categories.

---

### **2. Exploratory Data Analysis (EDA)**

Analyzed how each feature affects price using:

- Bar plots
- Boxplots
- Violin Plots
- Correlation heatmaps
- LOWESS smoothed trend lines

**Key Findings:**

- Airlines show huge price differences (Vistara & Air India highest).
- Metro cities have higher average fares.
- Morning/Evening flights are expensive.
- Non-stop flights cost the most.
- Business class is the biggest price driver.
- Duration has a moderate positive influence.
- Days left has a weak negative influence.

---

### **3. Feature Engineering**

- One-Hot Encoding: airline, cities, class, time slots, stops.
- Scaled numerical features using StandardScaler.
- Created a unified **ColumnTransformer** inside a pipeline.

---

### **4. Model Building**

Models evaluated:
 
- Decision Tree Regressor  
- AdaBoost Regressor
- GradientBoosting Regressor
- **XGBoost Regressor (Final Model)**  

Final pipeline:

```
ColumnTransformer → XGBoostRegressor
```

---

### **5. Hyperparameter Tuning**

Using **GridSearchCV**, tuned:

- learning_rate  
- max_depth  
- n_estimators  

Final R² Score: **~98%**

---

### **6. Feature Importance**

Top impacting features:

- **Class (Business/Economy)**
- Airline
- Duration
- Source & Destination city
- Arrival & Departure time
- Number of stops
- Days left

---

### **7. Deployment with Streamlit**

A complete Streamlit UI was built.  
Users can input:

- Airline  
- Source & Destination  
- Class  
- Duration  
- Stops  
- Departure Time  
- Arrival Time  
- Days Left  

It loads the saved model and predicts the flight price.

Run:

```
streamlit run app.py
```

---

## 🗂 Project Structure

```
Flight-price-prediction/
│── ML Project 1.ipynb
│── flight_price_model.pkl
│── app.py
│── README.md
│── requirements.txt
```

---

## 📦 Technologies Used

- Python
- Pandas, NumPy
- Scikit-Learn
- XGBoost
- Matplotlib, Seaborn
- Streamlit
- Pickle

---

## 🔍 Why XGBoost Works Best?

- Handles mixed numeric + categorical data.
- Captures non-linear pricing patterns.
- Very strong with outliers.
- Regularization prevents overfitting.
- Learns complex interactions like:  
  - Airline × Class  
  - Stops × Duration  
  - Time × Days Left  
- Highest accuracy (**R² ≈ 0.98**).

---

## 📈 Results

| Metric       | Value    |
|--------------|----------|
| **R² Score** | ~0.98    |
| **MAE**      | Low      |
| **MSE**      | Very Low |

---

## 📝 Conclusion

- Flight prices depend heavily on **Class**, **Airline**, **Stops**, and **Route**.
- XGBoost with proper preprocessing provides excellent results.
- A Streamlit app was created for real-time prediction.

---

## 🧑‍💻 Author

**Akurala Harshitha**

---

If you need:
✔ Project Presentation (PPT)  
✔ PDF Report  
✔ Better Streamlit UI  
✔ GitHub formatting  

Just tell me!
