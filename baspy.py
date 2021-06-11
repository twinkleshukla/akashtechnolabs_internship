n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

#evem or odd
num = int(input("Enter a number to find even or odd: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  

#leap year
year = int(input("Enter a year to check leap year or not: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  

#number is -ve,0,+ve
num = float(input("Enter a number  to check whether number is -VE 0 +VE: "))  
  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num))   

#greatest nd equal number
a = float(input(" Please Enter the First Value to find greatest nummber a: "))
b = float(input(" Please Enter the Second Value to find greatest nummber b: "))

if(a > b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")

#factorial
num = int(input("Enter a number to find factorial: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    

#swapping od two vars using 3rd var



# Python program to swap two variables

num1 = input('Enter First Number for swapping: ')
num2 = input('Enter Second Number for swapping: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)

#finding smallest value
num1=int(input("Enter your first number to find smallest number:"))
num2=int(input("Enter your second number to find smallest number: "))
if(num1<num2):
    print("{} is smallest".format(num1))
elif(num2<num1):
    print("{} is smallest".format(num2))
else:
    print("{} and {} are equal".format(num1,num2))

#swapping without using third var
x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

