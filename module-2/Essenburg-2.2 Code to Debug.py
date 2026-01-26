#Rebecca Essenburg
#Assignment 4.2
#11/9/25

#This code will convert miles into kilometers,
#prompting the user for the number of miles.

#Define the function.
def miles_to_km():
    kilometers = miles*1.60934
    print(f"{miles} miles is equal to {kilometers} kilometers.")
#Get the number of miles.
try:
    miles = float(input(f"Enter the amount of miles driven: "))
#Test for invalid inputs.
except ValueError:
    print("The input must be a number.")
else:
    if miles == 0:
        print("The input cannot be 0.")
    elif miles < 0:
        print("The input cannot be negative.")
#Execute the function.
    else:
        miles_to_km()