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
    rank = kryptomon.get("battle-rank")
    stats = stats.get("levels")
    level = stats and round(sum(stats.values()) / len(stats)) or 0
    return f"""
    <div class='kryptomon'>
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
            <p>{rank.get('rank')}</p>
            <p>{round(rank.get('points'))}</p>
        </div>
    </div>"""


def kryptomons_list(kryptomons, component=st):
    kmon_ids = [kmon.get("kryptomon-id") for kmon in kryptomons]
    images = get_kryptomon_images(kmon_ids)
    levels = get_kryptomon_game_stats(kmon_ids)
    html_list = "".join(
        display_kryptomon(kmon, image, stat, i=i)
        for i, (kmon, image, stat) in enumerate(zip(kryptomons, images, levels), 1)
    )
    div(component, _class="kryptomon-list", text=html_list)
