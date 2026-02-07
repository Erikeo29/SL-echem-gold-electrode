**Contents:**
1. Architecture
2. Circuit elements
3. Physical parameters
4. Metrics extraction
5. Parametric study
6. Dependencies

---


## Architecture

The EIS simulation is structured into 3 Python modules:

```
03_Scripts/
├── parameters_eis.py       # Physical parameters per metal and pH
├── circuit_elements.py     # Impedance elements (R, CPE, Warburg)
├── eis_simulation.py       # Main simulation + metric extraction
└── parametric_study_eis.py # Parametric study (27 runs)
```

---

## 1. Circuit Elements (`circuit_elements.py`)

### CPE (Constant Phase Element)

```python
def Z_CPE(omega, Q0, n):
    """Z = 1 / (Q₀ (jω)^n)"""
    n = np.clip(n, 0.0, 1.0)
    return 1.0 / (Q0 * (1j * omega) ** n)
```

### Warburg (semi-infinite diffusion)

```python
def Z_W(omega, sigma):
    """Z = σ/√ω (1 - j)"""
    return sigma / np.sqrt(omega) * (1.0 - 1j)
```

### Randles Circuit

```python
def Z_Randles(omega, Rs, Rct, Q0, n, sigma):
    """Rs → [ CPE_dl ‖ ( Rct + W ) ]"""
    Zcpe = Z_CPE(omega, Q0, n)
    Zw = Z_W(omega, sigma)
    Z_faradaic = Rct + Zw
    Z_parallel = 1.0 / (1.0 / Zcpe + 1.0 / Z_faradaic)
    return Rs + Z_parallel
```

### Two-Time-Constant Circuit

```python
def Z_TwoTimeConstant(omega, Rs, R_film, Q_film, n_film,
                       Rct, Q_dl, n_dl, sigma):
    """Rs → [ CPE_film ‖ R_film ] → [ CPE_dl ‖ ( Rct + Z_W ) ]"""
    # HF arc: passive film
    Z_film_parallel = 1.0 / (1.0/Z_CPE(omega, Q_film, n_film) + 1.0/R_film)
    # LF arc: charge transfer + Warburg
    Z_faradaic = Rct + Z_W(omega, sigma)
    Z_dl_parallel = 1.0 / (1.0/Z_CPE(omega, Q_dl, n_dl) + 1.0/Z_faradaic)
    return Rs + Z_film_parallel + Z_dl_parallel
```

### Adaptive Selection

```python
def Z_adaptive(omega, params):
    """Randles if R_film=0, otherwise 2-TC."""
    if params.get("R_film", 0) > 0:
        return Z_TwoTimeConstant(...)
    return Z_Randles(...)
```

---

## 2. Physical Parameters (`parameters_eis.py`)

### Q₀ to SI Conversion

```python
def _Q0_to_SI(Q0_uF_cm2):
    """µF·s^(n-1)/cm² → F·s^(n-1) (total)"""
    A_cm2 = A_ELECTRODE * 1e4  # m² → cm²
    return Q0_uF_cm2 * 1e-6 * A_cm2
```

### Mixing Laws

```python
def get_mixed_params(metals, fractions, pH):
    # Rct with Ni catalytic correction
    Rct = Rct_base * (1.0 - 0.04 * pct_Ni / 100.0)
    # Q0 with roughness factor
    Q0_SI = Q0_Au_SI * (1.0 + 0.02*pct_Ni + 0.03*pct_Cu)
    # n with heterogeneity correction
    n = n_base - 0.002*pct_Ni - 0.003*pct_Cu
```

---

## 3. Metric Extraction (`eis_simulation.py`)

The algorithm detects local maxima of $-\text{Im}(Z)$ to identify arcs:

```python
def extract_metrics(omega, Z, params):
    maxima = _find_local_maxima(-Z.imag)
    Rs_measured = Z.real[-1]  # HF intercept

    if has_film and len(maxima) >= 2:
        # 2 arcs: film (HF) + charge transfer (LF)
        R_film_meas = 2.0 * (Z_real[idx_film] - Rs_measured)
        Rct_measured = 2.0 * (Z_real[idx_ct] - Rs - R_film)
    else:
        # 1 arc: Randles
        Rct_measured = 2.0 * (Z_real[idx_max] - Rs_measured)

    Cdl_eff = 1.0 / (omega_max * Rct_measured)
```

---

## 4. Parametric Study

**27 simulations** (aligned with CV study): 3 %Ni × 3 %Cu × 3 pH

```python
PCT_NI_DEFAULT = [0, 10, 30]
PCT_CU_DEFAULT = [0, 10, 30]
PH_DEFAULT = [3.0, 7.0, 11.0]
```

Each run produces: `eis_data.csv`, `parameters.txt`, `metrics.txt`, `*_Nyquist.png`, `*_Bode.png`.

---

## 5. Dependencies

- **numpy**: complex impedance calculations
- **matplotlib**: Nyquist and Bode diagrams
- No FEM solver — purely algebraic computation
