#Write a program print 100 blank lines on your screen.
''
'''
print("\n"*100)
'''
#Write a program to enter your name and display your name 10 no of times.
''
'''
name = "anjali kumari"
for i in range(10):
    print(name)
'''
#Write a Python program to print poem.
''
'''
print("Twinkle,Twinkle,little star\n"
      "\tHow i wonder what you are.\n"
      "\t\tup above also high,\n"
      "\tlike ke dimond in the sky.\n"
      "\tTwinkle,Twinkle little star.\n"
      "\tHow i wonder what you are.")
'''
#Write a program to print  no. Of days of Month.
''
'''
month = input("enter month")
if month =="january":
    print('no of day of "january" is 31')
elif month =="february":
    print('no of day of "february" is 28')
elif month =="march":
    print('no of day of"march"is 31')
elif month =="april":
    print('no of day of "april"is 30')
elif month =="may":
    print('no of day of"may" is 31')
elif month =="june":
    print('no of day of "june" is 30')
elif month =="july":
    print('no of day of "july"is 31')
elif month =="august":
    print('no of day of "august" is 31')
elif month =="september":
    print('no of day of "september" is 30')
elif month =="october":
    print('no of day of "october" is 31')
elif month =="november":
    print('no of day of "november" is 30')
elif month =="december":
    print('no of day of "december" is 31')
else:
    print("invaild no of month")
'''
#Write a Program to check a character whether a character is Vowel or not.
''
'''
ch =input("enter a character:")
ch = ch.lower()
if ch in('a','e','i','o','u'):
    print(f"{ch} is a vowel.")
elif ch.isalpha():
    print(f"{ch} is a consonant.")
else:
    print("invalid input.please enter an alphabet character.")
'''
#Write a program to find biggest of given Two numbers from the Keyboard.
''
'''
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if num1 > num2:
    print(f"{num1} is the biggest number")
elif num2 > num1:
    print(f"{num2} is the biggest number")
else:
    print("find the biggest number{num1}{num2}")
'''
#Write a program to find biggest of given Three numbers from the Keyboard.
''
'''
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
if num1 > num2 :
    print(f"{num2}is the biggest number")
elif num2 > num3:
    print(f"{num3} is the biggest number")
else:
    print(f"{num3} is the biggest number")
'''
#Write a program to check whether the given number is between 1 and 100 or not.
''
'''
num = int(input("enter a number"))
if 1<=num<=100:
    print(f"{num} is between 1 and 100")
else:
    print(f"{num} NOT BETWEEN 1 AND 100")
'''
#Perform the following on the given string and interpret the output by writing a comment.
''
'''
str= "Python is Easy"
print(str)
print(str[0])
print(str[::-1])
print(str[:])
print(str[-3])
print(str[3:9])
print(str[:5])
print(str*2)
'''
# Print the following:
''
'''
print("Ram’s wife is Seeta in single quote Ram is also known as\n"
"\t“Maryada Purushottam” in double quote ")
'''
# Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
''
'''
physisc = float(input("enter physisc marks"))
chemistry = float(input("enter chemistry marks"))
biology = float(input("enter biology marks"))
mathematic = float(input("enter mathematic marks"))
computer = float(input("enter computer marks"))
total_marks = physisc + chemistry + biology + mathematic + computer
percentage = (total_marks/500)*100
if percentage >= 90:
    grade = "gradeA"
elif percentage >=80:
    grade = "gradeB"
elif percentage >=70:
    grade = "gradeC"
elif percentage >=60:
    grade = "gradeD"
elif percentage >= 50:
    grade = "gradeE"
elif percentage >=40:
    grade = "gradeE"
else:
    grade = "gradeF"
print(f"percentage:{percentage:.2f}%")
print(f"grade:{grade}")
'''
#Write a program to input basic salary of an employee and calculate its Gross salary according to following:
''
'''
basic_salary = float(input("enter the basic salary of the empolly:"))
if basic_Salary <= 10000 :
    har= basic_salary*0.25
    da= basic_salary*0.80
elif basic_Salary <= 20000 :
        har = basic_salary*0.25
        da= basic_salary*0.90
else:
     hra = basic_salary * 0.30
     da = basic_salary*0.95
gross_salary = basic_salary +hra+da
print(f"basic salary:{basic_salary:.2f}")
print(f"HRA basic_salary:{hra:.2f}")
print(f"DA basic_salary:{da:.2f}")
print(f"Gross salary:{gross_salary:.2f}")
'''
#Write a program to input week number and print week day.
''
'''
week_number = int(input("enter week number (1-7): "))
if week_day =="monday":
    print("week number is 1")
elif week_day =="tuesday":
    print("week number is 2")
elif week_day =="wednesday":
    print("week number is 3")
elif week_day =="thursday":
    print("week number is 4")
elif week_day =="friday":
    print("week number is 5")
elif week_day =="saturday":
    print("week number is 6")
elif week_day =="sunday":
    print("week number is 7")
else:
    print("Invalid day name!please enter a valid week_day")
'''
#Write a program to count total number of notes in given amount.
''
'''
amount = int(input("enter the total  amount:"))
notes = [500,200,100]
print("total number of notes:")
if amount >= 500:
         note500 = amount//500
         amount = amount % 500
         print(f"rs.500:{notes500}")
elif amount >=200:
    note200 =amount//200
    amount = amount%200
    print(f"rs.200:{notes200}")
elif amount >=100:
    note100 = amount//100
    amount = amount %100
    print(f"rs.100:{note100}")
'''
