# Study comparison

**Contents:**
1. Summary table
2. Fundamental differences
3. Complementarity

---

## 1. Summary table

| Criterion | Study 1: CV Au/Ni/Cu electrode | Study 2: EIS Au/Ni/Cu electrode |
| :--- | :--- | :--- |
| **Domain** | Time | **Frequency** |
| **Redox species** | On surface (MOH oxides) | Surface + solution |
| **Transport** | None (surface ODE) | 1D diffusion (Warburg) |
| **Variable** | $\theta(t)$ coverage [0,1] | $Z(\omega)$ complex impedance |
| **Solver** | Analytical implicit Euler | numpy (algebraic) |
| **Kinetics** | Langmuir + BV + hysteresis | Adaptive equivalent circuit |
| **Output** | I(E) voltammogram | Nyquist + Bode |
| **Studied parameters** | pH, %Ni, %Cu, $C_{dl}$ | pH, %Ni, %Cu |
| **Key metrics** | Ipa, Ipc, ΔEp | Rct, Cdl, R_film, phase_max |
| **Dependencies** | numpy, matplotlib | numpy, matplotlib |

---

## 2. Fundamental differences

### Adsorption vs. impedance

Study 1 models purely surface reactions: coverage $\theta$ is uniform across the electrode. Current depends on $d\theta/dt$ and hysteresis ($E^0_{ox} \neq E^0_{red}$) captures oxide nucleation.

Study 2 probes the same Au/Ni/Cu electrode at **equilibrium** via a frequency perturbation. It separates resistive contributions (Rs, Rct, R_film) from capacitive ones (Cdl, CPE) — a decomposition impossible through CV.

### Reversibility

- Study 1: oxide hysteresis always imposes $\Delta E_p > 100$ mV.
- Study 2: no ΔEp concept — reversibility is read from $R_{ct}$ and passive film presence.

---

## 3. Complementarity

These two studies cover the two complementary approaches for characterizing the Au/Ni/Cu electrode:
- **Surface process** (Study 1): multi-metallic electrode characterization, pH effect
- **Frequency analysis of a multi-metallic electrode** (Study 2): separation of resistive/capacitive contributions, passive film detection

EIS extracts quantities inaccessible through CV: **Rct** (charge transfer resistance), **Cdl** (double layer capacitance) and **R_film** (passive film resistance).
