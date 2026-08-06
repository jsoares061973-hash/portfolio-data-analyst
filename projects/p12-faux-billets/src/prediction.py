"""
Application de détection automatique de faux billets.

Ce script charge le modèle de classification entraîné dans le notebook
et permet de prédire si un ou plusieurs billets sont authentiques ou faux
à partir de leurs six caractéristiques géométriques.
"""

import argparse
from pathlib import Path

import joblib
import pandas as pd


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

# Dossier dans lequel se trouve ce script
DOSSIER_SCRIPT = Path(__file__).resolve().parent

# Racine du projet (dossier parent de src/)
DOSSIER_PROJET = DOSSIER_SCRIPT.parent

# Chemin vers le modèle sauvegardé
CHEMIN_MODELE = (
    DOSSIER_PROJET
    / "models"
    / "modele_detection_billets.joblib")

# Variables géométriques attendues par le modèle
VARIABLES_MODELE = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length",]


# -------------------------------------------------------------------
# Chargement du modèle
# -------------------------------------------------------------------

if not CHEMIN_MODELE.exists():
    raise FileNotFoundError(
        f"Le modèle est introuvable : {CHEMIN_MODELE}")

modele = joblib.load(CHEMIN_MODELE)

print("Modèle chargé avec succès.")


# -------------------------------------------------------------------
# Lecture et validation d'un fichier CSV
# -------------------------------------------------------------------

def charger_fichier_csv(
    chemin_fichier: str | Path) -> pd.DataFrame:
    """
    Charge un fichier CSV et vérifie la présence
    des variables attendues.
    """

    chemin = Path(chemin_fichier)

    if not chemin.exists():
        raise FileNotFoundError(
            f"Le fichier CSV est introuvable : {chemin}")

    donnees = pd.read_csv(
        chemin,
        sep=None,
        engine="python")

    colonnes_manquantes = [
        colonne
        for colonne in VARIABLES_MODELE
        if colonne not in donnees.columns]

    if colonnes_manquantes:
        raise ValueError(
            "Colonnes manquantes dans le fichier : "
            + ", ".join(colonnes_manquantes))

    return donnees


# -------------------------------------------------------------------
# Prédiction pour plusieurs billets contenus dans un CSV
# -------------------------------------------------------------------

def predire_fichier(
    chemin_fichier: str | Path) -> pd.DataFrame:
    """
    Prédit la nature de tous les billets
    contenus dans un fichier CSV.
    """

    donnees = charger_fichier_csv(chemin_fichier)

    # Sélection des six variables géométriques
    donnees_modele = donnees[VARIABLES_MODELE]

    # True = billet authentique ; False = faux billet
    predictions = modele.predict(donnees_modele)

    # Conservation de l'identifiant lorsqu'il est présent
    if "id" in donnees.columns:
        resultats = pd.DataFrame({
            "id": donnees["id"],
            "is_genuine": predictions})
    else:
        resultats = pd.DataFrame({
            "is_genuine": predictions})

    return resultats


# -------------------------------------------------------------------
# Prédiction pour un billet unique
# -------------------------------------------------------------------

def predire_billet(
    diagonal: float,
    height_left: float,
    height_right: float,
    margin_low: float,
    margin_up: float,
    length: float) -> bool:
    """
    Prédit la nature d'un billet
    à partir de ses six dimensions.
    """

    donnees_billet = pd.DataFrame([{
        "diagonal": diagonal,
        "height_left": height_left,
        "height_right": height_right,
        "margin_low": margin_low,
        "margin_up": margin_up,
        "length": length}])

    prediction = modele.predict(donnees_billet)[0]

    return bool(prediction)


# -------------------------------------------------------------------
# Fonction principale
# -------------------------------------------------------------------

def main() -> None:
    """
    Gère les arguments transmis depuis le terminal
    et lance le mode de prédiction demandé.
    """

    parser = argparse.ArgumentParser(
        description="Application de détection de faux billets.")

    sous_commandes = parser.add_subparsers(
        dest="mode")

    # Mode 1 : fichier CSV
    parser_fichier = sous_commandes.add_parser(
        "fichier",
        help="Prédire les billets contenus dans un fichier CSV.")

    parser_fichier.add_argument(
        "chemin",
        nargs="?",
        default=str(
            DOSSIER_SCRIPT / "billets_production.csv"),
        help="Chemin vers le fichier CSV.")

    # Mode 2 : billet unique
    parser_billet = sous_commandes.add_parser(
        "billet",
        help="Prédire un billet à partir de ses six dimensions.")

    parser_billet.add_argument(
        "--diagonal",
        type=float,
        required=True)

    parser_billet.add_argument(
        "--height-left",
        type=float,
        required=True)

    parser_billet.add_argument(
        "--height-right",
        type=float,
        required=True)

    parser_billet.add_argument(
        "--margin-low",
        type=float,
        required=True)

    parser_billet.add_argument(
        "--margin-up",
        type=float,
        required=True)

    parser_billet.add_argument(
        "--length",
        type=float,
        required=True)

    arguments = parser.parse_args()

    # Prédiction d'un billet unique
    if arguments.mode == "billet":
        prediction = predire_billet(
            diagonal=arguments.diagonal,
            height_left=arguments.height_left,
            height_right=arguments.height_right,
            margin_low=arguments.margin_low,
            margin_up=arguments.margin_up,
            length=arguments.length)

        print(f"\nPrédiction : {prediction}")

    # Prédiction à partir d'un fichier CSV
    else:
        chemin_fichier = getattr(
            arguments,
            "chemin",
            str(
                DOSSIER_SCRIPT
                / "billets_production.csv"))

        resultats = predire_fichier(
            chemin_fichier)

        print("\nRésultats des prédictions :")
        print(resultats.to_string(index=False))

        nombre_faux = (resultats["is_genuine"].eq(False).sum())

        nombre_vrais = (resultats["is_genuine"].eq(True).sum())

        print("\nRésumé :")
        print(f"Faux billets : {nombre_faux}")
        print("Billets authentiques : "f"{nombre_vrais}")


# -------------------------------------------------------------------
# Exécution du programme
# -------------------------------------------------------------------

if __name__ == "__main__":    main()
