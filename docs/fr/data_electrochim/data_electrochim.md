# Données électrochimiques

**Sommaire :**
1. Constantes fondamentales
2. Couple ferro/ferricyanide (études 1 & 2)
3. Oxydes métalliques (études 3 & 4)
4. Murs électrochimiques (HER/OER)
5. Hypothèses et limites des modèles

---

## 1. Constantes fondamentales

| Constante | Symbole | Valeur | Unité |
|-----------|---------|--------|-------|
| Constante de Faraday | $F$ | 96 485 | C/mol |
| Constante des gaz | $R$ | 8.314 | J/(mol·K) |
| Température standard | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |

---

## 2. Couple ferro/ferricyanide (études 1 & 2)

### Réaction électrochimique

$$\text{Fe(CN)}_6^{3-} + e^- \rightleftharpoons \text{Fe(CN)}_6^{4-}$$

### Paramètres cinétiques

| Paramètre | Symbole | Valeur | Unité | Remarque |
|-----------|---------|--------|-------|----------|
| Potentiel standard | $E^0$ | **+0.36** | V vs Ag/AgCl | Réversible |
| Constante de vitesse | $k^0$ | 1×10⁻⁵ | m/s | Quasi-réversible |
| Coefficient de transfert | $\alpha$ | 0.5 | — | Symétrique |
| Nombre d'électrons | $n$ | 1 | — | — |
| Coefficient de diffusion | $D$ | 7.6×10⁻¹⁰ | m²/s | Identique ox/red |

### Équation de Butler-Volmer

$$i = i_0 \left[ \exp\left(\alpha f \eta\right) - \exp\left(-(1-\alpha) f \eta\right) \right]$$

où $\eta = E - E^0$ est la surtension et $i_0 = nFAk^0 c$ le courant d'échange.

---

## 3. Oxydes métalliques (études 3 & 4)

### Équations redox de formation des oxydes

La nature du film passif dépend du métal et du pH. Voici les demi-réactions d'oxydation anodique en milieu aqueux.

> **Note** : tous les potentiels sont exprimés **vs Ag/AgCl (KCl sat.)** ($E_{\text{Ag/AgCl}} = E_{\text{SHE}} - 0.197$ V).

#### Or (Au) — oxydation multi-sites

$$2\text{Au} + 6\text{OH}^- \longrightarrow \text{Au}_2\text{O}_3 + 3\text{H}_2\text{O} + 6e^-$$

L'or forme un oxyde réversible à tous les pH. En milieu alcalin, la forme hydroxyde Au(OH)₃ (β-oxyde) est préférentiellement formée. Le plateau d'oxydation est modélisé par 20 sites uniformes.

#### Nickel (Ni) — comportement dépendant du pH

**Dissolution en milieu acide** (pH < 2) :

$$\text{Ni} \longrightarrow \text{Ni}^{2+} + 2e^- \quad (E^0 = -0.454 \text{ V vs Ag/AgCl})$$

**Transition Ni(II) → Ni(III)** (pH ≥ 7, couple actif en CV) :

$$\text{Ni(OH)}_2 + \text{OH}^- \longrightarrow \text{NiOOH} + \text{H}_2\text{O} + e^-$$

Ce couple est réversible à pH 13 et partiellement visible à pH 7 (signal faible, chevauche le plateau Au).

#### Cuivre (Cu) — oxydation séquentielle

**Dissolution en milieu acide** (pH < 4) :

$$\text{Cu} \longrightarrow \text{Cu}^{2+} + 2e^- \quad (E^0 = +0.14 \text{ V vs Ag/AgCl})$$

**Première oxydation** — formation de Cu₂O (pH ≥ 7) :

$$2\text{Cu} + 2\text{OH}^- \longrightarrow \text{Cu}_2\text{O} + \text{H}_2\text{O} + 2e^-$$

**Seconde oxydation** — formation de CuO :

$$\text{Cu}_2\text{O} + 2\text{OH}^- \longrightarrow 2\text{CuO} + \text{H}_2\text{O} + 2e^-$$

### Réaction de surface (modèle de Langmuir)

$$M + H_2O \rightleftharpoons MOH + H^+ + e^-$$

où $M$ = Au, Ni, ou Cu.

### Potentiels standard — pH 1 (H₂SO₄)

