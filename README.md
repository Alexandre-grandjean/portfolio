# Portfolio

> Mon portfolio, construit comme une carte du ciel interactive : la galaxie sert de
> navigation, chaque astre ouvre un panneau (Parcours, Projets, Contact).

**En ligne :** https://alexandre-grandjean.github.io/portfolio/

## Ce que c'est

Un site une page, en plein écran, où l'on navigue en cliquant des astres plutôt qu'en
faisant défiler. La scène est une galaxie de particules rendue en three.js ; la caméra
vole vers l'astre choisi, le panneau s'ouvre à côté. Trois sections : parcours,
projets, contact.

## Stack

Astro 7 · three.js · TypeScript · CSS. Polices servies en local, aucun appel externe.

## Lancer en local

| Commande          | Action                             |
| :---------------- | :--------------------------------- |
| `npm install`     | Installe les dépendances           |
| `npm run dev`     | Serveur local sur `localhost:4321` |
| `npm run build`   | Build de production dans `./dist/` |
| `npm run preview` | Prévisualise le build              |

> Après un `npm install`, redémarrer le serveur de dev : le cache de Vite pour three.js
> devient périmé et la galaxie ne s'affiche plus.

## Modifier le contenu

Tout est dans `src/data/` — aucune ligne de code à toucher :
`site.json` (nom, bio, liens), `projects.json`, `parcours.json`.

## Structure

- `src/components/Galaxy.astro` : scène three.js + astres de navigation
- `src/components/Hud.astro` : cadre, menu, identité
- `src/components/Panels.astro` : panneaux et contrôleur de navigation
- `src/styles/global.css` : variables et base

## Licence

MIT — voir [LICENSE](LICENSE).
