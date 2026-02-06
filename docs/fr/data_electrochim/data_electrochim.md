# Données électrochimiques

> Tous les potentiels sont exprimés **vs Ag/AgCl (KCl sat.)** ($E_{\text{Ag/AgCl}} = E_{\text{SHE}} - 0.197$ V).

**Sommaire :**
1. Constantes fondamentales
2. Potentiels redox et cinétique de surface (étude 1 — CV)
3. Paramètres d'impédance à l'OCP (étude 2 — EIS)
4. Hypothèses et limites

---

## 1. Constantes fondamentales

| Constante | Symbole | Valeur | Unité |
|-----------|---------|--------|-------|
| Faraday | $F$ | 96 485 | C/mol |
| Gaz parfaits | $R$ | 8.314 | J/(mol·K) |
| Température | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |
| Surface d'électrode | $A$ | 1.77×10⁻⁶ | m² |

---

## 2. Potentiels redox et cinétique de surface (étude 1 — CV)

### Réactions redox

> **Au** : $2\text{Au} + 6\text{OH}^- \to \text{Au}_2\text{O}_3 + 3\text{H}_2\text{O} + 6e^-$ — oxyde réversible à tous les pH (β-oxide Au(OH)₃ en milieu alcalin). Modèle multi-sites (20).

> **Ni** : dissolution $\text{Ni} \to \text{Ni}^{2+} + 2e^-$ à pH < 2 ; transition Ni(OH)₂ ↔ NiOOH à pH ≥ 7 (partiel à pH 7, réversible à pH 13).

> **Cu** : dissolution $\text{Cu} \to \text{Cu}^{2+} + 2e^-$ à pH < 4 ; formation séquentielle Cu₂O puis CuO à pH ≥ 7.

### Potentiels standard par métal et pH

| Métal | pH | Mécanisme | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Remarque |
|-------|:--:|-----------|:--------------:|:---------------:|----------|
| Au | 1 | Oxyde réversible | 1.10 → 1.50 | 0.90 | Multi-sites (20) |
| Ni | 1 | Dissolution | −0.454 | — | Irréversible |
| Cu | 1 | Dissolution | +0.14 | — | Irréversible |
| Au | 7 | Oxyde réversible | 0.70 → 1.10 | 0.50 | Multi-sites (20) |
| Ni | 7 | Oxyde partiel | +0.78 | +0.59 | Signal faible, chevauche Au |
| Cu | 7 | Oxyde partiel | −0.15 / +0.05 | −0.275 | Cu₂O (60%) + CuO (40%) |
| Au | 13 | Oxyde réversible | 0.25 → 0.65 | +0.15 | β-oxide Au(OH)₃ |
| Ni | 13 | Oxyde réversible | +0.43 | +0.24 | Ni(OH)₂ ↔ NiOOH |
| Cu | 13 | Oxyde réversible | −0.38 / +0.08 | −0.76 | Cu₂O (50%) + CuO (50%) |

Les potentiels suivent la loi de Nernst : $E^0(pH) = E^0_{pH=0} - 0.059 \times pH$. Fenêtre de balayage CV : **2.0 V** à chaque pH, centrée entre les murs HER et OER (voir onglet **Physique** de l'étude CV).

### Paramètres cinétiques de surface

| Paramètre | Au | Ni | Cu | Unité |
|-----------|:--:|:--:|:--:|-------|
| $k_0$ | 2.0 | 5.0 | 5.0 | s⁻¹ (réaction de surface) |
| $\Gamma_{max}$ | 4×10⁻⁵ | 3×10⁻⁵ | 3.5×10⁻⁵ | mol/m² |
| $\alpha$ | 0.5 | 0.5 | 0.5 | — |

---

## 3. Paramètres d'impédance à l'OCP (étude 2 — EIS)

L'EIS est réalisée au **potentiel de circuit ouvert** (OCP) : le potentiel où le courant net est nul. Pour les alliages : $E_{ocp} \approx \sum x_i \cdot E_{ocp,i}$ (approximation de potentiel mixte).

| Métal | pH | E_ocp (V) | Rct (Ω) | R_film (Ω) | Circuit | Source |
|-------|:--:|:---------:|:-------:|:----------:|---------|--------|
| Au | 3 | +0.50 | 1 200 | 0 | Randles | Hamelin 1994 |
| Ni | 3 | −0.25 | 700 | 0 | Randles | Beverskog 1997 |
| Cu | 3 | +0.02 | 500 | 0 | Randles | Beverskog 1997 |
| Au | 7 | +0.15 | 5 000 | 0 | Randles | Song 2025 |
| Ni | 7 | −0.20 | 1 500 | 0 ⚠️ | Randles | ACS Omega 2016 |
| Cu | 7 | −0.20 | 2 000 | 400 | 2-TC | JACS 2024 |
| Au | 11 | −0.10 | 2 000 | 150 | 2-TC | Diaz-Morales 2020 |
| Ni | 11 | +0.10 | 8 000 | 2 000 | 2-TC | Weininger 1963 |
| Cu | 11 | −0.40 | 4 000 | 800 | 2-TC | Ambrose 1973 |

⚠️ Ni instable à pH 7 : le film NiOOH se dissout lentement (ACS Omega 2016). Pas de R_film.

**Tendances** : à pH 3, Ni et Cu dissolvent activement (Rct faible). À pH 11, tous les métaux se passivent ; le Ni montre le R_film le plus élevé (2 000 Ω, film Ni(OH)₂ compact). L'or reste le plus inerte à pH 7 (Rct = 5 000 Ω, pas de film).

> Paramètres complets (Q₀, n, σ, lois de mélange) : voir l'onglet **Physique** de l'étude EIS.

---

## 4. Hypothèses et limites

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| Langmuir ($\theta \in [0,1]$) | Adsorption localisée | Ignore interactions latérales |
| $E^0_{ox} \neq E^0_{red}$ | Hystérésis expérimentale | Empirique, pas mécanistique |
| Multi-sites Au (20) | Élargissement pic d'oxydation | Distribution arbitraire |
| EIS simulée à l'OCP | État stationnaire reproductible | Pas d'exploration d'autres potentiels |
| OCP par potentiel mixte | $\sum x_i E_i$ simple | Ignore couplage galvanique |
| Rct bibliographiques | Valeurs typiques publiées | Pas dérivés de Butler-Volmer |
| Ni instable pH 7 | Pourbaix + ACS Omega 2016 | Simplifié (pas de film transitoire) |

**Ce que les modèles ne capturent pas** : nucléation des oxydes, restructuration de surface, effets d'orientation cristalline, interactions métal-métal, dépendance Rct(E).

---

*Étude 1 : parameters_oxide.py — Étude 2 : parameters_eis.py (04_EIS_with_OCP, 2026-02-06).*
