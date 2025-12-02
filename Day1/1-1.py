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
      pos = (pos + distance) % 100
    elif direction == 'L':
      pos = (pos - distance) % 100
    if pos == 0:
      times_at_zero += 1
    
  print('The number of times the combination lock landed on zero is:', times_at_zero)

main()