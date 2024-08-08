print("Type in two numbers to multiply them")

while True:
    try:
        num1 = int(input(">>"))
        num2 = int(input(">>"))
        break
    except ValueError:
        print("Please try again using numbers only!")
    except KeyboardInterrupt:   
        continue

print(num1*num2)


# num1 = int(input(">>"))
# num2 = int(input(">>"))
# print(num1*num2)