import os
os.chdir(os.getcwd())

######################################################################
############################# FIRST HALF #############################
######################################################################

# either the input1 is winning the round)
def we_win( input1: str, input2:str) -> bool:
    if input1 == 'A' and input2 == 'Y':
        return True
    elif input1 == 'B' and input2 == 'Z':
        return True
    elif input1 == 'C' and input2 == 'X':
        return True
    return False

score_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

# input1 is the opponent choice and input2 our own
def scoring( input1: str, input2:str, score_dict:dict) -> int:
    if score_dict[input1] == score_dict[input2]:
        return score_dict[input2] + 3
    elif we_win(input1, input2):
        return score_dict[input2] + 6
    else:
        return score_dict[input2]


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(' ')

scorings_first_half = []
for l in lines:
    score = scoring(l[0], l[1], score_dict)
    scorings_first_half.append(score)


######################################################################
############################ SECOND HALF #############################
######################################################################

move_response = {
    'AX' : 'Z',
    'AY' : 'X',
    'AZ' : 'Y',
    'BX' : 'X',
    'BY' : 'Y',
    'BZ' : 'Z',
    'CX' : 'Y',
    'CY' : 'Z',
    'CZ' : 'X',
}

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(' ')
    lines[i][1] = lines[i][0]+lines[i][1]

print(lines)

scorings_second_half = []
for l in lines:
    score = scoring(l[0], move_response[l[1]], score_dict)
    scorings_second_half.append(score)




print(""" 
 ██████████     █████████   █████ █████        ████████ 
░░███░░░░███   ███░░░░░███ ░░███ ░░███        ███░░░░███
 ░███   ░░███ ░███    ░███  ░░███ ███        ░░░    ░███
 ░███    ░███ ░███████████   ░░█████            ███████ 
 ░███    ░███ ░███░░░░░███    ░░███            ███░░░░  
 ░███    ███  ░███    ░███     ░███           ███      █
 ██████████   █████   █████    █████         ░██████████
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░          ░░░░░░░░░░ 
                                                        
""")

print("The answer to the first half is : " + str(sum(scorings_first_half)) )
print("The answer to the first half is : " + str(sum(scorings_second_half)) )