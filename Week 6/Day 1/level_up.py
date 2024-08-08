music = "classical"
shopping_list = []
num = 0
name = ""
my_name = "Josh"

print("Variable | (Value) | BOOL")
print(f"Music : ({music}) : {bool(music)}")
print(f"Shopping List: ({shopping_list}) : {bool(shopping_list)}")
print(f"Num : ({num}) : {bool(num)}")
print(f"Name: ({name}) : {bool(name)}")
print(f"My Name: ({my_name}) : {bool(my_name)}")

u_name = input("Please enter your name to complete our sign up process.")

# if u_name==True:
#     print(f"Thanks for signing up {u_name}")
# else:
#     print("You did not supply a name!")

# if u_name==my_name:
#     print(f"Thanks for signing up {u_name}")
# else:
#     print("You did not supply a name!")

if u_name:
    print(f"Thanks for signing up {u_name}")
else:
    print("You did not supply a name!")