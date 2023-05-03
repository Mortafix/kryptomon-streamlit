from os import getenv

import streamlit as st
from dotenv import load_dotenv
from requests import get, post

load_dotenv(".env")
API_URL = getenv("API_URL")
API_KEY = getenv("API_KEY")
BASE_ATTRIBUTES = [
    "kryptomon-id",
    "primary-family",
    "secondary-family",
    "generation",
    "battle-rank",
    "speciality",
]
LITTLE_DELAY = 60 * 2  # 2 minutes
BIG_DELAY = 60 * 60 * 1  # 1 hour

# ---- Main


def api_call(endpoint, method=get, payload=None, **params):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{API_URL}{endpoint}"
    return method(url, headers=headers, params=params, json=payload).json()


# ---- Base


@st.cache(ttl=BIG_DELAY, show_spinner=False)
def get_kryptomon_images(kmon_id):
    images = api_call(f"/kryptomons/images/{kmon_id}").get("data")
    image = images.get("junior") or images.get("baby") or images.get("egg")
    return image.get("png-image")


@st.cache(ttl=LITTLE_DELAY, show_spinner=False)
def get_kryptomon_game_stats(kmon_id):
    return api_call(f"/kryptomons/game/stats/{kmon_id}").get("data")


# ---- Funcs


@st.cache(ttl=LITTLE_DELAY, show_spinner=False)
def get_dashboard_wallet(wallet):
    return api_call(f"/user/{wallet}")


def get_kryptomon_ranks(kmon_ids):
    body = {
        "filters": {"kryptomon-id": kmon_ids},
        "attributes": BASE_ATTRIBUTES,
        "sort": {"battle-rank": "desc"},
    }
    return api_call("/kryptomons/v2", method=post, payload=body)


@st.cache(ttl=LITTLE_DELAY, show_spinner=False)
def get_top_kryptomons(primary_elem=None, secondary_elem=None):
    filters = dict()
    if primary_elem:
        filters |= {"primary-family": [primary_elem]}
    if secondary_elem:
        filters |= {"secondary-family": [secondary_elem]}
    body = {
        "filters": filters,
        "attributes": BASE_ATTRIBUTES,
        "sort": {"battle-rank": "desc"},
    }
    return api_call("/kryptomons/v2", method=post, payload=body)
