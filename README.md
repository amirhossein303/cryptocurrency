# Cryptocurrency
This program provides you with the real-time price of cryptocurrencies.

# Versions
- Version [v0.0.1](https://github.com/amirhosseinzibaei/cryptocurrency/tree/v0.0.1) is the first version that is not using the docker and some new feature. 
- Version [v0.1.0](https://github.com/amirhosseinzibaei/cryptocurrency/tree/v0.1.0) is the dockerized version. 

# Technologies
For this project we have used following technologies:
- **Python**[3.9.x] : [see here](https://www.python.org/)
- **Django**[4.x] : The Web framework. [see here](https://www.djangoproject.com/)
- **Gunicorn**: The `WSGI` server . [see here](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/)
- **Daphne**: The `ASGI` server. [see here](https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/daphne/)
- **Nginx**: The webserver as a proxy. [see here](https://www.nginx.com/)
- **Docker**: The container to use project easily. [see documentation of docker](https://docs.docker.com)
- **Docker-compose**: To collect all the services in one network. [see here](https://docs.docker.com/compose/)
- **Celery** : for controling background tasks. [see here](https://docs.celeryq.dev/en/stable/)
- **Channels** : for creating websocket and sending data as real-time purpose. see [Documentation](https://channels.readthedocs.io/en/stable/)
- **RabbitMq** : for **Broker** celery. more information [see here](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html)
- **Redis** : for [Django Caching](https://docs.djangoproject.com/en/4.0/topics/cache/#redis) & [Celery's Backend](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html) & [channels-layer](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
- **CoinMarketCap API** : the main api for interactive with cryptocurrencies data.  [Documentation](https://coinmarketcap.com/api/documentation/v1/)
- **Bootstrap4** : for the front-end part. [Documentation](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## Sample overview of project
![](https://github.com/amirhosseinzibaei/cryptocurrency/blob/main/docs/project_overview.gif)


# Installation
For Installation follow one the above version instructions.

# Thanks
It's my pleasure to know your opinion about this simple project

Also it's an `Open Source` project.<br>
if you have any good idea you can submit your **Pull Request**.<br>
after checking your **Pull request** This will be **Merged** or **Closed**
