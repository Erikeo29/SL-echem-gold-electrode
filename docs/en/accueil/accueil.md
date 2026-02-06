&nbsp;

**Author's note** — *This project was designed entirely by the author, from a blank slate through to publication. Content creation was carried out with the support of artificial intelligence tools, particularly for writing and debugging code and for internet research.
All results shown in this project are derived from analytical and deterministic physical models solved by validated numerical solvers.
This work is released as open-source: it may be freely copied, duplicated, and adapted for learning purposes or for the use of the physical and numerical models presented here.*

&nbsp;

**Contents:**
1. Objective
2. Available studies
3. Navigation
4. Methodological note

---

## 1. Objective

This application gathers **electrochemical** simulations solved in Python. The objective is to visualize and compare results from parametric studies for four distinct electrochemical systems, covering both the time domain (cyclic voltammetry) and the frequency domain (impedance).

---

## 2. Available studies

### Study 1: CV of a redox couple on Au

Modeling of unsteady mass transport coupled with Butler-Volmer kinetics. The $Fe(CN)_6^{3-} / Fe(CN)_6^{4-}$ system is solved by finite elements (Firedrake) in 2D geometry. The parametric study covers the kinetic constant $k^0$, transfer coefficient $\alpha$ and scan rate $\nu$.

### Study 2: EIS of a redox couple on Au

Electrochemical impedance spectroscopy on a pure gold electrode with a ferro/ferricyanide-type redox couple. The model uses a Randles circuit with CPE and Warburg impedance. The parametric study covers 5 parameters ($n$, $k^0$, $D$, $c$, $Q_0$) for 48 simulations. The extracted metrics ($R_{ct}$, $\sigma$, $C_{dl,eff}$) are complementary to Study 1.

### Study 3: CV of an Au electrode with Ni and Cu impurities

Simulation of surface reactions (metal oxides) on a gold electrode with nickel and copper traces. The model is based on a Langmuir–Butler-Volmer ODE solved by an analytical implicit scheme. The parametric study covers pH, electrode composition and double-layer capacitance $C_{dl}$.

### Study 4: EIS of an Au electrode with Ni and Cu impurities

Electrochemical impedance spectroscopy on the same Au/Ni/Cu electrode. The model uses an adaptive equivalent circuit: simple Randles at acidic pH, 2 time constants at neutral/alkaline pH (passive film). The parametric study covers pH, %Ni and %Cu (54 simulations). The extracted diagnostics ($R_{ct}$, $C_{dl}$, $R_{film}$) are complementary to the CV metrics from Study 3.

---

## 3. Navigation

The application is structured around several tools:

1. **Side menu (left)**: main navigation between project sections.
   - **Introduction**: scientific context and system presentation.
   - **Study comparison**: summary table of the four approaches.
   - **Study pages**: each study contains Physics, Code and Results tabs.
   - **Appendices**: conclusion, glossary, key equations and bibliographical references.

2. **Floating navigation buttons (right)**: quick scroll up/down.

3. **AI Assistant (side menu)**: answers questions about the physics or numerical methods.

---

## 4. Methodological note

The results presented come from **pre-computed** simulations. The project was carried out on a standard laptop: Linux environment via WSL2, 1.5-3.5 GHz processor, 6 CPU / 12 threads, 32 GB RAM. Computation times range from a few seconds (Studies 2 and 4, algebraic calculation) to 30 seconds (Study 3, ODE) and 60 seconds (Study 1, 2D FEM) per unit simulation.

This application is therefore a **results viewer**, not a real-time simulator. Indeed, running these simulations requires specific environment configurations and Python packages (Firedrake, numpy). The codes are available in the "Code" tabs of each study so they can be copied and used to reproduce these simulations on other machines.
