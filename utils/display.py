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


def display_kryptomon(kryptomon, image, stats, component=st):
    primary_fam = kryptomon.get("primary-family")
    secondary_fam = kryptomon.get("secondary-family")
    primary = ELEMENTS.get(primary_fam, primary_fam)
    secondary = ELEMENTS.get(secondary_fam, secondary_fam)
    rank = kryptomon.get("battle-rank")
    return f"""
    <div class='kryptomon'>
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
        </div>
        <div class='rank'>
            <p>{rank.get('rank')}</p>
            <p>{rank.get('points')}</p>
        </div>
    </div>"""


def kryptomons_list(kryptomons, component=st):
    kmon_ids = [kmon.get("kryptomon-id") for kmon in kryptomons]
    images = get_kryptomon_images(kmon_ids)
    levels = get_kryptomon_game_stats(kmon_ids)
    html_list = "".join(
        display_kryptomon(kmon, image, stat)
        for kmon, image, stat in zip(kryptomons, images, levels)
    )
    div(component, _class="kryptomon-list", text=html_list)
