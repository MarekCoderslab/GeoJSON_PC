import streamlit as st

st.set_page_config(layout="wide")

st.title("Pardubice – Polabiny dle barev")
st.subheader("GPS souřadnice na osách")

# Cesta k obrázku
img_path = "graf_Pardubice_Polabiny.png"

# Zobrazení obrázku
st.image(img_path, use_column_width=True)

# Barvy a popisky legendy
colors = ["yellow", "red", "green", "blue", "pink"]
labels = ["Polabiny I.", "Polabiny II.", "Polabiny III.", "Polabiny IV.", "Polabiny V."]

st.markdown("### Legenda")

# Vytvoření legendy pomocí Streamlit columns
cols = st.columns(len(colors))

for col, color, label in zip(cols, colors, labels):
    col.markdown(
        f"""
        <div style="display:flex; align-items:center;">
            <div style="width:20px; height:20px; background:{color}; border:1px solid #000; margin-right:8px;"></div>
            <span>{label}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<div style='text-align:center; margin-top: 30px;'>"
    "<a href='mailto:marek.coderslab@gmail.com'>Created: marek.coderslab@gmail.com</a>"
    "</div>",
    unsafe_allow_html=True
)
