# Task 1
# Make a list of 3 fav websites and add another two using a method and finally remove the last one 

# Create an array to store my strings
fav_website = [
    "google.com",
    "github.com",
    "telnet.live"
]

# print my string
print(fav_website)

# add two sites to my list
fav_website.extend(["docs.python.org","github.com/Quinny-J"])
# You can also do it this way using append
# fav_website.append("docs.python.org") # 
# fav_website.append("github.com/Quinny-J")

# print the updated string
print(fav_website)

# Remove the last item added
fav_website.pop()

# print the updated string
print(fav_website)