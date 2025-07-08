#!/usr/bin/env bash
# -*- coding: utf-8 -*-
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

security-check() {
    echo -n "Did you change the version in \`CHANGELOG.md\` and used \`dev/set_version.py\`? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/build_wheels.yml"
    echo "https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/actions/workflows/build_conda.yml"
}

compile-check() {
    echo -n "Compile local? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "ok, lets go ..."
    python3 setup.py bdist_wheel sdist
}

security-check
compile-check
