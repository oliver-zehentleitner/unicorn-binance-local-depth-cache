#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: test_plain.py
#
# Part of ‘UNICORN Binance Local Depth Cache’
# Project website: https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache
# Github: https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache
# Documentation: https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache
# PyPI: https://pypi.org/project/unicorn-binance-local-depth-cache
#
# License: MIT
# https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2023, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync
from lucit_licensing_python.exceptions import NoValidatedLucitLicense
import asyncio
import logging
import os
import sys

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


async def worker(ubldc):
    market = 'BTCUSDT'
    ubldc.create_depth_cache(markets=market)
    while ubldc.is_stop_request() is False:
        await asyncio.sleep(1)

try:
    with BinanceLocalDepthCacheManager(exchange="binance.com") as ubldc_manager:
        try:
            asyncio.run(worker(ubldc_manager))
        except KeyboardInterrupt:
            print("\r\nGracefully stopping ...")
except NoValidatedLucitLicense as error_msg:
    print(f"ERROR: {error_msg}")
    sys.exit(1)
