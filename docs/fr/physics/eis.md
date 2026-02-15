**Sommaire :**
1. Principe de l'EIS
2. Circuits équivalents
3. Éléments d'impédance
4. Références bibliographiques

---

## 1. Principe de l'EIS

### 1.1 Perturbation et réponse

Contrairement à l'étude 1 (CV oxydes de surface) qui opère dans le **domaine temporel** (balayage en potentiel → courant I(E)), l'EIS (étude 2) travaille dans le **domaine fréquentiel**. Une petite perturbation sinusoïdale de potentiel est superposée au potentiel DC :

$$E(t) = E_{ocp} + \Delta E \cdot \sin(\omega t)$$

où :
- $E_{ocp}$ = potentiel de circuit ouvert (*open circuit potential*) [V vs Ag/AgCl] — le potentiel auquel le courant net est nul. Les valeurs d'OCP par métal et pH sont documentées dans la page **Données électrochimiques**.
- $\Delta E$ = amplitude de la perturbation (10 mV, régime linéaire)
- $\omega = 2\pi f$ = pulsation angulaire [rad/s]

La réponse en courant est déphasée :

$$I(t) = I_0 + \Delta I \cdot \sin(\omega t + \varphi)$$

où :
- $I_0$ = courant DC stationnaire [A] (= 0 à l'OCP par définition)
- $\Delta I$ = amplitude de la réponse en courant [A]
- $\varphi$ = déphasage entre le potentiel et le courant [rad]

### 1.2 Impédance complexe

L'impédance électrochimique est définie comme :

$$Z(\omega) = \frac{\Delta E}{\Delta I} \cdot e^{j\varphi} = Z'(\omega) + j Z''(\omega)$$

où :
- $Z'(\omega)$ = partie réelle de l'impédance [Ω]
- $Z''(\omega)$ = partie imaginaire de l'impédance [Ω]
- $j$ = nombre imaginaire ($\sqrt{-1}$)

Le balayage fréquentiel couvre :

$$f \in [0.01 \text{ Hz}, 100 \text{ kHz}]$$, espacement logarithmique, 10 points/décade → 70 points

### 1.3 Représentations graphiques

| Diagramme | Axes | Information |
|-----------|------|-------------|
| **Nyquist** | $-\text{Im}(Z)$ vs $\text{Re}(Z)$ | Forme des arcs → mécanismes |
| **Bode magnitude** | $\log|Z|$ vs $\log(f)$ | Résistances limites |
| **Bode phase** | $-\varphi$ vs $\log(f)$ | Constantes de temps |

---

## 2. Circuits équivalents

### 2.1 Sélection adaptative du circuit

Le modèle sélectionne automatiquement le circuit selon le pH et la composition, car la chimie de surface change radicalement avec le milieu. Le critère est simple : si $R_{film} > 0$, le circuit à 2 constantes de temps (2-TC) est utilisé ; sinon, c'est un circuit de Randles.

### 2.2 Formation des oxydes

La nature du film passif dépend du métal et du pH. Les équations redox détaillées (Au₂O₃, Ni(OH)₂/NiOOH, Cu₂O/CuO) et les potentiels associés sont présentés dans la page **Données électrochimiques**.

### 2.3 Circuits par pH

| | **pH 3** (acide) | **pH 7** (neutre) | **pH 11** (alcalin) |
|---|---|---|---|
| **Nom** | Randles simple | Circuit variable | 2 constantes de temps (tous métaux) |
| **Circuit** | `Rs → [CPE_dl ‖ (Rct + Z_W)]` | Au, Ni : Randles ; Cu : `Rs → [CPE_film ‖ R_film] → [CPE_dl ‖ (Rct + Z_W)]` | `Rs → [CPE_oxide ‖ R_oxide] → [CPE_dl ‖ (Rct + Z_W)]` |
| **Justification** | Au nu ; Ni/Cu dissolution active (pas de passivation < pH 5) | Au nu ; ⚠️ Ni instable — NiOOH se dissout (ACS Omega 2017) ; Cu : Cu₂O semi-protecteur (R_film = 400 Ω) | Tous passivés : Au(OH)₃ (Burke 1997), Ni(OH)₂/NiOOH (R_film = 2 000 Ω), Cu₂O/CuO |
| **Signature Nyquist** | 1 semicercle + Warburg 45° | 1 arc (Au, Ni) ou 2 arcs superposés (Cu) + Warburg | 2 arcs nets + Warburg |

---

## 3. Éléments d'impédance

| Élément | Impédance | Paramètres | Rôle physique |
|---------|-----------|------------|---------------|
| Résistance | $Z_R = R$ | R (Ω) | Solution, transfert de charge, film |
| Capacité | $Z_C = \frac{1}{j\omega C}$ | C (F) | Double couche idéale |
| CPE | $Z_{CPE} = \frac{1}{Q_0 (j\omega)^n}$ | Q₀ (F·s^(n-1)), n ∈ [0,1] | Double couche non idéale |
| Warburg | $Z_W = \frac{\sigma}{\sqrt{\omega}}(1 - j)$ | σ (Ω·s^(-1/2)) | Diffusion semi-infinie |

### CPE vs capacité pure

Le CPE (Constant Phase Element) remplace la capacité idéale pour modéliser les surfaces réelles :
- $n = 1$ → capacité pure
- $n = 0.8\text{–}0.95$ → surface rugueuse, hétérogène
- $n < 0.8$ → distribution de constantes de temps, surface très désordonnée

### Circuit de Randles

$$Z(\omega) = R_s + \frac{1}{\frac{1}{Z_{CPE}} + \frac{1}{R_{ct} + Z_W}}$$

### Circuit à 2 constantes de temps

$$Z(\omega) = R_s + Z_{film\parallel} + Z_{dl\parallel}$$

avec $Z_{film\parallel} = \frac{R_{film} \cdot Z_{CPE,film}}{R_{film} + Z_{CPE,film}}$ et $Z_{dl\parallel} = \frac{(R_{ct} + Z_W) \cdot Z_{CPE,dl}}{(R_{ct} + Z_W) + Z_{CPE,dl}}$

---

## 4. Références bibliographiques

| # | Référence | Usage |
|---|-----------|-------|
| [1] | Hamelin *et al.* (1994) — *Electrochim. Acta* — Au/H₂SO₄ | Rct, Cdl Au |
| [2] | Song *et al.* (2025) — *ChemElectroChem* | Cdl vs pH |
| [3] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* 39, 969 | Pourbaix Ni |
| [4] | Beverskog & Puigdomenech (1997) — *J. Electrochem. Soc.* 144, 3476 | Pourbaix Cu |
| [5] | Diaz-Morales *et al.* (2020) — *ACS Catal.* 10, 12582 | Au oxide OER |
| [6] | ACS Omega (2017) — DOI: 10.1021/acsomega.6b00448 | NiOOH instabilité |
| [8] | Weininger & Breiter (1963) — *J. Electrochem. Soc.* 110, 484-490 | Ni film EIS |
| [9] | Ambrose *et al.* (1973) — *J. Electroanal. Chem.* 47, 47 | Cu alcalin |
| [11] | Lazanas & Prodromidis (2023) — *ACS Meas. Sci. Au* 3(3), 162 | Tutorial EIS |
| [12] | Gamry Instruments — "Basics of EIS" | Application Note |

*Pour la liste complète : voir Références bibliographiques dans le menu Annexes.*
