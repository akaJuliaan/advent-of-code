#!/usr/bin/env python3

joltage = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        first = max(line)
        index = line.find(first)
        if (index + 2) == len(line):
            second = first
            first = max(line[:index])
        else:
            second = max(line[index+1:])

        joltage += int(first)*10 + int(second)
        
print(f"Sum of max joltage {joltage}")