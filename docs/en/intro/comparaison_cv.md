# Study comparison

**Contents:**
1. Summary table
2. Fundamental differences
3. Complementarity

---

## 1. Summary table

| Criterion | Study 1: CV redox couple on Au | Study 2: EIS redox couple on Au | Study 3: CV Au/Ni/Cu electrode | Study 4: EIS Au/Ni/Cu electrode |
| :--- | :--- | :--- | :--- | :--- |
| **Domain** | Time | **Frequency** | Time | **Frequency** |
| **Redox species** | In solution ($Fe(CN)_6^{3-/4-}$) | In solution ($Fe(CN)_6^{3-/4-}$) | On surface (MOH oxides) | Surface + solution |
| **Transport** | Diffusion (Fick's law) | 1D diffusion (Warburg) | None (surface ODE) | 1D diffusion (Warburg) |
| **Variable** | $c(x,y,t)$ concentration | $Z(\omega)$ complex impedance | $\theta(t)$ coverage [0,1] | $Z(\omega)$ complex impedance |
| **Solver** | Firedrake + Newton (2D FEM) | numpy (algebraic) | Analytical implicit Euler | numpy (algebraic) |
| **Kinetics** | Classical Butler-Volmer | Randles circuit + CPE | Langmuir + BV + hysteresis | Adaptive equivalent circuit |
| **Output** | I(E) voltammogram | Nyquist + Bode | I(E) voltammogram | Nyquist + Bode |
| **Studied parameters** | $k^0$, $\alpha$, $\nu$ | $n$, $k^0$, $D$, $c$, $Q_0$ | pH, %Ni, %Cu, $C_{dl}$ | pH, %Ni, %Cu |
| **Key metrics** | Ipa, Ipc, ΔEp, ratio | Rct, σ, Cdl, ω_max | Ipa, Ipc, ΔEp | Rct, Cdl, R_film, phase_max |
| **Dependencies** | Firedrake, GMSH, scipy | numpy, matplotlib | numpy, matplotlib | numpy, matplotlib |

---

## 2. Fundamental differences

### Transport vs. adsorption vs. impedance

Study 1 solves a spatio-temporal diffusion problem: concentration evolves in space (diffusion layer) and time. Peak current follows the Randles-Ševčík equation: $I_p \propto \sqrt{\nu}$.

Study 2 probes the same redox couple but in the frequency domain. It extracts $R_{ct}$ (inversely proportional to $k^0$) and $\sigma$ (related to $D$), quantities inaccessible through CV.

Study 3 models purely surface reactions: coverage $\theta$ is uniform across the electrode. Current depends on $d\theta/dt$ and hysteresis ($E^0_{ox} \neq E^0_{red}$) captures oxide nucleation.

Study 4 probes the same Au/Ni/Cu electrode at **equilibrium** via a frequency perturbation. It separates resistive contributions (Rs, Rct, R_film) from capacitive ones (Cdl, CPE) — a decomposition impossible through CV.

### Reversibility

- Study 1: the system can be reversible ($\Delta E_p \approx 59$ mV) if $k^0$ is large enough.
- Study 2: reversibility is read from the Nyquist arc diameter (low $R_{ct}$ = fast reaction).
- Study 3: oxide hysteresis always imposes $\Delta E_p > 100$ mV.
- Study 4: no ΔEp concept — reversibility is read from $R_{ct}$ and passive film presence.

---

## 3. Complementarity

These four studies cover the main families of electrochemical characterization:
- **Diffusion-controlled process** (Study 1): reversibility diagnosis, effect of $\nu$
- **Frequency analysis of a redox couple** (Study 2): influence of $k^0$, $D$, $c$ on impedance
- **Surface process** (Study 3): multi-metallic electrode characterization, pH effect
- **Frequency analysis of a multi-metallic electrode** (Study 4): separation of resistive/capacitive contributions, passive film detection

EIS extracts quantities inaccessible through CV: **Rct** (charge transfer resistance), **Cdl** (double layer capacitance), **R_film** (passive film resistance) and **σ** (Warburg coefficient).
