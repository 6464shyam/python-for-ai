age =25
Name ="John"
has_passed = True
list = [Name,age,25.5,has_passed]


 
print(list[0])

list.append("john")
print(list)

list.insert(2,"Smith")
print(list)

list.remove(25.5)
print(list)

print("checking")

if "sam" in list :
    print("sam is in the list")
else:    print("sam is not in the list")