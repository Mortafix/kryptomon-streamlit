import streamlit as st
from utils.components import remove_streamlit_menu

st.set_page_config(
    page_title="Kryptomon API Viewer",
    page_icon="👾",
    layout="centered",
)

remove_streamlit_menu()


def app():
    st.title("Kryptomon API Viewer")
    st.subheader("🏅 Ranks")
    st.write("* 💼 → 🏅 [Ranks by Wallet](/Ranks_by_Wallet)")


if __name__ == "__main__":
    app()
