# Cryptocurrency
This program provides you with the real-time price of cryptocurrencies and is a simple exchange that allows prices to be converted into each other.

# Technologies
For this project we have used following technologies:
- Django[4.x] : The Web framework. [see here](https://www.djangoproject.com/)
- Python[3.9.x] : [see here](https://www.python.org/)
- Celery : for controling background tasks. [see here](https://docs.celeryq.dev/en/stable/)
- RabbitMq : for **Broker** celery. more information [see here](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html)
- Redis : for [Django Caching](https://docs.djangoproject.com/en/4.0/topics/cache/#redis) & [Celery's Backend](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html) & [channels-layer](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
- CoinMarketCap API : the main api for interactive with cryptocurrencies data.  [Documentation](https://coinmarketcap.com/api/documentation/v1/)
- Channels : for creating websocket and sending data as real-time purpose. see [Documentation](https://channels.readthedocs.io/en/stable/)
- Bootstrap4 : for the front-end part. [Documentation](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## Sample overview of project
![](https://github.com/amirhosseinzibaei/cryptocurrency/blob/main/docs/project_overview.gif)
