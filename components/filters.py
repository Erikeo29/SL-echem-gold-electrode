"""Composants de filtres en cascade — Électrode Au/Ni/Cu."""
import os
import pandas as pd
import streamlit as st

from config import DATA_PATH
from utils.translations import t


def render_oxide_cascading_filters(df_origin: pd.DataFrame, key_prefix: str, sim_num: int) -> dict | None:
    """
    Filtres en cascade pour l'étude oxydes Au/Ni/Cu (3 paramètres).
    pH → %Ni → %Cu

    Returns:
        Dict avec png_cv, run_id, metrics ou None
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else (1 if len(df) > 1 else 0)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])

    with c1:
        ph_opts = sorted(df["pH"].unique())
        idx = min(default_idx, len(ph_opts) - 1)
        val_ph = st.selectbox("pH", ph_opts, key=f"{key_prefix}_ph{sim_num}", index=idx)
        df = df[df["pH"] == val_ph]

    with c2:
        ni_opts = sorted(df["Ni_pct"].unique())
        val_ni = st.selectbox("% Ni", ni_opts, key=f"{key_prefix}_ni{sim_num}")
        df = df[df["Ni_pct"] == val_ni]

    with c3:
        cu_opts = sorted(df["Cu_pct"].unique())
        val_cu = st.selectbox("% Cu", cu_opts, key=f"{key_prefix}_cu{sim_num}")
        df = df[df["Cu_pct"] == val_cu]

    if not df.empty:
        row = df.iloc[0]
        run_id = int(row["run_id"])
        return {
            "png_cv": os.path.join(DATA_PATH, "cv_oxide_study", "png", row["cv_png"]),
            "run_id": run_id,
            "metrics": {
                "Ipa": row.get("Ipa_uA", ""),
                "Ipc": row.get("Ipc_uA", ""),
                "deltaEp": row.get("deltaEp_mV", ""),
                "ratio": row.get("ratio", ""),
            }
        }
    return None


def render_eis_cascading_filters(df_origin: pd.DataFrame, key_prefix: str, sim_num: int) -> dict | None:
    """
    Filtres en cascade pour l'étude EIS (3 paramètres).
    pH → %Ni → %Cu

    Returns:
        Dict avec nyquist_png, bode_png, run, metrics ou None
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else (1 if len(df) > 1 else 0)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])

    with c1:
        ph_opts = sorted(df["pH"].unique())
        idx = min(default_idx, len(ph_opts) - 1)
        val_ph = st.selectbox(t("lbl_ph"), ph_opts, key=f"{key_prefix}_ph{sim_num}", index=idx)
        df = df[df["pH"] == val_ph]

    with c2:
        ni_opts = sorted(df["pct_Ni"].unique())
        val_ni = st.selectbox(t("lbl_pct_ni"), ni_opts, key=f"{key_prefix}_ni{sim_num}")
        df = df[df["pct_Ni"] == val_ni]

    with c3:
        cu_opts = sorted(df["pct_Cu"].unique())
        val_cu = st.selectbox(t("lbl_pct_cu"), cu_opts, key=f"{key_prefix}_cu{sim_num}")
        df = df[df["pct_Cu"] == val_cu]

    if not df.empty:
        row = df.iloc[0]
        run_id = int(row["run"])
        run_dir = os.path.join(DATA_PATH, "eis_study", f"run_{run_id:03d}")
        return {
            "nyquist_png": os.path.join(run_dir, row["nyquist_png"]),
            "bode_png": os.path.join(run_dir, row["bode_png"]),
            "run": run_id,
            "label": row.get("label", ""),
            "metrics": {
                "circuit": row.get("circuit", ""),
                "Rs_measured": row.get("Rs_measured", ""),
                "Rct_measured": row.get("Rct_measured", ""),
                "R_film_measured": row.get("R_film_measured", ""),
                "Cdl_eff": row.get("Cdl_eff", ""),
                "phase_max_deg": row.get("phase_max_deg", ""),
            }
        }
    return None
