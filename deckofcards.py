import random

deck = []
suits = ["spades","clubs","diamonds","hearts"]


def shuffle(deck):
    a=len(deck)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      deck[d],deck[e]=deck[e],deck[d]
    return deck


for i in range(4):
    
    for j in range(1,14):
        value=str(j)
        if(j==1):
            value = "A"
        if(j==11):
            value = "J"
        elif(j==12):
            value = "Q"
        elif(j==13):
            value = "k"
            
        
        deck.append(f"{value}{suits}")

print (deck)



#fisher yates
