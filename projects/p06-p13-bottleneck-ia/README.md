# BottleNeck — amélioration du notebook P6

Ce projet reprend le notebook du projet 6 du parcours Data Analyst et l'améliore dans le cadre du projet 13. La démarche associe fiabilisation des données, analyses métier, comparaisons méthodologiques, POC prédictif, validation automatisée et documentation critique de l'utilisation de l'IA.

## Objectifs

- rapprocher les données ERP, Web et la table de liaison ;
- produire une base analytique contrôlée et traçable ;
- analyser le chiffre d'affaires, les marges, les stocks et les ruptures ;
- comparer plusieurs méthodes statistiques et outils de qualité ;
- tester la faisabilité d'une prédiction du volume mensuel des ventes ;
- documenter les anomalies, décisions, limites et recommandations métier ;
- expérimenter une segmentation non supervisée des profils de stock et de rotation.

## Fichiers sources

Les trois fichiers Excel doivent être placés dans le même répertoire que le notebook :

- `erp.xlsx` : données ERP ;
- `web.xlsx` : export du site e-commerce ;
- `liaison.xlsx` : correspondance entre les identifiants ERP et Web.

Le notebook vérifie leur présence avant le chargement et interrompt explicitement l'exécution si un fichier est absent.

## Organisation recommandée

```text
P13_BottleNeck/
├── P13_BottleNeck_ameliore.ipynb
├── README.md
├── requirements.txt
├── erp.xlsx
├── web.xlsx
├── liaison.xlsx
└── exports/                         # créé automatiquement
```

## Environnement de référence

- Python 3.12.9
- pandas 2.3.3
- NumPy 2.3.5
- Matplotlib 3.10.7
- Seaborn 0.13.2
- OpenPyXL 3.1.5
- scikit-learn 1.9.0
- Joblib 1.5.3
- Pandera 0.32.1

## Installation

Depuis un terminal ouvert dans le répertoire du projet :

```bash
python -m venv .venv
```

Sous Windows :

