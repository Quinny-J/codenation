# Activities/Task 6
# For vs. While
# Write a program that prints numbers 1-10 in this console and do it with a for and then a while loop
# Q.1 > Which solution has the most lines of code? 
# Q.2 > Did either require variables; if so, why?
# Q.3 > Which solution is more useful and why

# A.1 > While loop has the most lines of code
# A.2 > A `for` loop uses a value such as `i` which is handled bny the loop construct itself
# Whereas a 'While' loop requires the variables to be initialized before it starts and to be incremented inside the loop.
# This is so we can control the loops execution and termination.
# A.3 > For this example a for loop is sufficient since we know we only have to display ten numbers and we know what they are
# Whereas using a while loop for this would just be criminal unless we had multiple conditions and iterations that we may not know beforehand
# Just another point in this example the for loop is quicker


# Using a for loop
# [Done] exited with code=0 in 0.133 seconds
for i in range(1, 11):
    print(i)

# Using a while loop
# [Done] exited with code=0 in 0.137 seconds
i = 1
while i <= 10:
    print(i)
    i += 1
