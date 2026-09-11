# Content Monetization Modeler

## Project Overview

-->Content Monetization Modeler is a Machine Learning project that predicts YouTube ad revenue for individual videos based on video performance and contextual features.

-->The project includes data cleaning, exploratory data analysis (EDA), feature engineering, categorical encoding, feature scaling, regression model comparison, and an interactive Streamlit web application for ad revenue prediction and model insights.

---

## Problem Statement

-->Predict the estimated YouTube ad revenue (`ad_revenue_usd`) of a video using historical video performance and contextual information.

---

## Skills & Technologies

### Machine Learning & Modeling
--> Linear Regression
-->Decision Tree Regressor
-->Random Forest Regressor
-->Gradient Boosting Regressor

### Data Handling & Preprocessing
-->Python
-->Pandas
-->NumPy
-->Missing Value Handling
-->Duplicate Removal
-->Categorical Encoding
-->Feature Scaling using StandardScaler

### EDA & Data Visualization
-->Matplotlib
-->Seaborn
-->Correlation Analysis
-->Feature Influence Analysis

### Regression Metrics
-->R² Score
-->RMSE
-->MAE

### Web Application
-->Streamlit

## Dataset

**Dataset Name:** YouTube Monetization Modeler

**Format:** CSV

**Size:** Approximately 122,000 rows

**Type:** Synthetic dataset

**Target Variable:** ad_revenue_usd

### Dataset Columns

| Column | 

--> video_id 
--> date 
--> views 
--> likes 
--> comments 
--> watch_time_minutes 
--> video_length_minutes 
--> subscribers 
--> category 
--> device 
--> country 
--> ad_revenue_usd(target variable) 

## Data Preprocessing

The following preprocessing steps were performed on the dataset:

-->Checked the dataset structure and data types.
-->Identified missing values.
-->Handled missing values using appropriate imputation(filling with mean values).
-->Removed duplicate records.
-->Removed `video_id` and `date` as they were not used as model features.
-->Encoded categorical variables using one-hot encoding(performed dummy encoding).
-->Used `drop_first=True` to avoid redundant dummy variables.
-->Split the data into training and testing sets.
-->Applied `StandardScaler` to the numerical features.

## Feature Engineering

A new feature called `engagement_rate` was created to represent the level of audience engagement relative to video views.
engagement_rate = (likes + comments) / views

## Machine Learning

-->Best Model:Linear Regression
-->Model Performance:
    Linear regression:         R2_LR: 0.9482111364236181
                               RMSE_LR: 14.091871470700555
                               MAE_LR: 3.314155753805968

    DecisionTreeRegressor:     R2_DT: 0.8908765218801804
                               RMSE_DT: 20.455475658218145
                               MAE_DT: 5.476646401468546

    RandomForestRegressor:     R2_RF: 0.9482219389158859
                               RMSE_RF: 14.090401702288172
                               MAE_RF: 3.685269325448619

    GradientBoostingRegressor: R2_GB: 0.9480973445651045
                               RMSE_GB: 14.107344491974237
                               MAE_GB: 3.807946598774913

--> By Comparing the Metrics we come to conclusion that linear Regression is the best model.                                

## Project Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Exploratory Data Analysis
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Model Training
     ↓
Model Comparison
     ↓
Final Model Selection
     ↓
Streamlit Deployment
     ↓
Feature Influence Analysis