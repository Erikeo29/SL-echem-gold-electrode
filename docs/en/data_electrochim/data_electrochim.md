# Electrochemical Data

> All potentials are expressed **vs Ag/AgCl (sat. KCl)** ($E_{\text{Ag/AgCl}} = E_{\text{SHE}} - 0.197$ V).

**Contents:**
1. Fundamental constants
2. Redox potentials and surface kinetics (study 1 — CV)
3. Impedance parameters at OCP (study 2 — EIS)
4. Hypotheses and limitations

---

## 1. Fundamental constants

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Faraday | $F$ | 96,485 | C/mol |
| Gas constant | $R$ | 8.314 | J/(mol·K) |
| Temperature | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |
| Electrode area | $A$ | 1.77×10⁻⁶ | m² |

---

## 2. Redox potentials and surface kinetics (study 1 — CV)

### Redox reactions

> **Au**: $2\text{Au} + 6\text{OH}^- \to \text{Au}_2\text{O}_3 + 3\text{H}_2\text{O} + 6e^-$ — reversible oxide at all pH (β-oxide Au(OH)₃ in alkaline media). Multi-site model (20).

> **Ni**: dissolution $\text{Ni} \to \text{Ni}^{2+} + 2e^-$ at pH < 2; transition Ni(OH)₂ ↔ NiOOH at pH ≥ 7 (partial at pH 7, reversible at pH 13).

> **Cu**: dissolution $\text{Cu} \to \text{Cu}^{2+} + 2e^-$ at pH < 4; sequential Cu₂O then CuO formation at pH ≥ 7.

### Standard potentials by metal and pH

| Metal | pH | Mechanism | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Note |
|-------|:--:|-----------|:--------------:|:---------------:|------|
| Au | 1 | Reversible oxide | 1.10 → 1.50 | 0.90 | Multi-site (20) |
| Ni | 1 | Dissolution | −0.454 | — | Irreversible |
| Cu | 1 | Dissolution | +0.14 | — | Irreversible |
| Au | 7 | Reversible oxide | 0.70 → 1.10 | 0.50 | Multi-site (20) |
| Ni | 7 | Partial oxide | +0.78 | +0.59 | Weak signal, overlaps Au |
| Cu | 7 | Partial oxide | −0.15 / +0.05 | −0.275 | Cu₂O (60%) + CuO (40%) |
| Au | 13 | Reversible oxide | 0.25 → 0.65 | +0.15 | β-oxide Au(OH)₃ |
| Ni | 13 | Reversible oxide | +0.43 | +0.24 | Ni(OH)₂ ↔ NiOOH |
| Cu | 13 | Reversible oxide | −0.38 / +0.08 | −0.76 | Cu₂O (50%) + CuO (50%) |

Potentials follow the Nernst law: $E^0(pH) = E^0_{pH=0} - 0.059 \times pH$. CV scan window: **2.0 V** at each pH, centered between HER and OER walls (see **Physics** tab of the CV study).

### Surface kinetic parameters

| Parameter | Au | Ni | Cu | Unit |
|-----------|:--:|:--:|:--:|------|
| $k_0$ | 2.0 | 5.0 | 5.0 | s⁻¹ (surface reaction) |
| $\Gamma_{max}$ | 4×10⁻⁵ | 3×10⁻⁵ | 3.5×10⁻⁵ | mol/m² |
| $\alpha$ | 0.5 | 0.5 | 0.5 | — |

---

## 3. Impedance parameters at OCP (study 2 — EIS)

EIS is performed at the **open circuit potential** (OCP): the potential where the net current is zero. For alloys: $E_{ocp} \approx \sum x_i \cdot E_{ocp,i}$ (mixed-potential approximation).

| Metal | pH | E_ocp (V) | Rct (Ω) | R_film (Ω) | Circuit | Source |
|-------|:--:|:---------:|:-------:|:----------:|---------|--------|
| Au | 3 | +0.50 | 1,200 | 0 | Randles | Hamelin 1994 |
| Ni | 3 | −0.25 | 700 | 0 | Randles | Beverskog 1997 |
| Cu | 3 | +0.02 | 500 | 0 | Randles | Beverskog 1997 |
| Au | 7 | +0.15 | 5,000 | 0 | Randles | Song 2025 |
| Ni | 7 | −0.20 | 1,500 | 0 ⚠️ | Randles | ACS Omega 2016 |
| Cu | 7 | −0.20 | 2,000 | 400 | 2-TC | JACS 2024 |
| Au | 11 | −0.10 | 2,000 | 150 | 2-TC | Diaz-Morales 2020 |
| Ni | 11 | +0.10 | 8,000 | 2,000 | 2-TC | Weininger 1963 |
| Cu | 11 | −0.40 | 4,000 | 800 | 2-TC | Ambrose 1973 |

⚠️ Ni unstable at pH 7: NiOOH film dissolves slowly (ACS Omega 2016). No R_film.

**Trends**: at pH 3, Ni and Cu dissolve actively (low Rct). At pH 11, all metals passivate; Ni shows the highest R_film (2,000 Ω, compact Ni(OH)₂ film). Gold remains most inert at pH 7 (Rct = 5,000 Ω, no film).

> Full parameters (Q₀, n, σ, mixing laws): see the **Physics** tab of the EIS study.

---

## 4. Hypotheses and limitations

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| Langmuir ($\theta \in [0,1]$) | Localized adsorption | Ignores lateral interactions |
| $E^0_{ox} \neq E^0_{red}$ | Experimental hysteresis | Empirical, not mechanistic |
| Multi-site Au (20) | Oxidation peak broadening | Arbitrary distribution |
| EIS simulated at OCP | Reproducible steady state | No exploration of other potentials |
| OCP by mixed potential | $\sum x_i E_i$ simple | Ignores galvanic coupling |
| Bibliographic Rct | Published typical values | Not derived from Butler-Volmer |
| Ni unstable at pH 7 | Pourbaix + ACS Omega 2016 | Simplified (no transient film) |

**What the models do not capture**: oxide nucleation, surface restructuring, crystalline orientation effects, metal-metal interactions, Rct(E) dependence.

---

*Study 1: parameters_oxide.py — Study 2: parameters_eis.py (04_EIS_with_OCP, 2026-02-06).*
