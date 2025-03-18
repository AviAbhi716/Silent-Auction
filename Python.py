import os
print("Welcome to  silent Auction Program")
def find(details_info):
    max1=0
    winner1=""
    for i in details_info:
        value=details_info[i]
        if value>max1:
            max1=value
            winner1=i
    return winner1,max1
game=True
details={}
while game:
    name=input("What is your name?:")
    price=int(input("What is your bid?:"))
    details[name] = price
    check=input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if check == 'yes':
        os.system('cls')
    else:
        winner,Max=find(details)
        print(details)
        print(f"The winner is {winner} with a bid of {Max}.")
        game=False
