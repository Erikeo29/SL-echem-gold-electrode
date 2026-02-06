# Introduction

**Sommaire :**
1. Principe de la voltamétrie cyclique
2. Principe de la spectroscopie d'impédance
3. Enjeux de la modélisation
4. Références bibliographiques

---

## 1. Principe de la voltamétrie cyclique

La voltamétrie cyclique (CV) est sans doute la méthode électrochimique la plus utilisée pour acquérir des informations qualitatives sur les réactions électrochimiques.

Elle consiste à balayer le potentiel d'une électrode de travail à une vitesse constante $v$ entre deux bornes, tout en mesurant le courant résultant. Le graphique du courant en fonction du potentiel est appelé un **voltammogramme**.

## 2. Principe de la spectroscopie d'impédance

La spectroscopie d'impédance électrochimique (EIS) est complémentaire de la CV : elle travaille dans le **domaine fréquentiel**. Une petite perturbation sinusoïdale ($\Delta E = 10$ mV) est appliquée, et la réponse en courant (amplitude + déphasage) permet de construire l'impédance complexe $Z(\omega)$.

Les diagrammes de **Nyquist** et de **Bode** révèlent les résistances (solution, transfert de charge, film passif) et les capacités (double couche) inaccessibles en CV.

---

## 3. Enjeux de la modélisation

La simulation numérique permet de :
1. Prédire la forme des pics de courant en fonction de la vitesse de balayage (CV)
2. Extraire des constantes cinétiques ($k^0$) et des coefficients de diffusion ($D$)
3. Comprendre les phénomènes de déplétion à proximité de l'électrode
4. Séparer les contributions résistives et capacitives de l'interface (EIS)
5. Diagnostiquer la présence et les propriétés de films passifs
6. Quantifier l'influence des propriétés du couple redox sur la réponse en impédance

Dans ce projet, quatre études complémentaires couvrent :
- **Études 1 et 2** : le couple redox type **ferro/ferricyanure** ($Fe(CN)_6^{3-/4-}$) sur électrode d'or pure, en CV (étude 1) et en EIS (étude 2)
- **Études 3 et 4** : une électrode **Au avec impuretés Ni et Cu**, en CV avec oxydes de surface (étude 3) et en EIS avec circuit adaptatif (étude 4)

---

## 4. Références bibliographiques

*Note : Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
