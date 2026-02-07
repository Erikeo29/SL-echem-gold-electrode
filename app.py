"""Application Streamlit — CV et EIS de l'électrode Au avec impuretés Ni et Cu."""
import os
import streamlit as st

# --- Configuration de la page (DOIT être en premier) ---
st.set_page_config(page_title="CV & EIS — Au/Ni/Cu Electrode", layout="wide")

# --- Imports locaux ---
from config import ASSETS_PATH, CSS_PATH, DATA_PATH
from utils.translations import TRANSLATIONS, get_language, t
from utils.data_loaders import (
    load_oxide_mapping,
    load_eis_mapping,
    load_file_content,
    render_notebook,
)
from utils.media import load_media_as_base64, display_smart_markdown
from components.filters import (
    render_oxide_cascading_filters,
    render_eis_cascading_filters,
)
from components.chatbot import is_chatbot_enabled, render_chatbot


# --- Chargement CSS externe ---
def load_custom_css():
    """Charge le CSS et les boutons de navigation."""
    css_content = ""
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH, 'r', encoding='utf-8') as f:
            css_content = f.read()

    nav_buttons_html = """
<a href="#top" class="nav-button back-to-top" title="Retour en haut / Back to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 4l-8 8h5v8h6v-8h5z"/>
    </svg>
</a>
<a href="#bottom" class="nav-button scroll-to-bottom" title="Aller en bas / Go to bottom">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 20l8-8h-5V4h-6v8H4z"/>
    </svg>
</a>
<div id="top"></div>
"""
    return f"<style>{css_content}</style>{nav_buttons_html}"


st.markdown(load_custom_css(), unsafe_allow_html=True)


# --- Callbacks pour Navigation (INDEX-based) ---
def on_change_gen():
    selected = st.session_state.get('_radio_gen')
    if selected is not None:
        gen_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["gen_pages"]
        try:
            st.session_state.nav_gen_idx = gen_pages.index(selected)
        except ValueError:
            st.session_state.nav_gen_idx = 0
    st.session_state.nav_model_idx = None
    st.session_state.nav_annex_idx = None


def on_change_model():
    selected = st.session_state.get('_radio_model')
    if selected is not None:
        model_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["model_pages"]
        try:
            st.session_state.nav_model_idx = model_pages.index(selected)
        except ValueError:
            st.session_state.nav_model_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_annex_idx = None


def on_change_annex():
    selected = st.session_state.get('_radio_annex')
    if selected is not None:
        annex_pages = TRANSLATIONS[st.session_state.get('lang', 'fr')]["annex_pages"]
        try:
            st.session_state.nav_annex_idx = annex_pages.index(selected)
        except ValueError:
            st.session_state.nav_annex_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_model_idx = None


# --- Initialisation Centralisée des États ---
DEFAULT_SESSION_STATES = {
    # Navigation (stocke INDEX, pas texte - indépendant de la langue)
    'nav_gen_idx': 0,
    'nav_model_idx': None,
    'nav_annex_idx': None,
    # CV oxide Visualization
    'run_oxide_results': False,
    'files_oxide_results': (None, None),
    # EIS Visualization
    'run_eis_results': False,
    'files_eis_results': (None, None),
    # Chatbot
    'chat_messages': [],
}

for key, default in DEFAULT_SESSION_STATES.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Initialisation: Accueil (index 0) au premier chargement
if (st.session_state.nav_gen_idx is None and
    st.session_state.nav_model_idx is None and
    st.session_state.nav_annex_idx is None):
    st.session_state.nav_gen_idx = 0


# --- Barre Latérale ---

# Sélecteur de langue
old_lang = st.session_state.get('lang', 'fr')
lang_selection = st.sidebar.radio(
    "Language",
    ["Français", "English"],
    horizontal=True,
    label_visibility="collapsed",
    index=0 if old_lang == "fr" else 1,
)
new_lang = "fr" if "Français" in lang_selection else "en"

# Si la langue change, simplement rerun (les index sont indépendants de la langue)
if new_lang != old_lang:
    st.session_state.lang = new_lang
    st.rerun()

st.session_state.lang = new_lang

st.sidebar.title(t("sidebar_title"))
st.sidebar.markdown("---")

# Navigation par groupes avec callbacks INDEX-based
gen_pages = t("gen_pages")
model_pages = t("model_pages")
annex_pages = t("annex_pages")

st.sidebar.subheader(t("gen_header"))
nav_gen = st.sidebar.radio(
    "Nav Gen",
    gen_pages,
    key="_radio_gen",
    index=st.session_state.nav_gen_idx,
    on_change=on_change_gen,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("models_header"))
nav_model = st.sidebar.radio(
    "Nav Models",
    model_pages,
    key="_radio_model",
    index=st.session_state.nav_model_idx,
    on_change=on_change_model,
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("annex_header"))
nav_annex = st.sidebar.radio(
    "Nav Annex",
    annex_pages,
    key="_radio_annex",
    index=st.session_state.nav_annex_idx,
    on_change=on_change_annex,
    label_visibility="collapsed"
)

