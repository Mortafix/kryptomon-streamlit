import streamlit as st
from utils.api import get_dashboard_wallet, get_kryptomon_ranks
from utils.components import local_css, remove_streamlit_menu
from utils.display import kryptomons_list

remove_streamlit_menu()
local_css("static/css/kryptomons.css")
local_css("static/css/mobile.css")


def app():
    st.title("💼 → 🏆 | Ranks by Wallet")
    wallet = st.text_input("Wallet", placeholder="Wallet to search", max_chars=42)

    if not wallet:
        return

    with st.spinner("Searching"):
        dashboard = get_dashboard_wallet(wallet)
        if not dashboard.get("success"):
            return st.error("**Wallet** not found!", icon="🫣")
        data = dashboard.get("data")
        kryptomons = data.get("kryptomons").get("in-wallet")
        if kryptomons.get("quantity") <= 0:
            return st.warning("No **kryptomons** found in this wallet", icon="😵‍💫")
        kmon_ids = kryptomons.get("ids")
        kryptomon_ranks = get_kryptomon_ranks(kmon_ids)
        if not kryptomon_ranks.get("success"):
            return st.error("_Sorry_.. something went **wrong**..", icon="😢")
        kryptomons_list(kryptomon_ranks.get("data").get("kmons"))


if __name__ == "__main__":
    app()
