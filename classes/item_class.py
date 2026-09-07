

"""
This class represents an item with a name, quantity, and an optional ID.
It provides methods to set and get the item's attributes,
as well as to compare two items for equality based on their name and quantity.
"""

class Item:
    def __init__(self, item: str, quantity: int = 1, item_id: int = -1):
        """
        Initializes an Item object with the given item name, quantity, and item ID.

        :param item: str - the name of the item
        :param quantity: int - the quantity of the item
        :param item_id: int - the ID of the item on the list
        """
        self.__item: str = item
        self.__quantity: int = quantity if quantity > 0 else 1
        self.__item_id: int = item_id if item_id > 0 else -1

    def __repr__(self) -> str:
        """
        Returns a string representation for debugging of the Item object.

        :return: str - a string representation of the Item object
        """
        return f"item={self.__item} quantity={self.__quantity} item_id={self.__item_id}"

    def __str__(self) -> str:
        """
        Returns a string representation of the Item object.

        :return: str - a string representation of the Item object
        """
        return f"{self.__quantity} {self.__item}"

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Item objects are equal based on their item name and quantity.

        :param other: object - the other Item object to compare with
        :return: bool - True if the items are equal, False otherwise:return:
        """
        if isinstance(other, Item):
            return self.__item == other.__item and self.__quantity == other.__quantity
        return False

    def set_item(self, item: str) -> None:
        """
        Sets the name of the item.

        :param item: str - the new name of the item
        """
        self.__item = item

    def get_item(self) -> str:
        """
        Returns the name of the item.

        :return: str - the name of the item
        """
        return self.__item

    def set_quantity(self, quantity: int) -> None:
        """
        Sets the quantity of the item.

        :param quantity: int - the new quantity of the item
        """
        self.__quantity = quantity if quantity > 0 else self.__quantity

    def get_quantity(self) -> int:
        """
        Returns the quantity of the item.

        :return: int - the quantity of the item
        """
        return self.__quantity

    def set_item_id(self, item_id: int) -> None:
        """
        Sets the ID of the item.

        :param item_id: int - the new ID of the item
        """
        self.__item_id = item_id if item_id > 0 else self.__item_id

    def get_item_id(self) -> int:
        """
        Returns the ID of the item.

        :return: int - the ID of the item
        """
        return self.__item_id
