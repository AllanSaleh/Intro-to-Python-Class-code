# if-else statement is a way for your program to make decisions
# if condition:
#   Do something
# else:
#   do something else

print("=== Simple Calculator ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = int(input("Choose operation (1-5):\n"))
if choice < 1 or choice > 5:
  print("Invalid choice")
  exit()
  
num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))

if choice == 1:
  result = num1 + num2
  print(f"{num1} + {num2} = {result}")
elif choice == 2:
  result = num1 - num2
  print(f"{num1} - {num2} = {result}")
elif choice == 3:
  result = num1 * num2
  print(f"{num1} * {num2} = {result}")
elif choice == 4:
  if num2 == 0:
    print("Error: Cannot divide by Zero!")
  else:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif choice == 5:
  result = num1 ** num2
  print(f"{num1} to the power of {num2} = {result}")
else:
  print("Invalid Choice!")