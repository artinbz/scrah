number = input("Enter Number: ")
counter = 0
numbers = []
s = 0 
while number != '0':
    if number.isdigit():
        number.append(number) 
         counter += 1
     number = input("enter number: ")
for i in numbers:
    s = s + int(n)
print(number)
print(s)
print(f"you entered {counter} numbers.")



