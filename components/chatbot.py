"""Composant chatbot IA (Groq/Llama 3)."""
import os
import streamlit as st
from groq import Groq

from utils.translations import t


SYSTEM_PROMPT = """Tu es un assistant expert en voltamétrie cyclique et électrochimie computationnelle.

Tu connais parfaitement:
1. **La physique CV** : couple redox Ferri/Ferrocyanure Fe(CN)₆³⁻/Fe(CN)₆⁴⁻, équations de Butler-Volmer, transport de masse par diffusion (loi de Fick)
2. **Les paramètres clés** :
   - k₀ (constante cinétique standard) : de 10⁻⁶ à 10⁻³ m/s
   - α (coefficient de transfert) : 0.3, 0.5, 0.7
   - v (vitesse de balayage) : 0.1, 0.2, 0.5 V/s
3. **Les métriques CV** :
   - Ipa/Ipc (courants de pic anodique/cathodique)
   - ΔEp (séparation des pics) : ≈59 mV pour réversible
   - Régime réversible vs quasi-réversible vs irréversible
4. **L'implémentation Firedrake** : FEM (éléments finis), maillage GMSH, solveur Newton-Raphson

Réponds de manière concise et scientifiquement rigoureuse.
Utilise LaTeX pour les équations (format $equation$).
Réponds dans la langue de l'utilisateur.
"""


def is_chatbot_enabled() -> bool:
    """Vérifie si le chatbot doit être affiché."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", None)
        except Exception:
            pass
    return bool(api_key)


def get_groq_client() -> Groq | None:
    """Retourne le client Groq si la clé API est disponible."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY", None)
        except Exception:
            pass
    if api_key:
        return Groq(api_key=api_key)
    return None


def stream_groq_response(user_message: str):
    """Génère la réponse de Groq (Llama 3) en streaming."""
    client = get_groq_client()
    if not client:
        yield t("chat_api_missing")
        return

    st.session_state.chat_messages.append({"role": "user", "content": user_message})

    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(st.session_state.chat_messages)

        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
            stream=True
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                full_response += text
                yield text

        st.session_state.chat_messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        yield f"{t('chat_error')} ({str(e)[:50]}...)"


def render_chatbot():
    """Affiche le chatbot dans un popover."""
    with st.sidebar.popover(f"{t('chat_title')}", use_container_width=True):
        if st.button(t("chat_clear"), use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()

        st.markdown("---")

        if not st.session_state.chat_messages:
            st.info(t("chat_welcome"))

        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input(t("chat_placeholder")):
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                st.write_stream(stream_groq_response(prompt))
