
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random, math

st.title("Parameter Practice")
st.write("This is Kim Seyeon's Week 3 generative art project.")

plt.figure(figsize=(6,8))
plt.axis('off')
plt.gca().set_facecolor((0.98,0.98,0.97))
for i in range(6):
    cx, cy = random.random(), random.random()
    r = random.uniform(0.15,0.45)
    angles = np.linspace(0,2*np.pi,200)
    x = cx + r*np.cos(angles); y = cy + r*np.sin(angles)
    plt.fill(x,y,alpha=0.5,color=(random.random(),random.random(),random.random()))

st.pyplot(plt.gcf())
