# Student Grade Calculator
# Module 2 - Python Mini Project

# taking student/subject information
name = input("Enter Student Name = ")
subjects = []
marks = []
for i in range(1,6):
  subject = input(f"Enter Subject {i} name = ")
  subjects.append(subject)
  while True:
   try:
    mark = int(input(f"Enter marks of subject {i} = "))
    # validating marks
    if mark<0 or mark>100:
      print("invalid marks")
      continue
    marks.append(mark)
    break
   except ValueError:
     print("Enter a number : ")


total = sum(marks)
average = total/5
percentage = (total/500)*100

# calculating the result
print("\n\n----- STUDENT RESULT -----\n")
print("Student Name = ",name,"\n")
for subject, mark in zip(subjects,marks):
   print(f"{subject} : {mark}")
print("\nTotal Marks Scored = ",total)
print("Average = ", average)
print("Percentage = ",percentage,"%")

# assigning the grade
if 90 <= percentage<= 100:
   print("Grade = A")
elif 75 <= percentage <90:
    print("Grade = B")
elif 60 <= percentage <75:
    print("Grade = C")
else:
    print("Grade = D")    

