# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Greece', 'Netherlands', 'Finland', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Counter variable
short_name_count = 0

# Initializing index 
i = 0

# Sorting the countries based on length
while i < len(countries):
    if len(countries[i]) < 7:
        short_name_count += 1
    i += 1

# Testing
print('Number of short country names:', short_name_count)