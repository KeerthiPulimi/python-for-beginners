import sys

# try:
#   print("hello, my name is",sys.argv[1])

# except IndexError:
#   print("too few arguments") 

if len(sys.argv)<2:
  sys.exit("Too few arguments")
elif len(sys.argv)>2:
  sys.exit("Too many arguments") 
else:
  print("hello, my anme is", sys.argv[1])     