# Projet 10 — Tableau de bord DWFA sur l’accès à l’eau potable

## Objectif

Construire un tableau de bord Power BI permettant à DWFA de prioriser ses interventions en faveur de l’accès à l’eau potable selon trois domaines d’expertise : création de services, modernisation des services existants et conseil aux administrations.

## Livrables

- [`reports/dashboard.pdf`](reports/dashboard.pdf) — export des dix pages du dashboard.
- [`reports/presentation.pdf`](reports/presentation.pdf) — contexte, méthode, résultats et recommandations.
- [`reports/blueprint.pdf`](reports/blueprint.pdf) — besoins utilisateurs, indicateurs, visuels et exigences techniques.

## Données

L’analyse combine plusieurs indicateurs internationaux :

- accès de base et accès sécurisé à l’eau potable ;
- population totale, urbaine et rurale ;
- mortalité attribuée à des services WASH non sécurisés ;
- stabilité politique ;
- référentiel pays-région.

Les valeurs manquantes sont conservées comme indisponibles et ne sont pas remplacées par zéro.

## Architecture du dashboard

- Trois vues d’analyse : mondiale, continentale et nationale.
- Trois pages métier : création, modernisation et consulting.
- Trois pages techniques : préparation des données, modèle et mise à jour.
- Une page d’accueil pour la navigation.

## Démarche

1. Harmonisation des pays, périodes, régions et types dans Power Query.
2. Construction d’un modèle relationnel et d’une dimension temporelle.
3. Création de mesures DAX pour les écarts d’accès, la population couverte et l’efficacité WASH.
4. Conception de cartes, courbes, graphiques comparatifs, nuages de points et tables de priorisation.
5. Ajout de filtres par année, région, pays et stabilité politique.
6. Documentation du processus d’actualisation et des contrôles de reproductibilité.

## Résultats clés

| Indicateur mondial | Résultat |
| --- | ---: |
| Population couverte | 7,5 milliards |
| Accès de base à l’eau potable | 87,8 % |
| Accès sécurisé | 78,1 % |
| Écart entre accès de base et sécurisé | 9,7 points |
| Mortalité WASH | 12,5 pour 100 000 habitants |

Le dashboard fait ressortir plusieurs pays cumulant un accès faible et une mortalité WASH élevée, dont le Tchad, le Soudan du Sud, l’Éthiopie et la République démocratique du Congo.

## Recommandations

- Prioriser la création de services là où l’accès reste faible et la population concernée importante.
- Cibler la modernisation quand l’accès de base existe mais que l’accès sécurisé reste insuffisant.
- Utiliser la stabilité politique comme critère de faisabilité pour le consulting.
- Compléter la priorisation quantitative par une analyse terrain avant toute décision opérationnelle.

## Limites

- Les périodes et la couverture varient selon les indicateurs.
- L’indice d’efficacité WASH est construit pour cette analyse et n’est pas un indicateur officiel.
- Les besoins d’infrastructure, les financements et les partenaires locaux ne sont pas inclus dans les données.
- Le fichier Power BI source n’est pas diffusé dans ce portfolio ; les exports PDF documentent les vues et la démarche.
