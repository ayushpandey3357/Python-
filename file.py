# Q1

'''file = open("Student.txt","r")
data = file.read()
print(data)
file.close() '''

# Q2

'''file = open("Student.txt","r")
data = file.readline()
print(data)
file.close()'''

#Q3
'''file=open("Student.txt","r")
data=file.readline()
print(data)
file.close()'''

#Q4

'''file = open("Student.txt","r")
data = file.readlines()
for i in data:
    print(i)
file.close()'''

#Q5
'''file = open("Student.txt","r")
data = file.readlines()
count = 0
for i in data:
    print(i)
    count+=1
print(count)
file.close()'''

#Q6

# Write data
"""with open("Student.txt", "w") as file:
    file.write("donald,69,USA")
    file.write("shehbazz,420,paxstan")

# Read data
with open("Student.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i)"""


# Q7
'''file = open("Student.txt", "w") as file:
    file.write("donald,69,USA")
    file.write("shehbazz,420,paxstan")

# Read data
with open("Student.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i)'''


# Q8
'''file = open("Student.txt","a")
file.write("Karan,23,pune")
data = file.readlines()
for i in data:
    print(i)
file.close()'''


