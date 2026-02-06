# Conclusion et perspectives

**Sommaire :**
1. Conclusion
2. Perspectives

---

## 1. Conclusion

Les deux études présentées donnent des exemples de modélisations électrochimiques sur une électrode d'or avec impuretés de nickel et de cuivre :

- **Étude 1** (CV électrode Au/Ni/Cu) : les oxydes métalliques Au/Ni/Cu, résolus par ODE analytique, offrent une première approche de la caractérisation d'électrodes multi-métalliques. Les effets du pH et de la capacité de double couche sont qualitativement conformes aux attentes.

- **Étude 2** (EIS électrode Au/Ni/Cu) : la spectroscopie d'impédance sur la même électrode Au/Ni/Cu, avec circuit adaptatif (Randles / 2 constantes de temps), permet d'explorer l'extraction de grandeurs comme $R_{ct}$, $C_{dl}$ et $R_{film}$. Ces résultats sont complémentaires des métriques CV de l'étude 1.

Ces travaux constituent un point de départ pour des études plus approfondies, et non une caractérisation définitive des systèmes considérés. Une validation expérimentale reste nécessaire.

---

## 2. Perspectives

- Couplage avec des réactions chimiques homogènes (mécanismes EC, ECE)
- Extension aux géométries 3D complexes (microélectrodes)
- **Fitting inverse EIS** : partir de données expérimentales → extraire Rs, Rct, Cdl, R_film via `scipy.optimize`
- **Couplage CV–EIS** : utiliser les paramètres cinétiques de l'étude 1 (pH, composition) comme entrée du modèle EIS (étude 2)
- **PINNs (Physics-Informed Neural Networks)** : entraîner un réseau de neurones contraint par les équations de Langmuir-Butler-Volmer pour accélérer la résolution ou l'inversion paramétrique
