
### 🎶 Audio Signal Processing – COMM401 Project

This project demonstrates fundamental concepts in signal and system theory through audio signal generation and processing using Python. It is divided into four main stages:

1. **🎹 Signal Generation (The Pianist):**
   Pairs of piano notes from the 3rd and 4th octaves are combined to create a musical signal simulating a short song.

2. **🎼 Song Composition:**
   The combined notes are layered over time using sine wave representations, forming a full audio track.

3. **🔊 Noise Injection:**
   Random sinusoidal noise is added to the signal to simulate real-world signal interference.

4. **🧹 Noise Cancellation:**
   Using FFT, the noisy signal is analyzed in the frequency domain to identify and filter out noise components, restoring a cleaner version of the original signal.

Plots for the time and frequency domains are generated at each stage, and the result can be played back using the `sounddevice` library.

---

