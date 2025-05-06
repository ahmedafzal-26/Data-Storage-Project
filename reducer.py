#!/usr/bin/env python3
import sys

current_attack = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    attack, val = line.split("\t", 1)
    try:
        val = int(val)
    except ValueError:
        continue

    if current_attack == attack:
        count += val
    else:
        if current_attack is not None:
            # output the total for the previous attack type
            print(f"{current_attack}\t{count}")
        current_attack = attack
        count = val

# don't forget the last key
if current_attack is not None:
    print(f"{current_attack}\t{count}")

