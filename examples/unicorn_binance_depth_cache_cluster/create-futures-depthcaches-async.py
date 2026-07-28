#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# Creates a UBDCC DepthCache with 2 replicas for every active futures market
# (status == "TRADING") on binance.com-futures.

from dotenv import load_dotenv
from pprint import pprint
from unicorn_binance_local_depth_cache import (
    BinanceLocalDepthCacheManager,
    DepthCacheClusterNotReachableError,
)
from unicorn_binance_rest_api import BinanceRestApiManager
import asyncio
import logging
import os

load_dotenv()

exchange: str = "binance.com-futures"
ubdcc_address: str = os.getenv("UBDCC_ADDRESS")
ubdcc_port: int = int(os.getenv("UBDCC_PORT"))

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(
    level=logging.ERROR,
    filename=os.path.basename(__file__) + ".log",
    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
    style="{",
)


async def main():
    with BinanceRestApiManager(exchange=exchange) as ubra:
        exchange_info = ubra.futures_exchange_info()
        markets = [
            item["symbol"]
            for item in exchange_info["symbols"]
            if item["status"] == "TRADING"
        ]
    result = await ubldc.cluster.create_depthcaches_async(
        exchange=exchange, markets=markets, desired_quantity=2
    )
    print(
        f"Adding {len(markets)} DepthCaches for exchange '{exchange}' on UBDCC '{ubdcc_address}':"
    )
    pprint(result)


try:
    with BinanceLocalDepthCacheManager(
        exchange=exchange, ubdcc_address=ubdcc_address, ubdcc_port=ubdcc_port
    ) as ubldc:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\r\nGracefully stopping ...")
        except Exception as error_msg:
            print(f"ERROR: {error_msg}")
except DepthCacheClusterNotReachableError as error_msg:
    print(f"ERROR: {error_msg}")
