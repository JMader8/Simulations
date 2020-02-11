import random

rollcount = int(input("How many dice rolls ya want?"))
print(f"{rollcount} rolls. Rolling now.")



i=0


while(i<rollcount):

    
    
    i +=1
    
    num1=1
    num2=2
    num3=3
    num4=4
    num5=5
    num6=6
    st=random.randint(num1,num6)
    
    print(i, st )

    print("Next Roll: ")
    





