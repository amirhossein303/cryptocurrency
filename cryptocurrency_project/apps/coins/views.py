from django.views.generic.base import TemplateView
from decouple import config

from apps.coinmarketcap.api import CoinMarketCap



class CoinListView(TemplateView):
    template_name = 'coins/coins_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        API_KEY = config('API_KEY_COIN_MARKET_CAP')
        coin_market_cap = CoinMarketCap(API_KEY)
        context['coins_list'] = coin_market_cap.get_active_coins()
        
        return context