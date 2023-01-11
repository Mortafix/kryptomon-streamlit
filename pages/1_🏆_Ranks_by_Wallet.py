import streamlit as st
from utils.api import get_dashboard_wallet, get_kryptomon_ranks
from utils.display import display_kryptomon


def app():
    st.title("💼 → 🏆 | Ranks by Wallet")
    wallet = st.text_input("Wallet", placeholder="Wallet to search", max_chars=42)

    if wallet:
        dashboard = get_dashboard_wallet(wallet)
        if not dashboard.get("success"):
            return st.error("**Wallet** not found!", icon="🫣")
        data = dashboard.get("data")
        kryptomons = data.get("kryptomons").get("in-wallet")
        if kryptomons.get("quantity") <= 0:
            return st.warning("No **kryptomons** found in this wallet", icon="😵‍💫")
        kmon_ids = kryptomons.get("ids")
        with st.spinner("Searching"):
            kryptomon_ranks = get_kryptomon_ranks(kmon_ids)
        if not kryptomon_ranks.get("success"):
            return st.error("_Sorry_.. something went **wrong**..", icon="😢")
        display_kryptomon(kryptomon_ranks.get("data").get("kmons"))
        # tmp
        st.json(kryptomon_ranks.get("data").get("kmons"))


if __name__ == "__main__":
    app()
