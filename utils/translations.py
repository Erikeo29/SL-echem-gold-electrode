"""Traductions et gestion de la langue — Électrode Au/Ni/Cu."""
import streamlit as st

TRANSLATIONS = {
    "fr": {
        "title": "CV et EIS — Électrode Au avec impuretés Ni et Cu",
        "sidebar_title": "CV et EIS — Électrode Au/Ni/Cu",
        "gen_header": "Général",
        "models_header": "Résultats de modélisation",
        "annex_header": "Annexes",
        "gen_pages": ["Accueil", "Introduction", "Données électrochimiques", "Comparaison des études"],
        "model_pages": ["1 : CV électrode Au/Ni/Cu", "2 : EIS électrode Au/Ni/Cu"],
        "annex_pages": ["Conclusion et perspectives", "Lexique", "Équations clés", "Un peu d'histoire", "Références bibliographiques"],
        "tabs_cv_oxide": ["Physique", "Code", "Résultats"],
        "tabs_eis": ["Physique", "Code", "Résultats", "Analyse"],
        "version_info": """**Version 2.1.2** — Dec 2025 - *EQU*

**Nouveautés :**
- Étude paramétrique EIS
- Assistant IA Llama 3
- Filtres en cascade""",
        # Labels CV oxide
        "title_study_1": "Étude 1 : CV d'une électrode Au avec impuretés Ni et Cu",
        "title_study_2": "Étude 2 : EIS d'une électrode Au avec impuretés Ni et Cu",
        "lbl_ph": "pH",
        "lbl_pct_ni": "% Ni",
        "lbl_pct_cu": "% Cu",
        "lbl_composition": "Composition",
        "oxide_compare_title": "Comparaison côte à côte",
        "combo_unavailable": "Combinaison non disponible",
        # Labels EIS
        "eis_metrics_title": "Métriques EIS",
        "lbl_circuit": "Circuit",
        "lbl_Eocp": "E_ocp (V vs Ag/AgCl)",
        "lbl_Rct": "Rct (Ω)",
        "lbl_Rs": "Rs (Ω)",
        "lbl_Rfilm": "R_film (Ω)",
        "lbl_Cdl": "Cdl (F)",
        "lbl_phase_max": "Phase max (°)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LANCER LA VISUALISATION",
        "btn_reset": "RÉINITIALISER",
        "lbl_avail_sims": "Simulations disponibles",
        "image_unavailable": "Image non disponible",
        "placeholder_coming_soon": "Étude à venir - Contenu en cours de préparation",
        # Chatbot
        "chat_title": "Assistant IA",
        "chat_welcome": "Bonjour ! Je suis votre assistant pour comprendre les simulations de voltamétrie cyclique et d'impédance sur électrodes Au/Ni/Cu. Posez-moi vos questions sur les effets d'oxydes, la passivation, ou l'interprétation des diagrammes !",
        "chat_placeholder": "Posez votre question...",
        "chat_error": "Erreur de connexion à l'API.",
        "chat_clear": "Effacer",
        "chat_api_missing": "Clé API manquante. Configurez GROQ_API_KEY.",
    },
    "en": {
        "title": "CV & EIS — Au Electrode with Ni and Cu Impurities",
        "sidebar_title": "CV & EIS — Au/Ni/Cu Electrode",
        "gen_header": "General",
        "models_header": "Modeling Results",
        "annex_header": "Appendices",
        "gen_pages": ["Home", "Introduction", "Electrochemical Data", "Study Comparison"],
        "model_pages": ["1: CV Au/Ni/Cu electrode", "2: EIS Au/Ni/Cu electrode"],
        "annex_pages": ["Conclusion and Perspectives", "Glossary", "Key Equations", "A Bit of History", "Bibliographical References"],
        "tabs_cv_oxide": ["Physics", "Code", "Results"],
        "tabs_eis": ["Physics", "Code", "Results", "Analysis"],
        "version_info": """**Version 2.1.2** — Dec 2025 - *EQU*

**New Features:**
- EIS parametric study
- AI Assistant Llama 3
- Cascade filters""",
        # Labels CV oxide
        "title_study_1": "Study 1: CV of an Au electrode with Ni and Cu impurities",
        "title_study_2": "Study 2: EIS of an Au electrode with Ni and Cu impurities",
        "lbl_ph": "pH",
        "lbl_pct_ni": "% Ni",
        "lbl_pct_cu": "% Cu",
        "lbl_composition": "Composition",
        "oxide_compare_title": "Side-by-side comparison",
        "combo_unavailable": "Combination not available",
        # Labels EIS
        "eis_metrics_title": "EIS Metrics",
        "lbl_circuit": "Circuit",
        "lbl_Eocp": "E_ocp (V vs Ag/AgCl)",
        "lbl_Rct": "Rct (Ω)",
        "lbl_Rs": "Rs (Ω)",
        "lbl_Rfilm": "R_film (Ω)",
        "lbl_Cdl": "Cdl (F)",
        "lbl_phase_max": "Phase max (°)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LAUNCH VISUALIZATION",
        "btn_reset": "RESET",
        "lbl_avail_sims": "Available Simulations",
        "image_unavailable": "Image not available",
        "placeholder_coming_soon": "Coming Soon - Content under preparation",
        # Chatbot
        "chat_title": "AI Assistant",
        "chat_welcome": "Hello! I'm your assistant to help you understand CV and EIS simulations on Au/Ni/Cu electrodes. Ask me about oxide effects, passivation, or diagram interpretation!",
        "chat_placeholder": "Ask your question...",
        "chat_error": "API connection error.",
        "chat_clear": "Clear",
        "chat_api_missing": "API key missing. Configure GROQ_API_KEY.",
    }
}


def get_language() -> str:
    """Retourne la langue actuelle."""
    if 'lang' not in st.session_state:
        st.session_state.lang = 'fr'
    return st.session_state.lang


def t(key: str) -> str:
    """Retourne la traduction pour la clé donnée."""
    lang = get_language()
    return TRANSLATIONS[lang].get(key, key)
