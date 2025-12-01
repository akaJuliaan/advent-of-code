#!/usr/bin/env python3
counter = 0
dial = 50
dial_before = dial
with open('input.txt', 'r') as file:
   for ln in file:
      line = ln.strip()
      val = int(line[1:])
      counter += int(val / 100)
      
      if line.startswith("L"):
         dial -= val % 100
      else:
         dial += val % 100

      if dial >= 100:
         dial -= 100
         counter += 1
      elif dial < 0:
         dial += 100
         if dial_before != 0:
            counter += 1
      elif dial == 0:
         counter += 1

      dial_before = dial
      print(val)     

print(f"Pos: {dial}")
print(f"Counter: {counter}")