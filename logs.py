#!/usr/bin/env python3

import logging

## Boiler plate - configuring logger
# instance
log = logging.Logger(__name__, logging.DEBUG) # main

# level (default it only prints warning+)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# formatting
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# save to path
log.addHandler(ch)

log.debug("Message to dev, qe, sysadmin")
log.info("General message to the user")
log.warning("Message of warning that does not happen due to an error")
log.error("Error that affects a single exectution")
log.critical("General problem has occurred, ex. dataset does not exist!")

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    #print(f"[Error] An error has occurred {str(e)}")
    log.error("[Error] An error has occurred %s", str(e)) #cannot use f string
    # stdout (print on screen to the user)
    # stderr (send it to the log system, do not print to the user)
