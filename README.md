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


# Instalation
## Clone the sourse
At the first you have to clone the project.
```
$ git clone https://github.com/amirhosseinzibaei/cryptocurrency.git
```

## Making environment variable
Create **.env** file in the root directory and copy the following content
```
# Coin market cap configs
API_KEY_COIN_MARKET_CAP = '<your-api-key>'

## Endpoints
URL_ACTIVE_COINS = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
URL_KEY_INFO = 'https://pro-api.coinmarketcap.com/v1/key/info'

# Celery confs
CELERY_MAIN_NAME = 'cryptocurrency'

# Django
SECRET_KEY = '<your-secret-key>'
DEBUG = 1
ALLOWED_HOSTS = '*'
```
- `API_KEY_COIN_MARKET_CAP` is your api_key of coinmarketcap api.
for getting your first api_key go to [this](https://pro.coinmarketcap.com/signup/) page
- `SECRET_KEY` is the *django secret key*. you can also generate it from https://djecrety.ir/
- The `Endpoints` configs should not be change.
- `DEBUG` and `ALLOWED_HOSTS` is the configuration of your django project


## Running the app
Now just by run the containers in a network `docker-compose` you can run the project.
```
$ docker-compose up --build -d
```
This will run in the background with the `-d` flag<br>
you can also remove the `-d` flag to run in the foreground to see what happening.

OR

```
$ docker-compose logs -f
```
Ok it's time to open your browser and go to this url: http://0.0.0.0:8080/

# Thanks
It's my pleasure to know your opinion about this simple project

Also it's an `Open Source` project.<br>
if you have any good idea you can submit your **Pull Request**.<br>
after checking your **Pull request** This will be **Merged** or **Closed**