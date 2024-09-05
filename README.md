# Pitch-correction (Autotune)

La correction dynamique de fréquences est au coeur même du fonctionnement du plug-in AutoTune. Ce logiciel permet de conserver une certaine justesse, et donc d'éviter de chanter faux. Pour cela, le logiciel analyse la fréquence de la piste audio en temps réel et l'ajuste sur la note de la gamme la plus proche.

Une `gamme` est définie par une `clé`, et désigne un `ensemble de fréquences`(ou de notes) qui "sonnent correctement" entre elles.

Prenons un exemple rapide : Un artiste doit chanter sur un morceau en gamme "C" (Do). Ici, C est la clé de la gamme. 

Voici l'ensemble de fréquences de la gamme "C" :

| Note  | Fréquence (Hz) |
|-----|--------|
| Do  | 261.63 |
| Ré  | 293.66 |
| Mi  | 329.63 |
| Fa  | 349.23 |
| Sol | 392.00 |
| La  | 440.00 |
| Si  | 493.88 |

Si l'artiste chante une note de fréquence 285 hz, le correcteur de pitch va augmenter la fréquence de cette note afin de l'ajuster à la fréquence de la gamme la plus proche (ici Ré4).

## Objectif :

Votre objectif est de concevoir un programme permettant d'ajuster des fréquences relativement à une clé donnée, afin de simuler le fonctionnement d'un plug-in de correction automatique de pitch. Pour visualiser cela, `vous éditerez deux graphiques` (chacun comprenant une représentation du signal et de la répartition des fréquences).

Les fréquences sont stockées dans le tableau `frequencies`. Afin de simplifier la lisibilité du graphique, on génere notre onde sonore grace à une sélection de 50 fréquences aléatoirement choisies entre 200 et 500 hz.
Attention aux variables globales au début du code, qui ont leur importance.

Afin de déterminer la répartition des fréquences à partir d'un signal, utilisez la transformée de Fourrier (si vous ne connaissez pas, google est votre ami).

Il est également important d'identifier les fréquences dominantes d'un signal avant de le corriger (une fonction est fournie pour cela).

Bon courage ! (il en faudra)
