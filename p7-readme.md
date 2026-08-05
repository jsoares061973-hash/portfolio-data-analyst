# Pilotage d’un portefeuille de projets avec Power BI

## Contexte et besoin métier

Sanitoral souhaite disposer d’une vision consolidée de son portefeuille de projets afin de détecter rapidement les dérives, de prioriser les actions correctives et d’améliorer la gouvernance. Le rapport s’adresse à trois profils : direction générale, directeurs régionaux et directeurs pays.

## Données

Le projet utilise un jeu pédagogique structuré autour de sept sources : plans de projet, types de projet, coûts réels, durées réelles, livrables réels, localisations et profils pays. Les données permettent de comparer le planifié et le réalisé pour les coûts, les délais et les livrables.

La préparation réalisée avec Power Query comprend notamment :

- la standardisation des types ;
- le contrôle et la préparation des clés ;
- le traitement des doublons, des valeurs manquantes et des zones vides ;
- la consolidation des données réelles dans une table de faits ;
- la structuration des dimensions projet, pays, type de projet et date.

Les données sources ne sont pas redistribuées dans le portfolio public.

## Démarche et architecture

Le Product Strategy Canvas formalise les utilisateurs, leurs besoins, les KPI et les décisions à soutenir. Le modèle Power BI repose sur un schéma en étoile avec `Fact_Project_Phases` au centre et des dimensions dédiées aux projets, aux pays, aux types et aux dates.

Le rapport comporte onze pages : accueil, vue globale, risques et impact financier, détail projet, carte, vue régionale, performance des délais, chronologie, actualisation, préparation des données et modèle de données.

Les fonctionnalités mises en œuvre comprennent :

- des mesures DAX pour les coûts, les écarts, les alertes, les délais et les livrables ;
- des filtres, infobulles, interactions, navigation et fonctionnalité Q&A ;
- des vues par projet, pays et région ;
- des règles Row-Level Security adaptées aux profils utilisateurs.

## Résultats observés

- 104 projets suivis ;
- 50 projets en alerte, soit 48,1 % du portefeuille ;
- 76 projets avec un écart significatif, soit 73,1 % ;
- 89,5 % des livrables complétés ;
- environ 1,13 million de dollars d’impact financier cumulé sur le Top 10 des projets à risque affiché dans la vue globale.

Ces indicateurs permettent d’identifier les régions et les projets qui nécessitent une analyse prioritaire. Ils soutiennent les décisions de correction, de réallocation de ressources, de poursuite ou de réexamen d’un projet.

## Compétence évaluée

La compétence « Produire un reporting en analysant les visualisations pour faciliter les décisions » a été validée. L’évaluation souligne la qualité du Product Strategy Canvas, de la préparation Power Query, du modèle, des indicateurs, de l’interactivité et de la démonstration du dashboard.

## Limites et prochaines pistes

- Le rapport analyse un instantané pédagogique et non un historique complet de production.
- Le seuil d’alerte de 15 % et les règles de recommandation doivent être validés par les responsables métier.
- Une modification de la structure des sources peut nécessiter une adaptation des transformations Power Query.
- Les rôles RLS doivent être testés dans l’environnement de publication avec les comptes réels.
- Une alimentation historique permettrait d’étudier les tendances et d’envisager des alertes prédictives.

## Fichiers publiés

- `p7-dashboard.pbix` : fichier Power BI final ;
- `p7-powerbi-global-view.png` : vue globale du dashboard ;
- `p7-product-strategy-canvas.jpg` : cadrage produit ;
- `p7-star-schema.jpg` : aperçu du modèle de données.
