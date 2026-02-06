**Contents:**
1. Principle and difference with solution-phase CV
2. Physical model
3. Hypotheses and limitations
4. pH dependence
5. Numerical scheme
6. Validation and results

---

## 1. Principle and difference with solution-phase CV

| Aspect | Solution-phase CV | CV metal oxides |
|--------|:---------------------:|:----------------:|
| Redox species | In solution | Adsorbed on surface |
| Transport | Diffusion (2D FEM) | **None** |
| Variable | $c(x,y,t)$ | $\theta(t) \in [0,1]$ |
| Typical ΔEp | ~60 mV (reversible) | **100–2000 mV** |
| Solver | Non-linear Newton | Analytical |

This model handles **surface reactions**: formation and reduction of metal oxides/hydroxides directly on the electrode.

---

## 2. Physical model

### 2.1 Reactions

**Oxide formation** (pH ≥ 7 for Cu, pH ≥ 12 for Ni):

$$M + H_2O \rightleftharpoons MOH + H^+ + e^-$$

where $M$ = Au, Ni, or Cu.

**Dissolution** (acidic pH: Ni at pH < 2, Cu at pH < 4):

$$M \longrightarrow M^{n+} + ne^- \quad \text{(irreversible)}$$

### 2.2 Langmuir-Butler-Volmer kinetics

$$\frac{d\theta}{dt} = k_{ox}(E) \cdot (1 - \theta) - k_{red}(E) \cdot \theta$$

with:
- $k_{ox}(E) = k_0 \exp\left(\alpha f (E - E^0_{ox})\right)$
- $k_{red}(E) = k_0 \exp\left(-(1-\alpha) f (E - E^0_{red})\right)$

**Key point**: $E^0_{ox} \neq E^0_{red}$ to capture the characteristic oxide hysteresis.

### 2.3 Current

$$I = \sum_i f_i \cdot n F A \Gamma_{max,i} \frac{d\theta_i}{dt} + I_{HER} + I_{OER} + I_{C_{dl}}$$

*For values of $E^0$, $k_0$, $\Gamma_{max}$: see the **Electrochemical Data** page.*

---

## 3. Hypotheses and limitations

### What the model captures

| Phenomenon | How |
|------------|-----|
| Oxide hysteresis | $E^0_{ox} \neq E^0_{red}$ (empirical) |
| Au peak broadening | Multi-site model (20 uniform sites) |
| pH effect | Potentials tabulated by pH (1, 7, 13) |
| HER/OER walls | Butler-Volmer at boundaries |
| Double layer | $I_{Cdl} = C_{dl} \cdot A \cdot \nu$ |
| Ni/Cu dissolution in acid | Irreversible Butler-Volmer (no cathodic return) |

### Strong Langmuir model hypotheses

| Hypothesis | Reality | Impact |
|------------|---------|--------|
| Equivalent sites | Surface heterogeneity | Multi-site partially compensates |
| No lateral interactions | Oxides restructure | ΔEp underestimated |
| Localized adsorption | Nucleation and growth | Simplified peak shapes |

### What the model does not capture

- Oxide nucleation and growth (non-Langmuir kinetics)
- Crystalline orientation effects
- Metal-metal interactions in alloys
- Diffusion kinetics within the oxide

### Ni behavior as a function of pH

The nickel mechanism changes with pH:

| pH | Mechanism | Behavior |
|----|-----------|----------|
| 1 | Dissolution | Ni → Ni²⁺ in solution (irreversible) |
| 7 | Partial oxide | Ni(OH)₂/NiOOH weakly visible, overlaps with Au plateau |
| 13 | Reversible oxide | Well-defined Ni(OH)₂/NiOOH couple |

At pH 7, the Ni signal is present but weak because the Ni(OH)₂/NiOOH couple is only partially stable. Potentials are Nernst-shifted (+0.354 V from pH 13 values).

---

## 4. pH dependence

Oxide potentials follow the Nernst law:

$$E^0 = E^0_{pH=0} - 0.059 \times pH$$

Potential windows are adapted per pH to stay in the exploitable zone (between HER and OER).

| pH | Electrolyte | E_min (V) | E_max (V) | Total window (V) |
|:--:|-------------|:---------:|:---------:|:-----------------:|
| 1 | H₂SO₄ | −0.409 | +1.591 | 2.000 |
| 7 | Phosphate buffer | −0.763 | +1.237 | 2.000 |
| 13 | KOH 0.1M | −1.117 | +0.883 | 2.000 |

---

## 5. Numerical scheme

The ODE is **linear in θ** → exact analytical solution:

$$\theta^{n+1} = \frac{\theta^n + \Delta t \cdot k_{ox}}{1 + \Delta t \cdot (k_{ox} + k_{red})}$$

**Properties**:
- Unconditionally stable
- Guarantees $\theta \in [0, 1]$ (with clamping)
- No non-linear solver needed

---

## 6. Validation and results

### Observed behaviors consistent with literature

| Observation | Simulation | Literature | OK |
|-------------|:----------:|:----------:|:--:|
| Au reduction peak (pH 1) | ~0.9 V | 0.85–0.95 V | yes |
| Au reduction peak (pH 13) | ~0.15 V | 0.10–0.20 V | yes |
| Au hysteresis | 200–600 mV | 250–600 mV | yes |
| Ni(OH)₂/NiOOH peak (pH 13) | +0.43/+0.24 V | +0.40–0.50 V | yes |
| Ni weak at pH 7 | Partial signal | Weak signal expected | yes |
| Ni/Cu dissolution (pH 1) | Irreversible | Pourbaix: corrosion | yes |

### Observed limitations

- ΔEp sometimes very high for pure Au (~2000 mV) → HER/OER threshold reached
- Cu at pH 1: dissolution modeled but not corrosion products
- Au β-oxide (pH 13): empirical onset, not mechanistic

---

*Detailed electrochemical parameters are in the **Electrochemical Data** page of the General menu.*

---

## 7. Bibliographical references

*For the complete list of references, see the Bibliographical References section in the Annexes menu.*
