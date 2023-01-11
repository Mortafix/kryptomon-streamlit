from utils.api import get_kryptomon_game_stats, get_kryptomon_images


def display_kryptomon(kryptomons):
    kmon_ids = [kmon.get("kryptomon-id") for kmon in kryptomons]
    images = get_kryptomon_images(kmon_ids)
    levels = get_kryptomon_game_stats(kmon_ids)
    # TODO: list of kryptomons
