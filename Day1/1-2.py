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
    print()
    print('Rotation:', rotation)
    if direction == 'R':
      print('Position before starting is', pos)
      print('Going R for', distance, 'clicks to position', pos+distance)
      pos = pos + distance
      while pos >= 100:
        print('Position greater than 100; calculating times past 0...')
        pos -= 100
        times_at_zero += 1
      print('Times past zero is now:', times_at_zero)
    elif direction == 'L':
      print('Position before starting is', pos)
      print('Going L for', distance, 'clicks to position', pos-distance)
      pos = pos - distance
      while pos <= -1:
        print('Position less than 0; calculating times past 0...')
        pos += 100
        times_at_zero += 1
      print('Times past zero is now:', times_at_zero)
      # Account for ending on 0
      if pos == 0:
        times_at_zero += 1
        print('Ended at zero. Times past zero is now:', times_at_zero)
    #time.sleep(2)
  
  print()
  print('The number of times the combination lock hit zero, across any rotation, is:', times_at_zero)

main()