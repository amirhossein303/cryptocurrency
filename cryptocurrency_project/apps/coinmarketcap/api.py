from enum import Enum
from http.client import OK
import logging
from typing import Dict, Optional, Tuple

import requests
from decouple import config


logger = logging.Logger(__name__)

# Confs
URL_ACTIVE_COINS = config('URL_ACTIVE_COINS')
URL_KEY_INFO = config('URL_KEY_INFO')

# Types
_ENDPOINT = str


class Method(Enum):
    POST = 'post'
    GET = 'get'
    PUT = 'put'
    DELETE = 'delete'
    PATCH = 'patch'
    HEAD = 'head'
    OPTIONS = 'options'


class CoinMarketCap:
    """CoinMarketCap class provides the api of the coinmarketcap market
    
    You can interactive with coinmarketcap api by using this class as simple as possible"""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
    
    def __str__(self) -> str:
        return f'<{self.__class__.__name__} {self.api_key}>'
    
    def __requests(
        self,
        endpoint: _ENDPOINT,
        method: Method,
        excepted_status_code: int,
        params: Dict = {},
        headers: Dict = {},
        ) -> Tuple[Optional[requests.Response], Optional[Dict]]:
        """Provide specific request for the api"""

        # combine headers
        final_headers = headers | self.headers

        try:
            req = requests.request(
                method,
                endpoint,
                params=params,
                headers=final_headers,
            )
        
            json_data = req.json()
            
            if req.status_code == excepted_status_code:
                # it's correct
                logger.info(f'The request for api {endpoint} is successfully done.')
                return req, json_data
        
            # it's not correct as we except
            logger.error(f'Something went wrong while requesting to :{endpoint}.')
            logger.error(f'Response :{json_data}')
            return req, json_data
            
        except Exception as exc_info:
            logger.exception(exc_info)
            return None, None
    
    def is_authenticated(self) -> bool:
        """Check the API_KEY is valid or not"""
        response, _ = self.__requests(
            endpoint=URL_KEY_INFO,
            method=Method.GET.value,
            excepted_status_code=200
        )
        return True if response and response.status_code == OK else False
    
    def get_active_coins(
        self,
        params: Dict = {},
        headers : Dict = {}
        ) -> Optional[Dict]:
        """More information on this url

        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
        """
        response, data = self.__requests(
            endpoint=URL_ACTIVE_COINS,
            method=Method.GET.value,
            excepted_status_code=200,
            params=params,
            headers=headers
        )
        return data
    
    @staticmethod
    def is_updated_coin(coin: Dict, cached_coin: Dict) -> bool:
        """Check the coin is updated or not"""
        if not cached_coin:
            return True
        if coin['quote']['USD']['price'] != cached_coin['quote']['USD']['price']:
            logger.info(f'Coin {coin["symbol"]} has been updated.')
            return True
        return False