# Conclusion and perspectives

**Contents:**
1. Conclusion
2. Perspectives

---

## 1. Conclusion

The four studies presented provide examples of electrochemical modeling at different scales:

- **Study 1** (CV redox couple on Au): the ferro/ferricyanide-type redox couple in solution, solved by finite elements, illustrates reversibility diagnosis and the influence of $k^0$, $\alpha$ and $\nu$ on voltammogram shape. The observed trends (Randles-Ševčík law, irreversible → reversible transition) are consistent with theory.

- **Study 2** (EIS redox couple on Au): impedance spectroscopy on the same redox couple, with Randles circuit and 5 variable parameters, quantifies the influence of $k^0$, $D$, $c$, $n$ and $Q_0$ on impedance spectra. The extracted metrics ($R_{ct}$, $\sigma$, $C_{dl,eff}$) are complementary to Study 1.

- **Study 3** (CV Au/Ni/Cu electrode): Au/Ni/Cu metal oxides, solved by analytical ODE, offer a first approach to multi-metallic electrode characterization. The effects of pH and double-layer capacitance are qualitatively consistent with expectations.

- **Study 4** (EIS Au/Ni/Cu electrode): impedance spectroscopy on the same Au/Ni/Cu electrode, with adaptive circuit (Randles / 2 time constants), allows exploring the extraction of quantities such as $R_{ct}$, $C_{dl}$ and $R_{film}$. These results are complementary to the CV metrics from Study 3.

This work constitutes a starting point for more in-depth studies, rather than a definitive characterization of the systems considered. Experimental validation is still needed.

---

## 2. Perspectives

- Coupling with homogeneous chemical reactions (EC, ECE mechanisms)
- Convection effects (rotating electrodes, microchannels)
- Extension to complex 3D geometries (microelectrodes)
- **Inverse EIS fitting**: from experimental data → extract Rs, Rct, Q₀, n, σ, R_film via `scipy.optimize`
- **CV–EIS coupling**: use kinetic parameters from Study 1 ($k^0$, $\alpha$) as input for the EIS model (Study 2)
- **PINNs (Physics-Informed Neural Networks)**: train a neural network constrained by Butler-Volmer and diffusion equations to accelerate solving or parametric inversion
