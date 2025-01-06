#!/usr/bin/python3
"""Script for parsing log entries and computing metrics"""


import sys
import signal
import re


def print_statistics(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
        total_size (int): Total sum of file sizes
        status_codes (dict): Dictionary containing counts of status codes
    """
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_logs():
    """
    Process log entries from stdin and compute metrics.
    
    Log format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    # Regular expression pattern for log line validation
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

    def signal_handler(sig, frame):
        """Handle CTRL+C by printing statistics and exiting"""
        print_statistics(total_size, status_codes)
        sys.exit(0)

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            try:
                match = re.match(pattern, line.strip())
                if match:
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))

                    # Update metrics
                    total_size += file_size
                    if status_code in status_codes:
                        status_codes[status_code] += 1

                    # Print statistics after every 10 valid lines
                    line_count += 1
                    if line_count % 10 == 0:
                        print_statistics(total_size, status_codes)

            except (ValueError, IndexError):
                continue

    # Handle keyboard interruption
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

    # Print final statistics if the input ends normally
    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    process_logs()
