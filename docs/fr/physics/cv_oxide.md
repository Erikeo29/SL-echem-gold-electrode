**Sommaire :**
1. Principe et différence avec l'étude 1
2. Modèle physique
3. Hypothèses et limites
4. Dépendance au pH
5. Schéma numérique
6. Validation et résultats

---

## 1. Principe et différence avec CV couple redox

| Aspect | CV couple redox | CV oxydes métalliques |
|--------|:---------------------:|:----------------:|
| Espèces redox | En solution | Adsorbées à la surface |
| Transport | Diffusion (FEM 2D) | **Aucun** |
| Variable | $c(x,y,t)$ | $\theta(t) \in [0,1]$ |
| ΔEp typique | ~60 mV (réversible) | **100–2000 mV** |
| Solver | Newton non-linéaire | Analytique |

Ce modèle traite les **réactions de surface** : formation et réduction d'oxydes/hydroxydes métalliques directement sur l'électrode.

---

## 2. Modèle physique

### 2.1 Réactions

**Formation d'oxydes** (pH ≥ 7 pour Cu, pH ≥ 12 pour Ni) :

$$M + H_2O \rightleftharpoons MOH + H^+ + e^-$$

où $M$ = Au, Ni ou Cu.

**Dissolution** (pH acide : Ni à pH < 2, Cu à pH < 4) :

$$M \longrightarrow M^{n+} + ne^- \quad \text{(irréversible)}$$

### 2.2 Cinétique de Langmuir-Butler-Volmer

$$\frac{d\theta}{dt} = k_{ox}(E) \cdot (1 - \theta) - k_{red}(E) \cdot \theta$$

avec :
- $k_{ox}(E) = k_0 \exp\left(\alpha f (E - E^0_{ox})\right)$
- $k_{red}(E) = k_0 \exp\left(-(1-\alpha) f (E - E^0_{red})\right)$

**Point essentiel** : $E^0_{ox} \neq E^0_{red}$ pour capturer l'hystérésis caractéristique des oxydes de surface.

### 2.3 Courant

$$I = \sum_i f_i \cdot n F A \Gamma_{max,i} \frac{d\theta_i}{dt} + I_{HER} + I_{OER} + I_{C_{dl}}$$

*Pour les valeurs de $E^0$, $k_0$, $\Gamma_{max}$ : voir la page **Données électrochimiques**.*

---

## 3. Hypothèses et limites

### Ce que le modèle capture

| Phénomène | Comment |
|-----------|---------|
| Hystérésis des oxydes | $E^0_{ox} \neq E^0_{red}$ (empirique) |
| Élargissement du pic Au | Modèle multi-sites (20 sites uniformes) |
| Effet du pH | Potentiels tabulés par pH (1, 7, 13) |
| Murs HER/OER | Butler-Volmer aux limites |
| Double couche | $I_{Cdl} = C_{dl} \cdot A \cdot \nu$ |
| Dissolution Ni/Cu en acide | Butler-Volmer irréversible (pas de retour cathodique) |

### Hypothèses fortes du modèle de Langmuir

| Hypothèse | Réalité | Impact |
|-----------|---------|--------|
| Sites équivalents | Hétérogénéité de surface | Multi-sites compense partiellement |
| Pas d'interactions latérales | Oxydes se restructurent | ΔEp sous-estimé |
| Adsorption localisée | Nucléation et croissance | Forme des pics simplifiée |

### Ce que le modèle ne capture pas

- Nucléation et croissance des oxydes (cinétique non-Langmuir)
- Effets d'orientation cristalline
- Interactions métal-métal dans les alliages
- Cinétique de diffusion dans l'oxyde

### Comportement du Ni selon le pH

Le mécanisme du nickel change selon le pH :

| pH | Mécanisme | Comportement |
|----|-----------|-------------|
| 1 | Dissolution | Ni → Ni²⁺ en solution (irréversible) |
| 7 | Oxyde partiel | Ni(OH)₂/NiOOH faiblement visible, chevauche le plateau Au |
| 13 | Oxyde réversible | Couple Ni(OH)₂/NiOOH bien défini |

À pH 7, le signal Ni est présent mais faible car le couple Ni(OH)₂/NiOOH n'est que partiellement stable. Les potentiels sont décalés par Nernst (+0.354 V depuis pH 13).

---

## 4. Dépendance au pH

Les potentiels des oxydes suivent la loi de Nernst :

$$E^0 = E^0_{pH=0} - 0.059 \times pH$$

Les fenêtres de potentiel sont adaptées par pH pour rester dans la zone exploitable (entre HER et OER).

| pH | Électrolyte | E_min (V) | E_max (V) | Fenêtre totale (V) |
|:--:|-------------|:---------:|:---------:|:-------------------:|
| 1 | H₂SO₄ | −0.409 | +1.591 | 2.000 |
| 7 | Tampon phosphate | −0.763 | +1.237 | 2.000 |
| 13 | KOH 0.1M | −1.117 | +0.883 | 2.000 |

---

## 5. Schéma numérique

L'ODE est **linéaire en θ** → solution analytique exacte :

$$\theta^{n+1} = \frac{\theta^n + \Delta t \cdot k_{ox}}{1 + \Delta t \cdot (k_{ox} + k_{red})}$$

**Propriétés** :
- Inconditionnellement stable
- Garantit $\theta \in [0, 1]$ (avec clampage)
- Pas de solveur non-linéaire

---

## 6. Validation et résultats

### Comportements observés conformes à la littérature

| Observation | Simulation | Littérature | OK |
|-------------|:----------:|:-----------:|:--:|
| Pic réduction Au (pH 1) | ~0.9 V | 0.85–0.95 V | oui |
| Pic réduction Au (pH 13) | ~0.15 V | 0.10–0.20 V | oui |
| Hystérésis Au | 200–600 mV | 250–600 mV | oui |
| Pic Ni(OH)₂/NiOOH (pH 13) | +0.43/+0.24 V | +0.40–0.50 V | oui |
| Ni faible à pH 7 | Signal partiel | Signal faible attendu | oui |
| Dissolution Ni/Cu (pH 1) | Irréversible | Pourbaix : corrosion | oui |

### Limites observées

- ΔEp parfois très élevé pour Au pur (~2000 mV) → seuil HER/OER atteint
- Cu à pH 1 : dissolution modélisée mais pas les produits de corrosion
- Au β-oxide (pH 13) : onset empirique, pas mécanistique

---

*Les paramètres électrochimiques détaillés sont dans la page **Données électrochimiques** du menu Général.*

---

## 7. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
