#!/usr/bin/env python3
counter = 0
dial = 50

with open('input.txt', 'r') as file:
   for ln in file:
      line = ln.strip()
      val = int(line[1:]) % 100
      if line.startswith("L"):
         dial -= val
      else:
         dial += val

      if dial >= 100:
         dial -= 100
      elif dial < 0:
         dial += 100
         
      if dial == 0:
         counter += 1

print(f"Pos: {dial}")
print(f"Counter: {counter}")