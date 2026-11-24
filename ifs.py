"""Fonctions IFS reconstituées à partir de l'annexe du rapport.

Corrections limitées : indentation, validation et sauvegarde optionnelle.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def rotation(point, angle):
    """Tourne un point autour de l'origine d'un angle exprimé en degrés."""
    teta = np.radians(angle)
    rot_matrix = np.array([
        [np.cos(teta), -np.sin(teta)],
        [np.sin(teta), np.cos(teta)],
    ])
    return rot_matrix @ np.asarray(point, dtype=float)


def transformation(fig, ang, translation, fac_contr):
    """Applique une rotation, contraction et translation aux points d'une figure."""
    fig_transforme = []
    for point in fig:
        fig_rot = rotation(point, ang)
        fig_contr = fig_rot * fac_contr
        fig_transl = fig_contr + translation
        fig_transforme.append(fig_transl)
    return np.array(fig_transforme)


def gen_fractal(fig_initial, transform, nbre_iter):
    """Génère toutes les copies de la figure après nbre_iter itérations.

    Le nombre de copies croît comme len(transform) ** nbre_iter.
    """
    if nbre_iter < 0:
        raise ValueError("nbre_iter doit être positif ou nul")
    figure1 = np.asarray(fig_initial, dtype=float)
    fig_actuel = [figure1]
    for _ in range(nbre_iter):
        figure2 = []
        for pt in fig_actuel:
            for A, b in transform:
                fig_transf = np.array([A @ p + b for p in pt])
                figure2.append(fig_transf)
        fig_actuel = figure2
    return fig_actuel


def fractale(fig, titre="Fractale", fichier=None, couleur=None):
    """Affiche la fractale et peut enregistrer l'image en PNG."""
    if not fig:
        raise ValueError("La liste des figures est vide")
    image, axe = plt.subplots(figsize=(8, 8))
    if all(len(f) == 1 for f in fig):
        x = [f[0][0] for f in fig]
        y = [f[0][1] for f in fig]
        axe.scatter(x, y, s=0.2, color=couleur or "green", linewidths=0)
    else:
        for f in fig:
            f = np.asarray(f)
            axe.plot(f[:, 0], f[:, 1], color=couleur or "black", linewidth=0.5)
    axe.set_title(titre)
    axe.set_aspect("equal", adjustable="box")
    axe.axis("off")
    if fichier is not None:
        destination = Path(fichier)
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.savefig(destination, dpi=160, bbox_inches="tight")
    plt.close(image)
