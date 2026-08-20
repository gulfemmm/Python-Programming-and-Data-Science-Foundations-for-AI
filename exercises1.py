person = {"name":"Alice","age":25,"grade":"A"}
print(person)

#add new key value pair
person["address"] = "Ankara"
#update age
person["age"] = 32
#remove grade
if "grade" in person:
    del person["grade"]

print(person)    