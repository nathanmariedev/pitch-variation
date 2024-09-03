import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


# Paramètres du signal
duration = 1.0  # Durée en secondes
sampling_rate = 5000  # Fréquence d'échantillonnage en Hz (doit être élevée pour bien capturer les fréquences)
num_frequencies = 50  # Nombre de fréquences aléatoires

# Génération des fréquences aléatoires
np.random.seed(0)  # Pour reproductibilité
frequencies = np.random.uniform(200, 500, num_frequencies)  # Fréquences aléatoires entre 200 et 500 Hz

# Génération du signal temporel
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Vecteur temps
y = np.zeros_like(t)

# Ajouter des sinusoïdes avec les fréquences aléatoires
for f in frequencies:
    y += np.sin(2 * np.pi * f * t)

# Calcul de la transformée de Fourier
Y = np.fft.fft(y)
Y_magnitude = np.abs(Y)  # Magnitude de la FFT
freqs = np.fft.fftfreq(len(Y), 1 / sampling_rate)  # Fréquences associées

# Affichage du signal original
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.title("Signal temporel composé de 50 fréquences aléatoires entre 200 et 500 Hz")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")

# Affichage du spectre de fréquences
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs) // 2], Y_magnitude[:len(freqs) // 2])
plt.title("Transformée de Fourier (Magnitude)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

def closest_note(freq):
    # Fréquences des notes de musique (La4 = 440 Hz)
    notes_freq = [
        261.63,  # Do4
        293.66,  # Ré4
        329.63,  # Mi4
        349.23,  # Fa4
        392.00,  # Sol4
        440.00,  # La4
        493.88,  # Si4
    ]
    
    # Trouver la note la plus proche
    closest_note_idx = np.argmin(np.abs(np.array(notes_freq) - freq))
    return notes_freq[closest_note_idx]

# Trouver la note la plus proche pour chaque fréquence aléatoire
closest_notes = [closest_note(Y) for Y in Y_magnitude]



# Calcul de la transformée inverse de Fourier
y2 = np.fft.ifft(closest_notes)

# Affichage du signal original
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, y2)
plt.title("Signal temporel composé de 50 fréquences aléatoires entre 200 et 500 Hz")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")

# Affichage du spectre de fréquences
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs) // 2], Y_magnitude[:len(freqs) // 2])
plt.title("Transformée de Fourier (Magnitude)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()