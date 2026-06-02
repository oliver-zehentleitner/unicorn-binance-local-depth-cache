[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-binance-local-depth-cache.svg?label=github)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/oliver-zehentleitner/unicorn-binance-local-depth-cache/total?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/releases)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-local-depth-cache?color=blue)](https://pypi.org/project/unicorn-binance-local-depth-cache/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-local-depth-cache)](https://pepy.tech/project/unicorn-binance-local-depth-cache)
[![Conda-Forge Version](https://img.shields.io/conda/v/conda-forge/unicorn-binance-local-depth-cache?color=blue&label=conda)](https://anaconda.org/conda-forge/unicorn-binance-local-depth-cache)
[![Conda-Forge Downloads](https://img.shields.io/conda/dn/conda-forge/unicorn-binance-local-depth-cache?color=blue&label=downloads)](https://anaconda.org/conda-forge/unicorn-binance-local-depth-cache)
[![License](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-binance-local-depth-cache.svg?color=blue)](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_local_depth_cache.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_local_depth_cache.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/issues)
[![codecov](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-local-depth-cache/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-local-depth-cache)
[![CodeQL](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/codeql.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/codeql.yml)
[![Unit Tests](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/build_wheels.yml)
[![Conda-Forge Build](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/unicorn-binance-local-depth-cache-feedstock?branchName=main)](https://github.com/conda-forge/unicorn-binance-local-depth-cache-feedstock)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://blog.technopathy.club/series/unicorn-binance-suite)
[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)
[![Reddit](https://img.shields.io/badge/community-reddit-41ab8c)](https://www.reddit.com/r/UNICORNBinanceSuite)

[![UBS-Banner](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-suite/master/images/logo/UBS-Banner-Readme.png)](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

# UNICORN Binance Local Depth Cache 

[Description](#description) | [Installation](#installation-and-upgrade) | [Documentation](#documentation) | [Examples](#examples) | [Change Log](#change-log) | 
[Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | [Contributing](#contributing) |[Disclaimer](#disclaimer)

A Python SDK for accessing and managing multiple local Binance 
[order books](https://academy.binance.com/en/glossary/order-book) with Python in a simple, fast, flexible, robust 
and fully functional way. 

The organization of the DepthCache takes place in the same asyncio loop as the reception of the websocket data. The 
full stack of the UBS modules (REST, WebSocket and DepthCache) can be downloaded and installed by PyPi and Anaconda 
as a Python C extension for maximum performance.

Part of '[UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite)'.

## Using a DepthCache

### [Create a local DepthCache](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=create_depthcache#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.create_depthcache) for Binance with just 3 lines of code
```
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync

ubldc = BinanceLocalDepthCacheManager(exchange="binance.com", depth_cache_update_interval=100)
ubldc.create_depthcache("BTCUSDT")
```

### Get the [asks](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=get_asks#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.get_asks) and [bids](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=get_bids#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.get_bids)
#### To obtain the complete order book
```
asks = ubldc.get_asks("BTCUSDT")
bids = ubldc.get_bids("BTCUSDT")
```

#### Get the first X elements
```
asks = ubldc.get_asks("BTCUSDT", limit_count=10)
bids = ubldc.get_bids("BTCUSDT", limit_count=10)
```

#### Retain the elements until volume X has been exceeded
```
asks = ubldc.get_asks("BTCUSDT", threshold_volume=300000)
bids = ubldc.get_bids("BTCUSDT", threshold_volume=300000)
```

### Catch an exception, if the [DepthCache is out of sync](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_depth_cache_synchronized#unicorn_binance_local_depth_cache.exceptions.DepthCacheOutOfSync) while accessing its data
```
try:
    asks = ubldc.get_asks(market="BTCUSDT", limit_count=5, threshold_volume=300000)
    bids = ubldc.get_bids(market="BTCUSDT", limit_count=5, threshold_volume=300000)
except DepthCacheOutOfSync:
    asks = "Out of sync!"
    bids = "Out of sync!"
```

### [Stop and delete a DepthCache](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=stop_depth_cache#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.stop_depth_cache):
```
ubldc.stop_depthcache("BTCUSDT")
```

## Stop `ubldc` after usage to avoid memory leaks

When you instantiate UBLDC with `with`, `ubldc.stop_manager()` is automatically executed upon exiting the `with`-block.

```
with BinanceWebSocketApiManager() as ubldc:
    ubldc.create_depthcache("BTCUSDT")
```

Without `with`, you must explicitly execute `ubldc.stop_manager()` yourself.

```
ubldc.stop_manager()
```

[Discover more possibilities.](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html)

## Connect to a UNICORN Binance DepthCache Cluster
The [UNICORN Binance DepthCache Cluster (UBDCC)](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) 
manages thousands of DepthCaches with load balancing, automatic failover and self-healing state. It runs 
[locally on a single machine](https://blog.technopathy.club/from-pip-install-to-a-redundant-binance-order-book-cluster-ubdcc-dashboard-quickstart) 
(`pip install ubdcc`) or 
[scales across a Kubernetes cluster](https://blog.technopathy.club/install-ubdcc-on-kubernetes-with-helm-a-redundant-binance-order-book-cluster-in-20-minutes). Access is via REST API from any language — 
Python users can use the built-in cluster module shown below.

### Synchronous

```python
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheClusterNotReachableError

def main():
    ubldc.cluster.create_depthcaches(exchange="binance.com", markets=['BTCUSDT', 'ETHUSDT'], desired_quantity=2)
    while ubldc.is_stop_request() is False:
        print(ubldc.cluster.get_asks(exchange="binance.com", market='BTCUSDT', limit_count=2))
        
try:
    with BinanceLocalDepthCacheManager(exchange="binance.com", ubdcc_address="127.0.0.1", ubdcc_port=42081) as ubldc:
        try:
            main()
        except KeyboardInterrupt:
            print("\r\nGracefully stopping ...")
except DepthCacheClusterNotReachableError as error_msg:
    print(f"ERROR: {error_msg}")
```

### Asynchronous

```python
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheClusterNotReachableError

async def main():
    await ubldc.cluster.create_depthcaches_async(exchange="binance.com", 
                                                  markets=['BTCUSDT', 'ETHUSDT'], 
                                                  desired_quantity=2)
    while ubldc.is_stop_request() is False:
        print(await ubldc.cluster.get_asks_async(exchange="binance.com", market='BTCUSDT', limit_count=2))
        
try:
    with BinanceLocalDepthCacheManager(exchange="binance.com", ubdcc_address="127.0.0.1", ubdcc_port=42081) as ubldc:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\r\nGracefully stopping ...")
except DepthCacheClusterNotReachableError as error_msg:
    print(f"ERROR: {error_msg}")
```

[Try the cluster examples!](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/tree/master/examples/unicorn_binance_depth_cache_cluster)

[Discover more cluster possibilities ...](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html#module-unicorn_binance_local_depth_cache.cluster)

## Description
The Python package [UNICORN Binance Local Depth Cache](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) 
provides local order books for the Binance Exchanges 
[Binance](https://github.com/binance-exchange/binance-official-api-docs) ([+Testnet](https://testnet.binance.vision/)), 
Binance Cross Margin and Isolated Margin (+Testnet),
[Binance Futures](https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams) 
([+Testnet](https://testnet.binancefuture.com)),
[Binance European Options](https://developers.binance.com/docs/derivatives/option/general-info)
([+Testnet](https://testnet.binancefuture.com)),
[Binance US](https://www.binance.us/) and 
[TRBinance](https://www.binance.tr/).

***The algorithm of the DepthCache management was designed according to these instructions:***

Since, according to Binance's predefined algorithm, 
[all levels > 1000 would be orphaned and remain forever between valid levels](https://blog.technopathy.club/your-binance-order-book-is-wrong-here-s-why)
, UBLDC removes them as soon as they exceed the thousandth position.

- [Binance Spot: "How to manage a local order book correctly"](https://binance-docs.github.io/apidocs/spot/en/#how-to-manage-a-local-order-book-correctly)
- [Binance Futures: "How to manage a local order book correctly"](https://binance-docs.github.io/apidocs/futures/en/#diff-book-depth-streams)
- [Binance European Options: "How to manage a local order book correctly"](https://developers.binance.com/docs/derivatives/option/websocket-market-streams)
- [Binance US: "Managing a Local Order Book"](https://docs.binance.us/#order-book-depth-diff-stream)
- [TRBinance: "Diff. Depth Stream"](https://www.binance.tr/apidocs/#diff-depth-stream)

With [create_depthcache()`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=create_depthcache#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.create_depthcaches) 
the DepthCache is started and initialized, i.e. for each DepthCache that is to be created, a separate 
asyncio coroutine is inserted into the event loop of the stream. As soon as at least one depth update is received via 
websocket, a REST snapshot is downloaded and the depth updates are applied to it so that it is synchronized 
in real time. As soon as once this is done, the status of the cache get set to "synchronous".

Data in the DepthCache can be accessed with ['get_asks()'](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=get_asks#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.get_asks) 
and ['get_bids()'](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=get_bids#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.get_bids). 
If the state of the DepthCache is not synchronous during access, the exception 
['DepthCacheOutOfSync'](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_depth_cache_synchronized#unicorn_binance_local_depth_cache.exceptions.DepthCacheOutOfSync) 
is thrown.

The DepthCache will immediately start an automatic re-initialization if a gap in the UpdateID`s is detected (missing 
update event) or if the websocket connection is interrupted. As soon as this happens the state of the DepthCache is set 
to "out of sync" and when accessing the cache the exception ['DepthCacheOutOfSync'](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_depth_cache_synchronized#unicorn_binance_local_depth_cache.exceptions.DepthCacheOutOfSync) is thrown.

### Why a local DepthCache?
A local DepthCache is the fastest way to access the current order book depth at any time while transferring as little data as necessary. A REST snapshot takes a lot of time and the amount of data that is transferred is relatively large. Continuous full transmission of the order book via websocket is faster, but the amount of data is huge. A local depth_cache is initialized once with a REST snapshot and then handles Diff. Depth updates applied by the websocket connection. By transferring a small amount of data (only the changes), a local depth_cache is kept in sync in real time and also allows extremely fast (local) access to the data without exceeding the [Binance request weight limits](https://www.binance.com/en/support/faq/360004492232).

### What are the benefits of the UNICORN Binance Local Depth Cache?
- Always know if the cache is in sync! If the DepthCache is out of sync, the exception ['DepthCacheOutOfSync'](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_depth_cache_synchronized#unicorn_binance_local_depth_cache.exceptions.DepthCacheOutOfSync) 
is thrown or ask with [`is_depth_cache_synchronized()`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_depth_cache_synchronized#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.is_depth_cache_synchronized). 

- If a depth cache is out of sync it gets refreshed automatically within a few seconds.

- 100% Websocket auto-reconnect!

- Supported Exchanges

| Exchange                                                           | Exchange string               | 
|--------------------------------------------------------------------|-------------------------------| 
| [Binance](https://www.binance.com)                                 | `binance.com`                 |
| [Binance Testnet](https://testnet.binance.vision/)                 | `binance.com-testnet`         |
| [Binance Cross Margin](https://www.binance.com)                    | `binance.com-margin`          |
| [Binance Cross Margin Testnet](https://testnet.binance.vision/)    | `binance.com-margin-testnet`  |
| [Binance Isolated Margin](https://www.binance.com)                 | `binance.com-isolated_margin` |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) | `binance.com-isolated_margin-testnet` |
| [Binance USD-M Futures](https://www.binance.com)                   | `binance.com-futures`         |
| [Binance USD-M Futures Testnet](https://testnet.binancefuture.com) | `binance.com-futures-testnet` |
| [Binance European Options](https://www.binance.com)                | `binance.com-vanilla-options`         |
| [Binance European Options Testnet](https://testnet.binancefuture.com) | `binance.com-vanilla-options-testnet` |
| [Binance US](https://www.binance.us/)                              | `binance.us`                  |
| [TRBinance](https://www.binance.tr/)                               | `trbinance.com` ¹             |

  ¹ TRBinance requires an API key even for public REST endpoints (e.g. order book snapshots). 
  Pass `api_key` and `api_secret` to `BinanceRestApiManager` when using `exchange="trbinance.com"`.

- Create multiple depth caches within a single object instance. 

- Each DepthCache is managed in an asyncio coroutine.

- Start or stop multiple caches with just one command 
[`create_depthcache()`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=create_depthcache#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.create_depthcaches)
or [`stop_depthcache()`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=stop_depthcache#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.stop_depthcache).

- Control websocket out of sync detection with [`websocket_ping_interval`, `websocket_ping_timeout` and `websocket_close_timeout`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.create_depthcache) 

- Powered by [UNICORN Binance REST API](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) and 
[UNICORN Binance WebSocket API](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api).

- Available as a package via `pip` and `conda` as precompiled C extension with stub files for improved Intellisense 
  functions and source code for easier debugging of the source code. [To the installation.](#installation-and-upgrade)

If you like the project, please 
[![star](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/master/images/misc/star.png)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/stargazers) it on 
[GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)! 

## Installation and Upgrade
The module requires Python 3.9 and runs smoothly up to and including Python 3.14.

PyPy wheels are available for all supported Python versions.

**conda-forge note:** Conda packages are provided for Python 3.10 – 3.14. Python 3.9 is not available on conda-forge — it was dropped from the global pinning after reaching end-of-life in October 2025. For Python 3.9, use `pip install`.


The current dependencies are listed [here](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki/Installation).

### Packages are created automatically with GitHub Actions
When a new release is created, the
[Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/build_wheels.yml)
workflow spins up virtual Windows/Linux/Mac runners, compiles the Cython extensions, builds the
wheels and publishes them on GitHub and PyPI. The conda-forge feedstock
[conda-forge/unicorn-binance-local-depth-cache-feedstock](https://github.com/conda-forge/unicorn-binance-local-depth-cache-feedstock)
picks up the new PyPI release automatically and builds the Conda packages on its own infrastructure.
This is a transparent method that makes it possible to trace the source code behind a compilation.

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static typing and C-level performance. By compiling 
  Python code into C, Cython Wheels can significantly enhance the execution speed of Python code, especially in 
  computationally intensive tasks. This means faster runtimes and more efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and efficiency. It uses Just-In-Time (JIT) compilation, 
  which can dramatically improve the performance of Python code. Our PyPy Wheels are tailored for compatibility with 
  PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

#### Installation
`pip install unicorn-binance-local-depth-cache`

#### Update
`pip install unicorn-binance-local-depth-cache --upgrade`

### conda
```
conda install -c conda-forge unicorn-binance-local-depth-cache
```

### From source of the latest release with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-local-depth-cache/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 2.14.0) you determined 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/archive/2.14.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/tarball/master --upgrade`

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/changelog.html](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/changelog.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/modules.html)

## Examples
- [Look here!](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/tree/master/examples/)

## Related Articles
- [The Complete Binance Python API Guide 2026](https://blog.technopathy.club/the-complete-binance-python-api-guide-2026)
- [How to create a Binance API Key and API Secret?](https://blog.technopathy.club/how-to-create-a-binance-api-key-and-api-secret)
- [Why Your Binance Order Book Should Not Live Inside Your Bot](https://blog.technopathy.club/why-your-binance-order-book-should-not-live-inside-your-bot)
- [Your Binance Order Book Is Wrong — Here's Why](https://blog.technopathy.club/your-binance-order-book-is-wrong-here-s-why)
- [Your Binance DepthCache Is Rotting — Here's the Proof in 25 Hours](https://blog.technopathy.club/your-binance-depthcache-is-rotting-here-s-the-proof-in-25-hours)
- [UBDCC Deep Dive: Building a Trust Layer for Binance Order Books](https://blog.technopathy.club/ubdcc-deep-dive-building-a-trust-layer-for-binance-order-books)
- [Install UBDCC on Kubernetes with Helm: A Redundant Binance Order Book Cluster in 20 Minutes](https://blog.technopathy.club/install-ubdcc-on-kubernetes-with-helm-a-redundant-binance-order-book-cluster-in-20-minutes)
- [I Created 2013 Binance Order Books on Kubernetes with 2 Replicas in 25 Minutes — Then Stress-Tested the REST API](https://blog.technopathy.club/i-created-2013-binance-order-books-on-kubernetes-with-2-replicas-in-25-minutes-then-stress-tested-the-rest-api)
- [UNICORN Binance Suite Article Series](https://blog.technopathy.club/series/unicorn-binance-suite)

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/wiki](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/wiki)

## Social
- [Discussions](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/discussions)
- [Telegram](https://t.me/unicorndevs) 
- [Reddit Community](https://www.reddit.com/r/UNICORNBinanceSuite/) 
- [https://dev.binance.vision](https://dev.binance.vision)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/master/images/misc/watch.png)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/watchers) 
the repository on [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache), write your 
[own script](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/blob/master/examples/ubldc_package_update_check) 
with using 
[`is_update_available()`](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache/unicorn_binance_local_depth_cache.html?highlight=is_update_available#unicorn_binance_local_depth_cache.manager.BinanceLocalDepthCacheManager.is_update_available).

To receive news (like inspection windows/maintenance) about the Binance API`s subscribe to their telegram groups: 

- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/TRBinanceTR](https://t.me/TRBinanceTR)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you dont find an issue related to your topic, please open a new [issue](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/issues)!

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/security/policy)

## Contributing
[UNICORN Binance Local Depth Cache](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-local-depth-cache)](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/master/images/misc/heart.png) open source!

---

## AI Integration

This project provides a [`llms.txt`](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/refs/heads/master/llms.txt) file for AI tools (ChatGPT, Claude, Copilot, etc.) with structured 
usage instructions, code examples and module routing.

---

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.
