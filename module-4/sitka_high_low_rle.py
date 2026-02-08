# Rebecca Essenburg
# Assignment 4.2
# 2/8/26

# This code revises the sitka_highs.py file to allow the user
# to choose between high and low temps to display.

# Import necessary libraries.
import sys
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Open the data file.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# User instructions.
print('Hello! In this program you will be able to view the daily temperatures in Sitka.')
print('You can choose to view either the high, or low temperatures.')
print('You may exit this program at any time.')
print()

# User selection.
while True:
    plt.style.use('dark_background') #Graph Customization
    selection = input("Please type High, Low, or Exit: ").strip().upper()
    
    #User selected to exit the program.
    if selection == 'EXIT':
        print('The program has ended. Thank you!')
        break
    
    # User selected the high temps graph.
    elif selection == 'HIGH':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)

    # User selected the low temps graph.
    elif selection == 'LOW':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)

    # Input error.
    else:
        print('That is an invalid entry. Please try again.')
        continue
    
    # Format and print selected graph.
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Exit imported programs.
sys.exit()