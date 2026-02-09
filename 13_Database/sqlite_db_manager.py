import sqlite3

def get_connection():
    return sqlite3.connect("db_manager.db")


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print(" Table created successfully")


def insert_person(name, age):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO persons (name, age) VALUES (?, ?)",
        (name, age)
    )

    conn.commit()
    conn.close()
    print(" Record inserted successfully")


def view_persons():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM persons")
    rows = cur.fetchall()

    conn.close()

    print("\n Persons List")
    if not rows:
        print("No records found.")
    for row in rows:
        print(row)


def update_person(person_id, name, age):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE persons
        SET name = ?, age = ?
        WHERE id = ?
    """, (name, age, person_id))

    conn.commit()
    conn.close()
    print(" Record updated successfully")


def delete_person(person_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM persons WHERE id = ?", (person_id,))

    conn.commit()
    conn.close()
    print(" Record deleted successfully")



def menu():
    create_table()

    while True:
        print("""
========== SQLite DB Manager ==========
1. Insert Person
2. View Persons
3. Update Person
4. Delete Person
5. Exit
======================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            insert_person(name, age)

        elif choice == "2":
            view_persons()

        elif choice == "3":
            pid = int(input("Enter ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_person(pid, name, age)

        elif choice == "4":
            pid = int(input("Enter ID to delete: "))
            delete_person(pid)

        elif choice == "5":
            print(" Exiting DB Manager")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
