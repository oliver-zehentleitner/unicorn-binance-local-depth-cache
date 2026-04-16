#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯

from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync
import asyncio
import logging
import os

# Options symbols use the format: UNDERLYING-YYMMDD-STRIKE-C/P
# Adjust these to currently listed options on Binance
markets = ["BTC-260626-120000-C", "BTC-260626-120000-P"]
exchange = "binance.com-vanilla-options"
limit_count = 5

logging.getLogger("unicorn_binance_local_depth_cache")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


async def main():
    print(f"Starting {exchange} DepthCaches for {len(markets)} markets: {markets}")
    ubldc.create_depthcache(markets=markets)

    while ubldc.is_stop_request() is False:
        for market in markets:
            try:
                top_asks = ubldc.get_asks(market=market, limit_count=limit_count)
                top_bids = ubldc.get_bids(market=market, limit_count=limit_count)
            except DepthCacheOutOfSync:
                top_asks = "Out of sync!"
                top_bids = "Out of sync!"
            print(f"[{market}] synced={ubldc.is_depth_cache_synchronized(market=market)}")
            print(f"  asks: {top_asks}")
            print(f"  bids: {top_bids}")
        print()
        await asyncio.sleep(5)


# depth_cache_update_interval=500 → depth@500ms stream (recommended for Options)
with BinanceLocalDepthCacheManager(exchange=exchange,
                                   depth_cache_update_interval=500) as ubldc:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\r\nGracefully stopping ...")
    except Exception as e:
        print(f"\r\nERROR: {e}")
        print("Gracefully stopping ...")
