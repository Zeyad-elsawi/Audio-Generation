# -- coding: utf-8 --

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft, ifft

N = 3
fs = 44100
t = np.linspace(0, 3, 3 * fs)
ti = [i * 1.5 for i in np.arange(0, N)]
Ti = [1.5] * N

Fi = {'C': 130.81, 'D': 146.83, 'E': 164.81, 'F': 174.61, 'G': 196.00, 'A': 220.00, 'B': 246.94}
fi = {'C': 261.63, 'D': 293.66, 'E': 329.63, 'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.88}
notes = ['C', 'D', 'E']

# === Original Signal  ===
xt = np.zeros_like(t)
for j in range(N):
    note = notes[j]
    xt += ((np.sin(2 * np.pi * Fi[note] * t) + np.sin(2 * np.pi * fi[note] * t)) *
           ((t >= ti[j]).astype(float) - (t >= (ti[j] + Ti[j])).astype(float)))

# === FFT of original signal ===
N_fft = len(t)
f = np.linspace(0, fs / 2, int(N_fft / 2))
x_f = fft(xt)
x_f_mag = 2 / N_fft * np.abs(x_f[0:int(N_fft / 2)])

# === Add Noise ===
fn1, fn2 = np.random.randint(100, 500, 2)
nt = np.sin(2 * np.pi * fn1 * t) + np.sin(2 * np.pi * fn2 * t)
xnt = xt + nt

# === FFT of noisy signal ===
xnf = fft(xnt)
xnf_mag = 2 / N_fft * np.abs(xnf[0:int(N_fft / 2)])


plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t, xt)
plt.title("1. Original Signal (Time Domain)")
plt.xlabel("Time [s]")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(f, x_f_mag)
plt.title("2. Original Signal (Frequency Domain)")
plt.xlabel("Frequency [Hz]")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, xnt)
plt.title("3. Noisy Signal (Time Domain)")
plt.xlabel("Time [s]")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(f, xnf_mag)
plt.title("4. Noisy Signal (Frequency Domain)")
plt.xlabel("Frequency [Hz]")
plt.grid()
plt.tight_layout()
plt.show()

# === Filter Noise in Frequency Domain ===
xf_filtered = xnf.copy()
for freq in [fn1, fn2]:
    idx = np.argmin(np.abs(f - freq))
    xf_filtered[idx] = 0
    xf_filtered[-idx] = 0  # cancel symmetric freq

x_filtered = np.real(ifft(xf_filtered))

# === Plot Filtered Signal (Time Domain) ===
plt.figure()
plt.plot(t, x_filtered)
plt.title("5. Filtered Signal (Time Domain)")
plt.xlabel("Time [s]")
plt.grid()
plt.show()

# === Plot Filtered Signal (Frequency Domain) ===
xfilt_mag = 2 / N_fft * np.abs(xf_filtered[:int(N_fft / 2)])
plt.figure()
plt.plot(f, xfilt_mag)
plt.title("6. Filtered Signal (Frequency Domain)")
plt.xlabel("Frequency [Hz]")
plt.grid()
plt.show()

# === Play Noisy Signal ===
sd.play(xnt, fs)
sd.wait()
