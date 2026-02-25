import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

st.set_page_config(layout="wide")

st.title("Pardubice – Polabiny dle barev")
st.subheader("GPS souřadnice na osách")

# Načtení dat
@st.cache_data
def load_data():
    Pard1 = gpd.read_file("717657", layer="BUDOVY_P").to_crs(epsg=4326)
    Pard2 = gpd.read_file("717657", layer="DALSI_PRVKY_MAPY_L").to_crs(epsg=4326)
    Pard3 = gpd.read_file("717657", layer="VB_P").to_crs(epsg=4326)
    osm_data = [
        gpd.read_file(f"Polygon_Polabiny{i}.geojson").to_crs(epsg=4326)
        for i in range(1, 6)
    ]
    return Pard1, Pard2, Pard3, osm_data

Pard1, Pard2, Pard3, osm_data = load_data()

# Vykreslení mapy
fig, ax = plt.subplots(figsize=(8, 8))
Pard1.plot(ax=ax, color="#BCB8B1", edgecolor="black", zorder=1)
Pard2.plot(ax=ax, color="#BCB8B1", edgecolor="grey", zorder=2)
Pard3.plot(ax=ax, color="#BCB8B1", edgecolor="brown", linewidth=0.3, zorder=3)

colors = ["yellow", "red", "green", "blue", "pink"]
labels = ["Polabiny I.", "Polabiny II.", "Polabiny III.", "Polabiny IV.", "Polabiny V."]

for data, color in zip(osm_data, colors):
    data.plot(ax=ax, color=color, edgecolor=color, linewidth=1.0)

ax.set_aspect('equal')
ax.set_title("PARDUBICE", fontsize=16, loc='center', pad=20)

# Legenda
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label)
    for color, label in zip(colors, labels)
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)
# Uložení v maximálním rozlišení 
output_path = "pardubice_map_highres.png" 
fig.savefig(output_path, dpi=600, bbox_inches='tight')

# Zobrazení v Streamlitu
st.pyplot(fig)
