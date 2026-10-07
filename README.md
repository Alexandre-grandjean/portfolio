# Portfolio

Astro 7 + three.js. Une galaxie interactive sert de navigation : chaque astre ouvre un panneau (Parcours, Projets, Contact).

## Contenu

Tout se modifie dans `src/data/` : `site.json`, `projects.json`, `parcours.json`.

## Commandes

| Commande          | Action                                   |
| :---------------- | :--------------------------------------- |
| `npm install`     | Installe les dépendances                 |
| `npm run dev`     | Serveur local sur `localhost:4321`       |
| `npm run build`   | Build de production dans `./dist/`       |
| `npm run preview` | Prévisualise le build                    |

## Structure

- `src/components/Galaxy.astro` : scène three.js + astres de navigation
- `src/components/Hud.astro` : cadre, menu, identité
- `src/components/Panels.astro` : panneaux et contrôleur de navigation
- `src/styles/global.css` : variables et base
