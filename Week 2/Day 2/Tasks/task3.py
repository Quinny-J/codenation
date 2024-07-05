# Task 3
# Demonstrate several different methods

# Initial list
fav_website = [
    "google.com",
    "github.com",
    "telnet.live",
    "github.com"
]
# Display our original favorite websites
print(fav_website)
# this will remove telnet.live from our list
fav_website.remove("telnet.live") 
# Display our updated favorite websites
print(fav_website)

# This will reverse the order of our favorite websites
fav_website.reverse()
# Display our updated favorite websites
print(fav_website)

# This will sort our favorite websites alphabetically
fav_website.sort()
# This will sort our favorite websites alphabetically but reverse it 
# fav_website.sort(reverse=True)
# Display our updated favorite websites
print(fav_website)

# This will count how many times github.com appears in the list
github_count = fav_website.count("github.com")
# Display our updated favorite websites
print(github_count)

# Create a list to be added to our fav_websites list
additional_websites = ["docs.python.org", "wearecodenation.com"]
# Its the same as append but except your using a list or array
fav_website.extend(additional_websites)
print(fav_website)

#67.83