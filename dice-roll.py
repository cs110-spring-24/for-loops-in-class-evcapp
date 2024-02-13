import random 

ones=0
twos=0
threes=0
fours=0
fives=0
sixes=0

for roll in range(100):
    dice = random.randint(1,6)
    if (dice == 1):
        print("One")
        ones += 1
    if (dice == 2): 
        print("Two")
        twos += 1 
    if (dice == 3):
        print("One")
        threes += 1
    if (dice == 4):
        print("Two")
        fours += 1 
    if (dice == 5):
        print("Five")
        fives += 1
    if (dice == 6):
        print("Six")
        sixes += 1

print(f"After 100 rolls, we rolled {ones} ones, {twos} twos, {threes} threes, {fours} fours, {fives} fives, and {sixes} sixes  ")