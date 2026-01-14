import streamlit as st
import pandas as pd
import os
from backend.processor import calculate_health, maintenance_advice

st.set_page_config(page_title="Motor Health Dashboard")

st.title("Smart Motor Health Monitoring Dashboard")

DATA_PATH = os.path.join("data", "motor_data.csv")

if not os.path.exists(DATA_PATH):
    st.error("Motor data not available.")
    st.stop()

df = pd.read_csv(DATA_PATH)

if df.empty:
    st.warning("Waiting for motor data...")
    st.stop()

latest = df.iloc[-1]

health = calculate_health(
    latest["voltage"],
    latest["current"],
    latest["temperature"]
)

st.metric("Voltage (V)", latest["voltage"])
st.metric("Current (A)", latest["current"])
st.metric("RPM", latest["rpm"])
st.metric("Temperature (°C)", latest["temperature"])

st.progress(health)
st.write("Health Status:", maintenance_advice(health))

st.subheader("Motor Parameter Trends")
st.line_chart(df[["current", "temperature", "rpm"]])
