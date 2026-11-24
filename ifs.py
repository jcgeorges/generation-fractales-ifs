"""Fonctions communes pour la génération déterministe de fractales par IFS.

Les transformations sont issues de l'annexe du rapport. Les fonctions de
visualisation et de progression par étapes ont été adaptées pour ce dépôt.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def rotation(point, angle):
    """Tourne un point autour de l'origine (angle en degrés)."""
    theta = np.radians(angle)
    matrice = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])
    return matrice @ np.asarray(point, dtype=float)


def transformation(fig, ang, translation, fac_contr):
    """Applique successivement une rotation, une contraction et une translation."""
    resultat = []
    for point in fig:
        point_tourne = rotation(point, ang)
        resultat.append(point_tourne * fac_contr + translation)
    return np.asarray(resultat)


def etapes_fractale(fig_initial, transformations, nbre_iter):
    """Produit la figure à l'étape 0, puis après chaque itération de l'IFS."""
    if nbre_iter < 0:
        raise ValueError("nbre_iter doit être positif ou nul")
    figures = [np.asarray(fig_initial, dtype=float)]
    yield 0, figures
    for numero in range(1, nbre_iter + 1):
        nouvelles = []
        for figure in figures:
            for matrice, translation in transformations:
                nouvelles.append(figure @ matrice.T + translation)
        figures = nouvelles
        yield numero, figures


def gen_fractal(fig_initial, transform, nbre_iter):
    """Renvoie uniquement la figure obtenue après nbre_iter itérations."""
    resultat = None
    for _, resultat in etapes_fractale(fig_initial, transform, nbre_iter):
        pass
    return resultat


def dessiner_sur_axes(axe, figures, titre="Fractale", couleur=None):
    """Dessine une étape sur un axe Matplotlib existant."""
    axe.clear()
    if not figures:
        raise ValueError("La liste des figures est vide")
    if all(len(figure) == 1 for figure in figures):
        points = np.asarray([figure[0] for figure in figures])
        axe.scatter(points[:, 0], points[:, 1], s=0.8,
                    color=couleur or "green", linewidths=0)
    else:
        for figure in figures:
            pts = np.asarray(figure)
            # Ferme explicitement les polygones initiaux (3 sommets ou plus).
            if len(pts) >= 3:
                pts = np.vstack((pts, pts[0]))
            axe.plot(pts[:, 0], pts[:, 1],
                     color=couleur or "black", linewidth=0.8)
    axe.set_title(titre)
    axe.set_aspect("equal", adjustable="datalim")
    axe.axis("off")


def fractale(fig, titre="Fractale", fichier=None, couleur=None):
    """Dessine une fractale et sauvegarde éventuellement une image PNG."""
    image, axe = plt.subplots(figsize=(8, 8))
    dessiner_sur_axes(axe, fig, titre, couleur)
    if fichier is not None:
        chemin = Path(fichier)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        image.savefig(chemin, dpi=160, bbox_inches="tight")
    plt.close(image)


def animer_fractale(fig_initial, transformations, nbre_iter, titre,
                    fichier, pause=0.7, afficher=True, couleur=None):
    """Montre chaque itération dans la même fenêtre et sauvegarde la dernière.

    afficher=False permet de produire l'image finale sans interface graphique.
    """
    if pause < 0:
        raise ValueError("La durée de pause doit être positive ou nulle")
    if afficher:
        plt.ion()
        image, axe = plt.subplots(figsize=(8, 8))
    else:
        image = axe = None

    derniere_etape = None
    for etape, figures in etapes_fractale(fig_initial, transformations, nbre_iter):
        print(f"{titre} : étape {etape}/{nbre_iter} — {len(figures)} figure(s)", flush=True)
        derniere_etape = figures
        if afficher:
            dessiner_sur_axes(axe, figures, f"{titre} — Étape {etape}/{nbre_iter}", couleur)
            image.canvas.draw_idle()
            plt.pause(max(pause, 0.001))

    chemin = Path(fichier)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if afficher:
        # Enregistre exactement la dernière étape présentée à l'écran.
        image.savefig(chemin, dpi=160, bbox_inches="tight")
        print(f"Image finale enregistrée : {chemin}")
        plt.ioff()
        plt.show()  # Fenêtre finale maintenue ouverte jusqu'à fermeture.
    else:
        fractale(derniere_etape, f"{titre} — Étape {nbre_iter}", chemin, couleur)
        print(f"Image finale enregistrée : {chemin}")