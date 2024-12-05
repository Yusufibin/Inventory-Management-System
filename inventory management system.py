import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "kushi1012",
    "database": "inventorymanage",
}

def add_item(cursor):
    try:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        item_id = int(input("Enter item id: "))
        lrd = input("Enter item last restocking date (yyyy-mm-dd): ")
        quantity = int(input("Enter quantity of item as per last restocking date: "))

        sql = "INSERT INTO item (ID, Name, Product_price, Quantity, Last_restocking_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (item_id, name, price, quantity, lrd))
        db.commit()
        print("Record added")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except Error as e:
        print(f"Error adding item: {e}")

def update_item(cursor):
    try:
        show_all_records(cursor)
        to_edit = int(input("Enter item ID of record to edit: "))

        print("a- to edit name")
        print("b- to edit price")
        print("c- to edit item id")
        print("d- to edit last restocking date")
        print("e- to edit stock quantity")
        z = input("Enter a-e: ")

        if z == 'a':
            new_name = input("Enter new name:")
            sql = "UPDATE item SET Name = %s WHERE ID = %s"
            cursor.execute(sql, (new_name, to_edit))
        elif z == 'b':
            new_price = float(input("Enter new price:"))
            sql = "UPDATE item SET Product_price = %s WHERE ID = %s"
            cursor.execute(sql, (new_price, to_edit))
        elif z == 'c':
            new_id = int(input("Enter new ID:"))
            sql = "UPDATE item SET ID = %s WHERE ID = %s"
            cursor.execute(sql, (new_id, to_edit))
        elif z == 'd':
            new_lrd = input("Enter new last restocking date (yyyy-mm-dd):")
            sql = "UPDATE item SET Last_restocking_date = %s WHERE ID = %s"
            cursor.execute(sql, (new_lrd, to_edit))
        elif z == 'e':
            new_quantity = int(input("Enter new quantity:"))
            sql = "UPDATE item SET Quantity = %s WHERE ID = %s"
            cursor.execute(sql, (new_quantity, to_edit))
        else:
            print("Invalid choice.")
            return

        db.commit()
        print("Record updated")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except Error as e:
        print(f"Error updating item: {e}")

def delete_item(cursor):
    try:
        show_all_records(cursor)
        to_delete = int(input("Enter item ID of record to delete: "))
        sql = "DELETE FROM item WHERE ID = %s"
        cursor.execute(sql, (to_delete,))
        db.commit()
        print("Record deleted")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
    except Error as e:
        print(f"Error deleting item: {e}")

def show_all_records(cursor):
    try:
        sql = "SELECT * FROM item"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("No records found.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Quantity", "Last restocking date"]
        for row in rows:
            table.add_row(row)
        print(table)

    except Error as e:
        print(f"Error displaying records: {e}")

def search_item(cursor):
    try:
        search_term = input("Enter item ID, name, or last restocking date to search: ")
        sql = "SELECT * FROM item WHERE ID LIKE %s OR Name LIKE %s OR Last_restocking_date LIKE %s"
        cursor.execute(sql, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()

        if not rows:
            print("No records found.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Quantity", "Last restocking date"]
        for row in rows:
            table.add_row(row)
        print(table)

    except Error as e:
        print(f"Error searching items: {e}")

def display_help():
    print("1- Add an item")
    print("2- Delete an item")
    print("3- Update an item")
    print("4- Show all items")
    print("5- Search an item")
    print("6- Help: Show all commands")
    print("0- Quit")

def main():
    global db
    db = None
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        menu_options = {
            "1": add_item,
            "2": delete_item,
            "3": update_item,
            "4": show_all_records,
            "5": search_item,
            "6": display_help,
        }

        while True:
            print("************************************")
            display_help()
            print("************************************")
            choice = input("Enter your choice: ")

            if choice == "0":
                break
            elif choice in menu_options:
                menu_options[choice](cursor)
            else:
                print("Invalid choice. Please try again.")

    except Error as e:
        print(f"Database connection error: {e}")
    finally:
        if db and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    main()
