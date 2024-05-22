from re import search

import streamlit as st
from utils.api import get_kryptomon_game_stats, get_kryptomon_images
from utils.components import div

ELEMENTS = {
    "fire": "fire-element",
    "air": "wind",
    "ice": "cooling",
    "ground": "rock",
    "electro": "lightning-bolt",
}


def display_kryptomon(kryptomon, image, stats, component=st, i=None):
    primary_fam = kryptomon.get("primary-family")
    secondary_fam = kryptomon.get("secondary-family")
    primary = ELEMENTS.get(primary_fam, primary_fam)
    secondary = ELEMENTS.get(secondary_fam, secondary_fam)
    battle_rank = kryptomon.get("battle-rank")
    rank, rank_points = search(r"(.+)\s\((\d+\.\d+)\)", battle_rank).groups()
    stats = stats.get("levels")
    if stats:
        stats.pop("constitution", None)
    level = stats and round(sum(stats.values()) / len(stats)) or 0
    return f"""
        <div class='position'>{i if i is not None else ''}</div>
        <div class='image'><img src='{image}'></div>
        <div class='info'>
            <p>
                Kryptomon {kryptomon.get('kryptomon-id')}
                <span>(Gen {kryptomon.get('generation')})</span>
            </p>
            <p>
                <img src="https://img.icons8.com/stickers/100/null/{primary}.png"/>
                <img src="https://img.icons8.com/stickers/100/null/{secondary}.png"/>
            </p>
            <p>Level <span>{level}</span></p>
        </div>
        <div class='rank'>
            <p>{rank}</p>
            <p>{round(float(rank_points))}</p>
        </div>"""


def kryptomons_list(kryptomons, component=st):
    for i, kmon in enumerate(kryptomons, 1):
        kmon_id = kmon.get("kryptomon-id")
        image = get_kryptomon_images(kmon_id)
        in_game_stats = get_kryptomon_game_stats(kmon_id)
        html_kmon = display_kryptomon(kmon, image, in_game_stats, i=i)
        div(component, _class="kryptomon", text=html_kmon)
