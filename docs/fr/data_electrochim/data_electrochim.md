# Données électrochimiques

**Sommaire :**
1. Constantes fondamentales
2. Oxydes de surface et cinétique (étude 1 — CV)
3. Paramètres d'impédance à l'OCP (étude 2 — EIS)
4. Murs électrochimiques (HER/OER)
5. Hypothèses et limites des modèles

---

## 1. Constantes fondamentales

| Constante | Symbole | Valeur | Unité |
|-----------|---------|--------|-------|
| Constante de Faraday | $F$ | 96 485 | C/mol |
| Constante des gaz | $R$ | 8.314 | J/(mol·K) |
| Température standard | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.92 | V⁻¹ |
| Surface d'électrode | $A$ | 1.77×10⁻⁶ | m² |

---

## 2. Oxydes de surface et cinétique (étude 1 — CV)

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

## 3. Paramètres d'impédance à l'OCP (étude 2 — EIS)

### 3.1 Potentiel de circuit ouvert (OCP)

L'EIS est réalisée au **potentiel de circuit ouvert** (OCP, *open circuit potential*), c'est-à-dire le potentiel auquel le courant net traversant l'électrode est nul. Ce potentiel résulte de l'équilibre entre réactions anodiques et cathodiques à la surface ; il dépend donc du métal et du pH.

Les valeurs ci-dessous sont estimées à partir des **diagrammes de Pourbaix** et de mesures expérimentales publiées :

