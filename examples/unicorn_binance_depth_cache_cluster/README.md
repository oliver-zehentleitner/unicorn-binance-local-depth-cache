# UNICORN DepthCache Cluster for Binance
Examples for using [UBLDC](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)'s built-in 
cluster interface to connect to a 
[UNICORN Binance DepthCache Cluster (UBDCC)](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster).

## Overview
Instead of creating and using local DepthCaches, we connect to a 
[UBDCC](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) cluster and use 
[UBLDC](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache)'s `cluster` module for 
synchronous and asynchronous access to shared order book data.

## Prerequisites
Ensure you have Python 3.7+ installed on your system. 

Before running the provided script, install the required Python packages:
```bash
pip install -r requirements.txt
```

And set up your `.env` file with `UBDCC_ADDRESS` and `UBDCC_PORT`.

## Usage
### Running the Script:
```bash
python <script_name>.py
```

### Graceful Shutdown:
The script is designed to handle a graceful shutdown upon receiving a KeyboardInterrupt (e.g., Ctrl+C) or encountering 
an unexpected exception.

## Logging
The script employs logging to provide insights into its operation and to assist in troubleshooting. Logs are saved to a 
file named after the script with a .log extension.

For further assistance or to report issues, please open a 
[GitHub Issue](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache/issues/new/choose) 
or join the [UNICORN Binance Suite community on Telegram](https://t.me/unicorndevs).
