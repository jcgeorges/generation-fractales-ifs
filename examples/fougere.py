"""Fougère de Barnsley : matrices extraites de l'annexe du rapport."""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import animer_fractale

POINT_INITIAL = [np.array([0.0, 0.0])]
TRANSFORMATIONS = [
    (np.array([[0.85, 0.04], [-0.04, 0.85]]), np.array([0.0, 1.6])),
    (np.array([[0.20, -0.26], [0.23, 0.22]]), np.array([0.0, 1.6])),
    (np.array([[-0.15, 0.28], [0.26, 0.24]]), np.array([0.0, 0.44])),
    (np.array([[0.0, 0.0], [0.0, 0.16]]), np.array([0.0, 0.0])),
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int, nargs="?", default=8)
    parser.add_argument("--pause", type=float, default=0.8, help="Secondes entre les étapes")
    parser.add_argument("--no-show", action="store_true", help="Enregistrer le PNG sans ouvrir de fenêtre")
    args = parser.parse_args()
    if not 0 <= args.iterations <= 9:
        parser.error("choisir entre 0 et 9 itérations (croissance exponentielle)")
    chemin = Path(__file__).resolve().parents[1] / "images" / "fougere.png"
    animer_fractale(POINT_INITIAL, TRANSFORMATIONS, args.iterations,
                    "Fougère de Barnsley", chemin, args.pause, not args.no_show)