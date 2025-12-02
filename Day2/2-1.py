def main():
  
  with open('input.txt') as file:
    product_ranges = [[int(x) for x in item.split('-')] for item in file.read().strip().split(',')]

  print(product_ranges)

main()