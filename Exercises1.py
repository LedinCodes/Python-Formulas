# Math exercises

# radius = float(input(f"Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius, 2)
# print(f"The circumference is {circumference}")
# print(f"The area of the circle is: {round(area, 2)}cm²")

## The section {round(area, 2)} indicates that the number will be rounded up to only two decimals. If the result is 3.141529..., it will be just 3.14

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print (f"Side C = {round(c, 2)}cm")


# Python calculator

# operator = input("Enter an operator (+ - * /): ")
#num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

#if operator == "+":
 #   result = num1 + num2
  #  print(round (result, 3))
#elif operator == "-":
 #   result =  num1 - num2
 #print(round (result, 3))
#elif operator == "*":
 #   result = num1 * num2
 #   print(round (result, 3))
#elif operator == "/":
 #   result = num1 / num2
  #  print(round (result, 3))
#else:
 #   print(f"{operator} is not valid.")


 # Weight converter

#weight = float(input("Enter your weight: "))
#unit = input("Kilograms or Pounds? (K or L): ").upper()

#if unit == "K":
#    weight = weight / 0.454
#    unit = "lbs"
#    print(f"Your weight is: {round(weight, 3)}{unit}")
#elif unit == "L":
#    weight = weight * 0.454
#    unit = "kg"
#    print(f"Your weight is: {round(weight, 3)}{unit}")
#else:
#    print(f"{unit} isn't valid")


# Temperature converter

# temperature = float(input("Enter the temperature here: "))
#unit1 = input("Introduce the unit you want to convert (F, C, K): ").upper()
#unit2 = input("Introduce the unit you want it converted to (F, C, K): ").upper()

#valid_units = ("F", "C", "K")
#if unit1 not in valid_units:
#    print(f"{unit1} isn't valid. Type another unit.")
#elif unit2 not in valid_units:
#    print(f"{unit2} isn't valid. Type another unit.")
# elif unit1 == unit2:
#    print(f"You put the same unit twice. Try a different unit in whichever variable")

#if unit1 == "F" and unit2 == "C":
#    temperature = (temperature - 32) * 5/9
#    unit = "C"
#    print(f"The conversion from Fahrenheit to Celsius is {round(temperature, 2)} {unit}")
#elif unit1 == "C" and unit2 == "F":
#    temperature = (temperature * 9/5) + 32
 #   unit = "F"
 #   print(f"The conversion from Celsius to Fahrenheit is {round(temperature, 2)} {unit}")
#elif unit1 == "F" and unit2 == "K":
 #   temperature = (temperature - 32) * 5/9 + 273.15
#    unit = "K"
#    print(f"The conversion from Fahrenheit to Kelvin is {round(temperature, 2)} {unit}")
#elif unit1 == "C" and unit2 == "K":
#    temperature = temperature + 273.15
#    unit = "K"
#    print(f"The conversion from Celsius to Kelvin is {round(temperature, 2)} {unit}")
#elif unit1 == "K" and unit2 == "F":
#    temperature = (temperature - 273.15) * 9/5 + 32
#    unit = "F"
#    print(f"The conversion from Kelvin to Fahrenheit is {round(temperature, 2)} {unit}")
#elif unit1 == "K" and unit2 == "C":
#    temperature = temperature - 273.15
 #   unit = "C"
#    print(f"The conversion from Kelvin to Celsius is {round(temperature, 2)} {unit}")


# Exercise: validate user input

# username = input("Enter a username: ")
#if not username.isalpha():
   #print("Sorry, this username is not valid. The username must not contain any numbers.")
#elif not username.find(" ") == -1:
 #   print("Sorry, this username is not valid. The username must not contain spaces.")
#elif len(username) > 12:
#    print("Sorry, this username is not valid. The username must not contain more than 12 characters.")
#else:
#    print(f"Welcome to this world, {username}!")


# Indexing exercises

# credit_number = "1234-5678-9012-3456"

# exercise 1: censoring the last digits
# last_digits = credit_number[-4:]
# print(f"**** **** **** {last_digits}")

# exercise 2: reversing the string
# credit_number = credit_number[::-1]
# print(credit_number)

# exercise 3:
#user = "not found"
#credit_num = input("Please, enter your credit card number here: ")
#if credit_num == "1234567890123456":
#    user = "John Smith"
#balance = "$367.09"
#remain_digits = credit_num[0:4:]
#
#if len(credit_num) < 16:
#    print("Sorry, this isn't a valid input. It must be 16 digits long.")
#elif len(credit_num) > 16:
#    print("Sorry, this isn't a valid input. It must be 16 digits long.")
#elif user == "not found" and len(credit_num) == 16:
#    print("Sorry, user not found.")
#else:
#    print(f"Hi, {user}, welcome to DCBanks. ")
#    print(f"{remain_digits} **** **** ****. ")
#    print()
#    print(f"Here is your balance: {balance}")


# Exam 2 hours accomplished YouTube tutorial: create a user profiling application

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
height_cm = int(input("Enter your height (in centimeters): "))
fav_prog_lang = input("What is your favourite programming language? ")
age_yr = 2026 - birth_year
age_mo = age_yr * 12
height_m = height_cm / 100
full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
password = input("Add a password: ")

first_letter_first_name = first_name[0]
first_letter_last_name = last_name[0]

if age_yr < 13:
    status = "Child"
elif 13 <= age_yr <= 17:
    status = "Teenager"
elif 18 <= age_yr <= 64:
    status = "Adult"
else:
    status = "Senior citizen"

if status == "Adult" and fav_prog_lang.lower() == "python":
    access_level = "Full access."
elif status in ["Teenager", "Adult"]:
    access_level = "Limited access."
else:
    access_level = "Basic access."

if len(password) < 8:
    password_status = "Weak"
elif len(password) < 12:
    if password.isalpha():
        password_status = "Weak"
    else:
        password_status = "Medium"
else:
    if password.isalpha():
        password_status = "Medium"
    else:
        password_status = "Strong"

print()
print("==========USER REPORT==========")
print()
print(f"Name: {full_name}")
print(f"Name length: {len(full_name)}")
print(f"Age: {age_yr}")
print(f"Age in months: {age_mo}")
print(f"Height: {height_m:.2f}m")
print(f"Favourite programming language: {fav_prog_lang.upper()}")
print(f"Password strength: {password_status}")
print()
print(f"First initial: {first_letter_first_name}")
print(f"Last initial: {first_letter_last_name}")
print()
print(f"Age group: {status}")
print(f"Access level: {access_level}")
print("================================")

input("Do you want to create another profile? (Y/N) ")
# last line is an open continuation to the next topic: while loops. I'll update next monday another two hours worth of exercises an forms
