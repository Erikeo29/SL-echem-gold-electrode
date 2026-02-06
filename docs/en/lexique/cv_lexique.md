# Glossary

**Contents:**
1. General Acronyms
2. Electrochemical Acronyms
3. Dimensionless Numbers
4. Physical Symbols
5. Technical Terms
6. Software and Libraries
7. SI Units
---

## 1. General Acronyms

| Acronym | Meaning | Description |
|---------|---------|-------------|
| **FEM** | Finite Element Method | Numerical method for PDEs |
| **FVM** | Finite Volume Method | Conservation-based numerical method |
| **CFD** | Computational Fluid Dynamics | Numerical fluid mechanics |
| **BC** | Boundary Condition | Constraint at domain boundaries |
| **IC** | Initial Condition | State at t=0 |
| **PDE** | Partial Differential Equation | Governing equations |
| **DOF** | Degrees of Freedom | Number of unknowns |
| **SI** | International System | Standard unit system |

---

## 2. Electrochemical Acronyms

| Acronym | Meaning | Description |
|---------|---------|-------------|
| **CV** | Cyclic Voltammetry | Electroanalytical technique |
| **WE** | Working Electrode | Where the reaction of interest occurs |
| **CE** | Counter Electrode | Auxiliary electrode (closes circuit) |
| **RE** | Reference Electrode | Stable potential reference |
| **OCP** | Open Circuit Potential | Potential at zero current |
| **EIS** | Electrochemical Impedance Spectroscopy | Frequency-domain technique |
| **BV** | Butler-Volmer | Charge transfer kinetics equation |
| **NP** | Nernst-Planck | Transport equation with migration |
| **HER** | Hydrogen Evolution Reaction | H⁺ reduction to H₂ (cathodic wall) |
| **OER** | Oxygen Evolution Reaction | H₂O oxidation to O₂ (anodic wall) |

---

## 3. Dimensionless Numbers

| Symbol | Name | Expression | Physical Meaning |
|--------|------|------------|------------------|
| $Da$ | Damköhler | $\frac{k^0 L}{D}$ | Kinetics / Diffusion |
| $Pe$ | Péclet | $\frac{v L}{D}$ | Convection / Diffusion |
| $\Lambda$ | Kinetic parameter | $\frac{k^0}{\sqrt{n F v D / RT}}$ | CV system reversibility |

**Interpretation of $\Lambda$ parameter:**
- $\Lambda > 15$: Reversible system (fast transfer)
- $1 < \Lambda < 15$: Quasi-reversible system
- $\Lambda < 1$: Irreversible system (slow transfer)

---

## 4. Physical Symbols

### Electrochemical Parameters

| Symbol | Name | SI Unit |
|--------|------|---------|
| $E$ | Electrode potential | V |
| $E^0$ | Standard potential | V |
| $\eta$ | Overpotential ($E - E^0$) | V |
| $I$ | Current | A |
| $i$ | Current density | A/m² |
| $J$ | Molar flux | mol/(m²·s) |
| $n$ | Number of electrons transferred | - |

### Kinetic Parameters

| Symbol | Name | SI Unit |
|--------|------|---------|
| $k^0$ | Standard rate constant | m/s (solution) or s⁻¹ (surface) |
| $\alpha$ | Transfer coefficient | - |
| $v$ | Scan rate | V/s |
| $F$ | Faraday constant | 96485 C/mol |
| $R$ | Gas constant | 8.314 J/(mol·K) |
| $T$ | Temperature | K |

### Transport Parameters

| Symbol | Name | SI Unit |
|--------|------|---------|
| $c_i$ | Concentration of species $i$ | mol/m³ |
| $c_O$ | Oxidant concentration | mol/m³ |
| $c_R$ | Reductant concentration | mol/m³ |
| $C^*$ | Bulk concentration | mol/m³ |
| $D$ | Diffusion coefficient | m²/s |
| $\delta$ | Diffusion layer thickness | m |

### Surface Parameters (CV Au/Ni/Cu electrode)

| Symbol | Name | SI Unit |
|--------|------|---------|
| $\theta$ | Surface coverage (fraction of occupied sites) | - [0, 1] |
| $\Gamma_{max}$ | Maximum surface site density | mol/m² |
| $E^0_{ox}$ | Standard oxidation potential (oxide formation) | V |
| $E^0_{red}$ | Standard reduction potential (oxide dissolution) | V |
| $C_{dl}$ | Double-layer capacitance | F/m² (or µF/cm²) |

### CV Metrics

