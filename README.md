# Pitch-correction (Autotune)

La correction dynamique de fréquence est au coeur même du fonctionnement du plug-in AutoTune. Ce logiciel permet de conserver une certaine justesse, et donc d'éviter de chanter faux. Pour cela, le logiciel analyse la fréquence de la piste audio en temps réel et l'ajuste sur la note de la gamme la plus proche.

Une `gamme` est défini par une `clé`, et désigne un `ensemble de fréquences` qui "sonnent correctement" entre elles.

Prenons un exemple rapide : Un chanteur 

Note	Fréquence (Hz)
Do4	261.63
Ré4	293.66
Mi4	329.63
Fa4	349.23
Sol4	392.00
La4	440.00
Si4	493.88

``` pip install librosa ```


SOLUTION : 
Génerer liste de fréquences aléatoires entre 200 hz et 500 hz
Afficher la sinusoidale grace a fourrier

Appliquer l'algo de correction
Afficher la sinusoidale corrigée