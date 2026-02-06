# Electrochemical Data

**Contents:**
1. Fundamental constants
2. Surface oxides and kinetics (study 1 — CV)
3. Impedance parameters at OCP (study 2 — EIS)
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
| Electrode area | $A$ | 1.77×10⁻⁶ | m² |

---

## 2. Surface oxides and kinetics (study 1 — CV)

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

## 3. Impedance parameters at OCP (study 2 — EIS)

### 3.1 Open circuit potential (OCP)

EIS measurements are performed at the **open circuit potential** (OCP), i.e. the potential at which the net current through the electrode is zero. This potential results from the balance between anodic and cathodic reactions at the surface; it therefore depends on the metal and pH.

The values below are estimated from **Pourbaix diagrams** and published experimental data:

| Metal | pH 3 | pH 7 | pH 11 | Pourbaix domain at OCP | Sources |
|-------|:----:|:----:|:-----:|------------------------|---------|
| **Au** | +0.50 V | +0.15 V | −0.10 V | Capacitive (no oxide) | Hamelin 1994 [1], Song 2025 [2] |
| **Ni** | −0.25 V | −0.20 V | +0.10 V | Corrosion → dissolution → passivation | Beverskog 1997 [3] |
| **Cu** | +0.02 V | −0.20 V | −0.40 V | Cu²⁺ → Cu₂O → Cu₂O/CuO | Beverskog 1997 [4], Ambrose 1973 [9] |

> Potentials **vs Ag/AgCl (sat. KCl)**. For alloys: $E_{ocp} \approx \sum x_i \cdot E_{ocp,i}$ (mixed-potential approximation).

**Interpretation**:
- **Au** is noble: its OCP remains positive in acidic and neutral media, within the capacitive domain (no faradaic reaction). At pH 11, it drops just below the β-oxide Au(OH)₃ formation threshold, hence a passive film appears.
- **Ni** has the most negative OCP at pH 3 (active dissolution Ni → Ni²⁺). In alkaline media, Ni(OH)₂ film formation stabilizes the surface and the OCP rises into the passive zone.
- **Cu** follows the Cu/Cu²⁺ (acidic) → Cu/Cu₂O (neutral/alkaline) transition, consistent with Pourbaix diagrams. At pH 7, the OCP is close to −0.20 V, consistent with Cu₂O stability potential measured by pulsed methods (JACS 2024: −0.27 V).

### 3.2 Charge transfer resistance (Rct)

Rct reflects the speed of the faradaic reaction at OCP. It is related to the exchange current by the linearized Butler-Volmer equation: $R_{ct} = RT/(nFi_0)$. A high Rct indicates a poorly reactive interface (slow kinetics or protective film).

| pH | Au (Ω) | Ni (Ω) | Cu (Ω) | Physical trend |
|:--:|:------:|:------:|:------:|----------------|
| 3 | 1,200 | 700 | 500 | Ni/Cu dissolve actively → low Rct |
| 7 | 5,000 | 1,500 | 2,000 | Au inert → high Rct; Ni unstable without film |
| 11 | 2,000 | 8,000 | 4,000 | Ni: highly protective Ni(OH)₂ film → Rct ×10 |

Sources: Hamelin 1994 [1] (Au/H₂SO₄), Beverskog 1997 [3,4] (Pourbaix Ni/Cu), Weininger 1963 [8] (Ni/NaOH), Ambrose 1973 [9] (Cu alkaline).

> **Validation**: Rct measured experimentally on polycrystalline Au in H₂SO₄ gives 900–1,300 Ω·cm² (Piela & Wrona, *Electrochim. Acta* 1995). For Ni in acidic media, Saleh *et al.* (*Sci. Rep.* 2025) report 900–990 Ω·cm² — our 700 Ω is in the lower range, consistent with a more acidic pH.

### 3.3 Passive film and double-layer capacitance

**R_film** — Zero at pH 3 (no film: active dissolution), it appears as soon as the metal passivates:

| pH | Au | Ni | Cu | Comment |
|:--:|:--:|:--:|:--:|---------|
| 3 | 0 | 0 | 0 | All dissolving, no stable film |
| 7 | 0 | 0 ⚠️ | 400 Ω | ⚠️ Ni unstable at pH 7 (ACS Omega 2016 [6]) |
| 11 | 150 Ω | 2,000 Ω | 800 Ω | Stable films on all metals |

Ni's R_film at pH 11 (2,000 Ω) is the highest, reflecting a compact and protective Ni(OH)₂/NiOOH film — consistent with Weininger & Breiter (1963) measurements on Ni in NaOH.

**Q₀ (CPE)** — Non-ideal double-layer capacitance: 25–50 µF·s^(n-1)/cm² with exponent $n \approx 0.85$–$0.94$. These values are typical for polycrystalline electrodes (Lazanas 2023 [11]). The exponent $n$ decreases with increasing Ni and Cu content in the alloy (more heterogeneous surface).

> Full parameters (Q₀, n, σ, Q_film, n_film) and alloy mixing laws are detailed in the **Physics** tab of the EIS study.

### EIS references

| # | Reference | Data used |
|---|-----------|-----------|
| [1] | Hamelin *et al.* (1994) — *Electrochim. Acta* — Au in H₂SO₄ | Rct Au pH 3, Cdl Au |
| [2] | Song *et al.* (2025) — *ChemElectroChem* | Cdl vs pH for Au |
| [3] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* 39, 969 | Pourbaix Ni, OCP Ni |
| [4] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* | Pourbaix Cu, OCP Cu |
| [6] | ACS Omega (2016) — DOI: 10.1021/acsomega.6b00448 | NiOOH instability at pH 7 |
| [8] | Weininger & Breiter (1963) — *Electrochim. Acta* 8, 575 | Rct Ni, R_film Ni pH 11 |
| [9] | Ambrose *et al.* (1973) — *J. Electroanal. Chem.* 47, 47 | R_film Cu alkaline |
| [11] | Lazanas & Prodromidis (2023) — *ACS Meas. Sci. Au* 3(3), 162 | CPE, typical ranges |

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

### Study 1 — surface oxide CV

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| **Langmuir model** | Localized adsorption, $\theta \in [0,1]$ | Ignores lateral interactions |
| $E^0_{ox} \neq E^0_{red}$ | Observed experimental hysteresis | Empirical, not mechanistic |
| Multi-site (Au) | Broadening of oxidation peak | Arbitrary distribution (20 sites) |
| Ni partial at pH 7 | Ni(OH)₂/NiOOH visible but weak | Signal overlaps with Au plateau |
| Ni/Cu dissolution at pH < 2 | Pourbaix diagram | No cathodic return |

### Study 2 — EIS at OCP

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| **Simulation at OCP** | Reproducible steady state | No exploration of other potentials |
| **OCP by mixed potential** | $E_{ocp} = \sum x_i E_{ocp,i}$ | Ignores galvanic interactions |
| **Bibliographic Rct** | Published typical values | Not derived from Butler-Volmer |
| **CPE instead of pure C** | Real rough surfaces | n empirical, not linked to geometry |
| **Ni unstable at pH 7** | ACS Omega 2016, Pourbaix | Simplified (no transient film) |

### What the models **do not capture**

- Oxide nucleation and growth
- Surface restructuring
- Grain and crystalline orientation effects
- Diffusion kinetics within the oxide
- Metal-metal interactions in alloys (galvanic coupling)
- Potential dependence of EIS parameters (Rct varies with E)

---

*Study 1: parameters_oxide.py — Study 2: parameters_eis.py (run 04_EIS_with_OCP, 2026-02-06).*
