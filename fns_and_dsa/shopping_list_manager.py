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
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == "2":
            item = input("Enter item to remove: ")
            for n in shopping_list:
                if item == n:
                    shopping_list.remove(item)
                    break
            else:
                print("Item not in shopping list")
            pass
        elif choice == "3":
            for u in shopping_list:
                print(u)
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")
main()