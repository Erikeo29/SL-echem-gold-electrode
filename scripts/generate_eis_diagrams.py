"""Generate publication-quality EIS diagrams: annotated Nyquist/Bode and Randles circuit."""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import LineCollection
from pathlib import Path

# ---------------------------------------------------------------------------
# Output paths
# ---------------------------------------------------------------------------
BASE = Path(
    "/home/erikeo29/20_RD_Divers/04_Streamlit electrochemisty_v1"
    "/electrochemistry-v2/assets/eis/png"
)
BASE.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Physical / circuit parameters
# ---------------------------------------------------------------------------
Rs = 50.0          # Ohm
Rct = 500.0        # Ohm
Q0 = 30e-6         # F s^(n-1)
n_CPE = 0.92
sigma = 30.0       # Ohm s^(-0.5)
f_min, f_max = 0.01, 1e5
pts_per_decade = 10

n_decades = np.log10(f_max / f_min)
n_points = int(n_decades * pts_per_decade) + 1
f = np.logspace(np.log10(f_min), np.log10(f_max), n_points)
omega = 2.0 * np.pi * f

# ---------------------------------------------------------------------------
# Impedance calculation
# ---------------------------------------------------------------------------
Z_CPE = 1.0 / (Q0 * (1j * omega) ** n_CPE)
Z_W = (sigma / np.sqrt(omega)) * (1.0 - 1j)
Z_faradaic = Rct + Z_W
Z_total = Rs + 1.0 / (1.0 / Z_CPE + 1.0 / Z_faradaic)

Z_re = Z_total.real
Z_im = Z_total.imag
Z_mag = np.abs(Z_total)
Z_phase = -np.degrees(np.angle(Z_total))  # -phi in degrees

# ---------------------------------------------------------------------------
# Helper: find semicircle top (max -Im for charge-transfer region)
# ---------------------------------------------------------------------------
neg_im = -Z_im
idx_max = np.argmax(neg_im)
omega_max = omega[idx_max]
f_max_sc = f[idx_max]

# =========================================================================
# FIGURE 1 : Nyquist + Bode (3 panels)
# =========================================================================
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 16,
    "axes.linewidth": 1.0,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "axes.labelsize": 17,
    "axes.titlesize": 18,
    "axes.titleweight": "bold",
    "axes.labelweight": "bold",
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
})

fig1, axes = plt.subplots(1, 3, figsize=(20, 6.5), constrained_layout=True)
ax_ny, ax_bz, ax_bp = axes

# --- Nyquist panel --------------------------------------------------------
# Color gradient high-freq (blue) -> low-freq (red)
colors = plt.cm.coolwarm(np.linspace(0, 1, len(f)))

# Build line collection for gradient coloring
points = np.column_stack([Z_re, neg_im]).reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, colors=colors[:-1], linewidths=2.5)
ax_ny.add_collection(lc)
ax_ny.autoscale()
ax_ny.set_aspect("equal", adjustable="datalim")
ax_ny.set_xlabel(r"Re(Z) / $\Omega$")
ax_ny.set_ylabel(r"$-$Im(Z) / $\Omega$")
ax_ny.set_title("Nyquist diagram")

# Dashed vertical reference lines
for xval, label in [(Rs, r"$\mathbf{R_s}$"), (Rs + Rct, r"$\mathbf{R_s + R_{ct}}$")]:
    ax_ny.axvline(xval, color="gray", ls="--", lw=0.7, zorder=0)
    ax_ny.annotate(
        label,
        xy=(xval, 0),
        xytext=(xval, -35),
        fontsize=15,
        ha="center",
        color="#333",
        arrowprops=dict(arrowstyle="->", color="gray", lw=1.0),
    )

# omega_max dot + annotation
ax_ny.plot(Z_re[idx_max], neg_im[idx_max], "ko", ms=7, zorder=5)
ax_ny.annotate(
    rf"$\mathbf{{\omega_{{max}}}}$ = {omega_max:.1f} rad/s",
    xy=(Z_re[idx_max], neg_im[idx_max]),
    xytext=(Z_re[idx_max] + 70, neg_im[idx_max] + 50),
    fontsize=14, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="k", lw=1.0),
)