| Métal | Mécanisme | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | $\Delta E_{hyst}$ (mV) |
|-------|-----------|:--------------:|:---------------:|:----------------------:|
| **Au** | Oxyde réversible | 1.10 → 1.50 | 0.90 | 200–600 |
| **Ni** | Dissolution | −0.454 | — | — |
| **Cu** | Dissolution | +0.14 | — | — |

### Potentiels standard — pH 7 (tampon phosphate)

| Métal | Mécanisme | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Remarque |
|-------|-----------|:--------------:|:---------------:|----------|
| **Au** | Oxyde réversible | 0.70 → 1.10 | 0.50 | Multi-sites (20) |
| **Ni** | Oxyde partiel | +0.78 | +0.59 | Ni(OH)₂/NiOOH, Nernst depuis pH 13 |
| **Cu** | Oxyde partiel | −0.15 / +0.05 | −0.275 | Cu₂O (60%) + CuO (40%) |

### Potentiels standard — pH 13 (KOH 0.1M)

| Métal | Mécanisme | $E^0_{ox}$ (V) | $E^0_{red}$ (V) | Remarque |
|-------|-----------|:--------------:|:---------------:|----------|
| **Au** | Oxyde réversible | 0.25 → 0.65 | +0.15 | β-oxyde Au(OH)₃, multi-sites (20) |
| **Ni** | Oxyde réversible | +0.43 | +0.24 | Ni(OH)₂ ↔ NiOOH |
| **Cu** | Oxyde réversible | −0.38 / +0.08 | −0.76 | Cu₂O (50%) + CuO (50%) |

### Paramètres cinétiques de surface

| Paramètre | Au | Ni | Cu | Unité |
|-----------|:--:|:--:|:--:|-------|
| $k_0$ | 2.0 | 5.0 | 5.0 | s⁻¹ |
| $\Gamma_{max}$ | 4×10⁻⁵ | 3×10⁻⁵ | 3.5×10⁻⁵ | mol/m² |
| $\alpha$ | 0.5 | 0.5 | 0.5 | — |

**Note** : $k_0$ est en **s⁻¹** (réaction de surface), pas en m/s !

---

## 4. Murs électrochimiques (HER/OER)

### Réactions

| Réaction | Équation | $E^0$ (V vs SHE) |
|----------|----------|------------------|
| **HER** (cathodique) | $2H^+ + 2e^- \to H_2$ | 0.00 |
| **OER** (anodique) | $2H_2O \to O_2 + 4H^+ + 4e^-$ | +1.23 |

### Potentiels d'onset pratiques (vs Ag/AgCl sat.)

Le modèle utilise des potentiels d'onset empiriques (avec surtension) :

$$E_{HER}(pH) = -0.10 - 0.059 \times pH \text{ V}$$
$$E_{OER}(pH) = +1.50 - 0.059 \times pH \text{ V}$$

| pH | $E_{HER}$ (V) | $E_{OER}$ (V) | Fenêtre (V) |
|:--:|:-------------:|:-------------:|:-----------:|
| 1.0 | −0.159 | +1.441 | 1.600 |
| 7.0 | −0.513 | +1.087 | 1.600 |
| 13.0 | −0.867 | +0.733 | 1.600 |

---

## 5. Hypothèses et limites des modèles

### Étude 1 & 2 — Couple redox en solution

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| Diffusion 1D semi-infinie | Électrode plane, solution calme | Ignore convection naturelle |
| Espèces en excès | Électrolyte support >> espèces actives | Pas de migration |
| $D_{ox} = D_{red}$ | Simplification | Peut affecter $\Delta E_p$ |

### Étude 3 & 4 — Oxydes de surface

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| **Modèle de Langmuir** | Adsorption localisée, $\theta \in [0,1]$ | Ignore interactions latérales |
| $E^0_{ox} \neq E^0_{red}$ | Hystérésis expérimentale observée | Empirique, pas mécanistique |
| Multi-sites (Au) | Élargissement du pic d'oxydation | Distribution arbitraire (20 sites) |
| Ni partiel à pH 7 | Ni(OH)₂/NiOOH visible mais faible | Signal chevauche plateau Au |
| Ni/Cu dissolution pH < 2 | Diagramme de Pourbaix | Pas de retour cathodique |

### Ce que le modèle **ne capture pas**

- Nucléation et croissance des oxydes
- Restructuration de surface
- Effets de grain et orientation cristalline
- Cinétique de diffusion dans l'oxyde
- Interactions métal-métal dans les alliages

---

*Ces données proviennent de parameters_oxide.py (run 07, 2026-02-05) — source unique de vérité.*
