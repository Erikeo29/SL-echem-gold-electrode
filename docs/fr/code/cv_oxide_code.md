**Sommaire :**
1. Architecture
2. Schéma implicite analytique
3. Pilotage dynamique
4. Courant capacitif
5. Dépendances

---

## 1. Architecture

Le code est structuré en fichiers modulaires :

| Fichier | Rôle |
|---------|------|
| `cv_surface_oxide.py` | Simulation principale (boucle temporelle, calcul du courant) |
| `parameters_oxide.py` | Paramètres physiques (métaux, électrode, électrolyte) |
| `parametric_study.py` | Orchestrateur d'études paramétriques |

---

## 2. Schéma implicite analytique

L'ODE $d\theta/dt = k_{ox}(1-\theta) - k_{red} \cdot \theta$ est linéaire en $\theta$, ce qui permet une solution analytique du schéma implicite :

```python
theta_new = (theta_old + dt * k_ox) / (1 + dt * (k_ox + k_red))
theta_new = np.clip(theta_new, 0.0, 1.0)
```

Ce schéma est inconditionnellement stable et ne nécessite pas de solveur non-linéaire.

---

## 3. Pilotage dynamique (seuil de courant)

Le sens de balayage s'inverse automatiquement lorsque le courant dépasse un seuil, reproduisant le comportement d'un potentiostat réel :

```python
if scan_dir == +1 and I_step > +I_threshold:
    scan_dir = -1   # passage en balayage cathodique
elif scan_dir == -1 and I_step < -I_threshold:
    scan_dir = +1   # passage en balayage anodique
```

---

## 4. Courant capacitif (double couche)

La contribution capacitive est ajoutée au courant faradique :

```python
I_cdl = C_dl * A * scan_rate * scan_dir
I_total += I_cdl
```

---

## 5. Dépendances

- `numpy` : calcul numérique
- `matplotlib` : tracé des voltammogrammes
- Aucune dépendance FEM (pas de maillage, pas de solveur Newton)
