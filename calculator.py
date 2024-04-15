#add numbers 
x= int(input("whats the value of x?"))
y= int(input("whats the value of y?"))
print(x+y)

#doing float additions
x1= float(input("whats the value of x?"))
y= float(input("whats the value of y?"))
z = round(x+y)
print(z)
print(f"{z:,}")

z=x/y
print(f"{z:.2f}")

# square of number 
def main():
  x=int(input("what is x?"))
  print("x squared is", square(x))

def square(n):
  a=n*n
  return a 
main()