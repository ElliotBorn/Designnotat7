import pandas as pd
import matplotlib.pyplot as plt

# Les CSV-fil
df = pd.read_csv("bodil.csv")

# Plot amplituderespons for Channel 1
plt.figure(figsize=(8, 5))
plt.plot(df["Frequency (Hz)"], df["Channel 1 Magnitude (dB)"], label="Channel 1")


plt.axvline(x=2100, color="red", linestyle="--", linewidth=1.2, label="2100 Hz")
plt.axvline(x=2800, color="green", linestyle="--", linewidth=1.2, label="2800 Hz")

# Aksegrenser og oppsett
plt.title("Amplituderespons for 6. ordens LP-filter")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Demping (dB)")
plt.xlim(500, 4000)     # 0 til 10 kHz
plt.ylim(-20, 1)        # -20 dB til 0 dB
plt.grid(True, which="both", linewidth=0.7)
plt.legend()
plt.tight_layout()
plt.show()