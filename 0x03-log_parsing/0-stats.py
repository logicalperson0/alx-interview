#!/usr/bin/env python3
"""
module for script that reads stdin line by line and computes metrics
"""
import sys
from operator import itemgetter


def parser(logging):
    """
    Parses log into fields
    """
    fields = logging.split()
    size = int(fields[-1])
    code = fields[-2]
    return code, size


def validate(logging):
    """
    Validates logging formatter
    """
    if len(logging.split()) < 7:
        return False
    
    else: 
        return True


def status_code(code):
    """
    Check if code entry is valid
    """
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    if status_code in valid_codes:
        return True
    
    else:
        return False


def printlogging(size, codes) -> None:
    """
    Prints out log files
    """
    sorted_codes = sorted(codes.items(), key=itemgetter(0))
    print('File size: {}'.format(size))
    for code_count in sorted_codes:
        keys = code_count[0]
        values = code_count[1]
        print("{}: {}".format(keys, values))


def logging_stats():
    """
    Reads logs from std in and prints out statistic
    on status code and file size
    """
    status_count = {}
    total_size = 0
    log_count = 0
    try:
        for log in sys.stdin:
            log_count += 1
            if not validate(log):
                continue
            status_code, file_size = parser(log)
            total_size += file_size
            if status_code(status_code):
                entry = {status_code:
                         status_count.get(status_code, 0) + 1}
                status_count.update(entry)
            if not log_count % 10:
                printlogging(total_size, status_count)
    except KeyboardInterrupt:
        printlogging(total_size, status_count)
    printlogging(total_size, status_count)


if __name__ == '__main__':
    logging_stats()