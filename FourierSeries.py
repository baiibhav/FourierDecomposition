import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_fourier_spectrum(freq, spectrum, title):
    plt.plot(freq, np.abs(spectrum))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)

# Load the WAV file
sample_rate, audio_data = wavfile.read("C:/Users/barwa/Desktop/Math Project/InputData.wav.wav")

# Extract the mono audio channel (if stereo)
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Perform the DFT
spectrum = np.fft.fft(audio_data)
freq = np.fft.fftfreq(len(audio_data), d=1/sample_rate)

# Reconstruct the signal using only the first five Fourier coefficients
reconstructed_spectrum = np.zeros_like(spectrum)
reconstructed_spectrum[:5] = spectrum[:5]
reconstructed_signals = []
for i in range(5):
    reconstructed_spectrum_i = np.zeros_like(spectrum)
    reconstructed_spectrum_i[i] = spectrum[i]
    reconstructed_signal_i = np.fft.ifft(reconstructed_spectrum_i)
    reconstructed_signals.append(reconstructed_signal_i)

# Plot the original waveform
plt.figure(figsize=(8, 6))
plt.subplot(6, 1, 1)
plt.plot(audio_data)
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude")
plt.title("Original Waveform")

# Plot the reconstructed waveforms
for i in range(5):
    plt.subplot(6, 1, i+2)
    plt.plot(reconstructed_signals[i].real)
    plt.xlabel("Time (samples)")
    plt.ylabel("Amplitude")
    plt.title("Reconstructed Waveform ({} Fourier coefficient)".format(i+1))

plt.tight_layout()
plt.show()

# Plot the Fourier spectra of the reconstructed waveforms
plt.figure(figsize=(8, 6))
for i in range(5):
    plt.subplot(5, 1, i+1)
    reconstructed_spectrum_i = np.zeros_like(spectrum)
    reconstructed_spectrum_i[i] = spectrum[i]
    reconstructed_signal_i = np.fft.ifft(reconstructed_spectrum_i)
    reconstructed_spectrum_i = np.fft.fft(reconstructed_signal_i)
    plot_fourier_spectrum(freq, reconstructed_spectrum_i, "Frequency Spectrum ({} Fourier coefficient)".format(i+1))

plt.tight_layout()
plt.show()



