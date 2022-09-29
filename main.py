n = 0
print ("Welcome to nearly rock paper scissors")
while n!=10:
    go = input("what do you pick?")
    if ( go== "rock"):
        print ("I chose paper you lose")
        n+=1
    elif (go=="paper"):
        print ("I chose scissors you lose")
        n+=1
    else:
        print ("I chose rock you lose")
        n+=1