| Symbol | Name | Unit |
|--------|------|------|
| $I_{pa}$ | Anodic peak current | A (or µA) |
| $I_{pc}$ | Cathodic peak current | A (or µA) |
| $E_{pa}$ | Anodic peak potential | V |
| $E_{pc}$ | Cathodic peak potential | V |
| $\Delta E_p$ | Peak separation ($|E_{pa} - E_{pc}|$) | V (or mV) |

### Impedance quantities (EIS)

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| $Z(\omega)$ | Complex impedance | Ω | Ratio $\Delta E / \Delta I$ under sinusoidal excitation |
| $Z'$ | Real part | Ω | Resistive component |
| $Z''$ | Imaginary part | Ω | Reactive component |
| $\|Z\|$ | Impedance modulus | Ω | $\sqrt{Z'^2 + Z''^2}$ |
| $\varphi$ | Phase shift | ° or rad | Angle between current and voltage |

### Circuit elements (EIS)

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| $R_s$ | Solution resistance | Ω | Ohmic drop in the electrolyte |
| $R_{ct}$ | Charge transfer resistance | Ω | Redox reaction kinetics |
| $R_{film}$ | Passive film resistance | Ω | Oxide film (EIS Au/Ni/Cu electrode) |
| $Q_0$ | CPE parameter | F·s^(n-1) | Pseudo-capacitance (CPE) |
| $n_{CPE}$ | CPE exponent | — | 1 = ideal capacitor, < 1 = non-ideal |
| $\sigma$ | Warburg coefficient | Ω·s⁻⁰·⁵ | Semi-infinite diffusion |
| $C_{dl}$ | Double-layer capacitance | F | Electrode/solution interface |

### EIS-specific parameters

*Note: $k^0$, $D$ and $c$ are defined above (kinetic and transport parameters).*

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| $n_{el}$ | Number of electrons transferred | — | Electrons per elementary reaction |
| $A$ | Electrode surface area | m² | Active area of the working electrode |
| $\omega$ | Angular frequency | rad/s | $\omega = 2\pi f$ |
| $\omega_{max}$ | Peak angular frequency | rad/s | Characteristic frequency of the semicircle |

---

## 5. Technical Terms

### Electrochemistry

| Term | Definition |
|------|------------|
| **Voltammogram** | Plot of $I = f(E)$ obtained during a potential sweep |
| **Reversible** | System where electron transfer is fast vs. diffusion ($\Delta E_p \approx 59/n$ mV) |
| **Quasi-reversible** | System where kinetics and diffusion are comparable |
| **Irreversible** | System limited by charge transfer kinetics |
| **Depletion** | Consumption of reactive species near the electrode |
| **Diffusion layer** | Region where concentration gradient is non-zero |
| **Double layer** | Metal/solution interface with charge separation |
| **Redox couple** | Oxidized/reduced species pair |

### Numerical Methods

| Term | Definition |
|------|------------|
| **Mesh** | Spatial discretization of the computational domain |
| **Local refinement** | Increased mesh density in critical zones |
| **Implicit Euler** | Unconditionally stable time-stepping scheme |
| **Newton-Raphson** | Iterative algorithm for nonlinear systems |
| **Preconditioning** | Convergence acceleration technique |
| **Weak formulation** | Integral form of equations (FEM basis) |
| **P2 elements** | Quadratic Lagrange finite elements |

---

## 6. Software and Libraries

| Name | Type | Language | Method | Usage |
|------|------|----------|--------|-------|
| **Firedrake** | Open-source | Python | FEM | PDE solving (this project) |
| **FEniCSx** | Open-source | Python/C++ | FEM | FEM alternative |
| **GMSH** | Open-source | Python/C++ | - | Mesh generation |
| **OpenFOAM** | Open-source | C++ | FVM | CFD, multiphase |
| **COMSOL** | Commercial | GUI/MATLAB | FEM | Multiphysics |
| **PETSc** | Open-source | C | - | HPC solvers |
| **NumPy** | Open-source | Python | - | Scientific computing |
| **Matplotlib** | Open-source | Python | - | Visualization |

---

## 7. SI Units

### Fundamental Quantities

| Quantity | Unit | Symbol |
|----------|------|--------|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |

### Derived Quantities

| Quantity | Unit | Symbol | Equivalent |
|----------|------|--------|------------|
| Potential | volt | V | J/C |
| Charge | coulomb | C | A·s |
| Energy | joule | J | V·C |
| Concentration | mol per cubic meter | mol/m³ | - |
| Diffusivity | square meter per second | m²/s | - |
| Molar flux | mol/(m²·s) | - | - |

### Common Prefixes

| Prefix | Symbol | Factor | Example |
|--------|--------|--------|---------|
| micro | µ | 10⁻⁶ | µA (microampere) |
| milli | m | 10⁻³ | mV, mM |
| kilo | k | 10³ | kJ |



