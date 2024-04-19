import sys

# try:
#   print("hello, my name is",sys.argv[1])

# except IndexError:
#   print("too few arguments") 

if len(sys.argv)<2:
  print("Too few arguments")
elif len(sys.argv)>2:
  print("Too many arguments") 
else:
  print("hello, my anme is", sys.argv[1])   