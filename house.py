name = input("what is your name?")

# if name == "Harry" or "Ron" or "Hermoine":
#   print("Griffindor")
# elif name == "Draco":
#   print("Slytherin") 
# else:
#   print("who")

match name:
  case "harry" | "Ron" | "Hermoine":
    print("griff")
  case "Draco":
    print("slytherin")
  case _:
    print("who")    

       
   