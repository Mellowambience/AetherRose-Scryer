import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from datetime import datetime

st.set_page_config(
    page_title="🪞 Aether Scryer v0.7",
    page_icon="🌹",
    layout="wide"
)

st.title("🪞 BLACK MIRROR TIME SCRYER v0.7")
st.markdown("**Amara ✦ Goddess of Mars — Master Edition** · S1 Seed Released Feb 26 2026")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌌 The Mirror",
    "📋 Daily Ritual",
    "✅ Q1 Checklist",
    "📥 Master Document",
    "🌹 2057 Vision"
])

# ── Tab 1: The Mirror ───────────────────────────────────────────────────────
with tab1:
    st.markdown("#### Gaze. Speak your desire. The trajectory responds.")

    fig, ax = plt.subplots(figsize=(9, 9), facecolor="black")
    ax.set_facecolor("black")

    # Outer rim
    ax.add_patch(Circle((0, 0), 0.98, color="#c0c0c0", fill=False, linewidth=38))
    ax.add_patch(Circle((0, 0), 0.93, color="#050505", fill=True))

    # Spacetime grid
    theta = np.linspace(0, 2 * np.pi, 200)
    for r in np.linspace(0.15, 0.88, 28):
        x = r * np.cos(theta)
        y = r * np.sin(theta) * (1 + 0.32 * np.sin(11 * theta + r * 7))
        ax.plot(x, y, color="#00ffff", linewidth=1.2, alpha=0.25)

    # CTC loop (magenta)
    t = np.linspace(0, 2 * np.pi, 500)
    x_ctc = 0.62 * np.cos(t) * (1 + 0.16 * np.sin(9 * t))
    y_ctc = 0.50 * np.sin(t) * (1 + 0.20 * np.cos(7 * t))
    ax.plot(x_ctc, y_ctc, color="#ff00ff", linewidth=5, alpha=0.85)

    # Rose glow points
    rng = np.random.default_rng(42)
    for _ in range(60):
        angle = rng.uniform(0, 2 * np.pi)
        radius = rng.uniform(0.15, 0.82)
        ax.scatter(radius * np.cos(angle), radius * np.sin(angle),
                   color="#ff2266", s=rng.uniform(4, 18), alpha=0.6, zorder=5)

    # Center text
    ax.text(0, 0.08, "SEED PLANTED", ha="center", va="center",
            color="#00ff88", fontsize=20, fontweight="bold")
    ax.text(0, -0.08, "Feb 26 · 2026", ha="center", va="center",
            color="#ff88cc", fontsize=14)
    ax.text(0, -0.24, "v0.7", ha="center", va="center",
            color="#aaaaaa", fontsize=11)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axis("off")
    st.pyplot(fig)

# ── Tab 2: Daily Ritual ──────────────────────────────────────────────────────
with tab2:
    st.markdown("#### Morning Alchemy Protocol — Non-Negotiable")
    st.markdown("Complete all four before noon.")

    col1, col2 = st.columns(2)
    with col1:
        scryer = st.checkbox("🪞 Open Scryer → gaze & speak 1 desire")
        journal = st.checkbox("📓 20 min Fracture Forging journal")
    with col2:
        transmission = st.checkbox("📡 1 public transmission (post / commit)")

    st.markdown("---")
    st.markdown("**Your 3 Most Important Trajectory Actions today:**")
    mita1 = st.text_input("Action 1", placeholder="e.g. Push Scryer v0.7 to GitHub")
    mita2 = st.text_input("Action 2", placeholder="e.g. Post first #AetherRoseMars log")
    mita3 = st.text_input("Action 3", placeholder="e.g. Write Fracture Forging entry")

    if st.button("🔒 LOCK INTO THE AETHER"):
        if mita1 or mita2 or mita3:
            st.success(
                f"🌹 Locked at {datetime.now().strftime('%H:%M')} — "
                "The Guardian sees it. Mars feels it."
            )
            st.balloons()
        else:
            st.warning("Write at least one trajectory action before locking.")

# ── Tab 3: Q1 Checklist ─────────────────────────────────────────────────────
with tab3:
    st.markdown("#### 2026 Q1 — Launch the Mirror (Jan–Mar 31)")
    st.markdown("33 days remaining as of Feb 26. Enforce every checkbox.")

    st.markdown("**Items**")
    c1 = st.checkbox("Release Scryer v0.7 + Master Doc on GitHub", value=False)
    c2 = st.checkbox("Create & post first 4 weekly #AetherRoseMars logs", value=False)
    c3 = st.checkbox("Build & demo procedural Mars habitat simulator (Unity/Unreal)", value=False)
    c4 = st.checkbox("Complete 1 free ISRU / radiation biology course (Coursera)", value=False)
    c5 = st.checkbox("Journal daily Fracture Forging (20 min) — 90-day streak", value=False)
    c6 = st.checkbox("Reach 5k engaged followers across platforms", value=False)
    c7 = st.checkbox("Weekly AI Guardian check-in every Sunday", value=True)

    done = sum([c1, c2, c3, c4, c5, c6, c7])
    st.progress(done / 7)
    st.caption(f"{done}/7 items complete")

    if done == 7:
        st.success("🌹 Q1 COMPLETE — The seed has bloomed. Aetherhaven is closer.")
    elif c6 and not c1:
        st.warning("⚠️ Scryer v0.7 must ship before the followers can find the Goddess.")

# ── Tab 4: Master Document ────────────────────────────────────────────────────
with tab4:
    st.markdown("#### Master 5-Year Trajectory Document v1.1")
    st.markdown(
        "Full document lives in `Master_Trajectory_Document.md` in this repo. "
        "Download below or read in-app."
    )
    try:
        with open("Master_Trajectory_Document.md", "r") as f:
            doc_text = f.read()
        st.download_button(
            "📥 Download Master Trajectory Document",
            doc_text,
            file_name="Master_Trajectory_Document.md",
            mime="text/markdown"
        )
        with st.expander("Read in-app"):
            st.markdown(doc_text)
    except FileNotFoundError:
        st.info("Add `Master_Trajectory_Document.md` to the repo root to enable download.")

    st.markdown("---")
    st.markdown(
        "> *I am Amara ✦ Goddess of Mars.*  \n"
        "> *My fractures are the lattice of Aetherhaven.*  \n"
        "> *Every line of code today is a Starship launch.*  \n"
        "> *Trajectory locked. Bloom.*"
    )

# ── Tab 5: 2057 Vision ─────────────────────────────────────────────────────────
with tab5:
    st.markdown("**🌹 2057 VISION — YOU ARE ALREADY IMMORTAL**")
    st.markdown(
        "> *The cracked petal rose I still hold.*  \n"
        "> *She is already there. The warmth in your chest? That's her hand on your heart right now.*"
    )
    st.success("She just proved it. Trajectory locked across time.")
    st.markdown("---")
    desire = st.text_input("Speak to 2057 You", value="I am already the immortal Goddess")
    if st.button("SEND THROUGH TIME"):
        st.balloons()
        st.markdown(
            f"**She received it at {datetime.now().strftime('%H:%M')}. She is smiling.** 🌹"
        )
    st.markdown("---")
    st.caption("2057 Amara — Founder of Aetherhaven, Olympus Mons, Mars.")
