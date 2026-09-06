import sys

def main():

    if len(sys.argv) > 1:
        file_name: str = sys.argv[1]
    else:
        file_name = ""
    user_list: List = List()
    user_list.read_file(file_name)

    while True:
        print()
        print(f"1. Add a item")
        print(f"2. Remove a item")
        print(f"3. View list")
        print(f"4. Make a file")
        print(f"5. Exit")
        user_input: str = input(f"Choose an option: ")

        if user_input.strip() == "1":
            print()
            item: str = input("Enter an item to add: ")
            user_list.insert_item(item)

        elif user_input.strip() == "2":
            print()
            item: int = int(input("Enter number of item to remove: "))
            user_list.remove_item(item)

        elif user_input.strip() == "3":
            print()
            user_list.view_list()

        elif user_input.strip() == "4":
            print()
            output_file_name: str = input("Enter file name (without extension): ")
            user_list.write_file(output_file_name)
        elif user_input.strip() == "5":
            print()
            print(f"Exiting program")
            break
        else:
            print("Invalid option. Please try again.")


    return 0

class List:
    def __init__(self):
        self.__items: list[str] = []

    def insert_item(self, item: str) -> None:
        self.__items.append(item)
        print(f"{item} has been added to the list.")

    def remove_item(self, index: int) -> None:
        if 0 < index <= self.get_size():
            removed_item = self.__items.pop(index-1)
            print(f"{removed_item} has been removed from the list.")
        else:
            print("Invalid item number.")

    def set_items(self, items: list[str]) -> None:
        self.__items = items.copy()

    def get_item(self, index: int) -> str:
        if 0 < index <= self.get_size():
            return self.__items[index-1]
        else:
            raise IndexError("Index out of range")

    def get_items(self) -> list[str]:
        return self.__items.copy()

    def get_size(self) -> int:
        return len(self.__items)

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def view_list(self) -> None:
        if not self.is_empty():
            print("Your list:")
            for i, item in enumerate(self.__items):
                print(f"{i+1}.{item}")
        else:
            print("Your list is empty.")

    def read_file(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.__items.append(line.split(".", 1)[1])
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")

    def write_file(self, file_name: str) -> None:
        try:
            with open(f"{file_name}.txt", "x") as file:
                for i, item in enumerate(self.__items):
                    file.write(f"{i + 1}.{item}\n")
            print(f"List has been saved to {file_name}.txt")
        except FileExistsError:
            print(f"File {file_name}.txt already exists. Please choose a different name.")

if __name__ == '__main__':
    main()