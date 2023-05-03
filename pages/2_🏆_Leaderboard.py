import streamlit as st
from utils.api import get_top_kryptomons
from utils.components import local_css, remove_streamlit_menu
from utils.display import kryptomons_list

st.set_page_config(
    page_title="Kryptomon API Viewer | Leaderboard",
    page_icon="👾",
    layout="centered",
)

remove_streamlit_menu()
local_css("static/css/kryptomons.css")
local_css("static/css/mobile.css")


def app():

    side = st.sidebar.container()
    top = side.select_slider(
        "Top", [5, 10, 25, 50, 100, 250, 500, 1000, 2000], value=50
    )

    st.title(f"🏆 Learboard | Top `{top}`")
    st.info("Leaderboard is updated every **2** minutes", icon="🔄")

    with st.spinner("Finding strongest kryptomons"):
        data = get_top_kryptomons()
        if not data.get("success"):
            return st.error("_Sorry_.. something went **wrong**..", icon="😢")
        leaderboard = data.get("data").get("kmons")[:top]
        kryptomons_list(leaderboard)


if __name__ == "__main__":
    app()
