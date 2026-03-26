age= 20
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")  

score = 80
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
else:
    print("Grade:F")

#single line comment
"""
this is a multiline comment """


print("Enter your name:")
name =input()
print("Hello,"+name+"! ")

print("enter your age:")

age =int(input())
if age>=18:
    print("You are an adult.")
else:
    print("You are not an adult yet.") 

 #loops 

for i in range(5):
    print(i)

#output: 0,1,2,3,4

for i in range(0,10 ,2):
    print(i)
#output: 0,2,4,6,8