import logging
from binance.spot import Spot
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Spot()
logging.info(client.time())

client = Spot(api_key='iuorPYwKpkvyYvy1qzVw5TUVCSVFt76HU4RxtYfdNpzXpTSIb8GxwP1ZB6LEZAu7', api_secret='I3YhtFyv3g9lwZ5pMhgngPeIwkEdR4n6itWSUIfjsTv3Uq7hzz7ISgfZcndIK0zw')

# Get account information
# logging.info(client.account())

# withdraw to base chain
params = {
    'coin': 'ETH',
    'address': '0x49528C0472906AED6C7AFC458b08B23B79fcdf06',
    'network': 'base',
    'amount': '0.005',
    'walletType': 0
}

response = client.withdraw(**params)
logging.info(response)