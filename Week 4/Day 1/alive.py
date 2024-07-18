# alive.py
# Create a program which calculates how many days you've been alive for.
# Hints: Look into the datetime library, and don't use input! in python

# Import datetime and colorama for a bit of flair
from colorama import Fore
from datetime import datetime

# Define our birthday using a datetime object
birthday = datetime(year=2002, month=11, day=26)

# Define the date/time now to be compared with later
current_date = datetime.now()

# Define our days_alive var and provide it with the subtracted dates
# .days - Will return the days you can also grab the milliseconds and so on
days_alive = (current_date - birthday).days

# Print the result
print(f"[{Fore.CYAN}i{Fore.WHITE}] You have been alive for {Fore.YELLOW}{days_alive}{Fore.WHITE} days.")