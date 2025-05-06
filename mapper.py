#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
# Skip header and find the “Attack Type” column index
header = next(reader)
attack_idx = header.index("attack_type")

for row in reader:
    if len(row) <= attack_idx:
        continue
    attack = row[attack_idx].strip()
    if attack:
        # emit each attack type with count 1
        print(f"{attack}\t1")

