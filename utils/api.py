from concurrent.futures import ThreadPoolExecutor
from os import getenv

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
]

# ---- Main


def api_call(endpoint, method=get, payload=None, **params):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{API_URL}{endpoint}"
    return method(url, headers=headers, params=params, json=payload).json()


# ---- Funcs


def get_dashboard_wallet(wallet):
    return api_call(f"/user/{wallet}")


def get_kryptomon_images(kmon_ids):
    urls = [f"/kryptomons/images/{kmon_id}" for kmon_id in kmon_ids]
    with ThreadPoolExecutor(max_workers=3) as pool:
        res = pool.map(api_call, urls)
    return {
        kmon_id: (im.get("junior") or im.get("baby") or im.get("egg")).get("png-image")
        for kmon_id, result in zip(kmon_ids, res)
        if (im := result.get("data"))
    }


def get_kryptomon_game_stats(kmon_ids):
    urls = [f"/kryptomons/game/stats/{kmon_id}" for kmon_id in kmon_ids]
    with ThreadPoolExecutor(max_workers=3) as pool:
        res = pool.map(api_call, urls)
    return [kmon.get("data") for kmon in res]


def get_kryptomon_ranks(kmon_ids):
    body = {
        "filters": {"kryptomon-id": kmon_ids},
        "attributes": BASE_ATTRIBUTES,
        "sort": {"battle-rank": "desc"},
    }
    return api_call("/kryptomons/v2", method=post, payload=body)
