#Write a program to:
#1.Print the largest number
#2.Print the smallest number
#3.Calculate the total
#4.Calculate the average
#5.Count how many numbers are even

numbers = [12, 7, 20, 5, 18]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

count = 0  
for number in numbers:
    if number % 2 == 0: 
     count += 1 
print("total even numbers=",count)

print("Average =",(sum(numbers)/len(numbers)))   