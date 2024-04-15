#Ask user for their name
name= input("what is ypur name?")

#say hello to user 
print("hello,", name)

#some other ways - here this strip removes any spaces that user has given while writting the name
name = name.strip()
print(f"hello, {name}")