| Métal | pH 3 | pH 7 | pH 11 | Domaine Pourbaix à l'OCP | Sources |
|-------|:----:|:----:|:-----:|--------------------------|---------|
| **Au** | +0.50 V | +0.15 V | −0.10 V | Capacitif (pas d'oxyde) | Hamelin 1994 [1], Song 2025 [2] |
| **Ni** | −0.25 V | −0.20 V | +0.10 V | Corrosion → dissolution → passivation | Beverskog 1997 [3] |
| **Cu** | +0.02 V | −0.20 V | −0.40 V | Cu²⁺ → Cu₂O → Cu₂O/CuO | Beverskog 1997 [4], Ambrose 1973 [9] |

> Potentiels **vs Ag/AgCl (KCl sat.)**. Pour les alliages : $E_{ocp} \approx \sum x_i \cdot E_{ocp,i}$ (approximation de potentiel mixte).

**Interprétation** :
- **Au** est noble : son OCP reste positif en milieu acide et neutre, dans le domaine capacitif (pas de réaction faradique). À pH 11, il descend juste en dessous du seuil de formation du β-oxide Au(OH)₃, d'où l'apparition d'un film passif.
- **Ni** a l'OCP le plus négatif à pH 3 (dissolution active Ni → Ni²⁺). En milieu alcalin, la formation du film Ni(OH)₂ stabilise la surface et l'OCP remonte en zone passive.
- **Cu** suit la transition Cu/Cu²⁺ (acide) → Cu/Cu₂O (neutre/alcalin), en accord avec les diagrammes de Pourbaix. À pH 7, l'OCP est proche de −0.20 V, cohérent avec le potentiel de stabilité de Cu₂O mesuré par méthodes pulsées (JACS 2024 : −0.27 V).

### 3.2 Résistance de transfert de charge (Rct)

Le Rct traduit la vitesse de la réaction faradique à l'OCP. Il est relié au courant d'échange par la relation de Butler-Volmer linéarisée : $R_{ct} = RT/(nFi_0)$. Un Rct élevé signifie une interface peu réactive (cinétique lente ou film protecteur).

| pH | Au (Ω) | Ni (Ω) | Cu (Ω) | Tendance physique |
|:--:|:------:|:------:|:------:|-------------------|
| 3 | 1 200 | 700 | 500 | Ni/Cu dissolvent activement → Rct faible |
| 7 | 5 000 | 1 500 | 2 000 | Au inerte → Rct élevé ; Ni instable sans film |
| 11 | 2 000 | 8 000 | 4 000 | Ni : film Ni(OH)₂ très protecteur → Rct ×10 |

Sources : Hamelin 1994 [1] (Au/H₂SO₄), Beverskog 1997 [3,4] (Pourbaix Ni/Cu), Weininger 1963 [8] (Ni/NaOH), Ambrose 1973 [9] (Cu alcalin).

> **Validation** : le Rct mesuré expérimentalement sur Au polycristallin dans H₂SO₄ donne 900–1 300 Ω·cm² (Piela & Wrona, *Electrochim. Acta* 1995). Pour Ni en milieu acide, Saleh *et al.* (*Sci. Rep.* 2025) rapportent 900–990 Ω·cm² — nos 700 Ω sont dans la gamme basse, cohérent avec un pH plus acide.

### 3.3 Film passif et capacité de double couche

**R_film** — Nul à pH 3 (pas de film : dissolution active), il apparaît dès que le métal se passive :

| pH | Au | Ni | Cu | Commentaire |
|:--:|:--:|:--:|:--:|-------------|
| 3 | 0 | 0 | 0 | Tous en dissolution, pas de film stable |
| 7 | 0 | 0 ⚠️ | 400 Ω | ⚠️ Ni instable à pH 7 (ACS Omega 2017 [6]) |
| 11 | 150 Ω | 2 000 Ω | 800 Ω | Films stables sur tous les métaux |

Le R_film de Ni à pH 11 (2 000 Ω) est le plus élevé, reflétant un film Ni(OH)₂/NiOOH compact et protecteur — cohérent avec les mesures de Weininger & Breiter (1963) sur Ni en NaOH.

**Q₀ (CPE)** — Capacité de double couche non idéale : 25–50 µF·s^(n-1)/cm² avec exposant $n \approx 0.85$–$0.94$. Ces valeurs sont typiques d'électrodes polycristallines (Lazanas 2023 [11]). L'exposant $n$ diminue avec l'augmentation de Ni et Cu dans l'alliage (surface plus hétérogène).

> Les paramètres complets (Q₀, n, σ, Q_film, n_film) et les lois de mélange pour alliages sont détaillés dans l'onglet **Physique** de l'étude EIS.

### Références EIS

| # | Référence | Donnée utilisée |
|---|-----------|-----------------|
| [1] | Hamelin *et al.* (1994) — *Electrochim. Acta* — Au dans H₂SO₄ | Rct Au pH 3, Cdl Au |
| [2] | Song *et al.* (2025) — *ChemElectroChem* | Cdl vs pH pour Au |
| [3] | Beverskog & Puigdomenech (1997) — *Corros. Sci.* 39, 969 | Pourbaix Ni, OCP Ni |
| [4] | Beverskog & Puigdomenech (1997) — *J. Electrochem. Soc.* 144, 3476 | Pourbaix Cu, OCP Cu |
| [6] | ACS Omega (2017) — DOI: 10.1021/acsomega.6b00448 | Instabilité NiOOH pH 7 |
| [8] | Weininger & Breiter (1963) — *J. Electrochem. Soc.* 110, 484-490 | Rct Ni, R_film Ni pH 11 |
| [9] | Ambrose *et al.* (1973) — *J. Electroanal. Chem.* 47, 47 | R_film Cu alcalin |
| [11] | Lazanas & Prodromidis (2023) — *ACS Meas. Sci. Au* 3(3), 162 | CPE, gammes typiques |

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

### Étude 1 — CV oxydes de surface

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| **Modèle de Langmuir** | Adsorption localisée, $\theta \in [0,1]$ | Ignore interactions latérales |
| $E^0_{ox} \neq E^0_{red}$ | Hystérésis expérimentale observée | Empirique, pas mécanistique |
| Multi-sites (Au) | Élargissement du pic d'oxydation | Distribution arbitraire (20 sites) |
| Ni partiel à pH 7 | Ni(OH)₂/NiOOH visible mais faible | Signal chevauche plateau Au |
| Ni/Cu dissolution pH < 2 | Diagramme de Pourbaix | Pas de retour cathodique |

### Étude 2 — EIS à l'OCP

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| **Simulation à l'OCP** | État stationnaire reproductible | Pas d'exploration d'autres potentiels |
| **OCP par potentiel mixte** | $E_{ocp} = \sum x_i E_{ocp,i}$ | Ignore interactions galvaniques |
| **Rct bibliographiques** | Valeurs typiques publiées | Pas dérivés de Butler-Volmer |
| **CPE au lieu de C pure** | Surfaces réelles rugueuses | n empirique, pas relié à la géométrie |
| **Ni instable à pH 7** | ACS Omega 2017, Pourbaix | Simplifié (pas de film transitoire) |

### Ce que les modèles **ne capturent pas**

- Nucléation et croissance des oxydes
- Restructuration de surface
- Effets de grain et orientation cristalline
- Cinétique de diffusion dans l'oxyde
- Interactions métal-métal dans les alliages (couplage galvanique)
- Dépendance en potentiel des paramètres EIS (Rct varie avec E)

---

*Étude 1 : parameters_oxide.py — Étude 2 : parameters_eis.py (run 04_EIS_with_OCP, 2026-02-06).*
