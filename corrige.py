import numpy as np
import matplotlib.pyplot as plt


# Paramètres du signal
duration = 1.0  # Durée en secondes
sampling_rate = 5000  # Fréquence d'échantillonnage en Hz
num_frequencies = 50  # Nombre de fréquences aléatoires

keys = {
    "Do": [
        261.63,  # Do4
        293.66,  # Ré4
        329.63,  # Mi4
        349.23,  # Fa4
        392.00,  # Sol4
        440.00,  # La4
        493.88,  # Si4
    ],
    "Ré": [
        293.66,  # Ré4
        329.63,  # Mi4
        349.23,  # Fa4
        392.00,  # Sol4
        440.00,  # La4
        493.88,  # Si4
        523.25,  # Do5
    ]
}

# Génération des fréquences aléatoires
np.random.seed(0)  # Pour reproductibilité
frequencies = np.random.uniform(200, 500, num_frequencies)  # Fréquences aléatoires entre 200 et 500 Hz

def generation_signal(frequencies):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) # TEMPS
    y = np.zeros_like(t) # SIGNAL

    for f in frequencies:
        y += np.sin(2 * np.pi * f * t)

    return y, t


def plot_signal(y, t, freqs, Y):
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, y)
    plt.title("Signal")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")

    # Affichage du spectre de fréquences
    plt.subplot(2, 1, 2)
    plt.plot(freqs[:len(freqs) // 2], Y[:len(freqs) // 2])
    plt.title("Transformée de Fourier")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

def transfo_fourier(y, t, sampling_rate):
    Y = np.abs(np.fft.fft(y)) # Transformée de Fourier
    freqs = np.fft.fftfreq(len(Y), 1 / sampling_rate)  # Fréquences associées
    return Y, freqs

# Mapper les fréquences dominantes aux notes les plus proches
def closest_note(freq, key):  
    closest_note_idx = np.argmin(np.abs(np.array(key) - freq))
    return key[closest_note_idx]

# TODO

# Générer le signal normal
y, t = generation_signal(frequencies=frequencies)

# Calculer la transformée de Fourier du signal
Y, freqs = transfo_fourier(y, t, sampling_rate)

# Afficher le signal et son spectre de fréquences
plot_signal(y, t, freqs, Y)

# Trouver les fréquences dominantes
indices = np.argsort(Y)[-num_frequencies:]  # Indices des fréquences dominantes
dominant_freqs = np.abs(freqs[indices])  # Fréquences dominantes

# Remplacer les fréquences dominantes par les notes les plus proches de la gamme donnée
mapped_freqs = [closest_note(f, keys["Do"]) for f in dominant_freqs]

# Recomposer le signal avec les nouvelles fréquences
y2, t = generation_signal(mapped_freqs)

# Calculer la FFT du nouveau signal
Y2 = np.fft.fft(y2)
Y2_magnitude = np.abs(Y2)

# Afficher le nouveau signal et son spectre
plot_signal(y2, t, freqs, Y2_magnitude)
