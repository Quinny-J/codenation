#
# Task 1
# Create a var called password and check how many letters and if it has min 8

passwords = ["advg", "acbredgyrw"]

# You could swap this for a input so you can check users passsword but instead lets check a few passwords
for i in passwords:
    # Check min length of 8
    if len(i) >= 8:
        # Print result
        print(f"{i} is a great password")
    else:
        # Print result
        print(f"{i} is too short to be a password")

# Im just using the 2nd password as a vaiable
    # Check min length of 8
    if len(passwords[1]) >= 8:
        # Print result
        print(f"{i} is a great password")
    else:
        # Print result
        print(f"{i} is too short to be a password")