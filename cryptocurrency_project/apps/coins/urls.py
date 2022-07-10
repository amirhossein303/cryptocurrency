from django.urls import path

from .views import CoinListView


urlpatterns = [
    path('', CoinListView.as_view(), name='coins_list'),
]