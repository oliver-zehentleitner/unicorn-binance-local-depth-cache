# [UBLDC](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) Demo
## Overview
A demo script showing [UBLDC](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) in action 
with multiple DepthCaches, limit_count and threshold_volume filtering.

## Prerequisites
Ensure you have Python 3.7+ installed on your system. 

Before running the provided script, install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage
### Running the Script:
```bash
python ubldc-demo.py
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