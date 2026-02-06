"""Fonctions de gestion des médias (images, GIF)."""
import base64
import os
import re
import streamlit as st

from config import DOC_PATH, ROOT_DIR
from utils.translations import get_language


def load_media_as_base64(file_path: str) -> str | None:
    """Charge une image/GIF en base64 pour affichage inline."""
    try:
        with open(file_path, "rb") as file:
            contents = file.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        if file_path.lower().endswith('.gif'):
            mime_type = 'image/gif'
        elif file_path.lower().endswith(('.jpg', '.jpeg')):
            mime_type = 'image/jpeg'
        else:
            mime_type = 'image/png'
        return f'<img src="data:{mime_type};base64,{data_url}" style="width:100%; max-width:600px;">'
    except Exception:
        return None


def display_smart_markdown(content: str, doc_relative_path: str = None):
    """Affiche du markdown avec support des images locales.

    Détecte les balises ![alt](path) et les remplace par st.image().
    Les chemins relatifs sont résolus par rapport au fichier .md source.
    """
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

    # Determine base directory for resolving relative image paths
    if doc_relative_path:
        lang = get_language()
        doc_dir = os.path.dirname(os.path.join(DOC_PATH, lang, doc_relative_path))
    else:
        doc_dir = ROOT_DIR

    parts = img_pattern.split(content)
    # parts = [text, alt, path, text, alt, path, ...]
    i = 0
    while i < len(parts):
        if i % 3 == 0:
            # Text block
            text = parts[i].strip()
            if text:
                st.markdown(text)
        elif i % 3 == 2:
            # Image path (follows alt text at i-1)
            img_path = parts[i]
            alt_text = parts[i - 1]
            # Resolve relative path
            abs_path = os.path.normpath(os.path.join(doc_dir, img_path))
            if os.path.exists(abs_path):
                if "circuit" in img_path.lower():
                    st.image(abs_path, caption=alt_text if alt_text else None, width=450)
                else:
                    st.image(abs_path, caption=alt_text if alt_text else None, use_container_width=True)
            else:
                st.warning(f"Image not found: {img_path}")
        i += 1
