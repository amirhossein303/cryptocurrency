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


# Instalation
## Clone the sourse
At the first you have to clone the project.
```
$ git clone https://github.com/amirhosseinzibaei/cryptocurrency.git
```

## Install dependecies
For using this project locally! you should first install dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements/development.txt
```
> NOTE: if you haven't the pip already! follow this instruction: https://pip.pypa.io/en/stable/installation/
>
> Also you need the `redis`. install it if don't have by using [this](https://redis.io/docs/getting-started/installation/install-redis-on-linux/) instruction

For checking is the dependencies has been installed
```
$ pip freeze
```
This will get you the list of available dependencies

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
```
- `API_KEY_COIN_MARKET_CAP` is your api_key of coinmarketcap api.
for getting your first api_key go to [this](https://pro.coinmarketcap.com/signup/) page
- `SECRET_KEY` is the *django secret key*. you can also generate it from https://djecrety.ir/
- The `Endpoints` configs should not be change.

## Running the Celery stuff
Ok! now we must run the celery **worker** and celery **beat**

In your terminal do following things
```
(venv) $ celery -A config worker --loglevel INFO
```

And in another terminal do following things
```
(venv) $ celery -A config beat --loglevel INFO
```

> Note. you should run these two in separate terminals
>
> Also you can run these two in one terminal (Not Recommended)

Run celery **beat** and **worker** in one terminal
```
(venv) $ celery -A config worker --beat --loglevel=info
```

### Issue
Are you getting the following error?
```
Unable to load celery application.
The module config was not found.
```

You must change your current directory to the `cryptocurrency_project`
```
$ pwd
/home/<username>/cryptocurrency/
$ cd /home/<username>/cryptocurrency/cryptocurrency_project/
```

Then run the above commands all again :)
> It did'nt work too.
>
> You can submit an issue right [HERE](https://github.com/amirhosseinzibaei/cryptocurrency/issues) 


## Running the Django
It's almost done. just running the server locally by following commands:
```
(venv) $ python3 manage.py runserver
```

Then open your browser and open (http://127.0.0.1:8000/)

# Thanks
It's my pleasure to know your opinion about this simple project

Also it's an `Open Source` project.<br>
if you have any good idea you can submit your **Pull Request**.<br>
after checking your **Pull request** This will be **Merged** or **Closed**