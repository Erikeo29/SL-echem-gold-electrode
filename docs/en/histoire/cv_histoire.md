# History of Voltammetry and Impedance: From Mercury Drops to Supercomputers

**Contents:**
1. The Era of Polarography (1922-1950)
2. The Birth of "Cyclic Voltammetry" (1948-1964)
3. The Digital Revolution (1960s-1990s)
4. Today: Multi-scale Modeling
5. The Rise of Electrochemical Impedance Spectroscopy (EIS)
6. Bibliographical References

---

Cyclic Voltammetry (CV) is now the "king" of electrochemical tools, often compared to spectroscopy for its ability to reveal system identity and dynamics. But its history is one of slow maturation.

## 1. The Era of Polarography (1922-1950)

It all started in Prague in 1922. **Jaroslav Heyrovský** invented polarography using a dropping mercury electrode (DME). This constantly renewed surface allowed for reproducible current-potential curves.

- **1959**: Heyrovský receives the **Nobel Prize in Chemistry**, establishing electroanalysis as a major discipline.
- *Limitation*: Classical polarography worked at constant potential or very slow variation.

## 2. The Birth of "Cyclic Voltammetry" (1948-1964)

The shift to solid electrodes (Pt, Au, C) and modern electronics allowed for fast triangular signals.

- **1948**: **Randles** (UK) and **Sevcik** (Czechoslovakia) independently publish the famous peak current equation for linear diffusion:
    $$ I_p = 2.69 \times 10^5 n^{3/2} A D^{1/2} C v^{1/2} $$
- **1964**: The seminal paper. **Nicholson and Shain** publish in *Analytical Chemistry* the "theory of stationary electrode polarography". They tabulate diagnostic criteria ($\Delta E_p$, $I_{pa}/I_{pc}$) to distinguish reversible, irreversible, and coupled mechanisms (EC, ECE). Modern CV is born.

## 3. The Digital Revolution (1960s-1990s)

Analytical equations becoming too complex for real systems, numerical simulation took over.

- **Stephen Feldberg** introduces the explicit finite difference method to simulate electrochemical diffusion.
- **Rudolph Marcus** (Nobel Prize 1992) develops electron transfer theory, providing the microscopic framework that CV measures macroscopically.

## 4. Today: Multi-scale Modeling

Today, CV is no longer interpreted just "by eye". Software (DigiElch, COMSOL, and our Firedrake codes) couples CV with:

- Convection (Hydrodynamics)
- Complex 3D geometry (Microelectrodes, MEA)
- Quantum chemistry (DFT) to predict standard Redox potentials ($E^0$)

CV has evolved from a lab curiosity involving toxic mercury to the standard tool for designing tomorrow's Lithium-Ion batteries.

## 5. The Rise of Electrochemical Impedance Spectroscopy (EIS)

In parallel with CV, another characterization technique emerged in the frequency domain.

| Year | Milestone |
|------|-----------|
| ~1900 | **Emil Warburg** was the first to extend the concept of impedance to electrochemical systems, deriving the impedance function for a diffusional process that still bears his name |
| 1880s | **Oliver Heaviside** laid the foundations of Linear Systems Theory and coined the terms "impedance", "admittance", and "reactance" |
| 1940s | The invention of the **potentiostat** made controlled-potential impedance measurements possible |
| 1960s | **Epelboin and his group in Paris** propelled EIS to the forefront of electrochemical research |
| 1970s | The development of **Frequency Response Analyzers** (FRA) enabled exploration of very low frequencies |

EIS is now complementary to CV: where CV probes time-domain dynamics (current vs. potential), EIS decomposes the frequency response to separate resistive ($R_{ct}$, $R_s$), capacitive ($C_{dl}$), and diffusional ($\sigma$) contributions.

---

## 6. Bibliographical References

*Note: For the complete list of references, see the Bibliographical References section in the Annexes menu.*
