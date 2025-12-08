import matplotlib.pyplot as plt
import numpy as np

def plot_ecg_with_peaks(time, signal, peaks):
    """
    Returns a matplotlib figure plotting ECG and detected R-peaks.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, signal, label="ECG")
    ax.scatter(time[peaks], signal[peaks], color="red", s=20, label="R-peaks")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    return fig
