"""Triangle de Sierpiński.

Les définitions de `cercle` et `transform_sierpinski` ont disparu dans
l'export Markdown du rapport : cet exemple les RECONSTRUIT explicitement.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ifs import gen_fractal, fractale

triangle_initial = [[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]]
transform_sierpinski = [
    (0.5 * np.eye(2), np.array([0.0, 0.0])),
    (0.5 * np.eye(2), np.array([0.5, 0.0])),
    (0.5 * np.eye(2), np.array([0.25, np.sqrt(3) / 4])),
]

if __name__ == "__main__":
    iteration = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    if iteration > 8:
        raise SystemExit("Pour cette méthode exhaustive, utiliser au plus 8 itérations.")
    fig = gen_fractal(triangle_initial, transform_sierpinski, iteration)
    destination = Path(__file__).resolve().parents[1] / "images" / "sierpinski.png"
    fractale(fig, f"Triangle de Sierpiński — Étape {iteration}", fichier=destination)
    print(f"Image créée : {destination}")
