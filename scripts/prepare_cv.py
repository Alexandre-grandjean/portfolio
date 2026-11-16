"""Prépare le PDF public depuis le CV original, sans changer sa mise en page.

Usage : python scripts/prepare_cv.py "chemin/vers/le-cv-original.pdf"
Dépendance : PyMuPDF. Ne pas ajouter le PDF original avec téléphone au dépôt.
"""

import argparse
from pathlib import Path

import pymupdf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    output = Path(__file__).resolve().parent.parent / "public/documents/cv-light.pdf"
    if args.source.resolve() == output.resolve():
        raise SystemExit("Utiliser le PDF original comme source, pas le fichier de sortie.")

    with pymupdf.open(args.source) as doc:
        removed = 0
        for page in doc:
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    text = "".join(span["text"] for span in line["spans"])
                    if "téléphone" in text.casefold():
                        page.add_redact_annot(pymupdf.Rect(line["bbox"]), fill=(1, 1, 1))
                        removed += 1
            for link in page.get_links():
                if link.get("uri", "").casefold().startswith("tel:"):
                    page.delete_link(link)
            # Efface le texte réellement, pas seulement par un rectangle blanc.
            # Conserve les images et tracés, dont le logo de l'établissement.
            page.apply_redactions(images=0, graphics=0)

        if not removed:
            raise SystemExit("Aucune ligne Téléphone détectée : vérifier le PDF source.")
        if len(doc) != 1:
            raise SystemExit("Le CV source doit tenir sur une page.")
        text = "".join(page.get_text() for page in doc)
        if "téléphone" in text.casefold():
            raise SystemExit("Échec : la ligne Téléphone est toujours présente.")
        output.parent.mkdir(parents=True, exist_ok=True)
        doc.save(output, garbage=4, deflate=True, clean=True)
        print(f"CV public prêt : {output}")


if __name__ == "__main__":
    main()
