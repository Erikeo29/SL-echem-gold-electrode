# Comparaison des études

**Sommaire :**
1. Tableau synthétique
2. Différences fondamentales
3. Complémentarité

---

## 1. Tableau synthétique

| Critère | Étude 1 : CV couple redox sur Au | Étude 2 : EIS couple redox sur Au | Étude 3 : CV électrode Au/Ni/Cu | Étude 4 : EIS électrode Au/Ni/Cu |
| :--- | :--- | :--- | :--- | :--- |
| **Domaine** | Temps | **Fréquence** | Temps | **Fréquence** |
| **Espèces redox** | En solution ($Fe(CN)_6^{3-/4-}$) | En solution ($Fe(CN)_6^{3-/4-}$) | À la surface (oxydes MOH) | À la surface + solution |
| **Transport** | Diffusion (loi de Fick) | Diffusion 1D (Warburg) | Aucun (ODE de surface) | Diffusion 1D (Warburg) |
| **Variable** | $c(x,y,t)$ concentration | $Z(\omega)$ impédance complexe | $\theta(t)$ couverture [0,1] | $Z(\omega)$ impédance complexe |
| **Solveur** | Firedrake + Newton (FEM 2D) | numpy (algébrique) | Euler implicite analytique | numpy (algébrique) |
| **Cinétique** | Butler-Volmer classique | Circuit de Randles + CPE | Langmuir + BV + hystérésis | Circuit équivalent adaptatif |
| **Sortie** | I(E) voltammogramme | Nyquist + Bode | I(E) voltammogramme | Nyquist + Bode |
| **Paramètres étudiés** | $k^0$, $\alpha$, $\nu$ | $n$, $k^0$, $D$, $c$, $Q_0$ | pH, %Ni, %Cu, $C_{dl}$ | pH, %Ni, %Cu |
| **Métriques clés** | Ipa, Ipc, ΔEp, ratio | Rct, σ, Cdl, ω_max | Ipa, Ipc, ΔEp | Rct, Cdl, R_film, phase_max |
| **Dépendances** | Firedrake, GMSH, scipy | numpy, matplotlib | numpy, matplotlib | numpy, matplotlib |

---

## 2. Différences fondamentales

### Transport vs. adsorption vs. impédance

L'étude 1 résout un problème de diffusion spatio-temporel : la concentration évolue dans l'espace (couche de diffusion) et dans le temps. Le courant de pic suit la loi de Randles-Ševčík : $I_p \propto \sqrt{\nu}$.

L'étude 2 sonde le même couple redox mais dans le domaine fréquentiel. Elle extrait $R_{ct}$ (inversement proportionnel à $k^0$) et $\sigma$ (lié à $D$), des grandeurs inaccessibles en CV.

L'étude 3 modélise des réactions purement de surface : la couverture $\theta$ est uniforme sur l'électrode. Le courant dépend de $d\theta/dt$ et l'hystérésis ($E^0_{ox} \neq E^0_{red}$) capture la nucléation des oxydes.

L'étude 4 sonde la même électrode Au/Ni/Cu à l'**équilibre** via une perturbation fréquentielle. Elle sépare les contributions résistives (Rs, Rct, R_film) des contributions capacitives (Cdl, CPE) — une décomposition impossible en CV.

### Réversibilité

- Étude 1 : le système peut être réversible ($\Delta E_p \approx 59$ mV) si $k^0$ est suffisamment élevé.
- Étude 2 : la réversibilité se lit dans le diamètre de l'arc Nyquist ($R_{ct}$ faible = réaction rapide).
- Étude 3 : l'hystérésis des oxydes impose toujours $\Delta E_p > 100$ mV.
- Étude 4 : pas de notion de ΔEp — la réversibilité se lit dans $R_{ct}$ et la présence de films passifs.

---

## 3. Complémentarité

Ces quatre études couvrent les grandes familles de caractérisation électrochimique :
- **Processus contrôlé par diffusion** (étude 1) : diagnostic de réversibilité, effet de $\nu$
- **Analyse fréquentielle d'un couple redox** (étude 2) : influence de $k^0$, $D$, $c$ sur l'impédance
- **Processus de surface** (étude 3) : caractérisation d'électrodes multi-métalliques, effet du pH
- **Analyse fréquentielle d'une électrode multi-métallique** (étude 4) : séparation des contributions résistives/capacitives, détection de films passifs

L'EIS extrait des grandeurs inaccessibles en CV : **Rct** (résistance de transfert de charge), **Cdl** (capacité de double couche), **R_film** (résistance du film passif) et **σ** (coefficient de Warburg).
