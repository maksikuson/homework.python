#Part 1 

#Task 1

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
choose = input("Select an operation (enter 'sum' or 'product'): ")
if choose == 'sum':
    result = num1 + num2 + num3
elif choose == 'product':
    result = num1 * num2 * num3
else:
    print("Wrong choose selection. Please enter 'sum' or 'product'.")
if choose in ['sum', 'product']:
    print(f"The result of the {choose} of three numbers:{result}")

#Task 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
choose = input("Choose an operation (enter 'maximum', 'minimum' or 'average'): ")
if choose == 'maximum':
    result = max(num1,num2,num3)
    print(f"Maximum of three numbers: {result}")
elif choose == 'minimum':
    result = min(num1,num2,num3)
    print(f"Minimum of three numbers: {result}")
elif choose == 'averege':
    result = averege(num1,num2,num3)
    print(f"Averege of three numbers: {result}")
else:
    print("Invalid operation selection. Please enter 'maximum', 'minimum' or 'average'.")