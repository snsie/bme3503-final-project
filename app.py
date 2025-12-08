import streamlit as st
import pandas as pd
from src.processing import bandpass_filter, detect_r_peaks
import numpy as np
from src.plotting import plot_ecg_with_peaks

st.set_page_config(page_title="ECG Visualizer", layout="wide")
st.title("ECG Visualization & Analysis App")

uploaded = st.sidebar.file_uploader("Upload ECG CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("data/sample_ecg.csv")
    st.sidebar.info("Using sample ECG")

time = df["time"].values
ecg = df["ecg"].values

st.sidebar.subheader("Processing")
fs = st.sidebar.number_input("Sampling frequency (Hz)", value=360)
apply_filter = st.sidebar.checkbox("Apply bandpass filter (5–40 Hz)", value=True)
detect_peaks_flag = st.sidebar.checkbox("Detect R-peaks", value=True)

if apply_filter:
    ecg_processed = bandpass_filter(ecg, fs)
else:
    ecg_processed = ecg

st.subheader("ECG Signal (Processed)")
st.line_chart(pd.DataFrame({"time": time, "ecg": ecg_processed}).set_index("time"))

if detect_peaks_flag:
    peaks = detect_r_peaks(ecg_processed, fs)
    hr = len(peaks) * (60 / (time[-1] - time[0]))
    st.write(f"R-peaks detected: {len(peaks)}")
    st.write(f"Estimated Heart Rate: {hr:.1f} bpm")

    fig = plot_ecg_with_peaks(time, ecg_processed, peaks)
    st.pyplot(fig)

# Download processed data
csv_data = pd.DataFrame({"time": time, "ecg_processed": ecg_processed}).to_csv(index=False)
st.download_button("Download Processed ECG", csv_data, "processed_ecg.csv")

