import logging
from typing import Dict
from django.core.cache import cache
from decouple import config 

from apps.coinmarketcap.api import CoinMarketCap
from apps.core.helpers import update_coin_data
from .celery import app


logger = logging.Logger(__name__)


@app.task(name='update-cryptocurrencies-data')
def update_cryptocurrencies_data() -> None:
    """Update the cryptocurrencies data
    and keep updated data in the cache"""

    # 1. requests to get data
    API_KEY = config('API_KEY_COIN_MARKET_CAP')
    coin_market_cap = CoinMarketCap(API_KEY)
    
    active_coins = coin_market_cap.get_active_coins()
    if not active_coins:
        return None
    active_coins = active_coins['data']
    
    # 2. detect updated coins and update the cache
    updated_coins = [
        update_coin_data(coin_data) for coin_data in active_coins
        if CoinMarketCap.is_updated_coin(coin_data, cache.get(coin_data['symbol']))
    ]

    # 3. send result to websocket channel
    return None