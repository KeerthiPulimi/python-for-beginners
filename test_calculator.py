from calculator import square
def test_postive():
  assert square(2) ==4
  assert square(3) ==9

def test_negavite():  
  assert square(-2) ==4
  
  assert square(-3) ==9

def test_zero():  
  assert square(0) == 0

# def main():
#   test_square()


# def test_square():
#   try:
#     assert square(2) == 4
#   except AssertionError:
#     print("2 auared wa not 4")
  
  
#   try:
#     assert square(3) == 9
#   except AssertionError:

#     print("3 squared was notb9")  


# def test_square():
#   if square(2) != 4:
#     print("2 squared was not 4")
#   if square(3) != 9:
#     print("3 squared is not 9")

# if __name__ == "__main__":
#   main()

    
