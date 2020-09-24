def first_and_last():
    for line in f:
        line = line.lower()
        if first_name in line:
            output = line.split()
            print(output[0].title() + " " + output[1].title() + ", " + output[2])
            

def last_only():
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


#Output for testing
#print(name_list)
#print(name_list[0])
#print(len(name_list))
#print(last_name.title())




