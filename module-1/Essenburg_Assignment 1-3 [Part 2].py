#Rebecca Essenburg
#Assignment 1.3 (Part 2)
#1/18/26

#This code will ask the user how many bottles of beer
#are on the wall and then will subtract 1 bottle
#and count down until none are left.

#Get user input for how many bottles to start with.
def user_bottles():
    while True:
        try:
            bottles_input = int(input(f"How many bottles of beer are on the wall?: "))
            if bottles_input >= 1:
                break    #Valid entry!
            #Exceptions for negative/zero and non-number entries.
            else:
                print("The number cannot be zero or negative.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    return bottles_input

#Create countdown function that prints lyrics and subtracts a bottle each time.
def beer_song(beernum):
    while beernum > 1:
        print(f"{beernum} bottles of beer on the wall.")
        print()
        print(f"{beernum} bottles of beer on the wall,")
        print(f"{beernum} bottles of beer.")
        print("Take one down and pass it around...")
        beernum -= 1
    #Add lyrics for the last verse so it's not plural.
    while beernum == 1:
        print(f"{beernum} bottle of beer on the wall.")
        print()
        print(f"{beernum} bottle of beer on the wall,")
        print(f"{beernum} bottle of beer.")
        print("Take one down and pass it around...")
        print(f"NO MORE BOTTLES OF BEER ON THE WALL!")
        beernum -= 1
        print()
    #Reminder to buy more beer when the countdown is over.
    if beernum <= 0:
        print(f"It's time to buy more beer!!")

#Create the main function.
def main():
    bottles = user_bottles()
    beer_song(bottles)

#Call the main function.
if __name__ == '__main__':
    main()