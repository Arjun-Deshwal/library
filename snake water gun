import random 
print("Hey there, this is your own snake water gun game\n")
gp=0#game played
ps=0#player score
cs=0#computer score
c=10
lis=['s','w','g']
#games

while gp<c:
    

    choice=random.choice(lis)
    a=input("kya chunoge, Saap ke liye s dabao,panni ke liye w dabao,bandook ke liye g dabao.\n")
    
    if a==choice:
        print(f"{a} vs {choice}")
        print("maine bhi yahi cuhna, tie ho gya")
        gp+=1
        print(f"{gp} chances hogyi hai 10 mein se.")
    elif a=='s':
        if choice=="w":
            print(f"{a} vs {choice}")
            print("Saap sara panni pi gya aur tum jeet gye.")
            ps+=1
            gp+=1
            print(f"{gp} chances hogyi hai 10 mein se.")
        elif choice=='g':
            print(f"{a} vs {choice}")
            print("Maine saap ko goli mar di aur mai jeet gya")
            cs+=1
            gp+=1   
            print(f"{gp} chances hogyi hai 10 mein se.")
        else : print("input galat hai")     
    elif a=='w':
        if choice=="s":
            print(f"{a} vs {choice}")
            print("Saap sara panni pi gya aur mai jeet gye.")
            cs+=1
            gp+=1
            print(f"{gp} chances hogyi hai 10 mein se.")
        elif choice=='g':
            print(f"{a} vs {choice}")
            print(" Meri bandook panni mai doob gayi aur tum jeet gya")
            ps+=1
            gp+=1
            print(f"{gp} chances hogyi hai 10 mein se.")
        else : print("input galat hai")    
    elif a=='g':
        if choice=="w":
            print(f"{a} vs {choice}")
            print("bandook panni mein doob gyi aur mai jeet gye.")
            cs+=1
            gp+=1
            print(f"{gp} chances hogyi hai 10 mein se.")
        elif choice=='s':
            print(f"{a} vs {choice}")
            print("tumne saap ko goli mar di aur tum jeet gya")
            ps+=1
            gp+=1        
            print(f"{gp} chances hogyi hai 10 mein se.")
        else:
            print("input galat hai")

    else:
        print("sahi sahi batao")         
print(f"tumhara score hai{ps}")
print(f"mera score hai{cs}")
if cs>ps:
    print("Tum haar gaye aur mai jeet gya.")
elif ps>cs:
    print("Tum jeet gaye aur mai haar gya.")
else:
    print("Koi hara jeeta nhi game tie ho gya.")
