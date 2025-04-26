def factorial_loop(y):

# create a variable result and intitialize it to 1
  result = 1

# create a loop to multiply the number incrementally from 1 to y by the value stored in result
  for i in range(1, y + 1):
    result = result * i
    
  return result
