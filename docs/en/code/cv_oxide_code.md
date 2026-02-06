**Contents:**
1. Architecture
2. Analytical Implicit Scheme
3. Dynamic Steering
4. Capacitive Current
5. Dependencies

---

## 1. Architecture

The code is structured in modular files:

| File | Role |
|------|------|
| `cv_surface_oxide.py` | Main simulation (time loop, current calculation) |
| `parameters_oxide.py` | Physical parameters (metals, electrode, electrolyte) |
| `parametric_study.py` | Parametric study orchestrator |

---

## 2. Analytical Implicit Scheme

The ODE $d\theta/dt = k_{ox}(1-\theta) - k_{red} \cdot \theta$ is linear in $\theta$, which allows an analytical solution of the implicit scheme:

```python
theta_new = (theta_old + dt * k_ox) / (1 + dt * (k_ox + k_red))
theta_new = np.clip(theta_new, 0.0, 1.0)
```

This scheme is unconditionally stable and requires no nonlinear solver.

---

## 3. Dynamic Steering (current threshold)

The scan direction reverses automatically when current exceeds a threshold, reproducing real potentiostat behavior:

```python
if scan_dir == +1 and I_step > +I_threshold:
    scan_dir = -1   # switch to cathodic sweep
elif scan_dir == -1 and I_step < -I_threshold:
    scan_dir = +1   # switch to anodic sweep
```

---

## 4. Capacitive Current (double layer)

The capacitive contribution is added to the faradaic current:

```python
I_cdl = C_dl * A * scan_rate * scan_dir
I_total += I_cdl
```

---

## 5. Dependencies

- `numpy`: numerical computation
- `matplotlib`: voltammogram plotting
- No FEM dependency (no mesh, no Newton solver)
