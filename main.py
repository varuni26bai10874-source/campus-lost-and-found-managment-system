#------------------Main Program-------------------
from User_module import register,login
from lost_found_module import report_item,view_items
from search_module import search_item
from claim_module import claim_item
def user_menu(user):
    while True:
        print("\n===============================")
        print(" CAMPUS LOST AND FOUND ")
        print("\n===============================")
        print("Welcome,",user["name"])
        print("\n1. Report Lost/ Found Item")
        print("2. View All Items")
        print("3. Search Items")
        print("4. Claim Item")
        print("5. Logout")
        choice = input("\nEnter your choice:")
        if choice == "1":
            report_item(user)
        elif choice == "2":
            view_items()
        elif choice =="3":
            search_items()
        elif choice =="4":
            claim_item(user)
        elif choice =="5":
            print("\nlogged out successfully.")
            break
        else:
            print("\nInvalid choice. Please try again.")
def main():
    while True:
        print("\n======================================")
        print("    CAMPUS LOST AND FOUND       ")
        print("\n======================================")
        print("1. Register ")
        print("2. Login ")
        print("3. Exit ")
        choice = input("\nEnter your choice:")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user is not None :
                user_menu(user)
        elif choice == "3":
            print("\nThank You for using campus lost and found")
            break
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()
