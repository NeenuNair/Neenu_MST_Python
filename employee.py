import mysql.connector
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Neenz_30@88$",
            database = "empmansys"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        return False

def main():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to database. Exiting...")
        return
    cursor = connection.cursor()

    while(True):
        print("---Employee Management Application---")
        print("1. Add Employee")
        print("2.Update Employee")
        print("3.Delete Employee")
        print("4.View Employee")
        print("5.Search Employee") 
        print("6. Exit") 

        choice = int(input("Enter the choice: "))
        if choice == 1:
            add_employee(cursor)
        elif choice == 2:
            update_employee(cursor)
        elif choice == 3:
            delete_employee(cursor)
        elif choice == 4:
            view_empolyee(cursor)
        elif choice == 5:
            search_employee(cursor)
        elif choice == 6:
            connection.commit()
            print ("Existing..Good bye--")
            break

def add_employee(cursor):
    emp_id = int(input("Enter employee id : "))
    emp_name= input("Enter employee name : ")
    emp_salary = int(input("Enter employee salary : "))
    emp_dept= input("Enter employee ndept : ")

    query = "insert into employee values (%s,%s,%s,%s)"
    values=( emp_id,emp_name,emp_salary,emp_dept)
    cursor.execute(query,values)
    print("employee added successfully")

def view_empolyee(cursor):
    query ="select * from employee"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for item in result:
                print(f"ID: {item[0]}, Name: {item[1]}, Salary: {item[2]}, Department: {item[3]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_employee(cursor):
    try:
        emp_id = int(input("Enter the employee ID to update: "))
        print("What would you like to update?")
        print("1. Name\n2.Salary\n3.Dept")
        ch = int(input("Enter your choice: "))
        if ch ==1:
            new_name = input("Enter the new name")
            query = "update employee set emp_name = %s where emp_id = %s"
            values = (new_name,emp_id)
            cursor.execute(query,values)
        if ch ==2:
            new_salary = float(input("Enter the new salary"))
            query = "update employee set emp_salary = %s where emp_id = %s"
            values = (new_salary,emp_id)
            cursor.execute(query,values)
        if ch ==3:
            new_dept= input("Enter the new dept")
            query = "update employee set emp_dept = %s where emp_id = %s"
            values = (new_dept,emp_id)
            cursor.execute(query,values)
    except mysql.connector.Error as err:
        print(f"{err}")

def delete_employee(cursor):
    try:
        emp_id = int(input("Enter the employee ID to delete: "))
        query = "DELETE FROM employee WHERE emp_id = %s"
        values = (emp_id,)
        cursor.execute(query, values)
        print("Employee deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def search_employee(cursor):
    try:
        emp_id = int(input("Enter the employee ID to search: "))
        query = "SELECT * FROM employee WHERE emp_id = %s"
        values = (emp_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            print(f"ID: {result[0]}, Name: {result[1]}, Salary: {result[2]}, Department: {result[3]}")
        else:
            print("Employee not found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__=='__main__':
    main()