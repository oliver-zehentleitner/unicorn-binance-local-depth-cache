#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ¯\_(ツ)_/¯
#
# File: unicorn_binance_local_depth_cache/exceptions.py
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


class DepthCacheClusterNotReachableError(Exception):
    """
    Exception raised when the UBDCC is not reachable.
    """
    def __init__(self, url=None):
        if url is None:
            self.message = f"Connection with UBDCC could not be established!"
        else:
            self.message = f"Connection with UBDCC ({url}) could not be established!"
        super().__init__(self.message)


class DepthCacheOutOfSync(Exception):
    """
    Exception raised when an attempt is made to use a depth_cache that is out of sync.
    """
    def __init__(self, market=None):
        if market is None:
            self.message = f"The depth_cache is out of sync, please try again later"
        else:
            self.message = f"The depth_cache for market '{market}' is out of sync, please try again later"
        super().__init__(self.message)


class DepthCacheAlreadyStopped(Exception):
    """
    Exception raised when an attempt is made to use a depth_cache that has already been stopped.
    """
    def __init__(self, market=None):
        if market is None:
            self.message = f"The depth_cache is already stopped!"
        else:
            self.message = f"The depth_cache for market '{market}' is already stopped!"
        super().__init__(self.message)


class DepthCacheNotFound(Exception):
    """
    Exception raised when an attempt is made to use an instance that does not exist.
    """
    def __init__(self, market=None):
        if market is None:
            self.message = f"The depth_cache does not exist!"
        else:
            self.message = f"The depth_cache for market '{market}' does not exist!"
        super().__init__(self.message)
