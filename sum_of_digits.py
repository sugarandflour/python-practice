def sum_of_digits(y):

# initialize a variable to store the sum of the digits
  total = 0  

# loop while y is greater than 0
    while y > 0:  

# get the last digit of the number
        digit = y % 10  

# Add it to total
        total += digit  

# Remove the last digit from y
        y //= 10  

# Return the sum of digits
    return total  
