customers = {}

while True:
    # Main Menu Display
    print("CUSTOMER MANAGEMENT SYSTEM")
    print("="*45)
    print(" 1. Add New Customer")
    print(" 2. Remove Customer")
    print(" 3. Update Customer Details")
    print(" 4. View All Customers")
    print(" 5. Exit")
    print("="*45)

    choice = input("\nSelect an option (1-5): ").strip()

    # OPTION 1: ADD CUSTOMER
    if choice == "1":
        try:
            cust_id = int(input("Enter unique Customer ID: "))
            
            if cust_id in customers:
                print(f"\n[!] Error: ID {cust_id} is already taken by {customers[cust_id]['name']}.")
            else:
                name = input("Enter Name: ").strip()
                email = input("Enter Email: ").strip()
                address = input("Enter Address: ").strip()

              
                customers[cust_id] = {
                    "name": name,
                    "email": email,
                    "address": address
                }
                print(f"\n[+] Success: {name} has been added to the system.")

        except ValueError:
            print("\n[!] Invalid input! ID must be a whole number.")

    # OPTION 2: REMOVE CUSTOMER
    elif choice == "2":
        try:
            cust_id = int(input("Enter Customer ID to remove: "))
            
            if cust_id in customers:
                target_name = customers[cust_id]['name']
                confirm = input(f"Are you sure you want to delete {target_name}? (y/n): ").lower()
                if confirm == 'y':
                    del customers[cust_id]
                    print(f"\n[-] {target_name} has been removed.")
                else:
                    print("\nDeletion cancelled.")
            else:
                print("\n[!] Customer ID not found.")

        except ValueError:
            print("\n[!] Error: Please enter a valid numeric ID.")

    # OPTION 3: UPDATE CUSTOMER 
    elif choice == "3":
        try:
            cust_id = int(input("Enter Customer ID to update: "))
            
            if cust_id in customers:
                current = customers[cust_id]
                print(f"\n--- Editing Record for ID: {cust_id} ---")
                print(f"1. Name    (Current: {current['name']})")
                print(f"2. Email   (Current: {current['email']})")
                print(f"3. Address (Current: {current['address']})")
                print("4. Cancel")

                update_choice = input("\nWhich field would you like to change? ")

                if update_choice == "1":
                    new_val = input("Enter new name: ").strip()
                    customers[cust_id]["name"] = new_val
                    print(f"Updated: Name changed to {new_val}")

                elif update_choice == "2":
                    new_val = input("Enter new email: ").strip()
                    customers[cust_id]["email"] = new_val
                    print(f"Updated: Email changed to {new_val}")

                elif update_choice == "3":
                    new_val = input("Enter new address: ").strip()
                    customers[cust_id]["address"] = new_val
                    print(f"Updated: Address changed to {new_val}")
                
                elif update_choice == "4":
                    print("Update cancelled.")
                else:
                    print("Invalid selection.")
            else:
                print("\n[!] No customer found with that ID.")

        except ValueError:
            print("\n[!] Error: Invalid ID format.")

    # OPTION 4: VIEW ALL 
    elif choice == "4":
        print("\n--- CURRENT CUSTOMER LIST ---")
        if not customers:
            print("The database is currently empty.")
        else:
            
            print(f"{'ID':<6} | {'NAME':<15} | {'EMAIL':<22} | {'ADDRESS'}")
            print("-" * 65)
            
            for cid, info in customers.items():
                print(f"{cid:<6} | {info['name']:<15} | {info['email']:<22} | {info['address']}")
            
            print("-" * 65)
            
            input("\nPress ENTER to return to the menu...")

    # OPTION 5: EXIT
    elif choice == "5":
        print("END")
        break

    else:
        print("\n Invalid choice! Please select 1-5.")