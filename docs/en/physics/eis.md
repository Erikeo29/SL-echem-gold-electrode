**Contents:**
1. EIS Principle
2. Equivalent Circuits
3. Impedance Elements
4. Physical Parameters
5. Bibliographical References

---

## 1. EIS Principle

### 1.1 Perturbation and Response

Unlike Study 1 (surface oxide CV) which operates in the **time domain** (potential sweep → current I(E)), EIS (Study 2) works in the **frequency domain**. A small sinusoidal potential perturbation is superimposed on the DC potential:

$$E(t) = E_{ocp} + \Delta E \cdot \sin(\omega t)$$

where:
- $E_{ocp}$ = open circuit potential [V vs Ag/AgCl] — the potential at which the net current is zero. OCP values per metal and pH are documented in the **Electrochemical Data** page.
- $\Delta E$ = perturbation amplitude (10 mV, linear regime)
- $\omega = 2\pi f$ = angular frequency [rad/s]

The current response is phase-shifted:

$$I(t) = I_0 + \Delta I \cdot \sin(\omega t + \varphi)$$

where:
- $I_0$ = steady-state DC current [A] (= 0 at OCP by definition)
- $\Delta I$ = current response amplitude [A]
- $\varphi$ = phase shift between potential and current [rad]

### 1.2 Complex Impedance

The electrochemical impedance is defined as:

$$Z(\omega) = \frac{\Delta E}{\Delta I} \cdot e^{j\varphi} = Z'(\omega) + j Z''(\omega)$$

where:
- $Z'(\omega)$ = real part of impedance [Ω]
- $Z''(\omega)$ = imaginary part of impedance [Ω]
- $j$ = imaginary number ($\sqrt{-1}$)

The frequency sweep covers:

$$f \in [0.01 \text{ Hz}, 100 \text{ kHz}]$$, logarithmic spacing, 10 points/decade → 70 points

### 1.3 Graphical Representations

| Diagram | Axes | Information |
|---------|------|-------------|
| **Nyquist** | $-\text{Im}(Z)$ vs $\text{Re}(Z)$ | Arc shapes → mechanisms |
| **Bode magnitude** | $\log|Z|$ vs $\log(f)$ | Limiting resistances |
| **Bode phase** | $-\varphi$ vs $\log(f)$ | Time constants |

---

## 2. Equivalent Circuits

### 2.1 Adaptive Circuit Selection

The model automatically selects the circuit based on pH and composition, as surface chemistry changes dramatically with the medium. The criterion is simple: if $R_{film} > 0$, the 2 time-constant (2-TC) circuit is used; otherwise, a Randles circuit.

### 2.2 Oxide Formation

The nature of the passive film depends on the metal and pH. Detailed redox equations (Au₂O₃, Ni(OH)₂/NiOOH, Cu₂O/CuO) and associated potentials are presented in the **Electrochemical Data** page.

### 2.3 Circuits by pH

| | **pH 3** (acidic) | **pH 7** (neutral) | **pH 11** (alkaline) |
|---|---|---|---|
| **Name** | Simple Randles | Variable circuit | 2 time constants (all metals) |
| **Circuit** | `Rs → [CPE_dl ‖ (Rct + Z_W)]` | Au, Ni: Randles; Cu: `Rs → [CPE_film ‖ R_film] → [CPE_dl ‖ (Rct + Z_W)]` | `Rs → [CPE_oxide ‖ R_oxide] → [CPE_dl ‖ (Rct + Z_W)]` |
| **Justification** | Au bare; Ni/Cu active dissolution (no passivation < pH 5) | Au bare; ⚠️ Ni unstable — NiOOH dissolves (ACS Omega 2016); Cu: semi-protective Cu₂O (R_film = 400 Ω) | All passivated: Au(OH)₃ (Burke 1997), Ni(OH)₂/NiOOH (R_film = 2,000 Ω), Cu₂O/CuO |
| **Nyquist signature** | 1 semicircle + 45° Warburg | 1 arc (Au, Ni) or 2 overlapping arcs (Cu) + Warburg | 2 clear arcs + Warburg |

---

## 3. Impedance Elements

| Element | Impedance | Parameters | Physical role |
|---------|-----------|------------|---------------|
| Resistance | $Z_R = R$ | R (Ω) | Solution, charge transfer, film |
| Capacitance | $Z_C = \frac{1}{j\omega C}$ | C (F) | Ideal double layer |
| CPE | $Z_{CPE} = \frac{1}{Q_0 (j\omega)^n}$ | Q₀ (F·s^(n-1)), n ∈ [0,1] | Non-ideal double layer |
| Warburg | $Z_W = \frac{\sigma}{\sqrt{\omega}}(1 - j)$ | σ (Ω·s^(-1/2)) | Semi-infinite diffusion |

