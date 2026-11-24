"""Figure feuille : transformations de l'annexe du rapport."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import gen_fractal, fractale

carre = [[0, 0], [1, 0], [1, 1], [0, 1]]
transformations = [
    (0.7 * np.array([[1, 0], [0, 1]]), np.array([0.0, 0.5])),
    (0.7 * np.array([[1, 0], [0, 1]]), np.array([0.0, 0.0])),
    (0.65 * np.array([[np.cos(np.radians(45)), -np.sin(np.radians(45))],
                      [np.sin(np.radians(45)), np.cos(np.radians(45))]]),
     np.array([0.0, 0.2])),
    (0.65 * np.array([[np.cos(np.radians(-45)), -np.sin(np.radians(-45))],
                      [np.sin(np.radians(-45)), np.cos(np.radians(-45))]]),
     np.array([0.0, 0.2])),
]

if __name__ == "__main__":
    iteration = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    if iteration > 7:
        raise SystemExit("Pour cette méthode exhaustive, utiliser au plus 7 itérations.")
    fig = gen_fractal(carre, transformations, iteration)
    destination = Path(__file__).resolve().parents[1] / "images" / "feuille.png"
    fractale(fig, f"Feuille — Étape {iteration}", fichier=destination)
    print(f"Image créée : {destination}")
