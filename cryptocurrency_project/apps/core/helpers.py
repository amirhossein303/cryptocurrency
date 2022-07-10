from typing import Dict

from django.core.cache import cache


def update_coin_data(coin_data: Dict) -> Dict:
    """Update the coin and return coin's data"""
    cache.set(coin_data['symbol'], coin_data)
    return coin_data