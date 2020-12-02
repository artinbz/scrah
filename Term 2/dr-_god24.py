number = input("Enter Number: ")
counter = 0
number = []
s = 0 
while number != '0':
    if number.isdigit():
        number.append(number) 
    number = input("enter number: ")
    counter += 1
for i in number:
    s = s + int(n)
print(number)
print(s)
print(f"you entered {counter} numbers.")



