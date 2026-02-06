# Équations clés

**Sommaire :**
1. Transport de masse
2. Cinétique à l'Électrode (Butler-Volmer)
3. Signal de potentiel (cycles)
4. Analyse morphologique
5. Diagnostics : réversibilité et vitesse
6. Spectroscopie d'impédance électrochimique (EIS)
7. Références bibliographiques

---

La modélisation de la voltamétrie cyclique repose sur la résolution du transport de masse des espèces électroactives couplé à la cinétique de transfert de charge à l'interface électrode/électrolyte.

## 1. Transport de masse

Dans une solution support en excès, la migration est négligée. Le transport est régi par la loi de diffusion de Fick :

$$ \frac{\partial c_i}{\partial t} = D_i \nabla^2 c_i $$

Où :
- $c_i$ est la concentration de l'espèce $i$ (Oxydant $O$ ou Réducteur $R$) [mol/m³]
- $D_i$ est le coefficient de diffusion [m²/s]

## 2. Cinétique à l'Électrode (Butler-Volmer)

Le flux molaire à la surface de l'électrode de travail (WE) est défini par la relation de Butler-Volmer :

$$ J = k^0 \left[ c_R \exp\left(\frac{\alpha n F}{RT} \eta\right) - c_O \exp\left(-\frac{(1-\alpha) n F}{RT} \eta\right) \right] $$

Où :
- $J$ = flux molaire à la surface [mol/(m²·s)]
- $k^0$ = constante cinétique standard [m/s]
- $c_R$ = concentration du réducteur à la surface [mol/m³]
- $c_O$ = concentration de l'oxydant à la surface [mol/m³]
- $\alpha$ = coefficient de transfert de charge (sans dimension)
- $n$ = nombre d'électrons échangés
- $F$ = constante de Faraday (96485 C/mol)
- $R$ = constante des gaz parfaits (8.314 J/(mol·K))
- $T$ = température [K]
- $\eta = E(t) - E^0$ = surtension d'activation [V]

### Paramètres de simulation

| Paramètre | Symbole | Valeur |
|-----------|---------|--------|
| Constante de Faraday | $F$ | 96485 C/mol |
| Constante des gaz | $R$ | 8.314 J/(mol·K) |
| Température | $T$ | 298.15 K |
| Coefficient de transfert | $\alpha$ | 0.5 |
| Vitesse de réaction standard | $k^0$ | ~10⁻⁵ m/s |

## 3. Signal de potentiel (cycles)

Le potentiel appliqué $E(t)$ suit un signal triangulaire périodique :

$$ E(t) = \begin{cases} E_{start} + v \cdot t & \text{Aller (Anodique)} \\ E_{vertex} - v \cdot t & \text{Retour (Cathodique)} \end{cases} $$

Où :
- $E_{start}$ = potentiel initial [V]
- $E_{vertex}$ = potentiel de retournement [V]
- $v$ = vitesse de balayage [V/s]
- $t$ = temps [s]

L'enregistrement de plusieurs cycles permet de vérifier la stabilité du système (conditionnement de l'électrode) ou d'observer des réactions secondaires (adsorption, passivation).

## 4. Analyse morphologique : d'où vient la forme ?

L'allure caractéristique en "bec de canard" du voltammogramme résulte d'une compétition entre deux phénomènes antagonistes :

1. **La montée du courant (contrôle cinétique)** : l'augmentation du potentiel ($\eta$) accélère exponentiellement la vitesse de transfert d'électrons (loi de Butler-Volmer).

2. **Le pic et la chute (contrôle diffusif)** : À force de consommer l'espèce réactive à la surface, sa concentration locale chute vers zéro (déplétion). Il se crée une **couche de diffusion** dont l'épaisseur $\delta(t)$ augmente avec le temps ($\delta \propto \sqrt{Dt}$).

## 5. Diagnostics : réversibilité et vitesse

### 5.1 L'écart de pic ($\Delta e_p$)

C'est la différence de potentiel entre le pic anodique et le pic cathodique : $\Delta E_p = |E_{pa} - E_{pc}|$.

| Type de système | Caractéristique |
|-----------------|-----------------|
| **Réversible (Rapide)** | $\Delta E_p \approx 59/n$ mV (constant) |
| **Quasi-Réversible** | $\Delta E_p$ augmente avec $v$ |
| **Irréversible (Lent)** | Pics très écartés |

