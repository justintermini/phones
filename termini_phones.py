"""
Program: termini_phones
Author: Justin Termini

This program prompts the user for a name and then searches a separate file for a phone
number entry connected to that name. The user is prompted until they enter a blank entry.

Input: A last name or a first and last name
Output: The corresponding first and last name and phone number.
"""

def first_and_last():
    """Test first and last name against input file and output matches if found."""
    for line in f:
        line = line.lower()
        line = line.lower()
        name_list = line.split()
        first = name_list[0]
        last = name_list[1]
        phone = name_list[2]
        if first_name in first: 
            print(first.title() + " " + last.title() + ", " + phone)
            
def last_only():
    """Test last name only again input file and output matches if found."""
    for line in f:
        line = line.lower()
        name_list = line.split()
        first = name_list[0]
        last = name_list[1]
        phone = name_list[2]
        if last_name in last:
            print(first.title() + " " + last.title() + ", " + phone)

while True:
    # Open phone file in 'read' format
    f = open("phones.txt", 'r')

    # Prompt user for name
    name = input("Enter a last name, or first and last name: ")

    # End program if user enters an empty or blank linbe
    if name == "":
        break
    # Otherwise continue with the program
    else:
        # Convert name to lowercase format
        name = name.lower()

        # Split name into one or two parts
        name_list = name.split()

        # If there are two names enter, assume these are first and last names
        # and split list into appropriate variables, 
        # then call first_and_lastfunction.
        if len(name_list) == 2:
            first_name = name_list[0]
            last_name = name_list[1]
            first_and_last()
        # If just one name is entered, assume it is the last name only,
        # then create variable from last name, then call last_only function.
        elif len(name_list) == 1:
            last_name = name_list[0]
            last_only()
        # If more than two names entered, produce error message
        elif len(name_list) > 2:
            print("### Error: Please list just one name. ###")





