# Binance Options DepthCache
## Overview
Create local order book DepthCaches for Binance European Options (Vanilla Options) 
with `exchange="binance.com-vanilla-options"`.

Options symbols use the format `UNDERLYING-YYMMDD-STRIKE-C/P`, e.g. `BTC-260626-120000-C`.

## Prerequisites
Ensure you have Python 3.9+ installed on your system.

Before running the provided script, install the required Python packages:
```bash
pip install -r requirements.txt
```

No API key is needed for public market data.

## Usage
### Running the Script:
```bash
python binance_options_depthcache.py
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
