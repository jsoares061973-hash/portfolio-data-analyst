# Portfolio Data Analyst — Joana Aubry

Portfolio professionnel de projets d’analyse de données, conçu pour une lecture rapide par un recruteur, un manager ou un client.

**Positionnement :** Data Analyst · Finance & Supply Chain  
**Portfolio en ligne :** [jsoares061973-hash.github.io/portfolio-data-analyst](https://jsoares061973-hash.github.io/portfolio-data-analyst/)  
**Contact :** [LinkedIn](https://www.linkedin.com/in/joana-soares-aubry) · [E-mail](mailto:jsoares061973@gmail.com)

## Projets

| Projet | Besoin métier | Technologies et méthodes | Preuves publiées |
|---|---|---|---|
| [P6/P13 — BottleNeck & IA](projects/p06-p13-bottleneck-ia/) | Fiabiliser les données, piloter les ventes et les stocks | Python, pandas, Pandera, scikit-learn, IA responsable | Notebook, documentation, mini-formation, visualisation |
| [P10 — Accès à l’eau](projects/p10-dwfa-power-bi/) | Prioriser les interventions WASH | Power BI, Power Query, DAX, modélisation | Dashboard, présentation, blueprint |
| [P12 — Faux billets](projects/p12-faux-billets/) | Sécuriser une décision de contrôle | Python, classification, K-means, scikit-learn | Notebook, script de prédiction, présentation |
| [P7 — Pilotage de projets](projects/p07-pilotage-power-bi/) | Détecter les dérives d’un portefeuille | Power BI, Power Query, DAX, RLS | PBIX, canvas, modèle en étoile |
| [P8 — Pipeline sociodémographique](projects/p08-dbt-snowflake/) | Produire une donnée fiable et documentée | dbt, Snowflake, SQL, tests, Power BI | Workflow, export agrégé, présentation, documentation |
| [P9 — Ventes & clients](projects/p09-ventes-statistiques/) | Expliquer la performance commerciale | Python, séries temporelles, tests statistiques | Notebook, présentation, diagnostic |
| [P11 — Marché international](projects/p11-marche-international/) | Prioriser des marchés d’exportation | ACP, CAH, k-means, PESTEL | Deux notebooks, présentation, shortlist |
| [P4 — Sécurité alimentaire](projects/p04-securite-alimentaire/) | Mesurer la sous-nutrition et les disponibilités alimentaires | Python, données publiques, analyse exploratoire | Notebook, présentation, visualisation |
| [P5 — Immobilier, SQL & RGPD](projects/p05-immobilier-sql-rgpd/) | Structurer et interroger des données foncières | SQL, modèle relationnel, qualité, RGPD | Dictionnaire, schéma relationnel, requête documentée |
| [P2 — Performance e-commerce](projects/p02-ecommerce-excel/) | Suivre ventes, trafic, conversion et clients | Excel, visualisation, storytelling | Synthèse publique et visualisation |

> La numérotation reprend le parcours de formation. Le P3 correspond à un bilan avec le mentor et ne constitue pas un projet à publier. Les travaux P6 et P13 sont réunis dans une seule étude de cas enrichie.

## Structure du dépôt

```text
.
├── index.html                 # page GitHub Pages
├── styles.css                 # design responsive
├── assets/
│   └── cv/                    # CV public
├── docs/
│   └── architecture.md        # construction technique du portfolio
└── projects/
    └── pXX-nom-du-projet/
        ├── README.md          # synthèse recruteur/client
        ├── notebooks/         # analyses reproductibles
        ├── reports/           # présentations et rapports
        ├── images/            # preuves visuelles
        ├── data/              # données publiques ou agrégées
        └── src/               # scripts et workflows
```

Chaque dossier ne contient que les sous-dossiers utiles au projet concerné.

## Principes de publication

- les données pédagogiques brutes, personnelles ou confidentielles ne sont pas redistribuées ;
- les résultats sont accompagnés du contexte, de la démarche, de recommandations et de limites ;
- les notebooks publiés conservent leurs sorties pour permettre une lecture sans données sources ;
- les ressources du site utilisent des chemins relatifs afin de rester compatibles avec GitHub Pages.

La construction technique du site est décrite dans [`docs/architecture.md`](docs/architecture.md).
<!-- Trigger GitHub Pages redeploy -->
