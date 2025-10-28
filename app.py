
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random, math

st.title("🌀 Week 3 – Parameter Practice (Seed Version)")
st.caption("Kim Seyeon | Arts & Advanced Big Data")

# ---- Functions ----
def random_palette(k=5, style="random"):
    if style == "Pastel":
        base_colors = [(1.0,0.8,0.8),(1.0,0.9,0.7),(0.8,1.0,0.8),(0.7,0.9,1.0),(0.9,0.8,1.0)]
    elif style == "Vivid":
        base_colors = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1)]
    elif style == "Monochrome":
        base_colors = [(0.2,0.4,1.0),(0.3,0.5,1.0),(0.4,0.6,1.0),(0.5,0.7,1.0),(0.6,0.8,1.0)]
    else:
        base_colors = [(random.random(), random.random(), random.random()) for _ in range(k)]
    return random.choices(base_colors, k=k)

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2*math.pi, points)
    radii  = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# ---- Sidebar Controls ----
version = st.sidebar.selectbox("Select Version", [
    "Task 1", "Task 2 (ver1)", "Task 2 (ver2)",
    "Task 3 Pastel", "Task 3 Vivid", "Task 3 Monochrome"
])
seed_value = st.sidebar.slider("🎲 Random Seed", 0, 9999, 0)

# ---- Set Seed ----
random.seed(seed_value)
np.random.seed(seed_value)

# ---- Poster Setup ----
plt.figure(figsize=(7,10))
plt.axis("off")
plt.gca().set_facecolor((0.98,0.98,0.97))

# ---- Logic ----
if version == "Task 1":
    n_layers = 8; wobble_min, wobble_max = 0.05, 0.25; r_min, r_max = 0.15, 0.45; style="random"
elif version == "Task 2 (ver1)":
    n_layers = 3; wobble_min, wobble_max = 0.01, 0.05; r_min, r_max = 0.15, 0.45; style="random"
elif version == "Task 2 (ver2)":
    n_layers = 20; wobble_min, wobble_max = 0.2, 0.5; r_min, r_max = 0.25, 0.6; style="random"
elif version == "Task 3 Pastel":
    n_layers = 8; wobble_min, wobble_max = 0.05, 0.25; r_min, r_max = 0.15, 0.45; style="Pastel"
elif version == "Task 3 Vivid":
    n_layers = 8; wobble_min, wobble_max = 0.05, 0.25; r_min, r_max = 0.15, 0.45; style="Vivid"
else:
    n_layers = 8; wobble_min, wobble_max = 0.05, 0.25; r_min, r_max = 0.15, 0.45; style="Monochrome"

palette = random_palette(6, style=style)

for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(r_min, r_max)
    x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(wobble_min, wobble_max))
    color = random.choice(palette)
    alpha = random.uniform(0.25, 0.6)
    plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=plt.gca().transAxes)
plt.text(0.05, 0.91, f"{version} | Seed: {seed_value}", fontsize=11, transform=plt.gca().transAxes)
plt.xlim(0,1); plt.ylim(0,1)
st.pyplot(plt.gcf())
