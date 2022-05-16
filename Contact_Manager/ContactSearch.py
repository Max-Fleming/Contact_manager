import os
import json
from difflib import get_close_matches

nameEntered = ''
numberEntered = ''
searchResults = ''
sentinel = 'a'

# This try will allow us to handle exceptions when opening the json file
try:
    with open('contactList.json', 'r') as file:
        contacts = json.load(file)
except FileNotFoundError as ex:
    print(ex)
except IOError as ex:
    print(ex)

# This will print all contacts loaded onto the screen
for k, v in contacts.items():
    print(f'{k: <13} - {v: >13}')


input('Contacts Retrieved. Press any key.')

os.system('cls')

# this while loop will be used to allow the user to continue to edit contact information
# for as long as they need to
while sentinel != 'x':

    print(f'{"Manage Contacts": ^30}')
    nameEntered = input('Enter the name of a contact you wish to search for: ').capitalize()

    # We will use the get close matches function to allow for a search of names
    searchResults = get_close_matches(nameEntered, contacts, n=5, cutoff=1)

    # if user inputs an exact name this will allow them to find that contact exactly
    if nameEntered in contacts:
        print('\n\nContact Found:')
        print('Edit contact')
        print(f'{nameEntered: <11} - {contacts[nameEntered]: >13}')
    # if the user enters something that comes up with a list of close matches this will allow for the user to see all
    # of the matches
    elif len(searchResults) > 1:
        listNumber = 1
        print('\n\nContacts Found:')
        for value in searchResults:
            print(f'{listNumber}: {value: <13} - {contacts[value]: >13}')
            listNumber += 1
        nameEntered = input('Type the name you meant from the list or a new name you want to add: ').capitalize()
    # if no matches are found this will allow the user to add a new contact to the list
    else:
        print('\n\nContact Not Found:')
        print('Add New Contact')

    # after the user determines what contact they are editing this will allow them to change the number or not
    numberEntered = input(f"\nEnter {nameEntered}'s phone number (###)###-#### or press enter for no change: ")

    # this will check to see if a correctly formatted number was entered before we edit
    if len(numberEntered) == 13:
        contacts[nameEntered] = numberEntered

    os.system('cls')

    # this will allow the user to end the application and save the changed data
    sentinel = input('Press Enter to continue editing contacts or press "X" to exit and save: ').casefold()

    os.system('cls')

# this will then save the newly entered data to the json file after the user is done
try:
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)
except FileNotFoundError as ex:
    print(ex)
except IOError as ex:
    print(ex)
