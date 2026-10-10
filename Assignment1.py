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
