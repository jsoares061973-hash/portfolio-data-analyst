# Projet 05 — Base de données immobilière avec SQL

## Besoin métier

Laplace Immo souhaite centraliser plusieurs sources immobilières dans une base relationnelle fiable, puis interroger les ventes afin d’éclairer les décisions commerciales et l’analyse du marché.

## Données et qualité

Le travail repose sur trois jeux pédagogiques :

- données communales : 34 991 lignes et 9 colonnes ;
- référentiel géographique : 38 916 lignes et 37 colonnes ;
- valeurs foncières : 34 169 lignes et 46 colonnes.

Les sources ont été nettoyées, typées et rapprochées avant leur intégration. Un dictionnaire décrit les variables, les types, les clés et les règles de gestion. Les données brutes ne sont pas redistribuées dans ce portfolio.

## Démarche

- conception d’un modèle relationnel normalisé en troisième forme normale ;
- création de quatre tables : `Bien`, `Vente`, `Commune` et `Population` ;
- définition des clés primaires et étrangères et contrôle de l’intégrité référentielle ;
- chargement des données dans SQLite ;
- réalisation de douze requêtes répondant à des questions métier avec `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING` et `ORDER BY`, ainsi que des alias, sous-requêtes ou tables temporaires ;
- application du principe de minimisation RGPD, avec exclusion du nom de l’acquéreur.

## Résultats et apport métier

Les requêtes permettent notamment de :

- comptabiliser 31 378 appartements vendus au premier semestre 2020 ;
- identifier l’Île-de-France comme première région en volume avec 13 995 ventes ;
- comparer les prix au mètre carré, dont environ 11 136 € à Paris ;
- mesurer une hausse de 3,68 % du nombre de transactions entre les premier et deuxième trimestres 2020 ;
- rapporter le nombre de transactions à la population afin de limiter le biais lié à la taille des communes ;
- détecter des observations atypiques et tester des filtres alternatifs avant interprétation.

## Compétences validées

L’évaluation a validé :

1. la création d’une base conforme aux besoins clients et aux normes réglementaires ;
2. la réalisation de requêtes SQL répondant à des problématiques métier dans le respect du RGPD ;
3. la gestion d’une base relationnelle, de ses clés et de requêtes de complexité progressive.

## Preuves publiées

- [`data/dictionnaire-donnees.xlsx`](data/dictionnaire-donnees.xlsx) — tables, champs, types, clés et règles de gestion ;
- [`images/schema-relationnel.png`](images/schema-relationnel.png) — modèle normalisé et relations entre les tables ;
- [`images/requete-sql.png`](images/requete-sql.png) — exemple de requête métier et résultat obtenu.

## Limites et prochaines pistes

L’analyse couvre le premier semestre 2020 et repose sur des données pédagogiques. Certaines petites surfaces peuvent fortement influencer les prix au mètre carré. Une suite professionnelle consisterait à versionner les requêtes dans des fichiers SQL séparés, automatiser les contrôles de chargement et actualiser la base avec des périodes plus récentes.

Le ZIP évalué ne contient pas de script `.sql` autonome ; les requêtes originales sont présentées dans le support de soutenance. Aucun script reconstruit n’est donc publié comme preuve originale.
