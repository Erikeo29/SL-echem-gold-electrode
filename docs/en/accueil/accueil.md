&nbsp;

**Author's note** — *This project was designed entirely by the author, from a blank page through to its deployment online. The content was developed based on the author's own knowledge, supplemented by online research for the documentary part, definition of physical concepts, implementation of relevant numerical tools...*

*For the (very many!) topics beyond the author's initial area of expertise, artificial intelligence and automation tools were used to conduct in-depth internet research (parameterization of physical model equations, selection and use of numerical libraries), writing, testing and debugging code (Python, C++), creating this application's interface, automatic French/English translation...*

*Nonetheless, all results presented in this project are derived from analytical and deterministic physical models solved by recognized and validated numerical solvers. The objective is to enable advanced multiphysics modeling using free and open-source tools.*

*The input data used (equations, values...) is public and freely available on the internet, although widely scattered. The codes are original even if not innovative. As such, this work is made available to be freely used, reproduced and improved for learning purposes or for the use of the physical and numerical models presented here.*

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

Navigation through the different pages of this application is structured with the following tools:

1. **Side menu (left)**: navigation tool between the different sections of the project:
   - **Introduction**: scientific context and system presentation.
   - **Study comparison**: summary table of the two approaches.
   - **Modeling results**: each study contains Physics (description of the physical models and numerical resolution methods used), Code (codes entirely developed in this project, which can be duplicated) and Results (visual modelling) tabs.
   - **Appendices**: conclusion, glossary, key equations, bibliographical references and a history page on the key researchers and scientists who developed the physical and numerical concepts presented.

2. **Floating navigation buttons (right)**: quick scroll up/down.

3. **AI Assistant (side menu)**: answers questions about the physics or numerical methods.

---

## 4. Methodological note

The results presented come from **pre-computed** simulations. The project was carried out on a standard laptop: Linux environment via WSL2, 1.5-3.5 GHz processor, 6 CPU / 12 threads, 32 GB RAM. Computation times range from a few seconds (EIS study, algebraic calculation) to 30 seconds (CV study, ODE) per unit simulation.

This application is therefore a **results viewer**, not a real-time simulator. Indeed, running these simulations requires specific environment configurations and Python packages (numpy). The codes are available in the "Code" tabs of each study so they can be copied and used to reproduce these simulations on other machines.
