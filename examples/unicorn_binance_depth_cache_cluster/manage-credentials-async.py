#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# Async version of manage-credentials.py.

import asyncio
import logging
import os
from dotenv import load_dotenv
from pprint import pprint
from unicorn_binance_local_depth_cache import (
    BinanceLocalDepthCacheManager,
    DepthCacheClusterNotReachableError,
)

load_dotenv()

exchange: str = "binance.com-futures"
ubdcc_address: str = os.getenv("UBDCC_ADDRESS")
ubdcc_port: int = int(os.getenv("UBDCC_PORT"))

account_group: str = "binance.com"
api_key: str = os.getenv("BINANCE_API_KEY")
api_secret: str = os.getenv("BINANCE_API_SECRET")

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(
    level=logging.ERROR,
    filename=os.path.basename(__file__) + ".log",
    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
    style="{",
)


async def main():
    if api_key and api_secret:
        print(f"Adding credential for account_group '{account_group}' ...")
        add_result = await ubldc.cluster.add_credentials_async(
            account_group=account_group, api_key=api_key, api_secret=api_secret
        )
        pprint(add_result)
        new_id = add_result.get("id")
    else:
        print(
            "No BINANCE_API_KEY / BINANCE_API_SECRET in environment — skipping add step."
        )
        new_id = None

    print("\nCurrent credentials (keys masked):")
    pprint(await ubldc.cluster.get_credentials_list_async())

    if new_id:
        print(f"\nRemoving credential '{new_id}' ...")
        pprint(await ubldc.cluster.remove_credentials_async(credential_id=new_id))


try:
    with BinanceLocalDepthCacheManager(
        exchange=exchange, ubdcc_address=ubdcc_address, ubdcc_port=ubdcc_port
    ) as ubldc:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\r\nGracefully stopping ...")
except DepthCacheClusterNotReachableError as error_msg:
    print(f"ERROR: {error_msg}")
