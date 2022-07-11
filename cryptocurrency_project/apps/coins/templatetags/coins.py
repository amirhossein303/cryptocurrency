from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def load_icon_coin(coin_name: str) -> str:
    """Load the icon for the given coin"""
    return static(settings.ICONS_COINS_PATH.format(coin_name=coin_name.lower()))