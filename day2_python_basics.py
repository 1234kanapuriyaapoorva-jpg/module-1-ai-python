#print()
print ("Apoorva Kanapuriya") 
print("MCA")
print("I'm interested in AI/ML.")

#Variables
name = "apoorva"
education = "MCA" 
interest = "AI"
print(name +" "+ education+" "+interest )

name = 'APOORVA'
age = 10
percentage = 8.0
interest_in_ai = True

#print(name+" "+age+" "+percentage+" "+interest_in_ai)
#TypeError: can only concatenate str (not "int") to str

print(f'{name} {age} {percentage} {interest_in_ai}')
print(name,age,percentage,interest_in_ai)

#f-string (formatted) is a convenient way to put variables and expressions directly inside a string in Python.
print("my name is= "+name+" and my age is= " +str(age))
print(f"my name is {name} and my age is {age}")

#type()
print(type(name)) 
print(type(age)) 
print(type(interest)) 
print(type(percentage)) 
print(type(interest_in_ai))

#type conversion
age_str = str(age)
print(type(age_str))

x = "25"
y = int(x)
z = float(y)

print(type(x))
print(type(y))
print(type(z))

#Operators
#Arithmetic → +, -, *, /, %, //, **
#Comparison → >, <, >=, <=, ==, !=
#Logical → and, or, not
#Assignment → =, +=, -=, etc.

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b) #floor division
print(a**b) #exponentiation

a = 10
b = 10
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

a = 10
b = 20
print(a > 5 and b > 15)
print(a > 15 and b > 15)
print(a > 15 or b > 15)
print(not(a > 15))

age = 25
if age >= 18 and age <= 60: #if 18 <= age <=60:
    print(True)
else:
    print(False)    

#Program to classify a student's marks:
#90–100 → "A",75–89 → "B",60–74 → "C",Below 60 → "Needs Improvement"

marks = 95
if 100>= marks >= 90:
    print("A")
elif 90> marks >= 75:
    print("B")
elif 75> marks >= 60:
    print("C")
elif 0<= marks < 60:
    print("Needs Improvement")
else:
    print("invalid marks")  

#for loop
#Write a program that calculates:
#1 + 2 + 3 + ... + 10
a = 0
for i in range (0,11):
   a = i+a
print(a)   

#Calculate the sum of all even numbers from 1 to 100.    
x = 0
for i in range(1,101):
    if i % 2 == 0:
      x = i+x              #(x += i)
print(f"sum of all even numbers={x}")  

#Write a program that prints the multiplication table of 7:
for i in range (1,11):
    print(f"7 * {i} = {7*i}")

#while loop   
# Write a program that prints:1 2 3 4 5

i = 1
while i < 6:
    print(i)
    i += 1      

#Write a program that prints the numbers 10 down to 1: 10 9 ...1
i = 10
while i > 0:
    print(i)
    i -= 1

#create a function called greet that can accept a person's name.    
def greet(x):
    print(f"Hello! {x}")
     
greet("Apoorva")
greet("Divya")  

#here x is parameter & "Apoorva" and "Divya" are arguements

#Create a function called square that:1.accepts a number2.calculates its square3.returns the result

def square(x):
    return x*x
print(square(2))

def add(a,b):
     return a+b
print(add(10,20))

#list
#Create a list containing these 5 programming languages:Python,Java,C++,JavaScript,Go.


prog_lang=["Python", "Java", "C++", "JavaScript", "Go"]
print(prog_lang)
print(prog_lang[0:5:2])  #[start:stop:step]
print(prog_lang[0])
print(prog_lang[2])
print(prog_lang[4])
 
#List + for loop
for language in prog_lang:
  print (language)

prog_lang.append("javaScript")
print(prog_lang)

#find:1.The largest number,2.The smallest number3.The sum of all numbers
numbers1 = [10, 25, 7, 42, 18] 
print(max(numbers1))
print(min(numbers1))
print(sum(numbers1))

#Write a program that uses a loop to count how many numbers are even.
numbers2 = [10, 15, 22, 7, 30, 9, 18]
count = 0
for number in numbers2:
    if number % 2 == 0:
        count += 1
print(f"total even numbers are {count}")        