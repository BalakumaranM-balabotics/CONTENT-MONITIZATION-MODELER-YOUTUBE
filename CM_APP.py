import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model, scalar, and columns
LR_model = joblib.load("LR_model.pkl")
scalar = joblib.load("scalar.pkl")
X_train_columns = joblib.load("X_train_columns.pkl")

st.title("🎬 YouTube Ad Revenue Predictor")
st.write("Enter video and channel details below to estimate ad revenue.")

# Arrange inputs in 3 columns 

col1, col2, col3 = st.columns(3)

with col1:
    views = st.number_input("👁️ Views", min_value=0)
    likes = st.number_input("❤️ Likes", min_value=0)
    comments = st.number_input("💬 Comments", min_value=0)

with col2:
    watch_time_minutes = st.number_input(
        "⏱️ Watch Time (minutes)", min_value=0.0
    )
    video_length_minutes = st.number_input(
        "🎞️ Video Length (minutes)", min_value=0.0
    )
    subscribers = st.number_input("👥 Subscribers", min_value=0)

with col3:
    category = st.selectbox(
        "📊 Category",
        ["Entertainment", "Gaming", "Lifestyle", "Music", "Tech"]
    )

    device = st.selectbox(
        "📱 Device",
        ["Mobile", "TV", "Tablet"]
    )

    country = st.selectbox(
        "🌍 Country",
        ["CA", "DE", "IN", "UK", "US"]
    )
# Calculate engagement rate automatically
if views > 0:
    engagement_rate = (likes + comments) / views
else:
    engagement_rate = 0
# Predict Button
if st.button("Predict Ad Revenue"):
    # Build input dataframe
    input_dict = {
        'views': views,
        'likes': likes,
        'comments': comments,
        'watch_time_minutes': watch_time_minutes,
        'video_length_minutes': video_length_minutes,
        'subscribers': subscribers,
        'engagement_rate': engagement_rate,
        f'category_{category}': 1,
        f'device_{device}': 1,
        f'country_{country}': 1
    }

    # Fill missing dummy columns with 0
    input_df = pd.DataFrame([input_dict])
    for col in X_train_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[X_train_columns]

    # Scale numeric features
    num_cols = ['views', 'comments', 'watch_time_minutes', 'video_length_minutes', 'subscribers', 'engagement_rate']
    input_df[num_cols] = scalar.transform(input_df[num_cols])


    # Predict
    
    prediction = LR_model.predict(input_df)[0]
    st.success(f"💰 Predicted Ad Revenue: **${prediction:,.2f} USD**")

import matplotlib.pyplot as plt

st.subheader("📊 Features Influencing Ad Revenue")

coefficients = LR_model.coef_

feature_importance = pd.DataFrame({
    "Feature": X_train_columns,
    "Coefficient": coefficients
})

feature_importance["Absolute_Coefficient"] = (
    feature_importance["Coefficient"].abs()
)

feature_importance = feature_importance.sort_values(
    "Absolute_Coefficient",
    ascending=True
)

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(
    feature_importance["Feature"],
    feature_importance["Coefficient"]
)

ax.set_xlabel("Coefficient Value")
ax.set_ylabel("Feature")
ax.set_title("Feature Influence on Ad Revenue")

plt.tight_layout()

st.pyplot(fig)