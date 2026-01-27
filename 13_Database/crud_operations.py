import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary INTEGER
)
""")
conn.commit()


def insert_data():
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    cursor.execute("INSERT INTO employee (name, salary) VALUES (?, ?)", (name, salary))
    conn.commit()
    print("Record inserted successfully")


def read_data():
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_data():
    emp_id = int(input("Enter employee ID to update: "))
    salary = int(input("Enter new salary: "))
    cursor.execute("UPDATE employee SET salary=? WHERE id=?", (salary, emp_id))
    conn.commit()
    print("Record updated successfully")


def delete_data():
    emp_id = int(input("Enter employee ID to delete: "))
    cursor.execute("DELETE FROM employee WHERE id=?", (emp_id,))
    conn.commit()
    print("Record deleted successfully")


while True:
    print("\n1.Insert\n2.Display\n3.Update\n4.Delete\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        insert_data()
    elif choice == 2:
        read_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

conn.close()
