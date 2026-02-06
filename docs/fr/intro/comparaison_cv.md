# Comparaison des études

**Sommaire :**
1. Tableau synthétique
2. Différences fondamentales
3. Complémentarité

---

## 1. Tableau synthétique

| Critère | Étude 1 : CV électrode Au/Ni/Cu | Étude 2 : EIS électrode Au/Ni/Cu |
| :--- | :--- | :--- |
| **Domaine** | Temps | **Fréquence** |
| **Espèces redox** | À la surface (oxydes MOH) | À la surface + solution |
| **Transport** | Aucun (ODE de surface) | Diffusion 1D (Warburg) |
| **Variable** | $\theta(t)$ couverture [0,1] | $Z(\omega)$ impédance complexe |
| **Solveur** | Euler implicite analytique | numpy (algébrique) |
| **Cinétique** | Langmuir + BV + hystérésis | Circuit équivalent adaptatif |
| **Sortie** | I(E) voltammogramme | Nyquist + Bode |
| **Paramètres étudiés** | pH, %Ni, %Cu, $C_{dl}$ | pH, %Ni, %Cu |
| **Métriques clés** | Ipa, Ipc, ΔEp | Rct, Cdl, R_film, phase_max |
| **Dépendances** | numpy, matplotlib | numpy, matplotlib |

---

## 2. Différences fondamentales

### Adsorption vs. impédance

L'étude 1 modélise des réactions purement de surface : la couverture $\theta$ est uniforme sur l'électrode. Le courant dépend de $d\theta/dt$ et l'hystérésis ($E^0_{ox} \neq E^0_{red}$) capture la nucléation des oxydes.

L'étude 2 sonde la même électrode Au/Ni/Cu à l'**équilibre** via une perturbation fréquentielle. Elle sépare les contributions résistives (Rs, Rct, R_film) des contributions capacitives (Cdl, CPE) — une décomposition impossible en CV.

### Réversibilité

- Étude 1 : l'hystérésis des oxydes impose toujours $\Delta E_p > 100$ mV.
- Étude 2 : pas de notion de ΔEp — la réversibilité se lit dans $R_{ct}$ et la présence de films passifs.

---

## 3. Complémentarité

Ces deux études couvrent les deux approches complémentaires de caractérisation de l'électrode Au/Ni/Cu :
- **Processus de surface** (étude 1) : caractérisation d'électrodes multi-métalliques, effet du pH
- **Analyse fréquentielle d'une électrode multi-métallique** (étude 2) : séparation des contributions résistives/capacitives, détection de films passifs

L'EIS extrait des grandeurs inaccessibles en CV : **Rct** (résistance de transfert de charge), **Cdl** (capacité de double couche) et **R_film** (résistance du film passif).
