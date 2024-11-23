"""
比较pyth rest接口，pyth http长链接和assetIndex wss获取的价格是否一致

"""

import requests
import csv
import asyncio
import aiohttp
import websockets
import json
from datetime import datetime, timezone

# 定义CSV文件名
CSV_FILENAME = 'gbpprod_prices.csv'

# 定义获取价格的URL
'''qa pufeth'''
# REST_URL = 'https://hermes.pyth.network/v2/updates/price/latest?ids[]=0xe5801530292c348f322b7b4a48c1c0d59ab629846cce1c816fc27aee2054b560'
# HTTP_STREAM_URL = 'wss://hermes.pyth.network/v2/updates/price/stream?ids[]=0xe5801530292c348f322b7b4a48c1c0d59ab629846cce1c816fc27aee2054b560'
# ASSET_WSS_URL = 'wss://fstream.binanceqa.com/plain/stream?streams=pufethusd@assetIndex'
# SYMBOL_WSS_URL = 'wss://fstream.binanceqa.com/plain/stream?streams=pufethusd@priceIndex'

'''prod GBP'''
# REST_URL = 'https://hermes.pyth.network/v2/updates/price/latest?ids[]=0x84c2dde9633d93d1bcad84e7dc41c9d56578b7ec52fabedc1f335d673df0a7c1'
REST_URL = 'https://hermes-mainnet.rpc.extrnode.com/adf6e2da-430f-4f7f-b7c3-8f4e2123a319/v2/updates/price/latest?ids[]=0x84c2dde9633d93d1bcad84e7dc41c9d56578b7ec52fabedc1f335d673df0a7c1'
SYMBOL_WSS_URL = 'wss://fstream.apollox.finance/stream?streams=gbpusd@priceIndex'



# 共享数据结构来存储价格数据
price_data = {
    'timestampREST': None,
    'REST': None,
    'timestampHTTP': None,
    'HTTPStream': None,
    'timestampWSSAsset': None,
    'WebSocketAsset': None,
    'timestampWSSSymbol': None,
    'WebSocketSymbol': None
}


# 初始化CSV文件
def initialize_csv():
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'timestampREST', 'REST', 'timestampHTTP', 'HTTPStream', 'timestampWSSAsset', 'WebSocketAsset', 'timestampWSSSymbol', 'WebSocketSymbol'])


# 将价格数据保存到CSV文件
def save_to_csv():
    with open(CSV_FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        writer.writerow(
            [timestamp, price_data['timestampREST'], price_data['REST'], price_data['timestampHTTP'], price_data['HTTPStream'], price_data['timestampWSSAsset'], price_data['WebSocketAsset'], price_data['timestampWSSSymbol'], price_data['WebSocketSymbol']])


# 通过REST API获取价格
def get_price_from_rest():
    response = requests.get(REST_URL)
    data = response.json()
    # print(data['parsed'][0])
    decimal = int(data['parsed'][0]['price']['expo'])
    price = int(data['parsed'][0]['price']['price']) * 10 ** decimal
    timestamp = data['parsed'][0]['metadata']['proof_available_time']
    return price, timestamp


# 持续监听HTTP长链接
async def http_stream_listener():
    async with aiohttp.ClientSession() as session:
        async with session.get(HTTP_STREAM_URL) as response:
            last_timestamp_http = None
            async for line in response.content:
                if line:
                    # print(line)
                    line = line.decode('utf-8').strip()
                    if line.startswith('data:'):
                        line = line[5:].strip()
                        data = json.loads(line)
                        # print(data)
                        if 'parsed' in data:
                            timestamp_http = data['parsed'][0]['metadata']['proof_available_time']
                            if timestamp_http != last_timestamp_http:
                                last_timestamp_http = timestamp_http
                                price = int(data['parsed'][0]['price']['price']) / 10 ** 8
                                # timestamp = datetime.now(timezone.utc).replace(second=0, microsecond=0).isoformat()
                                price_data['timestampHTTP'] = timestamp_http
                                price_data['HTTPStream'] = price
                                print(f"HTTPStream: {price} at {timestamp_http}")


# 持续监听WebSocket
async def wss_listener_asset():
    async with websockets.connect(ASSET_WSS_URL) as websocket:
        async for message in websocket:
            data = json.loads(message)
            if 'data' in data and 'i' in data['data']:
                price = data['data']['i']
                timestamp_wss = data['data']['E']
                # timestamp = datetime.now(timezone.utc).replace(second=0, microsecond=0).isoformat()
                price_data['timestampWSSAsset'] = timestamp_wss
                price_data['WebSocketAsset'] = price
                print(f"WebSocketAsset: {price} at {timestamp_wss}")


async def wss_listener_symbol():
    async with websockets.connect(SYMBOL_WSS_URL) as websocket:
        async for message in websocket:
            data = json.loads(message)
            if 'data' in data and 'p' in data['data']:
                price = data['data']['p']
                timestamp_wss = data['data']['E']
                # timestamp = datetime.now(timezone.utc).replace(second=0, microsecond=0).isoformat()
                price_data['timestampWSSSymbol'] = timestamp_wss
                price_data['WebSocketSymbol'] = price
                print(f"WebSocketSymbol: {price} at {timestamp_wss}")


# 定期获取REST API价格
async def rest_price_fetcher():
    while True:
        try:
            price_rest, timestamp_rest = get_price_from_rest()
            # timestamp = datetime.now(timezone.utc).replace(second=0, microsecond=0).isoformat()
            price_data['timestampREST'] = timestamp_rest
            price_data['REST'] = price_rest
            print(f"REST: {price_rest} at {timestamp_rest}")
        except Exception as e:
            print(f"REST API Error: {e}")

        await asyncio.sleep(1)


# 定期将数据保存到CSV
async def csv_saver():
    while True:
        await asyncio.sleep(1)
        if price_data['REST'] and price_data['WebSocketSymbol']:
        # if price_data['HTTPStream'] and price_data['WebSocket']:
        # if price_data['REST'] and price_data['HTTPStream'] and price_data['WebSocketAsset'] and price_data['WebSocketSymbol']:
            save_to_csv()
            # 重置数据
            price_data['REST'] = None
            price_data['HTTPStream'] = None
            price_data['WebSocketAsset'] = None
            price_data['WebSocketSymbol'] = None
            price_data['timestampREST'] = None
            price_data['timestampHTTP'] = None
            price_data['timestampWSSAsset'] = None
            price_data['timestampWSSSymbol'] = None


# 主函数
async def main():
    initialize_csv()

    await asyncio.gather(
        # http_stream_listener(),
        # wss_listener_asset(),
        wss_listener_symbol(),
        rest_price_fetcher(),
        csv_saver()
    )


# 运行主函数
if __name__ == '__main__':
    asyncio.run(main())

