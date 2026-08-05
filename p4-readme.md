# Projet 4 — Étude de santé publique sur l’alimentation dans le monde

## Objectif

Analyser des données publiques de la FAO afin de comprendre les écarts entre disponibilité alimentaire, sous-nutrition, usages des ressources et aide internationale. L’étude cherche à montrer pourquoi une production globale suffisante ne garantit pas un accès équitable à l’alimentation.

## Livrables

- [`p4-food-security-notebook.ipynb`](p4-food-security-notebook.ipynb) — notebook Python exécuté et documenté.
- [`p4-food-security-presentation.pdf`](p4-food-security-presentation.pdf) — synthèse de l’analyse et des recommandations.

## Données

Quatre fichiers pédagogiques issus de données publiques FAO :

- population par pays ;
- nombre de personnes en sous-nutrition ;
- disponibilité et utilisation alimentaires ;
- aide alimentaire reçue.

Les fichiers sources ne sont pas redistribués dans ce portfolio. Le notebook attend les fichiers `population.csv`, `sous_nutrition.csv`, `dispo_alimentaire.csv` et `aide_alimentaire.csv` dans son répertoire d’exécution.

## Démarche

1. Contrôle des structures, types, unités, valeurs manquantes et périodes.
2. Nettoyage et rapprochement des quatre sources par pays et année.
3. Calcul des taux de sous-nutrition et de la capacité alimentaire théorique.
4. Analyse de la disponibilité intérieure, des pertes et de l’alimentation animale.
5. Comparaison des usages des principales céréales.
6. Étude de l’aide alimentaire entre 2013 et 2016.
7. Analyse du paradoxe du manioc en Thaïlande.

## Résultats clés

| Indicateur | Résultat |
| --- | ---: |
| Personnes en sous-nutrition en 2017 | ≈ 536 millions |
| Part de la population mondiale concernée | ≈ 7 % |
| Capacité alimentaire mondiale théorique | 9,1 milliards de personnes |
| Capacité théorique avec les seuls végétaux | 7,55 milliards de personnes |

L’analyse met en évidence une disponibilité calorique mondiale théoriquement suffisante, mais des vulnérabilités persistantes liées à l’accès, à la distribution, aux pertes, aux usages agricoles et aux contextes économiques et politiques.

## Limites

- La capacité alimentaire repose sur une hypothèse moyenne de 2 300 kcal par personne et par jour.
- Les périodes et la complétude diffèrent selon les jeux FAO.
- Une valeur manquante ne signifie pas une absence de besoin.
- Les associations observées entre disponibilité, aide et sous-nutrition ne démontrent pas seules une causalité.

## Environnement

Python 3.12.9 avec pandas, NumPy, Matplotlib, Seaborn, Plotly et Jupyter. Les dépendances principales sont listées dans [`p4-requirements.txt`](p4-requirements.txt).
