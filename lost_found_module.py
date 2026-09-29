#------------Lost and found---------------
from storage import items        
def report_item(user):
    print("\n------Report item---------")
    item_type = input("Enter type(lost/found):").lower()
    if item_type!= "lost" and item_type!= "found":
        print("\nPlease enter only 'lost' or 'found'.")
        return
    item_name=input("Enter Item Name")
    category = input("Enter Category:")
    location=input("enter location:")
    date=input("Enter Date:")
    description=input("Enter description:")
    item ={
        "type":item_type,
        "name":item_name,
        "category": category,
        "location": location,
        "date": date,
        "description": description,
        "reported_by": user["name"],
        "student_id": user["student_id"],
        "claimed": False
        }
    items.append(item)
    print("\nitem reported successfully!")
def view_items():
    print("\n------All items-----")
    if len(items)==0:
        print("No items have been reported yet.")
        return
    for i in range(len(items)):
        item=items[i]
        print("Item number:",i+1)
        print("Type:",item["type"])
        print("name:",item["name"])
        print("category:",item["category"])
        print("location:",item["location"])
        print("date:",item["date"])
        print("reprted by:",item["reported_by"])
        if item["claimed"]:
            print("status:claimed")
        else:
            print("status:Available")
print("--------------------------")        
