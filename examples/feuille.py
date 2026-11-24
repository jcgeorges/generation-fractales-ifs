"""Figure en forme de feuille : matrices extraites de l'annexe du rapport."""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import animer_fractale

CARRE = [[0, 0], [1, 0], [1, 1], [0, 1]]
TRANSFORMATIONS = [
    (0.7 * np.eye(2), np.array([0.0, 0.5])),
    (0.7 * np.eye(2), np.array([0.0, 0.0])),
    (0.65 * np.array([[np.cos(np.radians(45)), -np.sin(np.radians(45))],
                      [np.sin(np.radians(45)), np.cos(np.radians(45))]]), np.array([0.0, 0.2])),
    (0.65 * np.array([[np.cos(np.radians(-45)), -np.sin(np.radians(-45))],
                      [np.sin(np.radians(-45)), np.cos(np.radians(-45))]]), np.array([0.0, 0.2])),
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int, nargs="?", default=5)
    parser.add_argument("--pause", type=float, default=0.8, help="Secondes entre les étapes")
    parser.add_argument("--no-show", action="store_true", help="Enregistrer le PNG sans ouvrir de fenêtre")
    args = parser.parse_args()
    if not 0 <= args.iterations <= 7:
        parser.error("choisir entre 0 et 7 itérations (croissance exponentielle)")
    chemin = Path(__file__).resolve().parents[1] / "images" / "feuille.png"
    animer_fractale(CARRE, TRANSFORMATIONS, args.iterations,
                    "Figure en forme de feuille", chemin, args.pause, not args.no_show)