# Semicircle label
mid_re = Rs + Rct / 2
ax_ny.text(
    mid_re, neg_im[idx_max] * 0.45,
    "Semicircle\n= charge transfer",
    ha="center", va="center", fontsize=14, fontweight="bold",
    style="italic", color="#333",
)

# Warburg tail label (low-frequency points = end of array = index 0..~10)
idx_lf = int(len(f) * 0.07)  # pick a point in the low-freq Warburg region
ax_ny.annotate(
    r"Warburg (45$\degree$)",
    xy=(Z_re[idx_lf], neg_im[idx_lf]),
    xytext=(Z_re[idx_lf] + 80, neg_im[idx_lf] + 70),
    fontsize=14, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="k", lw=1.0),
)

# --- Bode |Z| panel -------------------------------------------------------
ax_bz.loglog(f, Z_mag, "k-", lw=2.0)
ax_bz.set_xlabel("f / Hz")
ax_bz.set_ylabel(r"|Z| / $\Omega$")
ax_bz.set_title("Bode magnitude")

# Plateau annotations
ax_bz.axhline(Rs, color="gray", ls=":", lw=0.8)
ax_bz.text(1e4, Rs * 1.3, r"$\mathbf{R_s}$", fontsize=15, color="#333")
ax_bz.axhline(Rs + Rct, color="gray", ls=":", lw=0.8)
ax_bz.text(0.05, (Rs + Rct) * 0.78, r"$\mathbf{R_s + R_{ct}}$", fontsize=15, color="#333")
ax_bz.annotate(
    "Transition",
    xy=(f_max_sc, Z_mag[idx_max]),
    xytext=(f_max_sc * 5, Z_mag[idx_max] * 1.8),
    fontsize=14, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="k", lw=1.0),
)

# --- Bode phase panel ------------------------------------------------------
ax_bp.semilogx(f, Z_phase, "k-", lw=2.0)
ax_bp.set_xlabel("f / Hz")
ax_bp.set_ylabel(r"$-\varphi$ / deg")
ax_bp.set_title("Bode phase")

idx_phase_max = np.argmax(Z_phase)
ax_bp.plot(f[idx_phase_max], Z_phase[idx_phase_max], "ko", ms=7)
ax_bp.annotate(
    rf"$\mathbf{{\varphi_{{max}}}}$ = {Z_phase[idx_phase_max]:.1f}$\degree$",
    xy=(f[idx_phase_max], Z_phase[idx_phase_max]),
    xytext=(f[idx_phase_max] * 8, Z_phase[idx_phase_max] - 5),
    fontsize=14, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="k", lw=1.0),
)

# Region labels
ax_bp.text(1e3, Z_phase.max() * 0.35, "Capacitive\nregion", fontsize=14,
           ha="center", color="#333", fontweight="bold", style="italic")
ax_bp.text(0.05, Z_phase.max() * 0.25, "Warburg\nregion", fontsize=14,
           ha="center", color="#333", fontweight="bold", style="italic")

out1 = BASE / "nyquist_bode_annotated.png"
fig1.savefig(out1, dpi=300, facecolor="white")
plt.close(fig1)
print(f"Saved {out1}")


# =========================================================================
# FIGURE 2 : Randles circuit diagram (pure matplotlib)
# =========================================================================
fig2, ax = plt.subplots(figsize=(5.5, 3.2))
ax.set_xlim(-0.5, 8.5)
ax.set_ylim(-1.5, 4.5)
ax.set_aspect("equal")
ax.axis("off")

# --- drawing helpers -------------------------------------------------------

def draw_resistor(ax, x0, y0, w, h, label, fontsize=9):
    """Rectangle resistor symbol."""
    rect = mpatches.FancyBboxPatch(
        (x0, y0 - h / 2), w, h,
        boxstyle="round,pad=0.02", ec="k", fc="white", lw=1.2,
    )
    ax.add_patch(rect)
    ax.text(x0 + w / 2, y0, label, ha="center", va="center", fontsize=fontsize,
            weight="bold")


def draw_wire(ax, x0, y0, x1, y1):
    ax.plot([x0, x1], [y0, y1], "k-", lw=1.2)