### CPE vs Pure Capacitance

The CPE (Constant Phase Element) replaces the ideal capacitance to model real surfaces:
- $n = 1$ → pure capacitance
- $n = 0.8\text{–}0.95$ → rough, heterogeneous surface
- $n < 0.8$ → distribution of time constants, highly disordered surface

### Randles Circuit

$$Z(\omega) = R_s + \frac{1}{\frac{1}{Z_{CPE}} + \frac{1}{R_{ct} + Z_W}}$$

### 2 Time-Constant Circuit

$$Z(\omega) = R_s + Z_{film\parallel} + Z_{dl\parallel}$$

with $Z_{film\parallel} = \frac{R_{film} \cdot Z_{CPE,film}}{R_{film} + Z_{CPE,film}}$ and $Z_{dl\parallel} = \frac{(R_{ct} + Z_W) \cdot Z_{CPE,dl}}{(R_{ct} + Z_W) + Z_{CPE,dl}}$

---

## 4. Physical Parameters

### 4.1 Constants

| Parameter | Value | Unit |
|-----------|-------|------|
| F (Faraday) | 96485 | C/mol |
| R (gas) | 8.314 | J/mol/K |
| T | 298.15 | K |
| n (electrons) | 1 | — |
| A (area) | 1.77×10⁻⁶ | m² |

### 4.2 Parameters by metal and pH

The values below are **typical bibliographic parameters at OCP** (not derived from Butler-Volmer). Detailed sources are in the **Electrochemical Data** page, section 3.

#### pH 3 (acidic, active dissolution, no film)

All metals are in active dissolution: low Rct for Ni and Cu, no passive film.

| Metal | Rs (Ω) | Rct (Ω) | Q₀ (µF·s^(n-1)/cm²) | n | σ (Ω·s^(-1/2)) |
|-------|---------|---------|---------------------|---|----------------|
| Au | 40 | 1200 | 30 | 0.94 | 60 |
| Ni | 40 | 700 | 40 | 0.91 | 75 |
| Cu | 40 | 500 | 50 | 0.89 | 90 |

*Sources: Hamelin 1994 (Au Rct), Beverskog 1997 (Ni/Cu Pourbaix).*

#### pH 7 (neutral, Cu₂O film only)

Au remains bare, Ni is unstable (no stable film — ACS Omega 2016), only Cu forms a semi-protective Cu₂O film.

| Metal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 60 | 5000 | 25 | 0.94 | 45 | 0 | — | — |
| Ni | 60 | 1500 | 35 | 0.90 | 70 | 0 | — | — |
| Cu | 60 | 2000 | 35 | 0.87 | 75 | 400 | 10 | 0.84 |

*Sources: Song 2025 (Au Cdl), JACS 2024 (Cu₂O), ACS Omega 2016 (Ni instability).*

#### pH 11 (alkaline, films on all metals)

All metals form a passive film: Au(OH)₃ (thin), Ni(OH)₂/NiOOH (thick, protective), Cu₂O/CuO.

| Metal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 10 | 2000 | 35 | 0.92 | 50 | 150 | 10 | 0.90 |
| Ni | 10 | 8000 | 25 | 0.88 | 100 | 2000 | 3 | 0.85 |
| Cu | 10 | 4000 | 30 | 0.85 | 90 | 800 | 7 | 0.82 |

*Sources: Diaz-Morales 2020 (Au oxide), Weininger 1963 (Ni film), Ambrose 1973 (Cu alkaline).*

---

## 5. Bibliographical References

| # | Reference | Usage |
|---|-----------|-------|
| [1] | Hamelin *et al.* (1994) — *Electrochim. Acta* — Au/H₂SO₄ | Rct, Cdl Au |
| [2] | Song *et al.* (2025) — *ChemElectroChem* | Cdl vs pH |
| [3] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* 39, 969 | Pourbaix Ni |
| [4] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* | Pourbaix Cu |
| [5] | Diaz-Morales *et al.* (2020) — *ACS Catal.* 10, 7532 | Au oxide OER |
| [6] | ACS Omega (2016) — DOI: 10.1021/acsomega.6b00448 | NiOOH instability |
| [8] | Weininger & Breiter (1963) — *Electrochim. Acta* 8, 575 | Ni film EIS |
| [9] | Ambrose *et al.* (1973) — *J. Electroanal. Chem.* 47, 47 | Cu alkaline |
| [11] | Lazanas & Prodromidis (2023) — *ACS Meas. Sci. Au* 3(3), 162 | EIS Tutorial |
| [12] | Gamry Instruments — "Basics of EIS" | Application Note |

*For the complete list, see Bibliographical References in the Appendices menu.*
