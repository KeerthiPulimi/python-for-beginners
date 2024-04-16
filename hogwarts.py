students = [
  {"name": "Hermoine", "house": "Griff", "patronus": "otter"},
  {"name": "Harry", "house": "Griff", "patronus": "stag"},
  {"name": "Roon", "house": "Griff", "patronus": "otter"},
  {"name": "Draco", "house": "Sly", "patronus": None}
]

# Correcting the loop to iterate over each student in the students list
for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")
