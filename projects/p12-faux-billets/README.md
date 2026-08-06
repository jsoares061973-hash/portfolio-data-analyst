# Détection automatique de faux billets

Projet de classification réalisé dans le cadre du parcours Data Analyst d’OpenClassrooms.

## Besoin métier

Construire un outil capable d’identifier automatiquement un billet authentique ou faux à partir de six caractéristiques géométriques. L’erreur la plus sensible est le faux billet classé comme authentique.

## Données

- 1 500 billets : 1 000 authentiques et 500 faux ;
- six mesures : `diagonal`, `height_left`, `height_right`, `margin_low`, `margin_up` et `length` ;
- 37 valeurs manquantes sur `margin_low` ;
- aucun doublon détecté.

Les fichiers pédagogiques `billets.csv` et `billets_production.csv` ne sont pas redistribués dans ce portfolio public.

## Démarche

- séparation stratifiée : 80 % entraînement et 20 % test ;
- imputation par la médiane et standardisation intégrées aux pipelines afin d’éviter la fuite de données ;
- validation croisée stratifiée à cinq plis ;
- comparaison de la régression logistique, du KNN, du Random Forest, du SVM et de K-means ;
- sélection selon l’accuracy, la précision, le rappel, le F1-score et le nombre de faux billets non détectés.

## Résultat

La régression logistique est retenue pour son compromis entre performance, stabilité, simplicité et interprétabilité :

- accuracy sur le jeu de test : 99,0 % ;
- rappel des faux billets : 98,0 % ;
- F1-score des faux billets : 98,5 % ;
- 297 billets correctement classés sur 300 ;
- deux faux billets classés comme authentiques.

En lançant Jupyter depuis la racine du projet, le modèle final est entraîné sur les 1 500 billets et sauvegardé dans `models/modele_detection_billets.joblib`. Le script [`src/prediction.py`](src/prediction.py) charge ensuite ce modèle pour traiter un fichier CSV ou un billet unique.

## Environnement indicatif

- Python ;
- pandas et NumPy ;
- scikit-learn ;
- matplotlib et seaborn ;
- joblib ;
- Jupyter Notebook.

## Fichiers publics

- [`notebooks/detection-faux-billets.ipynb`](notebooks/detection-faux-billets.ipynb) — préparation, comparaison des modèles et évaluation ;
- [`src/prediction.py`](src/prediction.py) — prédiction pour un billet ou un fichier CSV ;
- [`reports/presentation.pdf`](reports/presentation.pdf) — démarche et résultats ;
- [`images/selection-modele.png`](images/selection-modele.png) — synthèse de la sélection du modèle.

## Limites et prochaines pistes

- ajuster le seuil de décision selon le coût métier des faux négatifs ;
- suivre la performance sur de nouvelles données réelles et surveiller une éventuelle dérive ;
- mesurer le gain réel de méthodes de boosting par validation croisée ;
- caractériser plus finement les clusters K-means à l’aide de distributions et de boîtes à moustaches.
