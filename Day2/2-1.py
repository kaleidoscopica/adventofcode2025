def main():
  product_ids = []
  
  with open('input.txt') as file:
    product_ids = [line.strip().split(',') for line in file]

  print(product_ids)

main()