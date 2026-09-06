import sys
from list_class import ListClass

def main():

    user_list: ListClass = ListClass()
    if len(sys.argv) > 1:
        user_list.read_file(sys.argv[1])

    while True:
        print()
        print(f"1. Add an item")
        print(f"2. Remove an item")
        print(f"3. Replace an item")
        print(f"4. View list")
        print(f"5. Make a file")
        print(f"6. Exit")
        user_input: str = input(f"Choose an option: ")

        if user_input.strip() == "1":
            print()
            item: str = input("Enter an item to add: ")
            user_list.insert_item(item)
        elif user_input.strip() == "2":
            print()
            index: int = int(input("Enter number of item to remove: "))
            user_list.remove_item(index)
        elif user_input.strip() == "3":
            print()
            index = int(input("Enter number of item to replace: "))
            item = input("Enter new item: ")
            user_list.replace_item(index, item)
        elif user_input.strip() == "4":
            print()
            user_list.view_list()
        elif user_input.strip() == "5":
            print()
            output_file_name: str = input("Enter file name (without extension): ")
            user_list.write_file(output_file_name)
        elif user_input.strip() == "6":
            print()
            print(f"Exiting program")
            break
        else:
            print("Invalid option. Please try again.")
    sys.exit(0)

if __name__ == '__main__':
    main()