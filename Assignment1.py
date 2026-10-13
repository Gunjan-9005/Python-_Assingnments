#1.Check if a number is positive, negative, or zero.

# num=float(input("Enter the number:"))

# if num>0:
#     print("number is positive")
# elif num<0:
#     print(" number is negative")
# else:
#     print("number is zero")

#2. check whether a number is even or odd
# num=int(input("Enter the number:"))

# if num%2 ==0:
#     print("number is even")
# else:
#     print("number is odd")

#3.Find the greater of two numbers.
# a= int(input("Enter the first number:"))
# b= int(input("Enter the second number:"))
# if a>b:
#     print("first no.is greater")
# else:
#     print("Second no.is greater")

#4.Find thegreatest of three numbers
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if a>b and a>c:
#     print("first no.is greater")
# elif b>a and b>c:
#     print("second no.is greater")
# else:
#     print("third no.is greater")


#5.Check if a person is eligible to vote (age ≥ 18).
# age=int(input("Enter yor age:"))

# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

#6.Check whether a year is a leap year.
# year = int(input("Enter year: "))

# if year % 400 == 0:
#     print("Leap year")

# elif year % 100 == 0:
#     print("Not a leap year")

# elif year % 4 == 0:
#     print("Leap year")

# else:
#     print("Not a leap year")

#7.Check if a character is a vowel or consonant.
char = input("enter the character:")

if char in ('a', 'e', 'i', 'o', 'u'):
    print(char,"is vowel")
else:
    print(char,"is consonant")



# 1. Check whether a number is divisible by 5 and 11
num = int(input("1. Enter number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")


# 2. Check if a number is a multiple of both 3 and 7
num = int(input("\n2. Enter number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# 3. Assign grades based on marks
marks = int(input("\n3. Enter marks: "))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
elif marks < 60:
    print("Grade F")
else:
    print("Invalid marks")


# 4. Check if a character is uppercase or lowercase
ch = input("\n4. Enter a character: ")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
else:
    print("Not an alphabet")


# 5. Check whether alphabet is a vowel using if-elif
ch = input("\n5. Enter an alphabet: ")
if ch == 'a' or ch == 'A':
    print("Vowel")
elif ch == 'e' or ch == 'E':
    print("Vowel")
elif ch == 'i' or ch == 'I':
    print("Vowel")
elif ch == 'o' or ch == 'O':
    print("Vowel")
elif ch == 'u' or ch == 'U':
    print("Vowel")
else:
    print("Consonant")


# 6. Check if three sides can form a triangle
a = float(input("\n6. Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    print("Can form a triangle")
else:
    print("Cannot form a triangle")


# 7. Determine type of triangle
a = float(input("\n7. Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 8. Find largest among four numbers
a = int(input("\n8. Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
print("Largest:", largest)


# 9. Check whether a number is a three-digit number
num = int(input("\n9. Enter number: "))
if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 10. Calculate electricity bill using slab rates
units = int(input("\n10. Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print("Electricity Bill: Rs.", bill)


# 11. Calculate income tax based on income slabs
income = float(input("\n11. Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 250000 * 0.05 + (income - 500000) * 0.20
else:
    tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
print("Income Tax: Rs.", tax)


# 12. Check if a student passes
m1 = int(input("\n12. Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student Passes")
else:
    print("Student Fails")


# 13. Check whether a number is within a given range
num = int(input("\n13. Enter number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
if low <= num <= high:
    print("Number is within range")
else:
    print("Number is outside range")


# 14. Simple calculator using if-elif-else
a = float(input("\n14. Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 15. Check whether a year is a century leap year
year = int(input("\n15. Enter year: "))
if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
else:
    print("Not a century leap year")


# 16. Determine season based on month number
month = int(input("\n16. Enter month number: "))
if month in [3, 4, 5]:
    print("Summer")
elif month in [6, 7, 8, 9]:
    print("Monsoon")
elif month in [10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")
else:
    print("Invalid month")


# 17. Find number of days in a month
month = int(input("\n17. Enter month number: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month")


# 18. Check password minimum conditions
password = input("\n18. Enter password: ")
has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Valid password")
else:
    print("Invalid password")


# 19. Determine ticket price based on age
age = int(input("\n19. Enter age: "))
if age < 5:
    print("Ticket: Free")
elif age <= 12:
    print("Ticket: Rs. 50")
elif age <= 59:
    print("Ticket: Rs. 100")
else:
    print("Ticket: Rs. 70")


# 20. Calculate discount based on purchase amount
amount = float(input("\n20. Enter purchase amount: "))
if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.10
elif amount < 10000:
    discount = amount * 0.20
else:
    discount = amount * 0.30

print("Discount: Rs.", discount)
print("Final Amount: Rs.", amount - discount)


# 21. Driving license eligibility
age = int(input("\n21. Enter age: "))
eyesight = input("Meet eyesight requirement? (yes/no): ")
if age >= 18 and eyesight.lower() == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible")


# 22. Login system
username = input("\n22. Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")


# 23. Menu-driven calculator
while True:
    print("\n MENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Program ended")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

