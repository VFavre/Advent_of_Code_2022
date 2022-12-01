import numpy as np

######################################################################
############################# FIRST HALF #############################
######################################################################

answer_half_1 = 0                                               

with open("input.txt", "r") as f:
    lines = f.read()                                       
                                                   
elves = lines.split("\n\n")                                                 
                          
def calories(string:str) -> int:
    array = np.array(string.split('\n'))
    return np.sum(array.astype(int))

for elf in elves:
    answer_half_1 = max(answer_half_1, calories(elf))
    
######################################################################
############################ SECOND HALF #############################
######################################################################

top_3 = [0,0,0]

def evaluator(value:int , array):
    if array[2] < value:
        array.append(value)
    elif array[1] < value:
        array.insert(1, value)
    elif array[0] < value:
        array.insert(0, value)
    return array[-3:]

for elf in elves:
    top_3 = evaluator(calories(elf), top_3)
       
answer_half_2 = sum(top_3)
                                            
print(""" 
 ██████████     █████████   █████ █████       ████ 
░░███░░░░███   ███░░░░░███ ░░███ ░░███       ░░███ 
 ░███   ░░███ ░███    ░███  ░░███ ███         ░███ 
 ░███    ░███ ░███████████   ░░█████          ░███ 
 ░███    ░███ ░███░░░░░███    ░░███           ░███ 
 ░███    ███  ░███    ░███     ░███           ░███ 
 ██████████   █████   █████    █████          █████
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░          ░░░░░ 
                                                    """)
                                                                          
print(' First half answer is : ' + str(answer_half_1))
print(' Second half answer is : ' + str(answer_half_2))
