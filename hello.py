#Ask user for their name
#name= input("what is ypur name?")...

#say hello to user 
#print("hello,", name)

#some other ways - here this strip removes any spaces that user has given while writting the name from front and back
#name = name.strip()
#print(f"hello, {name}")
 
 #still the names first letter is small but to make it capital we use this
#name = name.capitalize()
#print(f"hello, {name}")

# the capitalize works on;y when u give one name but if you give 2 naes and want to amek both the first letters of the name capital its better that we use title

#name = name.title()
#print(f"hello, {name}")  


def hello(to):
   print("hello,",to)

name1=input("what is your name?")
hello(name1)

  
  