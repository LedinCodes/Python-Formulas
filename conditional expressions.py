# Formula for conditional expressions:
# (message) if (variable1) else (variable2)

# Function: print or assign one of two values based on a condition

# example:
# number = float(input("Enter a number: "))
# print("Is positive" if number > 0 else "Is negative")
# print("Is even" if number % 2 == 0 else "Is odd")

num = 5
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)