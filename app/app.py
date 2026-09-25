import streamlit as st
import pandas as pd
import joblib


# 1. Load model + dataset

model = joblib.load("artifacts/flight_price_model.joblib")

df = pd.read_csv("data/Clean_Dataset.csv")


# 2. Page configuration

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Flight Price Prediction")
st.write("Enter the flight information to predict the ticket price.")


# 3. User inputs

col1, col2 = st.columns(2)

with col1:

    airline = st.selectbox(
        "Airline",
        sorted(df["airline"].unique())
    )

    flight = st.selectbox(
        "Flight",
        sorted(df["flight"].unique())
    )

    source_city = st.selectbox(
        "Source City",
        sorted(df["source_city"].unique())
    )

    departure_time = st.selectbox(
        "Departure Time",
        sorted(df["departure_time"].unique())
    )

    stops = st.selectbox(
        "Stops",
        sorted(df["stops"].unique())
    )


with col2:

    arrival_time = st.selectbox(
        "Arrival Time",
        sorted(df["arrival_time"].unique())
    )

    destination_city = st.selectbox(
        "Destination City",
        sorted(df["destination_city"].unique())
    )

    flight_class = st.selectbox(
        "Class",
        sorted(df["class"].unique())
    )

    duration = st.number_input(
        "Duration (hours)",
        min_value=0.0,
        max_value=50.0,
        value=2.0,
        step=0.1
    )

    days_left = st.number_input(
        "Days Left",
        min_value=1,
        max_value=50,
        value=10,
        step=1
    )


# 4. Prediction button

if st.button("Predict Price"):

    # Create DataFrame with exactly the features
    # expected by the pipeline

    input_data = pd.DataFrame({
        "airline": [airline],
        "flight": [flight],
        "source_city": [source_city],
        "departure_time": [departure_time],
        "stops": [stops],
        "arrival_time": [arrival_time],
        "destination_city": [destination_city],
        "class": [flight_class],
        "duration": [duration],
        "days_left": [days_left]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(
        f"Predicted Ticket Price: {prediction:,.2f}"
    )