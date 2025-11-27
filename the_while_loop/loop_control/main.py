# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Greece', 'Netherlands', 'Finland', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []

# Initialzing index 
i = 0

# Creating the loop
while i < len(countries):
    if countries[i][0] != 'S':
        i += 1
        continue
    else:
        selected.append(countries[i])
        if len(selected) == 3:
            break
    i += 1



# Testing
print('First three countries starting with "S":', selected)