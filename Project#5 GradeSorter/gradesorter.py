a=[]
c=[]
b=1
#Getting Grades from the user
for i in range(5):
    val=int(input("Enter grade " + str(b) +"(0-100):"))
    b=int(b)+1
    a.append(val)
    c.append(val)
#Displaying the Grades
print("Your Grades are :" + str(a))

#Displaying the Grades from high to low
a.sort(reverse=True)
print("Your Grades from Highest to Lowest are: " + str(a))
print()
#Removing Lowest 2 Grades
print("Removing Lowest 2 Grades")
RGrade=a.pop()
print("Removed Grade: " +str(RGrade))
RGrade=a.pop()
print("Removed Grade: " +str(RGrade))

#displaying Highest grade
print()
print("Your Highest Grades are" + str(a))
print("Your Highest Grade is " + str(a[0]))

value=0
for i in range(5):
    value=value+c[i]
print()
print(" Your Total is :" + str(value))
per=value/5
print()
print("Your Total Percentage is :" + str(per))
