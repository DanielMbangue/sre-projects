# System Health Monitor

A Python tool that monitors system health and logs warnings when thresholds are exceeded.

## What it does
- Checks CPU, memory, and disk usage in real time
- Logs timestamped warnings to health_log.txt when thresholds are exceeded
- Handles errors and keyboard interrupts gracefully

## Thresholds
- CPU: 80%
- Memory: 80%
- Disk: 90%

## How to run
python3 health_monitor.py

## Skills used
Python, psutil, File I/O, Datetime, Error Handling