**Contents:**
1. EIS Principle
2. Equivalent Circuits
3. Impedance Elements
4. Physical Parameters
5. Mixing Laws
6. Complementarity with Studies 1 and 2
7. Bibliographical References

---

## 1. EIS Principle

### 1.1 Perturbation and Response

Unlike Studies 1 and 2 which operate in the **time domain** (potential sweep → current I(E)), EIS works in the **frequency domain**. A small sinusoidal potential perturbation is superimposed on the DC potential:

$$E(t) = E_0 + \Delta E \cdot \sin(\omega t)$$

where:
- $E_0$ = steady-state DC potential [V]
- $\Delta E$ = perturbation amplitude (10 mV, linear regime)
- $\omega = 2\pi f$ = angular frequency [rad/s]

The current response is phase-shifted:

$$I(t) = I_0 + \Delta I \cdot \sin(\omega t + \varphi)$$

where:
- $I_0$ = steady-state DC current [A]
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

The model automatically selects the circuit based on pH and composition, as surface chemistry changes dramatically with the medium.

### 2.2 Oxide Formation

The nature of the passive film depends on the metal and pH. Detailed redox equations (Au₂O₃, Ni(OH)₂/NiOOH, Cu₂O/CuO) and associated potentials are presented in the **Electrochemical Data** page.

### 2.3 pH 3 (acidic) — Simple Randles

> **Circuit**:  `Rs` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification**:
- Au remains bare (no oxide below ~1.2 V vs. RHE)
- Ni and Cu dissolve actively (no stable passivation below pH 5)
- **Single time constant**: the electrical double layer

**Nyquist signature**: 1 semicircle + 45° Warburg line.

### 2.4 pH 7 (neutral) — 2 Time Constants for Au+Ni/Cu

> **Circuit**:  `Rs` → `[ CPE_film ‖ R_film ]` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification**:
- Au remains bare at pH 7 (simple Randles circuit)
- Ni passivated: duplex film NiO / Ni(OH)₂ → introduces R_film + CPE_film
- Cu forms Cu₂O → semi-protective film

**Nyquist signature**: 2 arcs (possibly overlapping) + Warburg.

### 2.5 pH 11 (alkaline) — 2 Time Constants for ALL metals

> **Circuit**:  `Rs` → `[ CPE_oxide ‖ R_oxide ]` → `[ CPE_dl ‖ ( Rct + Z_W ) ]`

**Justification**:
- **Even Au** forms a surface oxide/hydroxide (Au₂O₃) in alkaline media (Burke & Nugent, 1997)
- Ni: deep passivation, thick NiO/Ni(OH)₂ film, very high R_film
- Cu: duplex film Cu₂O/CuO/Cu(OH)₂

**Nyquist signature**: 2 clear arcs for all compositions + Warburg.

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

---

## 4. Physical Parameters

### Constants

| Parameter | Value | Unit |
|-----------|-------|------|
| F (Faraday) | 96485 | C/mol |
| R (gas) | 8.314 | J/mol/K |
| T | 298.15 | K |
| n (electrons) | 1 | — |
| A (area) | 1.77×10⁻⁶ | m² |

### Parameters by metal and pH

#### pH 3 (acidic, active dissolution, no film)

| Metal | Rs (Ω) | Rct (Ω) | Q₀ (µF·s^(n-1)/cm²) | n | σ (Ω·s^(-1/2)) |
|-------|---------|---------|---------------------|---|----------------|
| Au | 40 | 1200 | 30 | 0.94 | 60 |
| Ni | 40 | 700 | 40 | 0.91 | 75 |
| Cu | 40 | 500 | 50 | 0.89 | 90 |

#### pH 7 (neutral, passive films on Ni/Cu)

| Metal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 60 | 5000 | 25 | 0.94 | 45 | 0 | — | — |
| Ni | 60 | 3000 | 30 | 0.90 | 60 | 800 | 5 | 0.87 |
| Cu | 60 | 2000 | 35 | 0.87 | 75 | 400 | 10 | 0.84 |

#### pH 11 (alkaline, films on all metals)

| Metal | Rs (Ω) | Rct (Ω) | Q₀ | n | σ | R_film (Ω) | Q_film | n_film |
|-------|---------|---------|-----|---|---|-----------|--------|--------|
| Au | 10 | 2000 | 35 | 0.92 | 50 | 150 | 10 | 0.90 |
| Ni | 10 | 8000 | 25 | 0.88 | 100 | 2000 | 3 | 0.85 |
| Cu | 10 | 4000 | 30 | 0.85 | 90 | 800 | 7 | 0.82 |

---

## 5. Mixing Laws

For Au+Ni+Cu alloys, effective parameters are computed by:

| Parameter | Mixing law |
|-----------|-----------|
| Rct | Weighted average × (1 − 0.04·%Ni/100) |
| Q₀_dl | Q₀_Au × (1 + 0.02·%Ni + 0.03·%Cu) |
| n | n_weighted − 0.002·%Ni − 0.003·%Cu |
| σ | Weighted average |
| R_film | Weighted average |
| Rs | Same for all (electrolyte property) |

---

## 6. Complementarity of Studies 1 and 2

| | Study 1 (CV Au/Ni/Cu) | **Study 2 (EIS Au/Ni/Cu)** |
|---|---|---|
| **Domain** | Time | **Frequency** |
| **Output** | I(E), θ(t) | **Z(ω), φ(ω)** |
| **Transport** | None (surface) | **1D diffusion (analytical)** |
| **Solver** | numpy ODE | **numpy (algebraic)** |
| **Circuit** | — | **Randles / 2-TC adaptive** |
| **Diagnostics** | Coverage θ, ΔEp, Ipa/Ipc | **Rct, Cdl, R_film, σ** |

**EIS extracts quantities inaccessible through CV**:
- **Rct** → reaction rate at equilibrium
- **Cdl** → interface structure
- **R_film** → passive film thickness and compactness
- **σ** (Warburg) → effective diffusion coefficient

---

## 7. Bibliographical References

*Note: For the complete list of references, see the Bibliographical References section in the Annexes menu.*
