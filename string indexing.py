# indexing = accessing elements of a sequence using [] (indexing operators)
#                   [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])

# in [0:4], the 4 is exclusive, meaning, the 4 is not counted. The 0 digit is the first, so: 1234 is counted

# print(credit_number[5:9])

# if you put a number, a colon and then nothing, the system assumes you need from the number up until the last digit
# print(credit_number[5:])

# if you put a negative number on the brackets, it´ll show the position starting from the end and going backwards
# print(credit_number[-1])

# the step section is to skip over other numbers in any sequence. If you put 2 for example, it'll show you the second number
# print(credit_number[::2])

