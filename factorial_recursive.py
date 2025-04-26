def factorial_recursive(y):

# check whether y is equal to 0 or 1
  if y == 0 or y == 1:

# establish as the base case since factorial of 0 or 1 is 1
    return 1
    
  else:
    
# and the recursive case to multiply y by y-1 until it is equal to 1
    return y * factorial_recursive(y-1)
