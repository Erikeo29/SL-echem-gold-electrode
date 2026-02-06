# Key Equations

**Contents:**
1. Mass Transport
2. Electrode Kinetics (Butler-Volmer)
3. Potential Signal (Cycles)
4. Morphological Analysis
5. Diagnostics: Reversibility and Scan Rate
6. Electrochemical Impedance Spectroscopy (EIS)
7. Bibliographical References

---

Modeling cyclic voltammetry relies on solving mass transport of electroactive species coupled with charge transfer kinetics at the electrode/electrolyte interface.

## 1. Mass Transport

In an excess supporting electrolyte, migration is neglected. Transport is governed by Fick's diffusion law:

$$ \frac{\partial c_i}{\partial t} = D_i \nabla^2 c_i $$

Where:
- $c_i$ is the concentration of species $i$ (Oxidant $O$ or Reductant $R$) [mol/m³]
- $D_i$ is the diffusion coefficient [m²/s]

## 2. Electrode Kinetics (Butler-Volmer)

The molar flux at the Working Electrode (WE) surface is defined by the Butler-Volmer relation:

$$ J = k^0 \left[ c_R \exp\left(\frac{\alpha n F}{RT} \eta\right) - c_O \exp\left(-\frac{(1-\alpha) n F}{RT} \eta\right) \right] $$

Where:
- $J$ = molar flux at the surface [mol/(m²·s)]
- $k^0$ = standard rate constant [m/s]
- $c_R$ = reductant concentration at the surface [mol/m³]
- $c_O$ = oxidant concentration at the surface [mol/m³]
- $\alpha$ = charge transfer coefficient (dimensionless)
- $n$ = number of electrons transferred
- $F$ = Faraday constant (96485 C/mol)
- $R$ = universal gas constant (8.314 J/(mol·K))
- $T$ = temperature [K]
- $\eta = E(t) - E^0$ = activation overpotential [V]

### Simulation Parameters

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Faraday Constant | $F$ | 96485 C/mol |
| Gas Constant | $R$ | 8.314 J/(mol·K) |
| Temperature | $T$ | 298.15 K |
| Transfer Coefficient | $\alpha$ | 0.5 |
| Standard Reaction Rate | $k^0$ | ~10⁻⁵ m/s |

## 3. Potential Signal (Cycles)

The applied potential $E(t)$ follows a periodic triangular waveform:

$$ E(t) = \begin{cases} E_{start} + v \cdot t & \text{Forward (Anodic)} \\ E_{vertex} - v \cdot t & \text{Reverse (Cathodic)} \end{cases} $$

Where:
- $E_{start}$ = initial potential [V]
- $E_{vertex}$ = vertex (switching) potential [V]
- $v$ = scan rate [V/s]
- $t$ = time [s]

Recording multiple cycles helps verify system stability (electrode conditioning) or observe secondary reactions (adsorption, passivation).

## 4. Morphological Analysis: Origin of the Shape

The characteristic "duck-shaped" voltammogram results from a competition between two opposing phenomena:

1. **Current Rise (Kinetic Control)**: The increasing potential ($\eta$) exponentially accelerates the electron transfer rate (Butler-Volmer law).

2. **Peak and Decay (Diffusion Control)**: As the reactant at the surface is consumed, its local concentration drops to zero (depletion). A **diffusion layer** creates, with thickness $\delta(t)$ increasing over time ($\delta \propto \sqrt{Dt}$).

## 5. Diagnostics: Reversibility and Scan Rate

### 5.1 Peak Separation ($\Delta E_p$)

This is the potential difference between anodic and cathodic peaks: $\Delta E_p = |E_{pa} - E_{pc}|$.

| System Type | Characteristic |
|-------------|----------------|
| **Reversible (Fast)** | $\Delta E_p \approx 59/n$ mV (constant) |
| **Quasi-Reversible** | $\Delta E_p$ increases with $v$ |
| **Irreversible (Slow)** | Peaks widely separated |

### 5.2 Influence of Scan Rate ($v$)

