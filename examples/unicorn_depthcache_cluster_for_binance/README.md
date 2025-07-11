# UNICORN DepthCache Cluster for Binance
A highly scalable Kubernetes application from LUCIT to manage multiple and redundant UNICORN Binance Local Depth Cache 
Instances on a Kubernetes Cluster for high-frequency access to Binance's DepthCache data (order books). 

[UNICORN DepthCache Cluster for Binance](https://github.com/oliver-zehentleitner/unicorn-depthcache-cluster-for-binance)

## Overview
Instead of creating and using local DepthCaches, we connect to a UNICORN DepthCache Cluster for Binance.

## Prerequisites
Ensure you have Python 3.7+ installed on your system. 

Before running the provided script, install the required Python packages:
```bash
pip install -r requirements.txt
```

And set up your `.env` file!

## Get a UNICORN Binance Suite License
To run modules of the *UNICORN Binance Suite* you need a [valid license](https://shop.lucit.services)!

## Usage
### Running the Script:
```bash
python xxx.py
```

### Graceful Shutdown:
The script is designed to handle a graceful shutdown upon receiving a KeyboardInterrupt (e.g., Ctrl+C) or encountering 
an unexpected exception.

## Logging
The script employs logging to provide insights into its operation and to assist in troubleshooting. Logs are saved to a 
file named after the script with a .log extension.

For further assistance or to report issues, please [contact our support team](https://www.lucit.tech/get-support.html) 
or [visit our GitHub repository](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache).
