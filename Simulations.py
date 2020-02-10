import random

rollcount = float(input("How many dice rolls ya want?"))
print(f"{rollcount} rolls. Rolling now.")

roll = random(1,6)

i=0

while(i<rollcount):
    i +=1
    print(i)
    


