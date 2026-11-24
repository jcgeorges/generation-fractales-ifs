"""Triangle de Sierpiński : transformations reconstruites (absentes de l'export du rapport)."""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import animer_fractale

TRIANGLE = [[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]]
TRANSFORMATIONS = [
    (0.5 * np.eye(2), np.array([0.0, 0.0])),
    (0.5 * np.eye(2), np.array([0.5, 0.0])),
    (0.5 * np.eye(2), np.array([0.25, np.sqrt(3) / 4])),
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int, nargs="?", default=6)
    parser.add_argument("--pause", type=float, default=0.8, help="Secondes entre les étapes")
    parser.add_argument("--no-show", action="store_true", help="Enregistrer le PNG sans ouvrir de fenêtre")
    args = parser.parse_args()
    if not 0 <= args.iterations <= 8:
        parser.error("choisir entre 0 et 8 itérations (croissance exponentielle)")
    chemin = Path(__file__).resolve().parents[1] / "images" / "sierpinski.png"
    animer_fractale(TRIANGLE, TRANSFORMATIONS, args.iterations,
                    "Triangle de Sierpiński", chemin, args.pause, not args.no_show)