# --- Chatbot dans la Sidebar ---
if is_chatbot_enabled():
    st.sidebar.markdown("---")
    render_chatbot()

st.sidebar.markdown("---")
st.sidebar.markdown(t("version_info"))

# --- Déterminer la page active ---
# Priorité : modèles > annexes > général
selected_page = None
if st.session_state.nav_model_idx is not None:
    selected_page = model_pages[st.session_state.nav_model_idx]
elif st.session_state.nav_annex_idx is not None:
    selected_page = annex_pages[st.session_state.nav_annex_idx]
elif st.session_state.nav_gen_idx is not None:
    selected_page = gen_pages[st.session_state.nav_gen_idx]
else:
    selected_page = gen_pages[0]


# ===========================================================================
# PAGES
# ===========================================================================

# ===== PAGE ACCUEIL =====
if selected_page == gen_pages[0]:
    st.title(t("title"))
    st.markdown(load_file_content("accueil/accueil.md"))

# ===== PAGE INTRODUCTION =====
elif selected_page == gen_pages[1]:
    st.markdown(load_file_content("intro/intro_cv.md"))

# ===== PAGE DONNÉES ÉLECTROCHIMIQUES =====
elif selected_page == gen_pages[2]:
    st.markdown(load_file_content("data_electrochim/data_electrochim.md"))

# ===== PAGE COMPARAISON =====
elif selected_page == gen_pages[3]:
    st.markdown(load_file_content("intro/comparaison_cv.md"))

# ===== ÉTUDE 1 - CV électrode Au/Ni/Cu =====
elif selected_page == model_pages[0]:
    st.title(t("title_study_1"))

    tabs_oxide = st.tabs(t("tabs_cv_oxide"))

    with tabs_oxide[0]:
        st.markdown(load_file_content("physics/cv_oxide.md"))

    with tabs_oxide[1]:
        render_notebook("code/cv_oxide_notebook.ipynb")

    with tabs_oxide[2]:
        df_oxide = load_oxide_mapping()

        if not df_oxide.empty:
            with st.container(border=True):
                c_pop, _ = st.columns([0.3, 0.7])
                with c_pop:
                    with st.popover(t("lbl_avail_sims"), use_container_width=True):
                        st.dataframe(
                            df_oxide[["run_id", "Au_pct", "Ni_pct", "Cu_pct", "pH"]],
                            use_container_width=True, hide_index=True
                        )

                files1 = render_oxide_cascading_filters(df_oxide, "ox", 1)
                st.divider()
                files2 = render_oxide_cascading_filters(df_oxide, "ox", 2)

                _, btn1, btn2, _ = st.columns([1, 1, 1, 1])
                with btn1:
                    if st.button(t("btn_launch"), type="primary", key="btn_oxide_results"):
                        st.session_state.run_oxide_results = True
                        st.session_state.files_oxide_results = (files1, files2)
                with btn2:
                    if st.button(t("btn_reset"), type="secondary", key="rst_oxide_results"):
                        st.session_state.run_oxide_results = False
                        st.rerun()

            if st.session_state.get("run_oxide_results", False):
                f1, f2 = st.session_state.files_oxide_results

                st.markdown("### Voltammogrammes (PNG)")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and os.path.exists(f["png_cv"]):
                            st.markdown(f"**{sim_label}** — Run {f['run_id']}")
                            st.image(f["png_cv"], use_container_width=True)
                        else:
                            st.warning(t("image_unavailable"))
        else:
            st.info(t("placeholder_coming_soon"))

