#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    du = shutil.disk_usage(disk)
    gigabytes_free = du.free / 2**30  # Calculate free space in gigabytes
    percent_free = 100 * gigabytes_free / du.total
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything is OK.")
sys.exit(0)
