"""Fougère de Barnsley : matrices reprises de l'annexe du rapport."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import gen_fractal, fractale

point_initial = [np.array([0.0, 0.0])]
transform_fougere = [
    (np.array([[0.85, 0.04], [-0.04, 0.85]]), np.array([0.0, 1.6])),
    (np.array([[0.20, -0.26], [0.23, 0.22]]), np.array([0.0, 1.6])),
    (np.array([[-0.15, 0.28], [0.26, 0.24]]), np.array([0.0, 0.44])),
    (np.array([[0.0, 0.0], [0.0, 0.16]]), np.array([0.0, 0.0])),
]

if __name__ == "__main__":
    # L'annexe suggère 7 à 14 itérations. La croissance 4**n devient
    # rapidement coûteuse ; 8 itérations suffisent pour un premier test.
    iteration = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    if iteration > 9:
        raise SystemExit("Pour cette méthode exhaustive, utiliser au plus 9 itérations.")
    fig = gen_fractal(point_initial, transform_fougere, iteration)
    destination = Path(__file__).resolve().parents[1] / "images" / "fougere.png"
    fractale(fig, f"Fougère — Étape {iteration}", fichier=destination)
    print(f"Image créée : {destination}")
