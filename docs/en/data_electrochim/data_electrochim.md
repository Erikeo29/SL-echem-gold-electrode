# Electrochemical Data

**Contents:**
1. Fundamental constants
2. Ferro/ferricyanide couple (studies 1 & 2)
3. Metal oxides (studies 3 & 4)
4. Electrochemical walls (HER/OER)
5. Model hypotheses and limitations

---

## 1. Fundamental constants

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Faraday constant | $F$ | 96,485 | C/mol |
| Gas constant | $R$ | 8.314 | J/(mol·K) |
| Standard temperature | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |

---

## 2. Ferro/ferricyanide couple (studies 1 & 2)

### Electrochemical reaction

$$\text{Fe(CN)}_6^{3-} + e^- \rightleftharpoons \text{Fe(CN)}_6^{4-}$$

### Kinetic parameters

| Parameter | Symbol | Value | Unit | Note |
|-----------|--------|-------|------|------|
| Standard potential | $E^0$ | **+0.36** | V vs Ag/AgCl | Reversible |
| Rate constant | $k^0$ | 1×10⁻⁵ | m/s | Quasi-reversible |
| Transfer coefficient | $\alpha$ | 0.5 | — | Symmetric |
| Electron number | $n$ | 1 | — | — |
| Diffusion coefficient | $D$ | 7.6×10⁻¹⁰ | m²/s | Same for ox/red |

### Butler-Volmer equation

$$i = i_0 \left[ \exp\left(\alpha f \eta\right) - \exp\left(-(1-\alpha) f \eta\right) \right]$$

where $\eta = E - E^0$ is the overpotential and $i_0 = nFAk^0 c$ the exchange current.

---

## 3. Metal oxides (studies 3 & 4)

### Oxide formation redox equations

The nature of the passive film depends on the metal and pH. Here are the anodic oxidation half-reactions in aqueous media.

> **Note**: all potentials are expressed **vs Ag/AgCl (sat. KCl)** ($E_{\text{Ag/AgCl}} = E_{\text{SHE}} - 0.197$ V).

#### Gold (Au) — multi-site oxidation

$$2\text{Au} + 6\text{OH}^- \longrightarrow \text{Au}_2\text{O}_3 + 3\text{H}_2\text{O} + 6e^-$$

Gold forms a reversible oxide at all pH values. In alkaline media, the hydroxide form Au(OH)₃ (β-oxide) is preferentially formed. The oxidation plateau is modeled with 20 uniform sites.

#### Nickel (Ni) — pH-dependent behavior

**Dissolution in acidic media** (pH < 2):

$$\text{Ni} \longrightarrow \text{Ni}^{2+} + 2e^- \quad (E^0 = -0.454 \text{ V vs Ag/AgCl})$$

**Ni(II) → Ni(III) transition** (pH ≥ 7, CV-active couple):

$$\text{Ni(OH)}_2 + \text{OH}^- \longrightarrow \text{NiOOH} + \text{H}_2\text{O} + e^-$$

This couple is reversible at pH 13 and partially visible at pH 7 (weak signal, overlaps with Au plateau).

#### Copper (Cu) — sequential oxidation

**Dissolution in acidic media** (pH < 4):

$$\text{Cu} \longrightarrow \text{Cu}^{2+} + 2e^- \quad (E^0 = +0.14 \text{ V vs Ag/AgCl})$$

**First oxidation** — Cu₂O formation (pH ≥ 7):

$$2\text{Cu} + 2\text{OH}^- \longrightarrow \text{Cu}_2\text{O} + \text{H}_2\text{O} + 2e^-$$

**Second oxidation** — CuO formation:

$$\text{Cu}_2\text{O} + 2\text{OH}^- \longrightarrow 2\text{CuO} + \text{H}_2\text{O} + 2e^-$$

### Surface reaction (Langmuir model)

$$M + H_2O \rightleftharpoons MOH + H^+ + e^-$$

where $M$ = Au, Ni, or Cu.

### Standard potentials — pH 1 (H₂SO₄)