```powershell
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Sélectionner ensuite l'environnement `.venv` comme kernel Python dans VS Code ou Jupyter.

## Exécution

1. Vérifier que les trois fichiers sources sont présents à côté du notebook.
2. Ouvrir `P13_BottleNeck_ameliore.ipynb`.
3. Sélectionner le kernel de l'environnement `.venv`.
4. Exécuter **Restart Kernel + Run All**.
5. Vérifier que les contrôles finaux affichent le statut `Conforme`.

Le notebook préserve les données brutes dans des DataFrames dédiés et crée des colonnes d'analyse séparées. Les fichiers sources ne sont jamais modifiés.

## Méthodes et POC

- **Prix atypiques** : IQR retenu comme méthode principale ; Z-score conservé comme contrôle complémentaire.
- **Corrélations** : Spearman retenu pour l'interprétation principale ; Pearson conservé comme contrôle complémentaire.
- **Prédiction des ventes** : référence naïve, régression linéaire, régression de Poisson et forêt aléatoire comparées par validation croisée à cinq partitions.
- **Régression linéaire** : conservée comme référence interprétable, mais non retenue en raison de performances insuffisantes, d’un R² de −0,08 et de dix prédictions négatives.
- **Modèle retenu pour le POC** : régression de Poisson sans le stock de fin de mois, avec une MAE de 2,46 unités, un RMSE de 3,31 et un R² de 0,36.
- **Interprétabilité** : les coefficients du modèle de Poisson ont été analysés afin d’estimer l’association entre les variables explicatives et le volume des ventes.
- **Scénario avec stock** : écarté en raison d’un risque de fuite temporelle.
- **Prédiction des ventes** : référence naïve, régression de Poisson et forêt aléatoire comparées par validation croisée à cinq partitions.
- **Modèle retenu pour le POC** : régression de Poisson sans le stock de fin de mois, avec une MAE de 2,46 unités et un R² de 0,36.
- **Scénario avec stock** : écarté en raison d'un risque de fuite temporelle.



- **Qualité des données** : contrôles Pandas complétés par un schéma Pandera portant sur huit colonnes.
- **Great Expectations** : étudié mais différé, car disproportionné pour trois fichiers mensuels de faible volumétrie.

Le modèle prédictif constitue un POC de faisabilité. Il ne doit pas être utilisé pour une prévision opérationnelle sans historique de plusieurs mois et validation chronologique.

## POC de segmentation non supervisée

Un clustering K-means a été expérimenté sur 713 produits à partir de trois variables : les quantités vendues, le stock disponible et sa valeur au prix d’achat.

Les variables ont été transformées avec `log1p`, puis standardisées avec `StandardScaler`. Plusieurs solutions comprises entre deux et six clusters ont été comparées à partir de l’inertie, du coefficient de silhouette et de leur interprétabilité métier.

La solution à deux clusters obtient la meilleure silhouette (0,697), mais reste trop générale. Une solution à cinq clusters est retenue malgré une silhouette inférieure (0,541), car elle distingue les profils de rotation, de rupture et d’immobilisation financière.

Principaux résultats :

- 20 des 22 ruptures actives sont isolées dans un cluster spécifique ;
- 28 produits, soit 3,9 % du catalogue analysé, concentrent 123 148,73 € de stock ;
- ce groupe représente 44,4 % de la valeur du stock analysé et rassemble 24 des 27 risques d’immobilisation.

L’analyse descriptive par catégorie montre que le cluster « Surstock / capital immobilisé » est composé à 96,4 % de Champagne, tandis que le cluster « Ruptures actives » est composé à 95,0 % de vins. Le cluster « Stock nul » est composé à 95,8 % de vins et à 4,2 % de whisky.

Les catégories de produits ont été croisées avec les clusters après l’apprentissage afin de faciliter leur interprétation métier. Elles n’ont pas été utilisées pour constituer les groupes et ces associations ne doivent pas être interprétées comme des relations causales.

Le clustering complète les règles métier mais ne les remplace pas. Il ne constitue pas une prédiction des ruptures futures.

## Fichiers générés

L'exécution crée automatiquement le dossier `exports/` contenant :

- `bottleneck_base_analytique_finale.csv` : base finale de 714 produits et 36 colonnes ;
- `bottleneck_journal_anomalies.csv` : journal des 41 anomalies documentées ;
- `bottleneck_predictions_ventes_poc.csv` : 714 prédictions hors échantillon du POC ;
- `bottleneck_modele_poisson_ventes.joblib` : pipeline final entraîné.

Les fichiers CSV utilisent le séparateur `;`, la virgule comme séparateur décimal et l'encodage `utf-8-sig`.

## Principaux résultats

- 714 produits rapprochés, sans `product_id` manquant ou dupliqué ;
- chiffre d'affaires TTC d'octobre : 143 680,10 € ;
- 5 751 unités vendues ;
- 41 anomalies consignées, dont 18 de priorité haute ;
- valeur du stock ERP au prix d'achat : 298 627,66 € ;
- DOH financier estimé : 119 jours ;
- 27 produits à risque d'immobilisation ;
- 22 produits vendus mais en rupture de stock.

## Reproductibilité et sécurité

- traitements locaux sur des données pédagogiques relatives aux produits ;
- aucune donnée personnelle identifiée dans les champs utilisés ;
- validation croisée `KFold` avec cinq partitions, `shuffle=True` et `random_state=42` ;
- paramètres aléatoires documentés pour la forêt aléatoire ;
- relecture des fichiers exportés et réconciliation automatique des principaux totaux ;
- modèle et prédictions rechargés et contrôlés après export ;
- clustering réexécuté avec KMeans(n_clusters=5, n_init=20, random_state=42), selon des transformations et variables explicitement documentées.

## Limites

- une seule période de ventes, correspondant au mois d'octobre ;
- absence d'historique permettant d'analyser la saisonnalité ;
- stock observé en fin de mois, non utilisable comme variable prédictive principale pour le même mois ;
- prix HT estimé avec un taux de TVA uniforme de 20 % ;
- anomalies nécessitant une validation métier avant toute correction dans les systèmes sources ;
- POC prédictif insuffisant pour un déploiement opérationnel.
- clusters décrivant une seule période et un stock observé au 31 octobre, dont la stabilité reste à vérifier sur plusieurs mois ;
- libellés métier attribués après l’apprentissage afin d’interpréter les groupes, sans influencer leur constitution.

## Utilisation de l'IA

ChatGPT/Codex a été utilisé comme assistant de code et de documentation pour explorer des options, proposer des implémentations, comparer les méthodes et structurer les contrôles. Les propositions ont été exécutées localement, vérifiées par des résultats chiffrés et conservées uniquement après décision de l'analyste. Les traces représentatives figurent dans la documentation du projet.

