def first_and_last():
    for line in f:
        line = line.lower()
        if first_name in line:
            print(line.title())

def last_only():
    for line in f:
        line = line.lower()
        if last_name in line:
            print(line.title())

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
    print("Error: Please list just one name.")


#Output for testing
#print(name_list)
#print(name_list[0])
#print(len(name_list))
#print(last_name.title())