### 5.2 Influence de la vitesse ($v$)

Pour un système réversible, le courant de pic suit l'équation de **Randles-Sevcik** :

$$ I_p = (2.69 \times 10^5) \, n^{3/2} \, A \, D^{1/2} \, C^* \, v^{1/2} $$

Où :
- $I_p$ = courant de pic [A]
- $n$ = nombre d'électrons échangés
- $A$ = surface de l'électrode [cm²]
- $D$ = coefficient de diffusion [cm²/s]
- $C^*$ = concentration en solution [mol/cm³]
- $v$ = vitesse de balayage [V/s]

**Diagnostic** :
- Si $I_p \propto \sqrt{v}$ : processus contrôlé par la diffusion pure
- Si $I_p \propto v$ : processus impliquant des espèces adsorbées (capacitif)

---

## 6. Spectroscopie d'impédance électrochimique (EIS)

### 6.1 Impédance complexe

L'EIS mesure la réponse en courant à une perturbation sinusoïdale de potentiel. L'impédance complexe est :

$$Z(\omega) = \frac{\Delta E}{\Delta I} \cdot e^{j\varphi} = Z'(\omega) + j Z''(\omega)$$

où $\omega = 2\pi f$ est la pulsation angulaire et $\varphi$ le déphasage entre courant et tension.

### 6.2 Éléments d'impédance

| Élément | Expression | Domaine |
|---------|------------|---------|
| Résistance | $Z_R = R$ | Réel pur |
| CPE | $Z_{CPE} = \frac{1}{Q_0 (j\omega)^n}$ | $n=1$ → capacité, $n<1$ → non idéal |
| Warburg | $Z_W = \frac{\sigma}{\sqrt{\omega}}(1-j)$ | Droite à 45° sur Nyquist |

### 6.3 Circuit de Randles (EIS couple redox)

$$Z(\omega) = R_s + \frac{1}{\frac{1}{Z_{CPE}} + \frac{1}{R_{ct} + Z_W}}$$

Circuit : $R_s$ en série avec le parallèle de $CPE_{dl}$ et ($R_{ct} + Z_W$).

### 6.4 Circuit à 2 constantes de temps (EIS électrodes Au/Ni/Cu)

Utilisé quand un film passif se forme sur l'électrode (pH ≥ 7 avec Ni ou Cu) :

$$Z(\omega) = R_s + Z_{film\parallel} + Z_{dl\parallel}$$

avec $Z_{film\parallel} = \frac{R_{film} \cdot Z_{CPE,film}}{R_{film} + Z_{CPE,film}}$ et $Z_{dl\parallel} = \frac{(R_{ct} + Z_W) \cdot Z_{CPE,dl}}{(R_{ct} + Z_W) + Z_{CPE,dl}}$

### 6.5 Résistance de transfert de charge

$R_{ct}$ est calculée à partir des paramètres physiques du couple redox :

$$R_{ct} = \frac{RT}{n^2 F^2 A \, k^0 \, c}$$

où $A$ = surface de l'électrode ($1.77 \times 10^{-6}$ m²), $k^0$ = constante de vitesse standard (m/s), $c$ = concentration (mol/m³).

### 6.6 Coefficient de Warburg

Pour un couple équimolaire ($D_O = D_R = D$, $c_O = c_R = c$) :

$$\sigma = \frac{RT}{n^2 F^2 A \sqrt{2}} \cdot \frac{2}{\sqrt{D} \cdot c}$$

### 6.7 Capacité effective de double couche

Au sommet du semicercle de Nyquist (pulsation $\omega_{max}$) :

$$C_{dl,eff} = \frac{1}{\omega_{max} \cdot R_{ct}}$$

### 6.8 Diagnostics

| Observation Nyquist | Interprétation |
|---------------------|----------------|
| Semicercle net + droite 45° | $R_{ct}$ et $\sigma$ comparables — régime mixte |
| Droite 45° uniquement | $k^0$ élevé → $R_{ct} \approx 0$, diffusion pure |
| Semicercle seul | $D$ élevé → $\sigma \approx 0$, transfert de charge pur |
| Semicercle aplati | $n_{CPE} < 1$ — surface hétérogène |
| 2 arcs distincts | Film passif (EIS électrodes Au/Ni/Cu) — 2 constantes de temps |

---

## 7. Références bibliographiques

*Note : Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
