import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

def remarks_update():
    display_remarks()
    update_remarks()
# Function to insert data into Remarks table
def insert_remarks():
    contract_owner = contract_owner_entry.get()
    project_title = project_title_entry.get()
    reason = reason_entry.get()

    if not contract_owner or not project_title or not reason:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0000', 
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_insert_query = """INSERT INTO Remarks (contractOwner, title_project, reason) VALUES (%s, %s, %s)"""
        cursor.execute(sql_insert_query, (contract_owner, project_title, reason))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_remarks()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to search data in Remarks table by contractOwner and title_project
def search_remarks():
    contract_owner = search_contract_owner_entry.get()
    project_title = search_project_title_entry.get()

    if not contract_owner or not project_title:
        messagebox.showwarning("Input Error", "Please enter Contract Owner and Project Title to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@', 
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM Remarks WHERE contractOwner = %s AND title_project = %s"""
        cursor.execute(sql_search_query, (contract_owner, project_title))
        result = cursor.fetchone()
        
        if result:
            # Displaying the result in the entry fields for update
            contract_owner_entry.delete(0, END)
            contract_owner_entry.insert(0, result[0])
            project_title_entry.delete(0, END)
            project_title_entry.insert(0, result[1])
            reason_entry.delete(0, END)
            reason_entry.insert(0, result[2])
        else:
            messagebox.showinfo("Info", "No record found with the given Contract Owner and Project Title")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to delete data from Remarks table by contractOwner and title_project
def delete_remarks():
    contract_owner = delete_contract_owner_entry.get()
    project_title = delete_project_title_entry.get()

    if not contract_owner or not project_title:
        messagebox.showwarning("Input Error", "Please enter Contract Owner and Project Title to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@', 
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM Remarks WHERE contractOwner = %s AND title_project = %s"""
        cursor.execute(sql_delete_query, (contract_owner, project_title))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given Contract Owner and Project Title")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_remarks()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to update data in Remarks table
def update_remarks():
    contract_owner = contract_owner_entry.get()
    project_title = project_title_entry.get()
    reason = reason_entry.get()

    if not contract_owner or not project_title:
        messagebox.showwarning("No Item Selected", "Please search and select a record to update")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@', 
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE Remarks SET reason = %s WHERE contractOwner = %s AND title_project = %s"""
        cursor.execute(sql_update_query, (reason, contract_owner, project_title))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_remarks()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to display data from Remarks table in Treeview
def display_remarks():
    for row in tree.get_children():
        tree.delete(row)

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@', 
            database='nha_database'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Remarks")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Create the main window
root = Tk()
root.title("Remarks Data Management")
root.configure(bg="#2c3e50")

# Define styles
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Arial", 12))
style.configure("TButton", background="#2980b9", foreground="white", font=("Arial", 12, "bold"), padding=6)
style.configure("TEntry", font=("Arial", 12), padding=6)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
style.configure("Treeview", font=("Arial", 12), rowheight=25, background="#ecf0f1", foreground="#2c3e50", fieldbackground="#ecf0f1")
style.map("TButton", background=[('active', '#3498db')])

# Create labels and entries for the form
contract_owner_label = ttk.Label(root, text="Contract Owner")
contract_owner_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
contract_owner_entry = ttk.Entry(root)
contract_owner_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)

project_title_label = ttk.Label(root, text="Project Title")
project_title_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
project_title_entry = ttk.Entry(root)
project_title_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

reason_label = ttk.Label(root, text="Reason")
reason_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
reason_entry = ttk.Entry(root)
reason_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Search by Contract Owner and Project Title section
search_frame = Frame(root, bg="#34495e", padx=10, pady=10)
search_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky=W)

search_contract_owner_label = ttk.Label(search_frame, text="Search Contract Owner:")
search_contract_owner_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

search_contract_owner_entry = ttk.Entry(search_frame)
search_contract_owner_entry.grid(row=0, column=1, padx=5, pady=5)

search_project_title_label = ttk.Label(search_frame, text="Search Project Title:")
search_project_title_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

search_project_title_entry = ttk.Entry(search_frame)
search_project_title_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = ttk.Button(search_frame, text="Search", command=search_remarks)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Delete by Contract Owner and Project Title section
delete_frame = Frame(root, bg="#34495e", padx=10, pady=10)
delete_frame.grid(row=2, column=2, rowspan=2, padx=10, pady=5, sticky=W)

delete_contract_owner_label = ttk.Label(delete_frame, text="Delete Contract Owner:")
delete_contract_owner_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

delete_contract_owner_entry = ttk.Entry(delete_frame)
delete_contract_owner_entry.grid(row=0, column=1, padx=5, pady=5)

delete_project_title_label = ttk.Label(delete_frame, text="Delete Project Title:")
delete_project_title_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

delete_project_title_entry = ttk.Entry(delete_frame)
delete_project_title_entry.grid(row=1, column=1, padx=5, pady=5)

delete_button = ttk.Button(delete_frame, text="Delete", command=delete_remarks)
delete_button.grid(row=1, column=2, padx=5, pady=5)

# Update button
update_button = ttk.Button(root, text="Update Data", command=update_remarks)
update_button.grid(row=3, column=1, padx=10, pady=10)

# Insert button
insert_button = ttk.Button(root, text="Insert Data", command=insert_remarks)
insert_button.grid(row=3, column=0, padx=10, pady=10)

# Treeview to display data
tree = ttk.Treeview(root, columns=("contractOwner", "title_project", "reason"), show="headings", height=10)
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)

tree.heading("contractOwner", text="Contract Owner")
tree.heading("title_project", text="Project Title")
tree.heading("reason", text="Reason")

window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window

# Configure column weights for Treeview
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Display initial data
display_remarks()

# Start the main loop
root.mainloop()
