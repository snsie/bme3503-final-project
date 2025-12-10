# ECG Visualization & Analysis App

A Streamlit-based tool for filtering, visualizing, and analyzing ECG signals.

## Biomedical Context

This application is designed for biomedical engineering students, clinicians, and researchers who need a simple tool to view ECG signals, apply noise-reducing filters, detect R-peaks, and estimate heart rate. The problem it addresses is that raw ECGs contain noise (baseline drift, muscle artifact, powerline interference) that has to be removed before meaningful interpretation.

## Quick Start Instructions

### Opening the Repository in GitHub Codespaces

1. Navigate to this repository on GitHub.
2. Click the green "Code" button on the top right of the page.
3. Select the Codespaces tab.
4. Click "Create codespace on main".
5. Once loaded, you can edit files and run the app.

### Running the Application

1. Launch the Streamlit app by typing "streamlit run app.py" in the Codespaces terminal
2. If prompted, click "Open in Browser."

## Usage Guide

- **Step 1:** Load or Use the Sample ECG
  - When the app launches, you can either upload your own CSV containing 'time' and 'ecg' columns, or use the included sample_ecg.csv dataset (loaded automatically if no file is uploaded)
- **Step 2:** Set Processing Options
  - In the left sidebar, you can:
      - Adjust the sampling frequency (Hz)
      - Enable/disable the bandpass filter (5-40 Hz)
      - Toggle R-peak detection
  - These settings allow for cleaning noisy ECGs and inspect important features like QRS complexes.
- **Step 3:** View ECG & Analysis Results
  - The main panel displays:
    - A line chart of the ECG waveform
    - Optional R-peak markers (if enabled)
    - Computed heart rate (bpm)
    - A download button to export the processed ECG data
  - This enables interactive exploration of signal quality, filtering effects, and physiological metrics.

## Data Description (optional)

The sample ECG included with this app is a synthetic ECG signal generated for demonstration purposes. It simulates clean QRS complexes with realistic timing and noise components.

### Data Source

If using real ECG data, recommended public sources include:

  - PhysioNet (MIT-BIH Arrhythmia Database)

  - University of Queensland ECG Database

The provided sample ECG (sample_ecg.csv) was algorithmically generated and is safe to distribute.


## Project Structure

app.py
  - Controls the user interface, data loading, filtering, and visualization.

src/processing.py
  - Contains the signal processing functions such as bandpass filtering and R-peak detection.

src/plotting.py
  - Provides optional matplotlib-based plotting functions for peak overlay.

data/sample_ecg.csv
  - A synthetic ECG dataset used when no file is uploaded.

