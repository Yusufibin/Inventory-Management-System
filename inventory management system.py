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
        name = input("Entrez le nom de l'article : ")
        price = float(input("Entrez le prix de l'article : "))
        item_id = int(input("Entrez l'ID de l'article : "))
        lrd = input("Entrez la dernière date de réapprovisionnement de l'article (aaaa-mm-jj) : ")
        quantity = int(input("Entrez la quantité de l'article à la dernière date de réapprovisionnement : "))

        sql = "INSERT INTO item (ID, Name, Product_price, Quantity, Last_restocking_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (item_id, name, price, quantity, lrd))
        db.commit()
        print("Enregistrement ajouté")
    except ValueError:
        print("Entrée invalide. Veuillez entrer des données valides.")
    except Error as e:
        print(f"Erreur lors de l'ajout de l'article : {e}")

def update_item(cursor):
    try:
        show_all_records(cursor)
        to_edit = int(input("Entrez l'ID de l'article à modifier : "))

        print("a- pour modifier le nom")
        print("b- pour modifier le prix")
        print("c- pour modifier l'ID de l'article")
        print("d- pour modifier la dernière date de réapprovisionnement")
        print("e- pour modifier la quantité en stock")
        z = input("Entrez a-e : ")

        if z == 'a':
            new_name = input("Entrez le nouveau nom : ")
            sql = "UPDATE item SET Name = %s WHERE ID = %s"
            cursor.execute(sql, (new_name, to_edit))
        elif z == 'b':
            new_price = float(input("Entrez le nouveau prix : "))
            sql = "UPDATE item SET Product_price = %s WHERE ID = %s"
            cursor.execute(sql, (new_price, to_edit))
        elif z == 'c':
            new_id = int(input("Entrez le nouvel ID : "))
            sql = "UPDATE item SET ID = %s WHERE ID = %s"
            cursor.execute(sql, (new_id, to_edit))
        elif z == 'd':
            new_lrd = input("Entrez la nouvelle date de réapprovisionnement (aaaa-mm-jj) : ")
            sql = "UPDATE item SET Last_restocking_date = %s WHERE ID = %s"
            cursor.execute(sql, (new_lrd, to_edit))
        elif z == 'e':
            new_quantity = int(input("Entrez la nouvelle quantité : "))
            sql = "UPDATE item SET Quantity = %s WHERE ID = %s"
            cursor.execute(sql, (new_quantity, to_edit))
        else:
            print("Choix invalide.")
            return

        db.commit()
        print("Enregistrement mis à jour")
    except ValueError:
        print("Entrée invalide. Veuillez entrer des données valides.")
    except Error as e:
        print(f"Erreur lors de la mise à jour de l'article : {e}")

def delete_item(cursor):
    try:
        show_all_records(cursor)
        to_delete = int(input("Entrez l'ID de l'article à supprimer : "))
        sql = "DELETE FROM item WHERE ID = %s"
        cursor.execute(sql, (to_delete,))
        db.commit()
        print("Enregistrement supprimé")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un ID valide.")
    except Error as e:
        print(f"Erreur lors de la suppression de l'article : {e}")

def show_all_records(cursor):
    try:
        sql = "SELECT * FROM item"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("Aucun enregistrement trouvé.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Prix", "Quantité", "Dernier réapprovisionnement"]
        for row in rows:
            table.add_row(row)
        print(table)

    except Error as e:
        print(f"Erreur lors de l'affichage des enregistrements : {e}")

def search_item(cursor):
    try:
        search_term = input("Entrez l'ID, le nom ou la date de réapprovisionnement de l'article à rechercher : ")
        sql = "SELECT * FROM item WHERE ID LIKE %s OR Name LIKE %s OR Last_restocking_date LIKE %s"
        cursor.execute(sql, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()

        if not rows:
            print("Aucun enregistrement trouvé.")
            return
            
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Prix", "Quantité", "Dernier réapprovisionnement"]
        for row in rows:
            table.add_row(row)
        print(table)

    except Error as e:
        print(f"Erreur lors de la recherche d'articles : {e}")

def display_help():
    print("1- Ajouter un article")
    print("2- Supprimer un article")
    print("3- Modifier un article")
    print("4- Afficher tous les articles")
    print("5- Rechercher un article")
    print("6- Aide : Afficher toutes les commandes")
    print("0- Quitter")

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
            choice = input("Entrez votre choix : ")

            if choice == "0":
                break
            elif choice in menu_options:
                menu_options[choice](cursor)
            else:
                print("Choix invalide. Veuillez réessayer.")

    except Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
    finally:
        if db and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    main()
