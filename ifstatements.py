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

count = 1
while count < 100:
    print(count)
    count += 1

count =100 
while count >0:
    print(count)
    count -= 1

i =1 
n=3
while i<= 10:
    print (n*i)
    i +=1


nums = [1,2,3,4,5,6,100,11,1,109]
idx =0
while idx < len(nums):
    print(nums[idx])
    idx +=1