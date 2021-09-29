num=int(input("Enter The length of the list:"))
l=[]
print("Enter the numbers to the list:")
for i in range(num):
    c=int(input())
    l.append(c)
str=input("Enter the string or symbol to appear:")
for i in l:
    print(str*i)