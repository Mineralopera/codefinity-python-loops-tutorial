# List of travel destinations
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Tokyo', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Paris', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Liverpool', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'New York', 'China', 'Munchen', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Counter variable
counter = 0

# Creating loop
for city in countries:
    if len(city) == 6:
        counter += 1
    

# Testing
print("Number of countries with exactly 6 letters:", counter)