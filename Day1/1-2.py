import time

def main():

  rotations = []
  
  with open('input.txt') as file:
    rotations = [line.strip() for line in file]

  pos = 50
  times_at_zero = 0
  
  for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    if direction == 'R':
      pos = pos + distance
      while pos >= 100:
        pos -= 100
        times_at_zero += 1
    elif direction == 'L':
      if pos == 0: 
        pos = pos + 100 - distance
      else:
        pos = pos - distance
      while pos < 0:
        pos += 100
        times_at_zero += 1
      # Account for ending on 0
      if pos == 0:
        times_at_zero += 1
  
  print('The number of times the combination lock hit zero, across any rotation, is:', times_at_zero)

main()