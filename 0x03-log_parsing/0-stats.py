#!/usr/bin/python3
'''
a script that reads stdin line by line and computes metrics
'''
import sys
import re


if __name__ == "__main__":
    total_size = 0
    code_count = {"200": 0, "301": 0, "400": 0,
                  "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            for i in range(10):
                data = sys.stdin.readline()
                if not data:
                    break
                info = str(data).replace('"', "")
                info = info.replace("\n", "")
                log_data = info.split(" ")
                if len(log_data) == 9 and \
                   log_data[-1].isdigit() \
                   and log_data[-2].isdigit()\
                   and log_data[-2] in code_count:
                    file_size = int(log_data[-1])
                    total_size += file_size
                    code_count[log_data[-2]] += 1
                else:
                    i -= 1
            print("File size: {}".format(total_size))
            for code in code_count:
                if code_count[code] > 0:
                    print("{}: {}".format(code, code_count[code]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in code_count:
            if code_count[code] > 0:
                print("{}: {}".format(code, code_count[code]))
