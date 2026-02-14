&nbsp;

**Note de l'auteur** — *Ce projet a été conçu intégralement par l'auteur, depuis une page blanche jusqu'à sa mise en ligne. Le contenu a été élaboré sur la base de ses connaissances complétées par des recherches en ligne pour la partie documentaire, définition des concepts physiques, mise en oeuvre des outils numériques pertinents...*

*Pour les sujets (très nombreux !) dépassant son domaine de compétence initial, des outils d'intelligence artificielle et d'automatisation ont été utilisés pour réaliser des recherches internet approfondies (paramétrage des équations des modèles physiques, sélection et utilisation des bibliothèques numériques), la rédaction, le test et la correction des codes (Python, C++), la création de l'interface de cette application, la traduction automatique français / anglais...*

*Il n'en demeure pas moins que tous les résultats présentés dans ce projet sont issus de modèles physiques analytiques et déterministes résolus par des solveurs numériques reconnus et validés. L'objectif est de permettre la réalisation de modélisations multiphysiques avancées au moyen d'outils open-source et gratuits.*

*Les données d'entrées utilisées (équations, valeurs...) sont publiques et disponibles en accès libres sur internet même si très éparpillées. Les codes sont originaux même si non innovants. De fait, ce travail est mis à disposition pour être librement utilisé, reproduit et amélioré à des fins d'apprentissage ou d'exploitation des modèles physiques et numériques présentés.*

&nbsp;

**Sommaire :**
1. Objectif
2. Études disponibles
3. Navigation
4. Note méthodologique

---

## 1. Objectif

Cette application regroupe des simulations **électrochimiques** résolues en Python. L'objectif est de visualiser et comparer les résultats d'études paramétriques pour deux systèmes électrochimiques complémentaires sur une électrode d'or avec présence d'impuretés de nickel et de cuivre, couvrant le domaine temporel (voltamétrie cyclique) et le domaine fréquentiel (impédance).

---

## 2. Études disponibles

### Étude 1 : CV d'une électrode Au avec impuretés Ni et Cu

Simulation des réactions de surface (oxydes métalliques) sur une électrode d'or avec traces de nickel et de cuivre. Le modèle repose sur une ODE (équation différentielle ordinaire) du type Langmuir–Butler-Volmer résolue par un schéma implicite analytique (sans itération numérique). L'étude paramétrique porte sur le pH, la composition de l'électrode et la capacité de double couche $C_{dl}$.

### Étude 2 : EIS d'une électrode Au avec impuretés Ni et Cu

Spectroscopie d'impédance électrochimique sur la même électrode Au/Ni/Cu. Le modèle utilise un circuit équivalent adaptatif : Randles simple à pH acide, 2 constantes de temps à pH neutre/alcalin (film passif). L'étude paramétrique porte sur le pH, %Ni et %Cu. Les résultats des calculs extraits de ces calaculs ($R_{ct}$, $C_{dl}$, $R_{film}$) sont complémentaires des métriques CV de l'étude 1.

---

## 3. Navigation

La navigation dans les différentes pages de cette application est structurée avec les outils suivants :

1. **Menu latéral (à gauche)** : outil de navigation entre les différentes sections du projet :
   - **Introduction** : contexte scientifique et présentation des systèmes.
   - **Comparaison des études** : tableau synthétique des deux approches.
   - **Résultats de modélisation** : chaque étude contient des onglets Physique (description des modèles physiques et de résolution numérique utilisés), Code (codes entièrement développés dans ce projet et pouvant être dupliqué) et Résultats (modélisations visuelles).
   - **Annexes** : conclusion, lexique, équations clés, références bibliographiques et une page d'histoire sur les principaux chercheurs et scientifiques ayant développés les concepts physiques et numériques présentés.

2. **Boutons de navigation flottants (à droite)** : déplacement rapide haut/bas de page.

3. **Assistant IA (menu latéral)** : réponses aux questions sur la physique ou les méthodes numériques.

---

## 4. Note méthodologique

Les résultats présentés proviennent de simulations **pré-calculées**. Le projet a été réalisé sur un PC portable standard : environnement Linux via WSL2, processeur 1.5-3.5 GHz, 6 CPU / 12 threads, 32 Go de RAM. Les temps de calcul varient de quelques secondes (étude EIS, calcul algébrique) à 30 secondes (étude CV, ODE) par simulation unitaire.

Cette application est donc un **visualiseur de résultats**, non un simulateur en temps réel. En effet, la réalisation de ces simulations nécessite des configurations spécifiques d'environnements et de packages Python (numpy). Les codes sont disponibles dans les onglets "Code" de chaque étude afin de permettre leur reproduction sur d'autres machines.
