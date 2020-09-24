
def first_and_last():
    """Test first and last name against input file and output matches if found."""
    for line in f:
        line = line.lower()
        line = line.lower()
        name_list = line.split()
        first = name_list[0]
        last = name_list[1]
        phone = name_list[2]
        if first in line & last in line:
            print(first.title() + " " + last.title() + ", " + phone)
            
def last_only():
    """Test last name only again inpu file and output matches if found."""
    for line in f:
        line = line.lower()
        name_list = line.split()
        first = name_list[0]
        last = name_list[1]
        phone = name_list[2]
        if last_name in last:
            print(first.title() + " " + last.title() + ", " + phone)

# Open phone file in 'read' format
f = open("phones.txt", 'r')
# Prompt user for name
name = input("Enter a last name, or first and last name: ")
# Convert name to lowercase format
name = name.lower()

# Split name into one or two parts
name_list = name.split()

if len(name_list) == 2:
    first_name = name_list[0]
    last_name = name_list[1]
    first_and_last()

elif len(name_list) == 1:
    last_name = name_list[0]
    last_only()

elif len(name_list) > 2:
    print("[+] Error: Please list just one name.")





