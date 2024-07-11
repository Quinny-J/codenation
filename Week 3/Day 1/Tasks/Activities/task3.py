# Activities/Task 3
# Write a program that uses a while loop to countdown from 10 and after one print blast off
# Also include "Countdown Initiated, Prepare for blast off".

# Let the user know we have started the countdown
print("Countdown Initiated, Prepare for blast off !")

# Countdown from 10 to 1
count = 10
# loop if the count is greater than 0 then print our count if not print our blast of message 
while count > 0:
    print(count)
    # since were going down we need to take away from the count
    count -= 1

# Blast off message
print("Blast off!")
