def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View list")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            shopping_list.append(input("Enter item: "))
            pass
        elif choice == "2":
            shopping_list.remove(input("Enter item to remove: "))
            pass
        elif choice == "3":
            print(shopping_list)
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")
main()