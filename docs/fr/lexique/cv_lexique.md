# Lexique

**Sommaire :**
1. Acronymes généraux
2. Acronymes électrochimiques
3. Nombres adimensionnels
4. Symboles physiques
5. Termes techniques
6. Logiciels et bibliothèques
7. Unités SI
---

## 1. Acronymes généraux

| Acronyme | Signification | Description |
|----------|---------------|-------------|
| **FEM** | Finite Element Method | Méthode des éléments finis |
| **FVM** | Finite Volume Method | Méthode des volumes finis |
| **CFD** | Computational Fluid Dynamics | Mécanique des fluides numérique |
| **BC** | Boundary Condition | Condition aux limites |
| **IC** | Initial Condition | Condition initiale |
| **PDE** | Partial Differential Equation | Équation aux dérivées partielles |
| **DOF** | Degrees of Freedom | Degrés de liberté |
| **SI** | Système International | Système d'unités international |

---

## 2. Acronymes électrochimiques

| Acronyme | Signification | Description |
|----------|---------------|-------------|
| **CV** | Cyclic Voltammetry | Voltamétrie cyclique |
| **WE** | Working Electrode | Électrode de travail (lieu de la réaction d'intérêt) |
| **CE** | Counter Electrode | Électrode auxiliaire (ferme le circuit) |
| **RE** | Reference Electrode | Électrode de référence (potentiel stable) |
| **OCP** | Open Circuit Potential | Potentiel en circuit ouvert |
| **EIS** | Electrochemical Impedance Spectroscopy | Spectroscopie d'impédance |
| **BV** | Butler-Volmer | Équation cinétique de transfert de charge |
| **NP** | Nernst-Planck | Équation de transport avec migration |
| **HER** | Hydrogen Evolution Reaction | Réduction de H⁺ en H₂ (mur cathodique) |
| **OER** | Oxygen Evolution Reaction | Oxydation de H₂O en O₂ (mur anodique) |

---

## 3. Nombres adimensionnels

| Symbole | Nom | Expression | Signification physique |
|---------|-----|------------|------------------------|
| $Da$ | Damköhler | $\frac{k^0 L}{D}$ | Cinétique / Diffusion |
| $Pe$ | Péclet | $\frac{v L}{D}$ | Convection / Diffusion |
| $\Lambda$ | Paramètre cinétique | $\frac{k^0}{\sqrt{n F v D / RT}}$ | Réversibilité du système CV |

**Interprétation du paramètre $\Lambda$ :**
- $\Lambda > 15$ : Système réversible (transfert rapide)
- $1 < \Lambda < 15$ : Système quasi-réversible
- $\Lambda < 1$ : Système irréversible (transfert lent)

---

## 4. Symboles physiques

### Paramètres électrochimiques

| Symbole | Nom | Unité SI |
|---------|-----|----------|
| $E$ | Potentiel d'électrode | V |
| $E^0$ | Potentiel standard | V |
| $\eta$ | Surtension ($E - E^0$) | V |
| $I$ | Courant | A |
| $i$ | Densité de courant | A/m² |
| $J$ | Flux molaire | mol/(m²·s) |
| $n$ | Nombre d'électrons transférés | - |

### Paramètres cinétiques

| Symbole | Nom | Unité SI |
|---------|-----|----------|
| $k^0$ | Constante de vitesse standard | m/s (solution) ou s⁻¹ (surface) |
| $\alpha$ | Coefficient de transfert | - |
| $v$ | Vitesse de balayage (scan rate) | V/s |
| $F$ | Constante de Faraday | 96485 C/mol |
| $R$ | Constante des gaz parfaits | 8.314 J/(mol·K) |
| $T$ | Température | K |

### Paramètres de transport

| Symbole | Nom | Unité SI |
|---------|-----|----------|
| $c_i$ | Concentration de l'espèce $i$ | mol/m³ |
| $c_O$ | Concentration de l'oxydant | mol/m³ |
| $c_R$ | Concentration du réducteur | mol/m³ |
| $C^*$ | Concentration bulk | mol/m³ |
| $D$ | Coefficient de diffusion | m²/s |
| $\delta$ | Épaisseur de couche de diffusion | m |

### Paramètres de surface (CV électrodes Au/Ni/Cu)

| Symbole | Nom | Unité SI |
|---------|-----|----------|
| $\theta$ | Couverture de surface (fraction de sites occupés) | - [0, 1] |
| $\Gamma_{max}$ | Densité maximale de sites de surface | mol/m² |
| $E^0_{ox}$ | Potentiel standard d'oxydation (formation d'oxyde) | V |
| $E^0_{red}$ | Potentiel standard de réduction (dissolution d'oxyde) | V |
| $C_{dl}$ | Capacité de double couche | F/m² (ou µF/cm²) |

### Métriques CV

| Symbole | Nom | Unité |
|---------|-----|-------|
| $I_{pa}$ | Courant de pic anodique | A (ou µA) |
| $I_{pc}$ | Courant de pic cathodique | A (ou µA) |
| $E_{pa}$ | Potentiel de pic anodique | V |
| $E_{pc}$ | Potentiel de pic cathodique | V |
| $\Delta E_p$ | Écart de pic ($\|E_{pa} - E_{pc}\|$) | V (ou mV) |

### Grandeurs d'impédance (EIS)

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $Z(\omega)$ | Impédance complexe | Ω | Rapport $\Delta E / \Delta I$ en régime sinusoïdal |
| $Z'$ | Partie réelle | Ω | Composante résistive |
| $Z''$ | Partie imaginaire | Ω | Composante réactive |
| $\|Z\|$ | Module de l'impédance | Ω | $\sqrt{Z'^2 + Z''^2}$ |
| $\varphi$ | Déphasage | ° ou rad | Angle entre courant et tension |

