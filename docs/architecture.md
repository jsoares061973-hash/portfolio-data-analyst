# Architecture technique du portfolio

## Vue d’ensemble

Le portfolio est un site statique **mono-page** hébergé par GitHub Pages. Il ne dépend ni d’un framework JavaScript, ni d’un serveur applicatif, ni d’une base de données.

| Couche | Choix technique | Rôle |
|---|---|---|
| Structure | HTML5 sémantique | Organiser le contenu et faciliter la lecture par les moteurs, les lecteurs d’écran et les recruteurs |
| Présentation | CSS3 | Design, grilles, composants, responsive et états de focus |
| Interaction | Ancres HTML et éléments `details/summary` | Navigation interne, menu mobile et développement progressif des études de cas |
| Hébergement | GitHub Pages | Publier automatiquement les fichiers statiques de la branche `main` |
| Livrables | PDF, notebooks, images, PBIX, ZIP, CSV et XLSX | Donner accès aux preuves techniques de chaque projet |

## Parcours de lecture

La page suit un ordre adapté à une première lecture de recrutement ou de prospection :

1. **Accueil** — positionnement professionnel et proposition de valeur.
2. **Index des projets** — accès direct aux dix études de cas.
3. **Études de cas** — contexte, données, indicateurs, démarche, recommandations, livrables et limites.
4. **Compétences** — synthèse des outils et méthodes réellement démontrés.
5. **Veille** — sources suivies, méthode de validation et application concrète.
6. **À propos** — articulation entre l’expérience finance/supply chain et la data.
7. **Contact** — e-mail, LinkedIn et CV public.

Le projet BottleNeck est développé par défaut. Les autres projets utilisent `details/summary` pour réduire la charge visuelle tout en conservant l’ensemble des preuves à un clic.

## Design responsive

Le fichier `styles.css` constitue un mini système de design : variables de couleurs, largeurs maximales, espacements, grilles, boutons, cartes et styles de focus.

- au-dessus de 900 px : navigation desktop et cartes en deux colonnes ;
- entre 560 px et 900 px : navigation mobile, sections en une colonne et index de projets en deux colonnes ;
- sous 560 px : index, indicateurs et contenus détaillés en une colonne ;
- `prefers-reduced-motion` désactive le défilement animé pour les personnes qui le demandent.

## Accessibilité et sécurité

- un seul titre `h1` et une hiérarchie de titres cohérente ;
- textes alternatifs descriptifs pour les images de projet ;
- libellés ARIA sur les navigations et les blocs principaux ;
- états de focus visibles pour la navigation au clavier ;
- `rel="noopener"` sur les liens ouverts dans un nouvel onglet ;
- aucune donnée privée inutile dans la page publique : pas de téléphone, d’adresse exacte ou de document administratif.

## Organisation des fichiers

`index.html`, `styles.css`, `README.md` et `.gitignore` restent à la racine, car GitHub Pages doit trouver directement la page d’accueil. Les preuves sont classées par projet dans `projects/`, tandis que les ressources transversales sont rangées dans `assets/` et la documentation dans `docs/`.

Les liens du site utilisent des chemins relatifs, par exemple :

```html
<img src="projects/p09-ventes-statistiques/images/diagnostic-ventes.png" alt="…">
```

Les notebooks et fichiers texte à examiner dans l’interface GitHub utilisent des liens `blob/main` vers leur nouvelle arborescence.

## Publication

Le flux de déploiement est volontairement simple :

1. les fichiers sont ajoutés ou modifiés dans la branche `main` ;
2. un commit conserve l’historique de la modification ;
3. GitHub Pages republie automatiquement le contenu statique ;
4. la page en ligne est contrôlée après le déploiement.

Une modification des noms ou dossiers d’un livrable doit toujours être accompagnée de la mise à jour du lien correspondant dans `index.html`.
