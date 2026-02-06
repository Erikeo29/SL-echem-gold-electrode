"""Configuration globale de l'application — Électrode Au/Ni/Cu."""
import os

# --- Chemins ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(ROOT_DIR, "docs")
DATA_PATH = os.path.join(ROOT_DIR, "data")
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
CSS_PATH = os.path.join(ASSETS_PATH, "style.css")

# --- Version ---
VERSION = "3.0.0"
VERSION_DATE = "Feb 2026"