### Éléments de circuit (EIS)

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $R_s$ | Résistance de solution | Ω | Chute ohmique dans l'électrolyte |
| $R_{ct}$ | Résistance de transfert de charge | Ω | Cinétique de la réaction redox |
| $R_{film}$ | Résistance de film passif | Ω | Film d'oxyde (EIS électrodes Au/Ni/Cu) |
| $Q_0$ | Paramètre CPE | F·s^(n-1) | Pseudo-capacité (CPE) |
| $n_{CPE}$ | Exposant CPE | — | 1 = capacité idéale, < 1 = non idéale |
| $\sigma$ | Coefficient de Warburg | Ω·s⁻⁰·⁵ | Diffusion semi-infinie |
| $C_{dl}$ | Capacité de double couche | F | Interface électrode/solution |

### Paramètres spécifiques EIS

*Note : $k^0$, $D$ et $c$ sont définis ci-dessus (paramètres cinétiques et de transport).*

| Symbole | Nom | Unité | Description |
|---------|-----|-------|-------------|
| $n_{el}$ | Nombre d'électrons transférés | — | Électrons par réaction élémentaire |
| $A$ | Surface de l'électrode | m² | Surface active de l'électrode de travail |
| $\omega$ | Pulsation | rad/s | $\omega = 2\pi f$ |
| $\omega_{max}$ | Pulsation au sommet | rad/s | Fréquence caractéristique du semicercle |

---

## 5. Termes techniques

### Électrochimie

| Terme | Définition |
|-------|------------|
| **Voltammogramme** | Courbe $I = f(E)$ obtenue lors d'un balayage de potentiel |
| **Réversible** | Système où le transfert d'électrons est rapide devant la diffusion ($\Delta E_p \approx 59/n$ mV) |
| **Quasi-réversible** | Système où cinétique et diffusion sont du même ordre |
| **Irréversible** | Système limité par la cinétique de transfert |
| **Déplétion** | Appauvrissement en espèce réactive à proximité de l'électrode |
| **Couche de diffusion** | Zone où le gradient de concentration est non nul |
| **Double couche** | Interface métal/solution avec séparation de charge |
| **Couple redox** | Paire espèce oxydée / espèce réduite |

### Méthodes numériques

| Terme | Définition |
|-------|------------|
| **Maillage** | Discrétisation spatiale du domaine de calcul |
| **Raffinement local** | Augmentation de la densité de mailles dans une zone critique |
| **Euler implicite** | Schéma temporel inconditionnellement stable |
| **Newton-Raphson** | Algorithme itératif pour systèmes non-linéaires |
| **Préconditionnement** | Technique d'accélération de convergence |
| **Formulation faible** | Forme intégrale des équations (base de FEM) |
| **Éléments P2** | Éléments Lagrange de degré 2 (quadratiques) |

---

## 6. Logiciels et bibliothèques

| Nom | Type | Langage | Méthode | Usage |
|-----|------|---------|---------|-------|
| **Firedrake** | Open-source | Python | FEM | Résolution EDP (ce projet) |
| **FEniCSx** | Open-source | Python/C++ | FEM | Alternative FEM |
| **GMSH** | Open-source | Python/C++ | - | Génération de maillage |
| **OpenFOAM** | Open-source | C++ | FVM | CFD, multiphasique |
| **COMSOL** | Commercial | GUI/MATLAB | FEM | Multiphysique |
| **PETSc** | Open-source | C | - | Solveurs HPC |
| **NumPy** | Open-source | Python | - | Calcul scientifique |
| **Matplotlib** | Open-source | Python | - | Visualisation |

---

## 7. Unités SI

### Grandeurs fondamentales

| Grandeur | Unité | Symbole |
|----------|-------|---------|
| Longueur | mètre | m |
| Masse | kilogramme | kg |
| Temps | seconde | s |
| Courant électrique | ampère | A |
| Température | kelvin | K |
| Quantité de matière | mole | mol |

### Grandeurs dérivées

| Grandeur | Unité | Symbole | Équivalent |
|----------|-------|---------|------------|
| Potentiel | volt | V | J/C |
| Charge | coulomb | C | A·s |
| Énergie | joule | J | V·C |
| Concentration | mol par mètre cube | mol/m³ | - |
| Diffusivité | mètre carré par seconde | m²/s | - |
| Flux molaire | mol/(m²·s) | - | - |

### Préfixes courants

| Préfixe | Symbole | Facteur | Exemple |
|---------|---------|---------|---------|
| micro | µ | 10⁻⁶ | µA (microampère) |
| milli | m | 10⁻³ | mV, mM |
| kilo | k | 10³ | kJ |


