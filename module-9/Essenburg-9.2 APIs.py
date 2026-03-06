#Rebecca Essenburg
#Assignment 9.2
#3/1/26

#This program will follow an API tutorial using Open Notify and print the results,
#and then will follow the same tutorial using a D&D 5e API and print those results as well.

#Import libraries.
import requests
import json

#Create function for formatting and printing JSON data.
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Create function for the Open Notify API tutorial.
def tutorial():
    response = requests.get('http://api.open-notify.org/astros.json')
    print(f"Connection status code: {response.status_code}")  #Connection test printout.
    print("------")
#Print requested data using the jprint function.
    print("People Currently in Space:")
    jprint(response.json())

#Create function for the D&D 5e API requests.
def dnd():
    response = requests.get('https://www.dnd5eapi.co/api/monsters/gelatinous-cube')
    print(f"Connection status Code: {response.status_code}")  #Connection test printout.
    print("------")
    print("Unformatted Gelatinous Cube Data:")
    print(response.json())
    print("------")
    print("Gelatinous Cube Data:")
    jprint(response.json())

def main():
    tutorial()
    print()
    print('~' * 40)
    print()
    dnd()

#Call the main function.
if __name__ == "__main__":
    main()