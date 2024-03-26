#!usr/bin.#!/usr/bin/env python3
import os
import sys
import shutil
import socket

import psutil

def check_reboot():
    "Return True if the computer ha pending reboot."
    return os.path.exists("/run/reboot-required")

def check_root_full():
    "Return True if the root partition is full, False otherwise."
    return check_disk_full(disk="/", min_gb=2, min_percent=10)


def check_disk_full(disk, min_gb, min_percent):
    "Returns True if there isn't enough disk space, False otherwise."
    du = shutil.disk_usage(disk)
    percent_free = 100*du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_no_network():
    "Returns True if it fails to open url, False otherwise"
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True
    
def check_disk_usage(min_percent):
    disk_usage = psutil.disk_usage('/')
    percent_free = disk_usage.free / disk_usage.total * 100
    return percent_free >= min_percent

def check_cpu_usage(max_percent):
    cpu_usage = psutil.cpu_percent(interval=5)
    return cpu_usage <= max_percent

def check_memory_usage(min_available_mb):
    memory_usage = psutil.virtual_memory()
    available_mb = memory_usage.available / 1024 / 1024
    return available_mb >= min_available_mb

def check_system_health():
    """Checks system health including disk usage, pending reboot, and network connectivity."""
    checks = [
        (check_reboot, "Pending Reboot."),
        (lambda: check_disk_full("/", 2, 10), "Root partition full."),
        (check_no_network, "No working network."),
        (lambda: check_cpu_usage(50), "High CPU usage."),
        (lambda: check_memory_usage(60), "Low memory."),
        (lambda: check_disk_usage(50), "Low memory."),
    ]
    for check, msg in checks:
        if check():
            return False, msg
    return True, "Everything OK."

if __name__ == "__main__":
    is_healthy, message = check_system_health()
    print(message)
    sys.exit(0 if is_healthy else 1)
