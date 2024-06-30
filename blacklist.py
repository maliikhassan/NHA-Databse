import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

def Blacklist_update():
    display_blacklist()
    load_selected_record()
    update_blacklist()
    
# Function to insert data into Blacklist table
def insert_blacklist():
    contract_owner = contract_owner_entry.get()
    firm_name = firm_name_entry.get()
    contractor_cnic = contractor_cnic_entry.get()
    contractor_phone = contractor_phone_entry.get()
    address = address_entry.get()
    statuses = statuses_entry.get()

    if not contract_owner or not firm_name or not contractor_cnic or not contractor_phone or not address or not statuses:
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
        sql_insert_query = """INSERT INTO Blacklist (contract_owner, firm_name, contractorCNIC, contractorPhone, adress, statuses) 
                            VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (contract_owner, firm_name, contractor_cnic, contractor_phone, address, statuses))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_blacklist()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to display data from Blacklist table in Treeview
def display_blacklist():
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
        cursor.execute("SELECT * FROM Blacklist")
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

# Function to search data in Blacklist table by Contract Owner
def search_blacklist():
    contract_owner = search_contract_owner_entry.get()

    if not contract_owner:
        messagebox.showwarning("Input Error", "Please enter a Contract Owner to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database' 
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM Blacklist WHERE contract_owner = %s"""
        cursor.execute(sql_search_query, (contract_owner,))
        result = cursor.fetchone()

        if result:
            result_label.config(text=f"Contract Owner: {result[0]}\nFirm Name: {result[1]}\nContractor CNIC: {result[2]}\nContractor Phone: {result[3]}\nAddress: {result[4]}\nStatuses: {result[5]}")
        else:
            result_label.config(text="No record found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to delete data from Blacklist table by Contract Owner
def delete_blacklist():
    contract_owner = delete_contract_owner_entry.get()

    if not contract_owner:
        messagebox.showwarning("Input Error", "Please enter a Contract Owner to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database' 
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM Blacklist WHERE contract_owner = %s"""
        cursor.execute(sql_delete_query, (contract_owner,))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given Contract Owner")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_blacklist()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to update data in Blacklist table
def update_blacklist():
    selected_item = tree.focus()
    values = tree.item(selected_item, "values")

    if not values:
        messagebox.showwarning("No Item Selected", "Please select a record to update")
        return

    contract_owner = values[0]
    firm_name = firm_name_entry.get()
    contractor_cnic = contractor_cnic_entry.get()
    contractor_phone = contractor_phone_entry.get()
    address = address_entry.get()
    statuses = statuses_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database'  
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE Blacklist SET firm_name = %s, contractorCNIC = %s, contractorPhone = %s, adress = %s, statuses = %s WHERE contract_owner = %s"""
        cursor.execute(sql_update_query, (firm_name, contractor_cnic, contractor_phone, address, statuses, contract_owner))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_blacklist()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to load selected record into form fields
def load_selected_record(event):
    selected_item = tree.focus()
    values = tree.item(selected_item, "values")

    if values:
        contract_owner_entry.delete(0, END)
        contract_owner_entry.insert(0, values[0])

        firm_name_entry.delete(0, END)
        firm_name_entry.insert(0, values[1])

        contractor_cnic_entry.delete(0, END)
        contractor_cnic_entry.insert(0, values[2])

        contractor_phone_entry.delete(0, END)
        contractor_phone_entry.insert(0, values[3])

        address_entry.delete(0, END)
        address_entry.insert(0, values[4])

        statuses_entry.delete(0, END)
        statuses_entry.insert(0, values[5])

# Create the main window
root = Tk()
root.title("Blacklist Data Management")
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

firm_name_label = ttk.Label(root, text="Firm Name")
firm_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
firm_name_entry = ttk.Entry(root)
firm_name_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

contractor_cnic_label = ttk.Label(root, text="Contractor CNIC")
contractor_cnic_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
contractor_cnic_entry = ttk.Entry(root)
contractor_cnic_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

contractor_phone_label = ttk.Label(root, text="Contractor Phone")
contractor_phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)
contractor_phone_entry = ttk.Entry(root)
contractor_phone_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=10, sticky=W)

address_label = ttk.Label(root, text="Address")
address_label.grid(row=4, column=0, padx=10, pady=5, sticky=E)
address_entry = ttk.Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=5, ipadx=10, sticky=W)

statuses_label = ttk.Label(root, text="Statuses")
statuses_label.grid(row=5, column=0, padx=10, pady=5, sticky=E)
statuses_entry = ttk.Entry(root)
statuses_entry.grid(row=5, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Create buttons for submit, update, and display
submit_button = ttk.Button(root, text="Submit", command=insert_blacklist)
submit_button.grid(row=6, column=0, padx=10, pady=10)

update_button = ttk.Button(root, text="Update", command=update_blacklist)
update_button.grid(row=6, column=1, padx=10, pady=10)

# Create search and delete form
search_contract_owner_label = ttk.Label(root, text="Search by Contract Owner")
search_contract_owner_label.grid(row=7, column=0, padx=10, pady=5, sticky=E)
search_contract_owner_entry = ttk.Entry(root)
search_contract_owner_entry.grid(row=7, column=1, padx=10, pady=5, ipadx=10, sticky=W)
search_button = ttk.Button(root, text="Search", command=search_blacklist)
search_button.grid(row=7, column=2, padx=10, pady=5)

delete_contract_owner_label = ttk.Label(root, text="Delete by Contract Owner")
delete_contract_owner_label.grid(row=8, column=0, padx=10, pady=5, sticky=E)
delete_contract_owner_entry = ttk.Entry(root)
delete_contract_owner_entry.grid(row=8, column=1, padx=10, pady=5, ipadx=10, sticky=W)
delete_button = ttk.Button(root, text="Delete", command=delete_blacklist)
delete_button.grid(row=8, column=2, padx=10, pady=5)

# Create Treeview to display the data
columns = ("Contract Owner", "Firm Name", "Contractor CNIC", "Contractor Phone", "Address", "Statuses")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
tree.bind("<<TreeviewSelect>>", load_selected_record)

# Create a label to display the search result
result_label = ttk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=4, padx=10, pady=5)

window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window

# Display data on startup
display_blacklist()

# Run the application
root.mainloop()
