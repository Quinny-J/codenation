capital_cities = {
    "United Kingdom": "London",
    "France" : "Paris",
    "Spain" : "Madrid"
}
# print our whole dict
print(capital_cities)

# print the keys in our dict
print(capital_cities.keys())

# print whatever are key France holds which in this case is Paris
print(capital_cities["France"])

# print all the values
print(capital_cities.values())

# print all items in the dict
print(capital_cities.items())

# print the value of they key
print(capital_cities.get("France"))

# print an error instead of crashing
print(capital_cities.get("Francey", "This key does not exist")) # This should throw a error msg because Francey is not a key in our dict

capital_cities.setdefault("USA", "Washington")
print(capital_cities)