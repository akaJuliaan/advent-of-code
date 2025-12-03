#!/usr/bin/env python3

joltage = 0
digits = 12

with open('input.txt', 'r') as f:
    for ln in f.readlines():
        line = ln.strip()
        lineJoltage = 0
        foundDigits = 0
        
        first = max(line)
        while foundDigits < digits:
            index = line.find(first)
            
            if len(line[index+1:]) >= digits - foundDigits - 1:
                foundDigits += 1
                lineJoltage += int(first) * 10 ** (digits - foundDigits)
                line = line[index+1:]
                if len(line) > 0:
                    first = max(line)
            else:
                first = max([x for x in line if x < first])
        joltage += lineJoltage

print(f"Sum of max joltage {joltage}")