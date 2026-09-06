
"""

This class can hold values put into a list and can read and write to a file.
Initially acts as a normal list, but will be able to used to compare products on list with products from storefronts,
such as Amazon, Kroger, Target, etc.

"""
class ListClass:
    def __init__(self, items: list[str] = None, id: int = None) -> None:
        """
        Initializes a List class object that can use an existing list of items or create a new one.

        :param items: list[str] - Takes a list of items to initialize the ListClass object.
        :param id: int - Takes an integer to set the id of the ListClass object for database identification.
        """
        if items is not None:
            self.__items: list[str] = items.copy()
        else:
            self.__items: list[str] = []
        if id:
            self.__id: int = id
        else:
            self.__id: int = 0 # Default id

    def insert_item(self, item: str, index: int = None) -> bool:
        """
        Inserts an item into the list prints a message (current stage of development, will want to remove printing after testing).

        :param item: str - takes a string to insert at the last element of the list.
        :return: bool - returns True if the item was added, False if the index was invalid.
        """
        if not index:
            self.__items.append(item)
            print(f"{item} has been added to the list.")
            return True
        elif 0 < index <= self.get_size() + 1:
            self.__items.insert(index-1, item)
            print(f"{item} has been added to the list at position {index}.")
            return True
        print("Invalid item number.")
        return False


    def remove_item(self, index: int) -> bool:
        """
        Removes an item from an index in the list and prints a message (current stage of development, will want to remove printing after testing).

        :param index: int - takes an integer to remove the index if it is located in the list, otherwise prints and error message.
        :return: bool - returns True if the item was removed, False if the index was invalid.
        """
        if 0 < index <= self.get_size():
            removed_item = self.__items.pop(index-1)
            print(f"{removed_item} has been removed from the list.")
            return True
        else:
            print("Invalid item number.")
            return False

    def replace_item(self, index: int, item: str) -> bool:
        """
        Replaces an item in the list at a given index with a new item.

        :param index: int - takes an integer that is the index of the item on the list
        :param item: str - takes a string that is the new item to replace the old item at the given index
        :return: bool - returns True if the item was replaced, False if the index was invalid.
        """
        if self.remove_item(index):
            return self.insert_item(item)
        return False

    def set_items(self, items: list[str]) -> None:
        """
        Changes the list of items to another list of items.

        :param items: list[str] - takes a list of strings to replace the current list of items.
        :return: None
        """
        self.__items = items.copy()

    def get_item(self, index: int) -> str:
        """
        Returns the item at the given index if it is within bounds.

        :param index: int - takes an integer that is the index of the item on the list
        :return: str - returns an item at the given index if it is within bounds
        """
        if 0 < index <= self.get_size():
            return self.__items[index-1]
        else:
            raise IndexError("Index out of range")

    def get_items(self) -> list[str]:
        """
        Returns a copy of the list of items.

        :return: list[str] - returns a copy of the list of items
        """
        return self.__items.copy()

    def get_size(self) -> int:
        """
        Returns the size of the list of items.

        :return: int - returns the size of the list of items
        """
        return len(self.__items)

    def is_empty(self) -> bool:
        """
        Returns True if the list of items is empty, False otherwise.

        :return: bool - returns True if the list of items is empty, False otherwise
        """
        return len(self.__items) == 0

    def view_list(self) -> None:
        """
        Prints the list of items.

        :return: None
        """
        if not self.is_empty():
            print("Your list:")
            for i, item in enumerate(self.__items):
                print(f"{i+1}.{item}")
        else:
            print("Your list is empty.")

    def read_file(self, file_name: str) -> bool:
        """
        Reads a file and adds all of those values to the list of items.
        If the file does not exit will return False and print an error message.
        Returns True if the file was read successfully.

        :param file_name: str - takes a string that is the name of the file to read from
        :return: bool - returns True if the file was read successfully, False if the file was not found.
        """
        try:
            if file_name and "." not in file_name:
                file_name += ".txt"
            with open(file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and "." in line:
                        self.__items.append(line.split(".", 1)[1])
            return True
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")
            return False

    def write_file(self, file_name: str) -> bool:
        """
        Writes the list of items from the list to a file. If the file already exists,
        it will request a new file name and return False. If the file is written successfully, it will return True.

        :param file_name: str - takes a string that is the name of the file to create and write to
        :return: bool - returns True if the file was written successfully, False if the file already exists.
        """
        try:
            with open(f"{file_name}.txt", "x") as file:
                for i, item in enumerate(self.__items):
                    file.write(f"{i + 1}.{item}\n")
            print(f"List has been saved to {file_name}.txt")
            return True
        except FileExistsError:
            print(f"File {file_name}.txt already exists. Please choose a different name.")
            return False