#Python program that checks whether two cities belong to the same country
# Define city lists for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Function to find country of a city
def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

# Get user input for two cities
city1 = input("Enter the first city: ").strip().title()
city2 = input("Enter the second city: ").strip().title()

# Determine the countries
country1 = get_country(city1)
country2 = get_country(city2)

# Check and print the result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not recognized")

