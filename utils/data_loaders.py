"""Fonctions de chargement des données — Électrode Au/Ni/Cu."""
import os
import pandas as pd
import streamlit as st

from config import DATA_PATH, DOC_PATH
from utils.translations import get_language


@st.cache_data(ttl=600)
def load_oxide_mapping():
    """Charge le CSV de l'étude oxydes Au/Ni/Cu."""
    try:
        csv_path = os.path.join(DATA_PATH, 'cv_oxide_study/study_summary.csv')
        df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        return df
    except Exception:
        return pd.DataFrame()


@st.cache_data(ttl=600)
def load_eis_mapping():
    """Charge le CSV de l'étude EIS Au/Ni/Cu."""
    try:
        csv_path = os.path.join(DATA_PATH, 'eis_study/parametric_summary.csv')
        df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        return df
    except Exception:
        return pd.DataFrame()


def load_file_content(relative_path: str) -> str:
    """Charge un fichier depuis docs/<lang>/relative_path."""
    lang = get_language()
    full_path = os.path.join(DOC_PATH, lang, relative_path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return f"Document not found: {relative_path}"
