# Analyse commerciale et comportement client d’un e-commerce

**Étude de cas Lapage - Python, analyse temporelle des ventes et tests statistiques**

> Transformer 687 534 lignes de ventes en leviers de pilotage du chiffre d’affaires, du mix produit et de la connaissance client.

## Synthèse

Lapage est une librairie ayant développé une activité de vente en ligne. L’objectif de cette étude est d’évaluer la performance commerciale du site, d’identifier les facteurs expliquant les variations du chiffre d’affaires et de mieux comprendre les comportements d’achat.

L’analyse couvre **24 mois**, de mars 2021 à février 2023, et consolide trois sources : transactions, produits et clients.

| Indicateur | Résultat |
|---|---:|
| Chiffre d’affaires analysé | **12,03 M€** |
| Lignes de ventes | **687 534** |
| Clients acheteurs | **8 600** |
| Références produits | **3 286** |
| Clients inscrits sans transaction | **21** |

## Besoin métier

- Mesurer la performance globale de l’activité en ligne.
- Comprendre les variations mensuelles du chiffre d’affaires.
- Identifier les catégories et produits les plus contributeurs.
- Mesurer la concentration du chiffre d’affaires par client.
- Étudier les liens entre le profil des clients et leurs comportements d’achat.
- Formuler des recommandations commerciales directement exploitables.

## Données et qualité

Le fichier de transactions comportait initialement **1 048 575 lignes**, dont **361 041 lignes entièrement vides** issues de l’export. Elles ont été identifiées et supprimées avant l’analyse, sans perte de transaction exploitable.

Les contrôles réalisés ont ensuite confirmé :

- l’absence de doublons dans les trois sources ;
- l’absence de valeur manquante dans les lignes conservées ;
- le rattachement de chaque transaction à un client et à un produit référencé ;
- la couverture complète de la période, y compris février 2023.

Les données sources ne sont pas publiées dans ce portfolio. Pour reproduire l’analyse localement, il faut disposer des trois fichiers pédagogiques `customers.csv`, `products.csv` et `Transactions.csv` dans un dossier `data/`.

## Démarche analytique

1. Contrôle de la qualité et des clés de jointure.
2. Consolidation des transactions, produits et clients.
3. Construction des indicateurs mensuels : chiffre d’affaires, transactions, clients actifs et panier moyen.
4. Analyse valeur/volume du mix produit.
5. Étude de la concentration client par courbe de Lorenz et méthode IQR.
6. Tests statistiques adaptés à la nature des variables :
   - Chi² et V de Cramer ;
   - corrélations de Pearson et Spearman ;
   - Jarque-Bera et Levene ;
   - Kruskal-Wallis et Mann-Whitney avec correction de Bonferroni.
7. Traduction des résultats en recommandations opérationnelles.

## Principaux résultats

### La baisse de février 2023 provient du volume

Entre janvier et février 2023 :

- le chiffre d’affaires diminue de **12 %** ;
- le nombre de transactions diminue de **11 %** ;
- le panier moyen reste pratiquement stable, de **35,07 € à 34,93 €**.

La baisse observée est donc principalement liée au recul du nombre de transactions, et non à une dégradation du panier moyen.

### Valeur et volume nécessitent deux pilotages distincts

Seuls **2 produits** figurent simultanément dans les Top 10 chiffre d’affaires et volume. Le prix moyen des produits du Top CA atteint **57,97 €**, contre **20,26 €** pour le Top volume.

Les produits générateurs de revenus et les produits générateurs de trafic ne répondent donc pas aux mêmes logiques commerciales.

### La concentration client reste modérée, mais certains profils pèsent fortement

- Les **20 %** de clients les plus contributeurs génèrent **48,1 % du chiffre d’affaires**.
- Les clients atypiques représentent **2,92 % de la base**, mais contribuent à **15,91 % du chiffre d’affaires**.

Ces profils doivent être suivis spécifiquement, sans être qualifiés de BtoB en l’absence d’une variable dédiée.

### L’âge est plus structurant que le genre

Le test du Chi² indique une association entre le genre et les catégories achetées, mais le V de Cramer de **0,0152** montre que son intensité est négligeable.

L’âge est davantage associé aux comportements d’achat, notamment au panier moyen :

- Pearson : **-0,6165** ;
- Spearman : **-0,7004**.

Ces résultats décrivent des associations statistiques et ne démontrent pas de relation causale.

## Recommandations opérationnelles

- Suivre conjointement le chiffre d’affaires, le nombre de transactions et le panier moyen.
- Piloter séparément les produits à fort chiffre d’affaires et les produits à fort volume.
- Adapter les recommandations produits et les campagnes aux profils d’âge observés.
- Qualifier les clients atypiques et analyser les inscrits sans transaction.
- Enrichir la base avec les marges, stocks, ruptures, campagnes, trafic web et typologie BtoB/BtoC.

## Limites et prochaines étapes

L’analyse temporelle est descriptive : elle ne comprend ni décomposition saisonnière ni prévision. L’absence de données de marge empêche également d’évaluer la rentabilité réelle des produits et des clients.

Une prochaine version pourrait intégrer :

- une décomposition tendance/saisonnalité ;
- un modèle de prévision du chiffre d’affaires ;
- des indicateurs de marge et de rentabilité ;
- une segmentation BtoB/BtoC ;
- le croisement des ventes avec le trafic, les campagnes et les stocks.

## Livrables publiés

- [`notebooks/analyse-ventes-clients.ipynb`](notebooks/analyse-ventes-clients.ipynb) : analyse Python complète avec sorties conservées ;
- [`reports/presentation.pdf`](reports/presentation.pdf) : présentation de la démarche, des résultats et des recommandations ;
- [`images/diagnostic-ventes.png`](images/diagnostic-ventes.png) : diagnostic synthétique de la baisse observée en février 2023 ;
- [`README.md`](README.md) : synthèse publique orientée recruteur, manager et client.

## Exécution locale

1. Créer un dossier `data/` à la racine de ce projet, puis y placer `customers.csv`, `products.csv` et `Transactions.csv`.
2. Créer un environnement Python et installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Ouvrir `notebooks/analyse-ventes-clients.ipynb` dans Jupyter Notebook ou JupyterLab.

## Compétences démontrées

- Analyse commerciale et pilotage de la performance
- Analyse temporelle de données de ventes
- Contrôle qualité et consolidation multi-sources
- Analyse de concentration et détection de profils atypiques
- Tests d’hypothèses et mesure de l’intensité des relations
- Data visualisation et restitution à un public non technique
- Recommandations orientées décision

## Outils

Python · Pandas · NumPy · Matplotlib · Seaborn · SciPy · Jupyter Notebook · PowerPoint

---

**Joana D’Arc Soares Aubry**  
Projet réalisé dans le cadre de la formation Data Analyst d’OpenClassrooms.
