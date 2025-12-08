import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

def bandpass_filter(sig, fs, low=5, high=40, order=2):
    """
    Applies a Butterworth bandpass filter to an ECG signal.
    Parameters:
        sig: ECG signal (numpy array)
        fs: sampling frequency
        low: low cutoff frequency
        high: high cutoff frequency
    """
    ny = fs / 2
    b, a = butter(order, [low/ny, high/ny], btype='band')
    return filtfilt(b, a, sig)

def detect_r_peaks(sig, fs):
    """
    Detects R-peaks using prominence and physiological spacing.
    Returns:
        peaks: array of sample indices for peak locations
    """
    # Minimum distance between R peaks (~250 ms)
    min_distance = int(0.25 * fs)

    peaks, props = find_peaks(
        sig,
        distance=min_distance,
        prominence=0.3  # ensures peaks stand out
    )
    return peaks
