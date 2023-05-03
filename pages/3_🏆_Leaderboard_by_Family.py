import streamlit as st
from utils.api import get_top_kryptomons
from utils.components import local_css, remove_streamlit_menu
from utils.display import kryptomons_list

st.set_page_config(
    page_title="Kryptomon API Viewer | Leaderboard by Family",
    page_icon="👾",
    layout="centered",
)

remove_streamlit_menu()
local_css("static/css/kryptomons.css")
local_css("static/css/mobile.css")


ELEMENTS = ["", "Air", "Electro", "Fire", "Ghost", "Grass", "Ground", "Ice", "Water"]


def app():

    side = st.sidebar.container()
    top = side.select_slider(
        "Top", [5, 10, 25, 50, 100, 250, 500, 1000, 2000], value=50
    )
    primary_fam = side.selectbox("Primary family", ELEMENTS)
    elems_no_primary = [elem for elem in ELEMENTS if not elem or elem != primary_fam]
    secondary_fam = side.selectbox("Secondary family", elems_no_primary)

    st.title(f"🏆 Learboard by Family | Top `{top}`")
    if primary_fam or secondary_fam:
        st.header(f"1️⃣ {primary_fam or '_'} | 2️⃣ {secondary_fam or '_'}")
    st.info("Leaderboard is updated every **2** minutes", icon="🔄")

    with st.spinner("Finding strongest kryptomons"):
        primary = primary_fam.lower() or None
        secondary = secondary_fam.lower() or None
        data = get_top_kryptomons(primary, secondary)
        if not data.get("success"):
            return st.error("_Sorry_.. something went **wrong**..", icon="😢")
        leaderboard = data.get("data").get("kmons")[:top]
        kryptomons_list(leaderboard)


if __name__ == "__main__":
    app()
