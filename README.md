# bcp38-tests
Python client/server utility to test for BCP38 compliance.

## Usage

* Run a server somewhere
  * `./bcp38-server.py`
* Edit the server value/run the client:
  * `sudo ./bcp38-client-spoof.py`
* Check the server console for output, 1 single line which shows the packet source, and packet contents being the same means you're BCP38 compliant. Up to 23 lines will be output sourced from randomly generated IP addresses.

## Requirements

* `apt-get install python-scapy`