# ===== ÉTUDE 2 - EIS électrode Au/Ni/Cu =====
elif selected_page == model_pages[1]:
    st.title(t("title_study_2"))

    tabs_eis = st.tabs(t("tabs_eis"))

    with tabs_eis[0]:
        st.markdown(load_file_content("physics/eis.md"))

    with tabs_eis[1]:
        st.markdown(load_file_content("code/eis_code.md"))

    with tabs_eis[2]:
        df_eis = load_eis_mapping()

        if not df_eis.empty:
            with st.container(border=True):
                c_pop, _ = st.columns([0.3, 0.7])
                with c_pop:
                    with st.popover(t("lbl_avail_sims"), use_container_width=True):
                        st.dataframe(
                            df_eis[["run", "pct_Ni", "pct_Cu", "pH", "E_ocp_V", "circuit",
                                    "Rct_measured", "R_film_measured", "Cdl_eff"]],
                            use_container_width=True, hide_index=True
                        )

                files1 = render_eis_cascading_filters(df_eis, "eis", 1)
                st.divider()
                files2 = render_eis_cascading_filters(df_eis, "eis", 2)

                _, btn1, btn2, _ = st.columns([1, 1, 1, 1])
                with btn1:
                    if st.button(t("btn_launch"), type="primary", key="btn_eis_results"):
                        st.session_state.run_eis_results = True
                        st.session_state.files_eis_results = (files1, files2)
                with btn2:
                    if st.button(t("btn_reset"), type="secondary", key="rst_eis_results"):
                        st.session_state.run_eis_results = False
                        st.rerun()

            if st.session_state.get("run_eis_results", False):
                f1, f2 = st.session_state.files_eis_results

                st.markdown("### 1. Diagrammes de Nyquist")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and os.path.exists(f["nyquist_png"]):
                            st.markdown(f"**{sim_label}** — Run {f['run']} ({f['label']})")
                            st.image(f["nyquist_png"], use_container_width=True)
                        else:
                            st.warning(t("image_unavailable"))

                st.markdown("---")

                st.markdown("### 2. Diagrammes de Bode")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and os.path.exists(f["bode_png"]):
                            st.image(f["bode_png"], use_container_width=True)
                        else:
                            st.warning(t("image_unavailable"))

                st.markdown("---")

                st.markdown(f"### 3. {t('eis_metrics_title')}")
                c1, c2 = st.columns(2)
                for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
                    with col:
                        if f and f.get("metrics"):
                            m = f["metrics"]
                            st.markdown(f"**{sim_label}** — Run {f['run']}")
                            mc1, mc2, mc3 = st.columns(3)
                            mc1.metric(t("lbl_circuit"), m["circuit"])
                            mc2.metric(t("lbl_Eocp"), f"{m['E_ocp_V']:+.3f} V" if isinstance(m['E_ocp_V'], (int, float)) else str(m['E_ocp_V']))
                            mc3.metric(t("lbl_Rs"), f"{m['Rs_measured']:.1f}" if isinstance(m['Rs_measured'], (int, float)) else str(m['Rs_measured']))
                            mc4, mc5, mc6 = st.columns(3)
                            mc4.metric(t("lbl_Rct"), f"{m['Rct_measured']:.1f}" if isinstance(m['Rct_measured'], (int, float)) else str(m['Rct_measured']))
                            mc5.metric(t("lbl_Rfilm"), f"{m['R_film_measured']:.1f}" if isinstance(m['R_film_measured'], (int, float)) else str(m['R_film_measured']))
                            mc6.metric(t("lbl_Cdl"), f"{m['Cdl_eff']:.2e}" if isinstance(m['Cdl_eff'], (int, float)) else str(m['Cdl_eff']))
                            mc7, _, _ = st.columns(3)
                            mc7.metric(t("lbl_phase_max"), f"{m['phase_max_deg']:.1f}°" if isinstance(m['phase_max_deg'], (int, float)) else str(m['phase_max_deg']))
        else:
            st.info(t("placeholder_coming_soon"))

    with tabs_eis[3]:
        st.markdown("### Analyse de l'étude 2 — EIS électrode Au/Ni/Cu")

        st.markdown("""
L'étude paramétrique de 27 simulations EIS (Ni/Cu = 0, 10, 30 %, pH = 3, 7, 11) — alignée
avec l'étude CV — met en évidence les tendances suivantes :

**Potentiel de circuit ouvert (OCP)** :
L'EIS est simulée à l'OCP, estimé par moyenne pondérée des E_ocp de chaque métal pur
(approximation de potentiel mixte). Les valeurs Rct sont des données bibliographiques à l'OCP,
non dérivées de Butler-Volmer.
- Au pur : E_ocp = +0.50 V (pH 3), +0.15 V (pH 7), −0.10 V (pH 11) vs Ag/AgCl
- Ni/Cu tirent l'OCP vers des valeurs plus négatives (Ni : −0.25 V, Cu : +0.02 V à pH 3)

**Effet du pH sur Rct** :
- pH 3 : Rct faible (~800–1280 Ω) — dissolution active, cinétique rapide
- pH 7 : Rct maximal (~3100–4700 Ω) — passivation partielle, cinétique lente
- pH 11 : Rct élevé (~2270–6000 Ω) — films passifs sur tous les métaux

**Effet du Ni** : augmente Rct à pH 11 de façon marquée (Ni(OH)₂/NiOOH très protecteur,
R_film intrinsèque = 2000 Ω). Au70%Ni30% atteint Rct ≈ 5170 Ω à pH 11.

**Effet du Cu** : réduit Rct à pH 3 (dissolution rapide, Rct intrinsèque Cu = 500 Ω)
mais augmente la résistance de film à pH 11 (Cu₂O/CuO, R_film = 800 Ω).

**Composition extrême** : Au40%Ni30%Cu30% à pH 11 présente le Rct le plus élevé (~6000 Ω)
avec un film passif mixte (R_film = 900 Ω), cohérent avec les diagrammes de Pourbaix.
""")


# ===== PAGES ANNEXES =====
elif selected_page in annex_pages:
    idx = annex_pages.index(selected_page)
    annex_files = [
        "conclusion/cv_conclusion.md",
        "lexique/cv_lexique.md",
        "equations/cv_equations.md",
        "histoire/cv_histoire.md",
        "biblio/cv_biblio.md"
    ]

    try:
        st.markdown(load_file_content(annex_files[idx]))
    except Exception as e:
        st.error(f"Erreur de chargement: {e}")

# --- Ancre de fin de page ---
st.markdown('<div id="bottom"></div>', unsafe_allow_html=True)
