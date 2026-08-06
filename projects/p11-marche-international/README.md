# Projet 11 - Étude de marché internationale

## Contexte et besoin métier

L'entreprise **La poule qui chante** souhaite développer l'exportation de poulet biologique, sans disposer au départ d'une liste de pays cibles. L'objectif du projet est de comparer les marchés disponibles, d'identifier des profils homogènes et de proposer une shortlist exploitable par le COMEX.

## Données

La base analytique rassemble des données ouvertes provenant notamment de la FAO, de la Banque mondiale, des Worldwide Governance Indicators, de WITS, de Doing Business et d'Our World in Data.

- 163 pays ;
- 30 colonnes dans la base consolidée ;
- 14 indicateurs quantitatifs retenus pour les analyses multivariées ;
- aucune valeur manquante dans la base finale ;
- aucun code ISO3 dupliqué.

Les indicateurs couvrent le marché de la volaille, l'économie, les institutions, la logistique, le commerce international et le contexte de l'agriculture biologique. Les données sources ne sont pas redistribuées dans ce portfolio.

## Démarche

1. Collecte, nettoyage, harmonisation et rapprochement des sources par pays.
2. Sélection des variables selon un cadre PESTEL et création d'indicateurs complémentaires.
3. Standardisation de 14 variables quantitatives.
4. Analyse en composantes principales pour réduire la redondance entre variables corrélées.
5. Conservation des six premiers axes, représentant **82,93 % de la variance totale**.
6. Segmentation par classification ascendante hiérarchique avec la méthode de Ward.
7. Comparaison des profils obtenus avec une segmentation k-means indépendante.
8. Construction d'un score métier combinant potentiel de marché, ouverture aux importations et attractivité structurelle.

## Principaux résultats

La segmentation retenue distingue cinq profils de marchés :

- marchés moins favorables ;
- marchés attractifs et développés ;
- marchés dépendants des importations ;
- méga-marchés atypiques ;
- marchés orientés vers la production locale.

Le croisement entre les clusters, le score de priorisation et les filtres métier conduit à deux niveaux de recommandation :

- **priorité 1** : Hong Kong, Allemagne, Royaume-Uni, Japon, Pays-Bas et Émirats arabes unis ;
- **priorité 2** : Danemark, Suède, Autriche, Belgique et Suisse.

La contribution du modèle consiste à réduire un périmètre mondial à une shortlist structurée. Il ne remplace pas la décision commerciale.

## Impact et recommandations

- concentrer la première étude commerciale approfondie sur les six marchés de priorité 1 ;
- vérifier la demande réelle en produits biologiques et le positionnement prix ;
- analyser les circuits de distribution, la concurrence locale et les exigences sanitaires ;
- ajuster les pondérations du score avec les responsables métier avant tout engagement opérationnel.

## Compétences validées

L'évaluation du projet valide quatre compétences :

- exploiter un modèle d'apprentissage pour approfondir la connaissance des données ;
- réaliser des analyses multivariées ;
- réduire la dimension du jeu de données ;
- sélectionner des variables pertinentes.

L'évaluateur souligne la pertinence des recommandations, la justification des choix, la bonne compréhension de l'ACP et du clustering, ainsi que l'accessibilité de la restitution pour un public non technique.

## Limites

- analyse quantitative reposant principalement sur des données de 2017 ;
- précision et couverture variables selon les sources ;
- pondérations du score dépendantes des hypothèses métier ;
- part des terres arables biologiques utilisée comme proxy du contexte bio, et non comme mesure directe de la demande ;
- absence d'étude qualitative détaillée de la concurrence, de la réglementation, de la distribution et du prix.

## Fichiers publics

- [`notebooks/preparation-donnees.ipynb`](notebooks/preparation-donnees.ipynb) — préparation, nettoyage et enrichissement ;
- [`notebooks/analyse-marche.ipynb`](notebooks/analyse-marche.ipynb) — ACP, clustering et priorisation ;
- [`reports/presentation.pdf`](reports/presentation.pdf) — synthèse destinée au COMEX ;
- [`images/priorisation-marches.png`](images/priorisation-marches.png) — shortlist et score de priorisation.

Les notebooks conservent leurs sorties afin de rendre la démarche et les résultats directement examinables. Leur réexécution complète nécessite les sources de données décrites dans le notebook de préparation.
