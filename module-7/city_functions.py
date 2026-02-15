# Rebecca Essenburg
# Assignment 7.2
# 2/22/26

# This function will accept a city and country name
# and then print the city and country name.
# The code will call the function 3 times.

# Define the function accepting a city and country into one string.
def format_location(city,country,population='Unknown',language='English'):
    location = f'{city}, {country} - Population {population}, {language}'
    return location.title()

# List three different cities and countries in correct formatting.
def main():
    print(format_location('Phoenix','United States'))
    print(format_location('Toronto','Canada','50000'))
    print(format_location('Tokyo','Japan','68000','Japanese'))

# Call the main function.
if __name__ == '__main__':
    main()