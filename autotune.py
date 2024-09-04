import numpy as np
import matplotlib.pyplot as plt


# Paramètres du signal
duration = 1.0  # Durée en secondes
sampling_rate = 5000  # Fréquence d'échantillonnage en Hz
num_frequencies = 50  # Nombre de fréquences aléatoires
keys = {
    "C": [
        261.63,  # Do4
        293.66,  # Ré4
        329.63,  # Mi4
        349.23,  # Fa4
        392.00,  # Sol4
        440.00,  # La4
        493.88,  # Si4
    ],
    "D": [
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

def generation_signal(frequences:np.ndarray) -> tuple[np.ndarray,np.ndarray] :
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) # TEMPS
    y = np.zeros_like(t) # SIGNAL
    for f in frequences:
        y += np.sin(2 * np.pi * f * t)
    return y, t

def transfo_fourier(y:np.ndarray, t:np.ndarray, sampling_rate:int) -> tuple[np.ndarray,np.ndarray] :
    Y = np.abs(np.fft.fft(y))
    freqs = np.fft.fftfreq(len(Y), 1 / sampling_rate)
    return Y, freqs

def freqs_dominantes(Y:np.ndarray, freqs:np.ndarray, num_frequencies:int) -> np.ndarray :
    indices = np.argsort(Y)[-num_frequencies:]  # Indices des fréquences dominantes
    dominant_freqs = np.abs(freqs[indices])  # Fréquences dominantes
    return dominant_freqs

def plot_signal(y:np.ndarray, t:np.ndarray, freqs:np.ndarray, Y:np.ndarray) -> None:
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
    
    
# A IMPLEMENTER

# TODO: Prends une fréquence et une clé et retourne la note la plus proche
def closest_note(freq:float, key:list[float]) -> float:  
    return 

# TODO: Générer le signal normal

# TODO: Calculer la transformée de Fourier du signal

# TODO: Afficher le signal et son spectre de fréquences

# TODO: Trouver les fréquences dominantes

# TODO: Remplacer les fréquences dominantes par les notes les plus proches de la gamme donnée

# TODO: Recomposer le signal avec les nouvelles fréquences

# TODO: Calculer la FFT du nouveau signal

# TODO: Afficher le nouveau signal et son spectre
