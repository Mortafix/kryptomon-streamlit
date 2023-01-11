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
    left_col, right_col = st.columns(2)
    left_col.subheader("🏅 Ranks")
    left_col.write("* 💼 → 🏅 [Ranks by Wallet](/Ranks_by_Wallet)")
    right_col.subheader("🏅 Leaderboards")
    right_col.write("* 🏅 [Leaderboard](/Leaderboard)")
    right_col.write("* 🔥 → 🏅 [Leaderboard_by_Family](/Leaderboard_by_Family)")


if __name__ == "__main__":
    app()
