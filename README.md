# Portfolio

> Mon portfolio, construit comme une carte du ciel interactive : la galaxie sert de
> navigation, chaque astre ouvre un panneau (Parcours, Projets, CV).

**En ligne :** https://alexandre-grandjean.github.io/portfolio/

## Ce que c'est

Un site une page, en plein écran, où l'on navigue en cliquant des astres plutôt qu'en
faisant défiler. La scène est une galaxie de particules rendue en three.js ; la caméra
vole vers l'astre choisi, le panneau s'ouvre à côté. Trois sections : parcours,
projets, CV. Les liens GitHub, LinkedIn et mail sont accessibles directement en haut
à gauche, avec une icône et un libellé, y compris sur mobile. L'ancien lien
`#contact` reste compatible et ouvre le panneau `#cv`.

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

## CV public

Les boutons de contact utilisent uniquement `public/documents/cv-light.pdf`.
Il s'agit du CV clair fourni par Alexandre, avec le logo Epitech en haut à droite.
Sa mise en page est conservée ; la ligne du téléphone est supprimée du PDF.
Pour préparer une nouvelle version avec Python 3 et PyMuPDF :

```bash
python scripts/prepare_cv.py "chemin/vers/le-cv-original.pdf"
```

Le traitement est local et ne charge aucune ressource distante. Vérifier que le PDF
reste sur une page, que le logo est intact et que ses liens fonctionnent avant publication.
Ne jamais ajouter le PDF original avec téléphone au dépôt. Pas de version sombre et
pas de recréation du CV dans une autre mise en page.

## Structure

- `src/components/Galaxy.astro` : scène three.js + astres de navigation
- `src/components/Hud.astro` : cadre, menu, identité
- `src/components/Panels.astro` : panneaux et contrôleur de navigation
- `src/styles/global.css` : variables et base

## Licence

MIT — voir [LICENSE](LICENSE).
