# List of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Tokyo', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Paris', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Liverpool', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'New York', 'China', 'Munchen', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List of countries that require a visa
visa_required = ['China', 'India', 'Saudi Arabia', 'Russia', 'Brazil', 'United Arab Emirates', 'Egypt']

# List of visa-free travel destinations
travel_list = []

for country in countries:
    if country in visa_required:
        continue
    if len(travel_list) == 10:
        break
    travel_list.append(country)
    

# Testing
print('Visa-free travel destinations:', travel_list)