| Metal | Mechanism | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | $\Delta E_{hyst}$ (mV) |
|-------|-----------|:--------------:|:---------------:|:----------------------:|
| **Au** | Reversible oxide | 1.10 → 1.50 | 0.90 | 200–600 |
| **Ni** | Dissolution | −0.454 | — | — |
| **Cu** | Dissolution | +0.14 | — | — |

### Standard potentials — pH 7 (phosphate buffer)

| Metal | Mechanism | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Note |
|-------|-----------|:--------------:|:---------------:|------|
| **Au** | Reversible oxide | 0.70 → 1.10 | 0.50 | Multi-site (20) |
| **Ni** | Partial oxide | +0.78 | +0.59 | Ni(OH)₂/NiOOH, Nernst from pH 13 |
| **Cu** | Partial oxide | −0.15 / +0.05 | −0.275 | Cu₂O (60%) + CuO (40%) |

### Standard potentials — pH 13 (KOH 0.1M)

| Metal | Mechanism | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Note |
|-------|-----------|:--------------:|:---------------:|------|
| **Au** | Reversible oxide | 0.25 → 0.65 | +0.15 | β-oxide Au(OH)₃, multi-site (20) |
| **Ni** | Reversible oxide | +0.43 | +0.24 | Ni(OH)₂ ↔ NiOOH |
| **Cu** | Reversible oxide | −0.38 / +0.08 | −0.76 | Cu₂O (50%) + CuO (50%) |

### Surface kinetic parameters

| Parameter | Au | Ni | Cu | Unit |
|-----------|:--:|:--:|:--:|------|
| $k_0$ | 2.0 | 5.0 | 5.0 | s⁻¹ |
| $\Gamma_{max}$ | 4×10⁻⁵ | 3×10⁻⁵ | 3.5×10⁻⁵ | mol/m² |
| $\alpha$ | 0.5 | 0.5 | 0.5 | — |

**Note**: $k_0$ is in **s⁻¹** (surface reaction), not m/s!

---

## 4. Electrochemical walls (HER/OER)

### Reactions

| Reaction | Equation | $E^0$ (V vs SHE) |
|----------|----------|------------------|
| **HER** (cathodic) | $2H^+ + 2e^- \to H_2$ | 0.00 |
| **OER** (anodic) | $2H_2O \to O_2 + 4H^+ + 4e^-$ | +1.23 |

### Practical onset potentials (vs Ag/AgCl sat.)

The model uses empirical onset potentials (including overpotential):

$$E_{HER}(pH) = -0.10 - 0.059 \times pH \text{ V}$$
$$E_{OER}(pH) = +1.50 - 0.059 \times pH \text{ V}$$

| pH | $E_{HER}$ (V) | $E_{OER}$ (V) | Window (V) |
|:--:|:-------------:|:-------------:|:----------:|
| 1.0 | −0.159 | +1.441 | 1.600 |
| 7.0 | −0.513 | +1.087 | 1.600 |
| 13.0 | −0.867 | +0.733 | 1.600 |

---

## 5. Model hypotheses and limitations

### Studies 1 & 2 — Solution redox couple

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| 1D semi-infinite diffusion | Planar electrode, quiescent solution | Ignores natural convection |
| Excess species | Supporting electrolyte >> active species | No migration |
| $D_{ox} = D_{red}$ | Simplification | May affect $\Delta E_p$ |

### Studies 3 & 4 — Surface oxides

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| **Langmuir model** | Localized adsorption, $\theta \in [0,1]$ | Ignores lateral interactions |
| $E^0_{ox} \neq E^0_{red}$ | Observed experimental hysteresis | Empirical, not mechanistic |
| Multi-site (Au) | Broadening of oxidation peak | Arbitrary distribution (20 sites) |
| Ni partial at pH 7 | Ni(OH)₂/NiOOH visible but weak | Signal overlaps with Au plateau |
| Ni/Cu dissolution at pH < 2 | Pourbaix diagram | No cathodic return |

### What the model **does not capture**

- Oxide nucleation and growth
- Surface restructuring
- Grain and crystalline orientation effects
- Diffusion kinetics within the oxide
- Metal-metal interactions in alloys

---

*These data come from parameters_oxide.py (run 07, 2026-02-05) — single source of truth.*
