#!/usr/bin/env python3

invalidIDs = 0

with open('input.txt', 'r') as f:
    line = f.readline()
    for idRange in line.split(','):
        splitID = idRange.split('-')
        firstID = int(splitID[0])
        lastID = int(splitID[1])

        for ID in range(firstID, lastID+1):
            number = ''
            for i, digit in enumerate(str(ID)):
                number += digit
                if number == str(ID)[i+1:]:
                    print(f"Found invalid ID: {ID}")
                    invalidIDs += ID
                    break

print(f'Sum of all invalid IDs: {invalidIDs}')