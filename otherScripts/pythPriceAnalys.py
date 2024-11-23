"""
比较pyth rest接口，pyth http长链接和assetIndex wss获取的价格是否一致

"""
from config import *
import requests
import csv
import asyncio
import aiohttp
import websockets
import json
from datetime import datetime, timezone

# 定义CSV文件名
CSV_FILENAME = 'pyth_prices_tset.csv'

'''prod url'''
# REST_URL = 'https://hermes.pyth.network/v2/updates/price/latest?ids[]=0x84c2dde9633d93d1bcad84e7dc41c9d56578b7ec52fabedc1f335d673df0a7c1'
PYTH_HISTORY_URL = 'https://hermes.pyth.network/v2/updates/price'
# PYTH_HISTORY_URL = 'https://hermes-mainnet.rpc.extrnode.com/adf6e2da-430f-4f7f-b7c3-8f4e2123a319/v2/updates/price'
FEED_MAP = {PYTH_BTCUSD: "BTC", PYTH_ETHUSD: "ETH", PYTH_BNBUSD: "BNB", PYTH_ARBUSD: "ARB", PYTH_CAKEUSD: "CAKE", PYTH_SOLUSD: "SOL",
            PYTH_XRPUSD: "XRP", PYTH_ADAUSD: "ADA", PYTH_AAVEUSD: "AAVE", PYTH_INJUSD: "INJ", PYTH_LINKUSD: "LINK"}

data_info = {
    'name': None,
    'price': None,
    'conf': None,
    'percent': None,
    'publish_time': None
}


def generate_pyth_url(base_url, timestamp, feed_ids):
    """
    生成包含多个 Pyth feed ID 和时间戳的 URL。

    :param base_url: 基础 URL，例如 "https://hermes.pyth.network/v2/updates/price"
    :param timestamp: 时间戳，例如 "1721025674"
    :param feed_ids: Pyth feed ID 列表
    :return: 拼接好的 URL
    """
    # 初始化 URL
    url = f"{base_url}/{timestamp}?"

    # 拼接 feed ID
    for key in feed_ids:
        url += f'ids[]={key}&'

    # 去掉最后一个 '&'
    if url.endswith('&'):
        url = url[:-1]

    return url

def get_pyth_price(url):
    price_datas = []
    response = requests.get(url)
    datas = response.json()['parsed']
    for data in datas:
        data_info = {
            'name': FEED_MAP['0x'+data['id']],
            'price': data['price']['price'],
            'conf': data['price']['conf'],
            'percent': int(data['price']['conf']) / int(data['price']['price']),
            'publish_time': data['price']['publish_time']
        }
        price_datas.append(data_info)
    return price_datas


# 初始化CSV文件
def initialize_csv():
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price', 'conf', 'percent', 'publish_time'])


# 将价格数据保存到CSV文件
def save_to_csv(data_info):
    with open(CSV_FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        # timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        writer.writerow(
            [data_info['name'], data_info['price'], data_info['conf'], data_info['percent'], data_info['publish_time']])


# 运行主函数
if __name__ == '__main__':
    initialize_csv()
    for time_stamp in range(1722213134, 1722297600):
        url = generate_pyth_url(PYTH_HISTORY_URL, time_stamp, FEED_MAP)
        price_datas = get_pyth_price(url)
        for data_info in price_datas:
            save_to_csv(data_info)

        print('{} price finish'.format(time_stamp))



