#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# Demo: add, list and remove Binance API credentials on a running UBDCC
# cluster. Credentials are optional — public-only operation works without
# them, but adding keys lifts DCN rate limits (faster initial sync, more
# refreshes).
#
# Multiple key pairs per account group are allowed; mgmt load-balances them
# across DCNs. Public responses only show a masked preview and never the
# secret.

import logging
import os
from dotenv import load_dotenv
from pprint import pprint
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheClusterNotReachableError

load_dotenv()

exchange: str = "binance.com-futures"
ubdcc_address: str = os.getenv('UBDCC_ADDRESS')
ubdcc_port: int = int(os.getenv('UBDCC_PORT'))

# Credentials to add — normally pulled from a vault / .env, not hard-coded
account_group: str = "binance.com"
api_key: str = os.getenv('BINANCE_API_KEY')
api_secret: str = os.getenv('BINANCE_API_SECRET')

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(level=logging.ERROR,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


try:
    with BinanceLocalDepthCacheManager(exchange=exchange,
                                       ubdcc_address=ubdcc_address,
                                       ubdcc_port=ubdcc_port) as ubldc:
        if api_key and api_secret:
            print(f"Adding credential for account_group '{account_group}' ...")
            add_result = ubldc.cluster.ubdcc_add_credentials(account_group=account_group,
                                                             api_key=api_key,
                                                             api_secret=api_secret)
            pprint(add_result)
            new_id = add_result.get('id')
        else:
            print("No BINANCE_API_KEY / BINANCE_API_SECRET in environment — skipping add step.")
            new_id = None

        print("\nCurrent credentials (keys masked):")
        pprint(ubldc.cluster.ubdcc_get_credentials_list())

        if new_id:
            print(f"\nRemoving credential '{new_id}' ...")
            #pprint(ubldc.cluster.ubdcc_remove_credentials(credential_id=new_id))

except DepthCacheClusterNotReachableError as error_msg:
    print(f"ERROR: {error_msg}")
