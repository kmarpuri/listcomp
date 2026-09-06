
def main():

    user_list: list[str] = []

    while True:
        print(f"1. Add a item")
        print(f"2. Remove a item")
        print(f"3. View list")
        print(f"4. Exit")
        user_input: str = input(f"Choose an option: ")

        if user_input == "1":
            item: str = input("Enter an item to add: ")
            user_list.append(item)
            print(f"{item} has been added to the list.\n")
        elif user_input == "2":
            item: int = int(input("Enter number of item to remove: "))
            if 0 < item <= len(user_list):
                removed_item: str = user_list.pop(item-1)
                print(f"{removed_item} has been removed from the list.\n")
            else:
                print("Invalid item number.")
        elif user_input == "3":
            if user_list:
                print("Your list:")
                for i, item in enumerate(user_list):
                    print(f"{i+1}. {item}")
                print()
        elif user_input == "4":

            print(f"Exiting program")
            break
        else:
            print("Invalid option. Please try again.\n")


    return 0

if __name__ == '__main__':
    main()