import string

letter_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

letter_values = dict(zip(letter_list, range(1,53)))

######################################################################
############################# FIRST HALF #############################
######################################################################

with open("./Day3/input.txt", "r") as f:
    lines = f.readlines()

intersec_values = 0

for i in range(len(lines)) :
    content = list(lines[i].strip('\n'))
    h_l_content = len(content)//2
    space1,space2 = content[:h_l_content],content[h_l_content:]
    intersection = list(set(space1) & set(space2))
    intersec_values += letter_values[intersection[0]]

######################################################################
############################ SECOND HALF #############################
######################################################################

badges_values = 0 

for i in range(0,len(lines),3) :
    rucksack0 = list(lines[i].strip('\n'))
    rucksack1 = list(lines[i+1].strip('\n'))
    rucksack2 = list(lines[i+2].strip('\n'))
    b_intersection = list(set(rucksack0) & set(rucksack1) & set(rucksack2))
    badges_values += letter_values[b_intersection[0]]


print("""
 ██████████     █████████   █████ █████        ████████ 
░░███░░░░███   ███░░░░░███ ░░███ ░░███        ███░░░░███
 ░███   ░░███ ░███    ░███  ░░███ ███        ░░░    ░███
 ░███    ░███ ░███████████   ░░█████            ██████░ 
 ░███    ░███ ░███░░░░░███    ░░███            ░░░░░░███
 ░███    ███  ░███    ░███     ░███           ███   ░███
 ██████████   █████   █████    █████         ░░████████ 
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░           ░░░░░░░░                                                     
"""
)

print('The answer for the first half is : ' + str(intersec_values))
print('The answer for the first half is : ' + str(badges_values))