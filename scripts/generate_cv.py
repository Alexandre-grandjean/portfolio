"""Génère les deux CV publics sans téléphone avec Microsoft Edge.

Depuis la racine du dépôt : python scripts/generate_cv.py
Aucune dépendance Python externe. Ne charge aucune ressource distante.
"""

from pathlib import Path
import os
import shutil
import subprocess
import tempfile


def main():
    root = Path(__file__).resolve().parent.parent
    candidates = [
        shutil.which("msedge"),
        str(Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)"))
            / "Microsoft/Edge/Application/msedge.exe"),
        str(Path(os.environ.get("PROGRAMFILES", "C:/Program Files"))
            / "Microsoft/Edge/Application/msedge.exe"),
    ]
    edge = next((p for p in candidates if p and Path(p).is_file()), None)
    if not edge:
        raise SystemExit("Microsoft Edge introuvable. Ce générateur nécessite Edge sur Windows.")

    template = (root / "scripts/cv.html").read_text(encoding="utf-8")
    output = root / "public/documents"
    output.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="portfolio-cv-") as temp:
        temp = Path(temp)
        for theme in ("light", "dark"):
            source = temp / f"cv-{theme}.html"
            source.write_text(template.replace('data-theme="light"', f'data-theme="{theme}"'),
                              encoding="utf-8")
            pdf = temp / f"cv-{theme}.pdf"
            result = subprocess.run([
                edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--disable-extensions", "--no-first-run",
                f"--user-data-dir={temp / ('edge-' + theme)}",
                f"--print-to-pdf={pdf}", source.as_uri(),
            ], capture_output=True, timeout=90)
            if result.returncode or not pdf.is_file() or pdf.stat().st_size == 0:
                raise SystemExit(f"Échec de génération du CV {theme}.")
            shutil.copyfile(pdf, output / pdf.name)
            print(f"Créé : public/documents/{pdf.name}")


if __name__ == "__main__":
    main()
