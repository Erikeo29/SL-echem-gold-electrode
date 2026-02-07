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

This application gathers **electrochemical** simulations solved in Python. The objective is to visualize and compare results from parametric studies for two complementary electrochemical systems on a gold electrode with the presence of nickel and copper impurities, covering both the time domain (cyclic voltammetry) and the frequency domain (impedance).

---

## 2. Available studies

### Study 1: CV of an Au electrode with Ni and Cu impurities

Simulation of surface reactions (metal oxides) on a gold electrode with nickel and copper traces. The model is based on a Langmuir–Butler-Volmer ODE (ordinary differential equation) solved by an analytical implicit scheme (without numerical iteration). The parametric study covers pH, electrode composition and double-layer capacitance $C_{dl}$.

### Study 2: EIS of an Au electrode with Ni and Cu impurities

Electrochemical impedance spectroscopy on the same Au/Ni/Cu electrode. The model uses an adaptive equivalent circuit: simple Randles at acidic pH, 2 time constants at neutral/alkaline pH (passive film). The parametric study covers pH, %Ni and %Cu. The computed results extracted from these calculations ($R_{ct}$, $C_{dl}$, $R_{film}$) are complementary to the CV metrics from Study 1.

---

## 3. Navigation

The navigation in this application is structured around the following tools:

1. **Side menu (left)**: main navigation between project sections.
   - **Introduction**: scientific context and system presentation.
   - **Study comparison**: summary table of the two approaches.
   - **Study pages**: each study contains Physics (description of the physical models and numerical resolution methods used), Code (codes entirely developed in this project, which can be duplicated) and Results (visual modelling) tabs.
   - **Appendices**: conclusion, glossary, key equations, bibliographical references and a history page on the key researchers and scientists who developed the physical and numerical concepts presented.

2. **Floating navigation buttons (right)**: quick scroll up/down.

3. **AI Assistant (side menu)**: answers questions about the physics or numerical methods.

---

## 4. Methodological note

The results presented come from **pre-computed** simulations. The project was carried out on a standard laptop: Linux environment via WSL2, 1.5-3.5 GHz processor, 6 CPU / 12 threads, 32 GB RAM. Computation times range from a few seconds (EIS study, algebraic calculation) to 30 seconds (CV study, ODE) per unit simulation.

This application is therefore a **results viewer**, not a real-time simulator. Indeed, running these simulations requires specific environment configurations and Python packages (numpy). The codes are available in the "Code" tabs of each study so they can be copied and used to reproduce these simulations on other machines.
