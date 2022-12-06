import queue

######################################################################
############################# FIRST HALF #############################
######################################################################

class dock():

    def __init__(self,length:int):
        self.q_list =[queue.LifoQueue() for i in range(length)]
        self.length = length
    
    def get(self, pos:int) -> str:
        return self.q_list[pos].get()

    def add(self, pos:int, value:str):
        self.q_list[pos].put(value)

    def move(self,  _from:int, _to:int):
        self.add(_to, self.get(_from))

    def multi_move(self, iteration:int, _from:int, _to:int):
        for i in range(iteration):
            self.move(_from, _to)
    def display(self):
        for q in self.q_list:
            print(q)

temp = dock(4)

with open("./Day5/input.txt", "r") as f:
    lines = f.read().splitlines()

i=0
crates = []
while True:
    line = lines.pop(0)
    if line[0] == "[":
        crates.append(line)
    else:
        break

lines.pop(0)

movements = lines

def crates_emplacement(crate_list):
    number_stack = ((len(crate_list[0])-3) //4) + 1
    emplacement = dock(number_stack)
    for l in crate_list[::-1]:
        for i in range(1, number_stack, 4):
            crate_letter = l[i]
            if crate_letter != " ":
                emplacement.add(i%4, crate_letter)
    return emplacement

enplacement = crates_emplacement(crates)
enplacement.display()

print("""
 ██████████     █████████   █████ █████       ██████████
░░███░░░░███   ███░░░░░███ ░░███ ░░███       ░███░░░░░░█
 ░███   ░░███ ░███    ░███  ░░███ ███        ░███     ░ 
 ░███    ░███ ░███████████   ░░█████         ░█████████ 
 ░███    ░███ ░███░░░░░███    ░░███          ░░░░░░░░███
 ░███    ███  ░███    ░███     ░███           ███   ░███
 ██████████   █████   █████    █████         ░░████████ 
░░░░░░░░░░   ░░░░░   ░░░░░    ░░░░░           ░░░░░░░░  
                                                                                                             
""")