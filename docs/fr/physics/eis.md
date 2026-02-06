**Sommaire :**
1. Principe de l'EIS
2. Circuits équivalents
3. Éléments d'impédance
4. Paramètres physiques
5. Lois de mélange
6. Complémentarité avec les études 1 et 2
7. Références bibliographiques

---

## 1. Principe de l'EIS

### 1.1 Perturbation et réponse

Contrairement aux Études 1 et 2 qui opèrent dans le **domaine temporel** (balayage en potentiel → courant I(E)), l'EIS travaille dans le **domaine fréquentiel**. Une petite perturbation sinusoïdale de potentiel est superposée au potentiel DC :

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

### 2.3 pH 3 (acide) — Randles simple

> **Circuit** :  `Rs` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification** :
- Au reste nu (pas d'oxyde en dessous de ~1.2 V vs. RHE)
- Ni et Cu se dissolvent activement (pas de passivation stable sous pH 5)
- **1 seule constante de temps** : la double couche électrique

**Signature Nyquist** : 1 semicercle + droite de Warburg à 45°.

### 2.4 pH 7 (neutre) — circuit variable selon le métal

Le comportement à pH 7 dépend du métal :

**Au et Ni → Randles simple** (pas de film) :
> `Rs` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Cu → 2 constantes de temps** (film Cu₂O) :
> `Rs` → `[ CPE_film ‖ R_film ]` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification** :
- Au reste nu à pH 7 (circuit Randles simple)
- ⚠️ **Ni instable à pH 7** : le film NiOOH se dissout lentement (ACS Omega 2016). Traité comme dissolution lente, pas de R_film.
- Cu forme Cu₂O semi-protecteur → R_film = 400 Ω

**Signature Nyquist** : 1 arc (Au, Ni) ou 2 arcs possiblement superposés (Cu) + Warburg.

### 2.5 pH 11 (alcalin) — 2 constantes de temps pour TOUS les métaux

> **Circuit** :  `Rs` → `[ CPE_oxide ‖ R_oxide ]` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification** :
- **Même Au** forme un oxyde/hydroxyde de surface (Au₂O₃) en milieu alcalin (Burke & Nugent, 1997)
- Ni : passivation profonde, film NiO/Ni(OH)₂ épais, R_film très élevé (2 000 Ω)
- Cu : film duplex Cu₂O/CuO/Cu(OH)₂

**Signature Nyquist** : 2 arcs nets pour toutes les compositions + Warburg.

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

## 4. Paramètres physiques

### 4.1 Constantes

| Paramètre | Valeur | Unité |
|-----------|--------|-------|
| F (Faraday) | 96485 | C/mol |
| R (gaz) | 8.314 | J/mol/K |
| T | 298.15 | K |
| n (électrons) | 1 | — |
| A (surface) | 1.77×10⁻⁶ | m² |

### 4.2 Paramètres par métal et pH

Les valeurs ci-dessous sont des **paramètres bibliographiques typiques à l'OCP** (pas dérivés de Butler-Volmer). Les sources détaillées sont dans la page **Données électrochimiques**, section 3.

#### pH 3 (acide, dissolution active, pas de film)

Tous les métaux sont en dissolution active : Rct faible pour Ni et Cu, pas de film passif.

| Métal | Rs (Ω) | Rct (Ω) | Q₀ (µF·s^(n-1)/cm²) | n | σ (Ω·s^(-1/2)) |
|-------|---------|---------|---------------------|---|----------------|
| Au | 40 | 1200 | 30 | 0.94 | 60 |
| Ni | 40 | 700 | 40 | 0.91 | 75 |
| Cu | 40 | 500 | 50 | 0.89 | 90 |

*Sources : Hamelin 1994 (Au Rct), Beverskog 1997 (Ni/Cu Pourbaix).*

#### pH 7 (neutre, film Cu₂O uniquement)

Au reste nu, Ni est instable (pas de film stable — ACS Omega 2016), seul Cu forme un film Cu₂O semi-protecteur.

| Métal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 60 | 5000 | 25 | 0.94 | 45 | 0 | — | — |
| Ni | 60 | 1500 | 35 | 0.90 | 70 | 0 | — | — |
| Cu | 60 | 2000 | 35 | 0.87 | 75 | 400 | 10 | 0.84 |

*Sources : Song 2025 (Au Cdl), JACS 2024 (Cu₂O), ACS Omega 2016 (Ni instabilité).*

#### pH 11 (alcalin, films sur tous les métaux)

Tous les métaux forment un film passif : Au(OH)₃ (léger), Ni(OH)₂/NiOOH (épais, protecteur), Cu₂O/CuO.

| Métal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 10 | 2000 | 35 | 0.92 | 50 | 150 | 10 | 0.90 |
| Ni | 10 | 8000 | 25 | 0.88 | 100 | 2000 | 3 | 0.85 |
| Cu | 10 | 4000 | 30 | 0.85 | 90 | 800 | 7 | 0.82 |

*Sources : Diaz-Morales 2020 (Au oxide), Weininger 1963 (Ni film), Ambrose 1973 (Cu alcalin).*

---

## 5. Lois de mélange

Pour les alliages Au+Ni+Cu, les paramètres effectifs sont calculés par :

| Paramètre | Loi de mélange |
|-----------|---------------|
| Rct | Moyenne pondérée × (1 − 0.04·%Ni/100) |
| Q₀_dl | Q₀_Au × (1 + 0.02·%Ni + 0.03·%Cu) |
| n | n_pondéré − 0.002·%Ni − 0.003·%Cu |
| σ | Moyenne pondérée |
| R_film | Moyenne pondérée |
| E_ocp | Moyenne pondérée (approx. potentiel mixte) |
| Rs | Identique pour tous (propriété de l'électrolyte) |

---

## 6. Complémentarité des études 1 et 2

| | Étude 1 (CV Au/Ni/Cu) | **Étude 2 (EIS Au/Ni/Cu)** |
|---|---|---|
| **Domaine** | Temps | **Fréquence** |
| **Sortie** | I(E), θ(t) | **Z(ω), φ(ω)** |
| **Potentiel** | Balayage ($E_{min}$ → $E_{max}$) | **Fixe ($E_{ocp}$)** |
| **Transport** | Aucun (surface) | **Diffusion 1D (analytique)** |
| **Solver** | numpy ODE | **numpy (algébrique)** |
| **Circuit** | — | **Randles / 2-TC adaptatif** |
| **Diagnostic** | Couverture θ, ΔEp, Ipa/Ipc | **Rct, Cdl, R_film, σ** |

**L'EIS extrait des grandeurs inaccessibles en CV** :
- **Rct** → vitesse de la réaction à l'équilibre
- **Cdl** → structure de l'interface
- **R_film** → épaisseur et compacité du film passif
- **σ** (Warburg) → coefficient de diffusion effectif

---

## 7. Références bibliographiques

| # | Référence | Usage |
|---|-----------|-------|
| [1] | Hamelin *et al.* (1994) — *Electrochim. Acta* — Au/H₂SO₄ | Rct, Cdl Au |
| [2] | Song *et al.* (2025) — *ChemElectroChem* | Cdl vs pH |
| [3] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* 39, 969 | Pourbaix Ni |
| [4] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* | Pourbaix Cu |
| [5] | Diaz-Morales *et al.* (2020) — *ACS Catal.* 10, 7532 | Au oxide OER |
| [6] | ACS Omega (2016) — DOI: 10.1021/acsomega.6b00448 | NiOOH instabilité |
| [8] | Weininger & Breiter (1963) — *Electrochim. Acta* 8, 575 | Ni film EIS |
| [9] | Ambrose *et al.* (1973) — *J. Electroanal. Chem.* 47, 47 | Cu alcalin |
| [11] | Lazanas & Prodromidis (2023) — *ACS Meas. Sci. Au* 3(3), 162 | Tutorial EIS |
| [12] | Gamry Instruments — "Basics of EIS" | Application Note |

*Pour la liste complète : voir Références bibliographiques dans le menu Annexes.*
