#!/usr/bin/env python3

import os
import sys
import logging
import time

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than Permission

def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines() # FileNotFoundError
        except FileNotFoundError as e:
            print("{str(e)}")
            time.sleep(2)
            if retry > 1:
                # recurssive
                return try_to_open_a_file(filepath, retry=retry - 1)
        else:
            print("Success!")
        finally:
            print("Always run this text!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
