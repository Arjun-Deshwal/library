print("HII THERE , THIS PROGRAM WILL TELL YOU WHETHER YOU ARE ELIGIBLE FOR VOTING OR NOT.")
age=int(input("PLEASE ENTER YOUR AGE HERE="))
print(age)
if age<18:
    print('SORRY! BUT YOU CANNOT VOTE NOW. \n SOME YEARS LEFT TO VOTE.')
elif age==18:
    print('YOU ARE READY TO VOTE. \n YOU CAN GET YOUR VOTING CARD NOW!')
elif age>110:
    print('SORRY BUT ARE YOU ALIVE?:)HA HA HA!')  
else :
    print('YOU ARE ELIGIBLE FOR VOTING.\n BE PREPARED FOR THE NEXT ELECTIONS!')