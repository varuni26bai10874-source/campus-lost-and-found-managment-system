#----------------Claim Module-------------
def claim_item():
    print("\n--Claim Item----")
    view_items()
    if len(items)==0:
        return
    try:
        number=int(input("\nEnter item number you want to claim:"))
        if number < 1 or number > len(items):
            print("invalid to print(item number.")
            return
        item = items[number-1]
        if item["type"].lower()!="found":
            print("\nYou can only claim a FOUND item.")
            return
        if item ["claimed"]:
            print("\nThis item has already been claimed")
            return
        print("\nItem:",item["name"])
        reason=input("Why do you think this item belongs to you?")
        print("\nclaim submitted successfully!")
        print("Your reason:",reason)
        item["claimed"]=True
    except ValueError:
        print("Please enter a valid number")
        
