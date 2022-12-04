######################################################################
############################# FIRST HALF #############################
######################################################################

with open("./Day4/input.txt", "r") as f:
    lines = f.readlines()

number_contained = 0
for l in lines :
    assignement0, assignement1 = l.strip("\n").split(',')
    assignement0 = list(map(int, assignement0.split("-")))
    assignement1 = list(map(int, assignement1.split("-")))
    if (assignement0[0] <= assignement1[0] and assignement1[1] <= assignement0[1]) or (assignement1[0] <= assignement0[0] and assignement0[1] <= assignement1[1]) :
        number_contained += 1

######################################################################
############################ SECOND HALF #############################
######################################################################

number_overlap = 0
for l in lines :
    assignement0, assignement1 = l.strip("\n").split(',')
    assignement0 = list(map(int, assignement0.split("-")))
    assignement1 = list(map(int, assignement1.split("-")))
    if  set( range(assignement0[0], assignement0[1]+1) ) & set( range(assignement1[0], (assignement1[1]+1)) ) :
        number_overlap += 1

print("""
 ██████████     █████████   █████ █████       █████ █████ 
░░███░░░░███   ███░░░░░███ ░░███ ░░███       ░░███ ░░███  
 ░███   ░░███ ░███    ░███  ░░███ ███         ░███  ░███ █
 ░███    ░███ ░███████████   ░░█████          ░███████████
 ░███    ░███ ░███░░░░░███    ░░███           ░░░░░░░███░█
 ░███    ███  ░███    ░███     ░███                 ░███░ 
 ██████████   █████   █████    █████                █████ 
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░                ░░░░░  
                                                                                                                
""")

print('The answer for the first half is : ' + str(number_contained))
print('The answer for the second half is : ' + str(number_overlap))