def draw_cpe(ax, xc, yc, size=0.35, label="CPE"):
    """Two slanted parallel lines for CPE symbol."""
    dx, dy = size, size * 0.7
    # left plate (slanted)
    ax.plot([xc - dx, xc - dx + 0.1], [yc - dy, yc + dy], "k-", lw=1.5)
    # right plate (slanted)
    ax.plot([xc + dx, xc + dx - 0.1], [yc - dy, yc + dy], "k-", lw=1.5)
    ax.text(xc, yc + dy + 0.25, label, ha="center", va="bottom", fontsize=9,
            weight="bold")
    return (xc - dx, yc), (xc + dx, yc)  # connection points


def draw_warburg(ax, xc, yc, size=0.4, label=r"$Z_W$"):
    """Warburg: open semi-circle / hatched half-circle symbol approximation."""
    # Draw as a small rectangle with diagonal hatching inside
    w, h = size * 2, size * 1.2
    rect = mpatches.FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.02", ec="k", fc="white", lw=1.2,
    )
    ax.add_patch(rect)
    # Diagonal hatching lines inside
    n_lines = 4
    for i in range(n_lines):
        frac = (i + 1) / (n_lines + 1)
        lx = xc - w / 2 + frac * w
        ax.plot([lx - 0.08, lx + 0.08], [yc - h / 2 + 0.05, yc + h / 2 - 0.05],
                "k-", lw=0.6, alpha=0.5)
    ax.text(xc, yc, label, ha="center", va="center", fontsize=8, weight="bold")


# --- Main circuit layout ---------------------------------------------------
# y levels
y_main = 2.0
y_top = 3.5    # CPE branch
y_bot = 0.5    # Rct + ZW branch

# Left terminal
ax.plot(-0.3, y_main, "ko", ms=6)
ax.text(-0.3, y_main + 0.3, "E", ha="center", fontsize=8)

# Wire to Rs
draw_wire(ax, -0.3, y_main, 0.5, y_main)

# Rs resistor
draw_resistor(ax, 0.5, y_main, 1.2, 0.5, r"$R_s$")

# Wire from Rs to junction
draw_wire(ax, 1.7, y_main, 2.5, y_main)

# Junction - split into top/bottom
jx = 2.5
draw_wire(ax, jx, y_main, jx, y_top)
draw_wire(ax, jx, y_main, jx, y_bot)

# ---- Top branch: CPE ----
draw_wire(ax, jx, y_top, 3.8, y_top)
cpe_left, cpe_right = draw_cpe(ax, 4.3, y_top, size=0.35, label=r"$CPE_{dl}$")
draw_wire(ax, 3.8, y_top, cpe_left[0], y_top)
draw_wire(ax, cpe_right[0], y_top, 5.3, y_top)

# ---- Bottom branch: Rct + ZW ----
draw_wire(ax, jx, y_bot, 3.0, y_bot)
draw_resistor(ax, 3.0, y_bot, 1.2, 0.5, r"$R_{ct}$")
draw_wire(ax, 4.2, y_bot, 4.8, y_bot)
draw_warburg(ax, 5.3, y_bot, size=0.4, label=r"$Z_W$")
draw_wire(ax, 5.7, y_bot, 6.3, y_bot)

# Rejoin
rx = 6.3
draw_wire(ax, 5.3, y_top, rx, y_top)
draw_wire(ax, rx, y_top, rx, y_main)
draw_wire(ax, rx, y_bot, rx, y_main)

# Wire to right terminal
draw_wire(ax, rx, y_main, 7.5, y_main)
ax.plot(7.5, y_main, "ko", ms=6)
ax.text(7.5, y_main + 0.3, "E'", ha="center", fontsize=8)

# Junction dots
ax.plot(jx, y_main, "ko", ms=4)
ax.plot(rx, y_main, "ko", ms=4)

# --- Equation below -------------------------------------------------------
eq = (
    r"$Z(\omega) = R_s + \dfrac{1}{\dfrac{1}{Z_{CPE}} + "
    r"\dfrac{1}{R_{ct} + Z_W}}$"
)
ax.text(3.6, -1.0, eq, ha="center", va="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", fc="#f7f7f7", ec="gray", lw=0.8))

out2 = BASE / "randles_circuit.png"
fig2.savefig(out2, dpi=300, facecolor="white", bbox_inches="tight")
plt.close(fig2)
print(f"Saved {out2}")
