&nbsp;

**Note de l'auteur** — *Ce projet a été conçu intégralement par l'auteur, depuis une page blanche jusqu'à sa mise en ligne. La création du contenu a été réalisée avec le support d'outils d'intelligence artificielle en particulier pour la rédaction et la correction des codes et pour les recherches internet.
Tous les résultats montrés dans ce projet sont issus de modèles physiques analytiques et déterministes résolus par des solveurs numériques validés.
Ce travail est mis à disposition en open-source : il peut être librement copié, dupliqué et adapté à des fins d'apprentissage ou d'exploitation des modèles physiques et numériques présentés.*

&nbsp;

**Sommaire :**
1. Objectif
2. Études disponibles
3. Navigation
4. Note méthodologique

---

## 1. Objectif

Cette application regroupe des simulations **électrochimiques** résolues en Python. L'objectif est de visualiser et comparer les résultats d'études paramétriques pour deux systèmes électrochimiques complémentaires sur une électrode d'or avec impuretés de nickel et cuivre, couvrant le domaine temporel (voltamétrie cyclique) et le domaine fréquentiel (impédance).

---

## 2. Études disponibles

### Étude 1 : CV d'une électrode Au avec impuretés Ni et Cu

Simulation des réactions de surface (oxydes métalliques) sur une électrode d'or avec traces de nickel et de cuivre. Le modèle repose sur une ODE de Langmuir–Butler-Volmer résolue par un schéma implicite analytique. L'étude paramétrique porte sur le pH, la composition de l'électrode et la capacité de double couche $C_{dl}$.

### Étude 2 : EIS d'une électrode Au avec impuretés Ni et Cu

Spectroscopie d'impédance électrochimique sur la même électrode Au/Ni/Cu. Le modèle utilise un circuit équivalent adaptatif : Randles simple à pH acide, 2 constantes de temps à pH neutre/alcalin (film passif). L'étude paramétrique porte sur le pH, %Ni et %Cu (27 simulations, aligné avec l'étude CV). Les diagnostics extraits ($R_{ct}$, $C_{dl}$, $R_{film}$) sont complémentaires des métriques CV de l'étude 1.

---

## 3. Navigation

L'application est structurée autour de plusieurs outils :

1. **Menu latéral (à gauche)** : navigation principale entre les sections du projet.
   - **Introduction** : contexte scientifique et présentation des systèmes.
   - **Comparaison des études** : tableau synthétique des deux approches.
   - **Pages par étude** : chaque étude contient des onglets Physique, Code et Résultats.
   - **Annexes** : conclusion, lexique technique, équations clés et références bibliographiques.

2. **Boutons de navigation flottants (à droite)** : déplacement rapide haut/bas de page.

3. **Assistant IA (menu latéral)** : réponses aux questions sur la physique ou les méthodes numériques.

---

## 4. Note méthodologique

Les résultats présentés proviennent de simulations **pré-calculées**. Le projet a été réalisé sur un PC portable standard : environnement Linux via WSL2, processeur 1.5-3.5 GHz, 6 CPU / 12 threads, 32 Go de RAM. Les temps de calcul varient de quelques secondes (étude 2, calcul algébrique) à 30 secondes (étude 1, ODE) par simulation unitaire.

Cette application est donc un **visualiseur de résultats**, non un simulateur en temps réel. En effet, la réalisation de ces simulations nécessite des configurations spécifiques d'environnements et de packages Python (numpy). Les codes sont disponibles dans les onglets "Code" de chaque étude afin de permettre leur reproduction sur d'autres machines.
