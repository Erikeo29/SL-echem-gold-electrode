**Sommaire :**
1. Architecture
2. Éléments de circuit
3. Paramètres physiques
4. Extraction de métriques
5. Étude paramétrique
6. Dépendances

---


## Architecture

La simulation EIS est structurée en 3 modules Python :

```
03_Scripts/
├── parameters_eis.py       # Paramètres physiques par métal et pH
├── circuit_elements.py     # Éléments d'impédance (R, CPE, Warburg)
├── eis_simulation.py       # Simulation principale + extraction métriques
└── parametric_study_eis.py # Étude paramétrique (54 runs)
```

---

## 1. Éléments de circuit (`circuit_elements.py`)

### CPE (Constant Phase Element)

```python
def Z_CPE(omega, Q0, n):
    """Z = 1 / (Q₀ (jω)^n)"""
    n = np.clip(n, 0.0, 1.0)
    return 1.0 / (Q0 * (1j * omega) ** n)
```

### Warburg (diffusion semi-infinie)

```python
def Z_W(omega, sigma):
    """Z = σ/√ω (1 - j)"""
    return sigma / np.sqrt(omega) * (1.0 - 1j)
```

### Circuit de Randles

```python
def Z_Randles(omega, Rs, Rct, Q0, n, sigma):
    """Rs → [ CPE_dl ‖ ( Rct + W ) ]"""
    Zcpe = Z_CPE(omega, Q0, n)
    Zw = Z_W(omega, sigma)
    Z_faradaic = Rct + Zw
    Z_parallel = 1.0 / (1.0 / Zcpe + 1.0 / Z_faradaic)
    return Rs + Z_parallel
```

### Circuit à 2 constantes de temps

```python
def Z_TwoTimeConstant(omega, Rs, R_film, Q_film, n_film,
                       Rct, Q_dl, n_dl, sigma):
    """Rs → [ CPE_film ‖ R_film ] → [ CPE_dl ‖ ( Rct + Z_W ) ]"""
    # Arc HF : film passif
    Z_film_parallel = 1.0 / (1.0/Z_CPE(omega, Q_film, n_film) + 1.0/R_film)
    # Arc BF : transfert de charge + Warburg
    Z_faradaic = Rct + Z_W(omega, sigma)
    Z_dl_parallel = 1.0 / (1.0/Z_CPE(omega, Q_dl, n_dl) + 1.0/Z_faradaic)
    return Rs + Z_film_parallel + Z_dl_parallel
```

### Sélection adaptative

```python
def Z_adaptive(omega, params):
    """Randles si R_film=0, sinon 2-TC."""
    if params.get("R_film", 0) > 0:
        return Z_TwoTimeConstant(...)
    return Z_Randles(...)
```

---

## 2. Paramètres physiques (`parameters_eis.py`)

### Conversion Q₀ vers SI

```python
def _Q0_to_SI(Q0_uF_cm2):
    """µF·s^(n-1)/cm² → F·s^(n-1) (total)"""
    A_cm2 = A_ELECTRODE * 1e4  # m² → cm²
    return Q0_uF_cm2 * 1e-6 * A_cm2
```

### Lois de mélange

```python
def get_mixed_params(metals, fractions, pH):
    # Rct avec correction catalytique Ni
    Rct = Rct_base * (1.0 - 0.04 * pct_Ni / 100.0)
    # Q0 avec facteur de rugosité
    Q0_SI = Q0_Au_SI * (1.0 + 0.02*pct_Ni + 0.03*pct_Cu)
    # n avec correction hétérogénéité
    n = n_base - 0.002*pct_Ni - 0.003*pct_Cu
```

---

## 3. Extraction de métriques (`eis_simulation.py`)

L'algorithme détecte les maxima locaux de $-\text{Im}(Z)$ pour identifier les arcs :

```python
def extract_metrics(omega, Z, params):
    maxima = _find_local_maxima(-Z.imag)
    Rs_measured = Z.real[-1]  # intercept HF

    if has_film and len(maxima) >= 2:
        # 2 arcs : film (HF) + transfert de charge (BF)
        R_film_meas = 2.0 * (Z_real[idx_film] - Rs_measured)
        Rct_measured = 2.0 * (Z_real[idx_ct] - Rs - R_film)
    else:
        # 1 arc : Randles
        Rct_measured = 2.0 * (Z_real[idx_max] - Rs_measured)

    Cdl_eff = 1.0 / (omega_max * Rct_measured)
```

---

## 4. Étude paramétrique

**54 simulations** : 6 %Ni × 3 %Cu × 3 pH

```python
NI_RANGE = [0, 5, 10, 15, 20, 25]
CU_RANGE = [0, 5, 10]
PH_RANGE = [3.0, 7.0, 11.0]
```

Chaque run produit : `eis_data.csv`, `parameters.txt`, `metrics.txt`, `*_Nyquist.png`, `*_Bode.png`.

---

## 5. Dépendances

- **numpy** : calcul d'impédance complexe
- **matplotlib** : diagrammes Nyquist et Bode
- Pas de solveur FEM — calcul purement algébrique
