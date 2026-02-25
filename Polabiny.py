import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.image as mpimg

st.set_page_config(layout="wide")

st.title("Pardubice – Polabiny dle barev")
st.subheader("GPS souřadnice na osách")

# Cesta k obrázku
img_path = "graf_Pardubice_Polabiny.png"


# Načtení obrázku
img = mpimg.imread(img_path)

# Barvy a popisky legendy
colors = ["yellow", "red", "green", "blue", "pink"]
labels = ["Polabiny I.", "Polabiny II.", "Polabiny III.", "Polabiny IV.", "Polabiny V."]

# Vytvoření figure
fig, ax = plt.subplots(figsize=(10, 10))

# Zobrazení obrázku
ax.imshow(img)
ax.axis("off")

# Titulek
# plt.title("PARDUBICE", fontsize=20, pad=20)

# Legenda
# legend_elements = [
#    Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
#           markersize=12, label=label)
#    for color, label in zip(colors, labels)
#] 
# ax.legend(handles=legend_elements, loc='lower right', fontsize=12)

# Uložení ve vysokém rozlišení
output_path = "pardubice_map_highres.png"
fig.savefig(output_path, dpi=600, bbox_inches='tight')

# Zobrazení ve Streamlit
st.pyplot(fig)
