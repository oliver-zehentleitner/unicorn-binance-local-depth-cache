#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# File: unicorn_binance_local_depth_cache/cluster_endpoints.py
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
# Author: Oliver Zehentleitner
#
# Copyright (c) 2019-2025, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

class ClusterEndpoints:
    create_depthcache: str = "create_depthcache"
    create_depthcaches: str = "create_depthcaches"
    get_asks: str = "get_asks"
    get_bids: str = "get_bids"
    get_cluster_info: str = "get_cluster_info"
    get_depthcache_list: str = "get_depthcache_list"
    get_depthcache_info: str = "get_depthcache_info"
    stop_depthcache: str = "stop_depthcache"
    submit_license: str = "submit_license"
    test: str = "test"
