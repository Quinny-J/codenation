# Task 2
# Use the two lists to create a dict where country is key and value is language


countries = ["England", "Spain", "Ethiopia", "Iran"]
languages = ["English", "Spanish", "Amharic", "Farsi"]

# Here im using zip to pair the items together England:English
country_language_dict = dict(zip(countries, languages))

print(country_language_dict)