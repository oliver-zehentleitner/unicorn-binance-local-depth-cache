#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: pypi/upload_wheel.sh
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
# Copyright (c) 2019-2026, Oliver Zehentleitner (https://about.me/oliver-zehentleitner)
# All rights reserved.
#
# create this file:
# ~/.pypirc


python3 -m twine upload dist/*
