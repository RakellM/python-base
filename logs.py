#!/usr/bin/env python3

import os
import logging

## BOILERPLATE - configuring logger
# TODO: use fuction
# TODO: use lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper() # create a env variable to set the log level the user wants to see
log = logging.Logger("raquel", log_level) 
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""
log.debug("Message to dev, qe, sysadmin")
log.info("General message to the user")
log.warning("Message of warning that does not happen due to an error")
log.error("Error that affects a single exectution")
log.critical("General problem has occurred, ex. dataset does not exist!")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    #print(f"[Error] An error has occurred {str(e)}")
    log.error("[Error] An error has occurred %s", str(e)) #cannot use f string
    # stdout (print on screen to the user)
    # stderr (send it to the log system, do not print to the user)
