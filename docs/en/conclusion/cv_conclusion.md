# Conclusion and perspectives

**Contents:**
1. Conclusion
2. Perspectives

---

## 1. Conclusion

The two studies presented provide examples of electrochemical modeling on a gold electrode with nickel and copper impurities:

- **Study 1** (CV Au/Ni/Cu electrode): Au/Ni/Cu metal oxides, solved by analytical ODE, offer a first approach to multi-metallic electrode characterization. The effects of pH and double-layer capacitance are qualitatively consistent with expectations.

- **Study 2** (EIS Au/Ni/Cu electrode): impedance spectroscopy on the same Au/Ni/Cu electrode, with adaptive circuit (Randles / 2 time constants), allows exploring the extraction of quantities such as $R_{ct}$, $C_{dl}$ and $R_{film}$. These results are complementary to the CV metrics from Study 1.

This work constitutes a starting point for more in-depth studies, rather than a definitive characterization of the systems considered. Experimental validation is still needed.

---

## 2. Perspectives

- Coupling with homogeneous chemical reactions (EC, ECE mechanisms)
- Extension to complex 3D geometries (microelectrodes)
- **Inverse EIS fitting**: from experimental data → extract Rs, Rct, Cdl, R_film via `scipy.optimize`
- **CV–EIS coupling**: use kinetic parameters from Study 1 (pH, composition) as input for the EIS model (Study 2)
- **PINNs (Physics-Informed Neural Networks)**: train a neural network constrained by Langmuir-Butler-Volmer equations to accelerate solving or parametric inversion