For a reversible system, the peak current follows the **Randles-Sevcik** equation:

$$ I_p = (2.69 \times 10^5) \, n^{3/2} \, A \, D^{1/2} \, C^* \, v^{1/2} $$

Where:
- $I_p$ = peak current [A]
- $n$ = number of electrons transferred
- $A$ = electrode area [cm²]
- $D$ = diffusion coefficient [cm²/s]
- $C^*$ = bulk concentration [mol/cm³]
- $v$ = scan rate [V/s]

**Diagnostic**:
- If $I_p \propto \sqrt{v}$: process controlled by pure diffusion
- If $I_p \propto v$: process involving adsorbed species (capacitive)

---

## 6. Electrochemical Impedance Spectroscopy (EIS)

### 6.1 Complex impedance

EIS measures the current response to a sinusoidal potential perturbation. The complex impedance is:

$$Z(\omega) = \frac{\Delta E}{\Delta I} \cdot e^{j\varphi} = Z'(\omega) + j Z''(\omega)$$

where $\omega = 2\pi f$ is the angular frequency and $\varphi$ the phase shift between current and voltage.

### 6.2 Impedance elements

| Element | Expression | Domain |
|---------|------------|--------|
| Resistance | $Z_R = R$ | Pure real |
| CPE | $Z_{CPE} = \frac{1}{Q_0 (j\omega)^n}$ | $n=1$ → capacitance, $n<1$ → non-ideal |
| Warburg | $Z_W = \frac{\sigma}{\sqrt{\omega}}(1-j)$ | 45° line on Nyquist |

### 6.3 Randles circuit (EIS redox couple)

$$Z(\omega) = R_s + \frac{1}{\frac{1}{Z_{CPE}} + \frac{1}{R_{ct} + Z_W}}$$

Circuit: $R_s$ in series with the parallel combination of $CPE_{dl}$ and ($R_{ct} + Z_W$).

### 6.4 Two-time-constant circuit (EIS Au/Ni/Cu electrode)

Used when a passive film forms on the electrode (pH ≥ 7 with Ni or Cu):

$$Z(\omega) = R_s + Z_{film\parallel} + Z_{dl\parallel}$$

with $Z_{film\parallel} = \frac{R_{film} \cdot Z_{CPE,film}}{R_{film} + Z_{CPE,film}}$ and $Z_{dl\parallel} = \frac{(R_{ct} + Z_W) \cdot Z_{CPE,dl}}{(R_{ct} + Z_W) + Z_{CPE,dl}}$

### 6.5 Charge transfer resistance

$R_{ct}$ is computed from the physical parameters of the redox couple:

$$R_{ct} = \frac{RT}{n^2 F^2 A \, k^0 \, c}$$

where $A$ = electrode surface area ($1.77 \times 10^{-6}$ m²), $k^0$ = standard rate constant (m/s), $c$ = concentration (mol/m³).

### 6.6 Warburg coefficient

For an equimolar couple ($D_O = D_R = D$, $c_O = c_R = c$):

$$\sigma = \frac{RT}{n^2 F^2 A \sqrt{2}} \cdot \frac{2}{\sqrt{D} \cdot c}$$

### 6.7 Effective double-layer capacitance

At the Nyquist semicircle apex (angular frequency $\omega_{max}$):

$$C_{dl,eff} = \frac{1}{\omega_{max} \cdot R_{ct}}$$

### 6.8 Diagnostics

| Nyquist observation | Interpretation |
|---------------------|----------------|
| Clear semicircle + 45° line | $R_{ct}$ and $\sigma$ comparable — mixed regime |
| 45° line only | High $k^0$ → $R_{ct} \approx 0$, pure diffusion |
| Semicircle only | High $D$ → $\sigma \approx 0$, pure charge transfer |
| Flattened semicircle | $n_{CPE} < 1$ — heterogeneous surface |
| 2 distinct arcs | Passive film (EIS Au/Ni/Cu electrode) — 2 time constants |

---

## 7. Bibliographical References

*Note: For the complete list of references, see the Bibliographical References section in the Annexes menu.*
