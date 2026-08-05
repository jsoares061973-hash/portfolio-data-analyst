# Projet 08 — Analyse sociodémographique avec dbt

## Besoin métier

OpenClassrooms souhaite comprendre l’évolution du profil sociodémographique des étudiants des parcours Data entre 2022 et 2025 afin d’orienter les actions en faveur de l’accessibilité et de l’égalité des chances.

## Données, qualité et RGPD

L’analyse rapproche :

- 4 647 inscriptions pédagogiques OpenClassrooms réparties entre 2022 et 2025 ;
- des données publiques INSEE 2025 utilisées comme référentiel externe ;
- quatre dimensions principales : année d’entrée, genre, tranche d’âge et région.

La restitution finale est agrégée et ne contient aucun identifiant individuel. Les données internes brutes et le seed comportant `USER_ID` ne sont pas publiés. Le principe de minimisation est appliqué au CSV final.

## Pipeline

Le workflow dbt exécuté sur Snowflake sépare clairement les responsabilités :

1. déclaration des sources ;
2. **staging** pour nettoyer, typer et harmoniser ;
3. **intermediate** pour préparer les données INSEE à la granularité régionale ;
4. **marts** pour produire les tables analytiques ;
5. export d’un CSV consolidé utilisé dans Power BI.

Le projet comporte 11 modèles SQL, trois sources de référence et huit tests dbt génériques déclarés dans les fichiers YAML. Les contrôles portent notamment sur les valeurs nulles, les modalités acceptées, les années, les volumes et la cohérence entre dbt, le CSV final et les visualisations.

## Résultats et recommandations

- 1 696 étudiants en 2022, 1 150 en 2023, 850 en 2024 et 951 en 2025 ;
- en 2025, 71,7 % des étudiants ont entre 20 et 39 ans ;
- 41,1 % des étudiants 2025 sont rattachés à l’Île-de-France ;
- la part des femmes progresse, mais reste inférieure au référentiel INSEE sur le périmètre comparable ;
- 6,7 % des valeurs de genre sont encore « Non renseigné » en 2025.

Les recommandations consistent à suivre la progression de la diversité de genre, examiner la concentration territoriale, adapter l’accompagnement au profil d’âge dominant et améliorer la collecte des informations manquantes.

## Compétences validées

L’évaluation a validé :

1. l’agrégation d’extractions en définissant des règles de nettoyage ;
2. la collecte de données pertinentes dans le respect des normes et bonnes pratiques ;
3. la vérification de la cohérence et de la fiabilité des données préparées.

## Limites et prochaines pistes

Le benchmark INSEE est limité à 2025 et à des catégories harmonisées. Il fournit une contextualisation, pas une relation causale. La prochaine étape est de renforcer les tests sur les marts finaux : non-négativité de `NB_STUDENTS`, recomposition automatisée des parts à environ 100 %, contrôle de `PERIMETRE_ANALYSE` et conservation d’une preuve d’exécution de `dbt test`.

Le workflow public contient le code SQL, les fichiers YAML et la configuration dbt, mais exclut volontairement les seeds internes comportant des identifiants.
