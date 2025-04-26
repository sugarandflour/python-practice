def reverse_string(s):

#create an empty string
  reversed_string = ""

# loop through each character in the string add the current character to the front of the reversed string
  for char in s:
    reversed_string = char + reversed_string

  # return the new reversed string
  return reversed_string
