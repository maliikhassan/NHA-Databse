import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

def tender_update():
    display_data()
    load_data_to_form()
    update_data

def insert_data():
    ppra_no = ppra_no_entry.get()
    title = title_entry.get()
    title_procurement = title_procurement_entry.get()
    no_of_bids = no_of_bids_entry.get()
    contract_no = contract_no_entry.get()
    estimated_amount = estimated_amount_entry.get()
    agency_name = agency_name_entry.get()
    ppra_publish_date = ppra_publish_date_entry.get()

    # Validate date format
    try:
        ppra_publish_date = datetime.strptime(ppra_publish_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showwarning("Input Error", "Invalid Publish Date format. Use YYYY-MM-DD")
        return

    if not ppra_no or not title or not title_procurement or not no_of_bids or not contract_no or not estimated_amount or not agency_name or not ppra_publish_date:
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
        sql_insert_query = """INSERT INTO Tenders (PPRA_no, title, title_procurrement, no_of_bids, contract_no, estimated_amount, agencyName, PPRA_No_publish_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (ppra_no, title, title_procurement, no_of_bids, contract_no, estimated_amount, agency_name, ppra_publish_date))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def search_data():
    ppra_no = search_ppra_no_entry.get()

    if not ppra_no:
        messagebox.showwarning("Input Error", "Please enter a PPRA number to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM Tenders WHERE PPRA_no = %s"""
        cursor.execute(sql_search_query, (ppra_no,))
        result = cursor.fetchone()
        
        if result:
            result_label.config(text=f"PPRA No: {result[0]}\nTitle: {result[1]}\nTitle Procurement: {result[2]}\nNo. of Bids: {result[3]}\nContract No: {result[4]}\nEstimated Amount: {result[5]}\nAgency Name: {result[6]}\nPPRA No Publish Date: {result[7]}")
        else:
            result_label.config(text="No record found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def delete_data():
    ppra_no = delete_ppra_no_entry.get()

    if not ppra_no:
        messagebox.showwarning("Input Error", "Please enter a PPRA number to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM Tenders WHERE PPRA_no = %s"""
        cursor.execute(sql_delete_query, (ppra_no,))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given PPRA number")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def load_data_to_form(event):
    selected_item = tree.selection()[0]
    selected_data = tree.item(selected_item, 'values')
    
    ppra_no_entry.delete(0, END)
    ppra_no_entry.insert(0, selected_data[0])
    title_entry.delete(0, END)
    title_entry.insert(0, selected_data[1])
    title_procurement_entry.delete(0, END)
    title_procurement_entry.insert(0, selected_data[2])
    no_of_bids_entry.delete(0, END)
    no_of_bids_entry.insert(0, selected_data[3])
    contract_no_entry.delete(0, END)
    contract_no_entry.insert(0, selected_data[4])
    estimated_amount_entry.delete(0, END)
    estimated_amount_entry.insert(0, selected_data[5])
    agency_name_entry.delete(0, END)
    agency_name_entry.insert(0, selected_data[6])
    ppra_publish_date_entry.delete(0, END)
    ppra_publish_date_entry.insert(0, selected_data[7])

def update_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No Item Selected", "Please select a record to update")
        return

    ppra_no = ppra_no_entry.get()
    title = title_entry.get()
    title_procurement = title_procurement_entry.get()
    no_of_bids = no_of_bids_entry.get()
    contract_no = contract_no_entry.get()
    estimated_amount = estimated_amount_entry.get()
    agency_name = agency_name_entry.get()
    ppra_publish_date = ppra_publish_date_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE Tenders SET title = %s, title_procurrement = %s, no_of_bids = %s, contract_no = %s, estimated_amount = %s, agencyName = %s, PPRA_No_publish_date = %s WHERE PPRA_no = %s"""
        cursor.execute(sql_update_query, (title, title_procurement, no_of_bids, contract_no, estimated_amount, agency_name, ppra_publish_date, ppra_no))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def display_data():
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
        cursor.execute("SELECT * FROM Tenders")
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
root.title("Tenders Data Management")
root.configure(bg="#2c3e50")

# Define styles
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Arial", 12))
style.configure("TButton", background="#2980b9", foreground="white", font=("Arial", 12, "bold"), padding=6)
style.configure("TEntry", font=("Arial", 12), padding=6)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
style.configure("Treeview", font=("Arial", 12), rowheight=23, background="#ecf0f1", foreground="#2c3e50", fieldbackground="#ecf0f1")
style.map("TButton", background=[('active', '#3498db')])

# Create labels and entries for the form
ppra_no_label = ttk.Label(root, text="PPRA No")
ppra_no_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
ppra_no_entry = ttk.Entry(root)
ppra_no_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)

title_label = ttk.Label(root, text="Title")
title_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
title_entry = ttk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

title_procurement_label = ttk.Label(root, text="Title Procurement")
title_procurement_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
title_procurement_entry = ttk.Entry(root)
title_procurement_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

no_of_bids_label = ttk.Label(root, text="No. of Bids")
no_of_bids_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)
no_of_bids_entry = ttk.Entry(root)
no_of_bids_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=10, sticky=W)

contract_no_label = ttk.Label(root, text="Contract No")
contract_no_label.grid(row=4, column=0, padx=10, pady=5, sticky=E)
contract_no_entry = ttk.Entry(root)
contract_no_entry.grid(row=4, column=1, padx=10, pady=5, ipadx=10, sticky=W)

estimated_amount_label = ttk.Label(root, text="Estimated Amount")
estimated_amount_label.grid(row=5, column=0, padx=10, pady=5, sticky=E)
estimated_amount_entry = ttk.Entry(root)
estimated_amount_entry.grid(row=5, column=1, padx=10, pady=5, ipadx=10, sticky=W)

agency_name_label = ttk.Label(root, text="Agency Name")
agency_name_label.grid(row=6, column=0, padx=10, pady=5, sticky=E)
agency_name_entry = ttk.Entry(root)
agency_name_entry.grid(row=6, column=1, padx=10, pady=5, ipadx=10, sticky=W)

ppra_publish_date_label = ttk.Label(root, text="PPRA Publish Date (YYYY-MM-DD)")
ppra_publish_date_label.grid(row=7, column=0, padx=10, pady=5, sticky=E)
ppra_publish_date_entry = ttk.Entry(root)
ppra_publish_date_entry.grid(row=7, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Create buttons for CRUD operations with same width
button_width = 15
insert_button = ttk.Button(root, text="Insert Data", command=insert_data, width=button_width)
insert_button.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

update_button = ttk.Button(root, text="Update Data", command=update_data, width=button_width)
update_button.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

# Create search entry, label, and button
search_ppra_no_label = ttk.Label(root, text="Search by PPRA No")
search_ppra_no_label.grid(row=9, column=0, padx=10, pady=5, sticky=E)
search_ppra_no_entry = ttk.Entry(root)
search_ppra_no_entry.grid(row=9, column=1, padx=10, pady=5, ipadx=10, sticky=W)
search_button = ttk.Button(root, text="Search Data", command=search_data)
search_button.grid(row=9, column=2, padx=10, pady=5, sticky=W)

# Create delete entry, label, and button
delete_ppra_no_label = ttk.Label(root, text="Delete by PPRA No")
delete_ppra_no_label.grid(row=10, column=0, padx=10, pady=5, sticky=E)
delete_ppra_no_entry = ttk.Entry(root)
delete_ppra_no_entry.grid(row=10, column=1, padx=10, pady=5, ipadx=10, sticky=W)
delete_button = ttk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=10, column=2, padx=10, pady=5, sticky=W)

# Create result label
result_label = ttk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

# Create Treeview for displaying data
tree = ttk.Treeview(root, columns=("PPRA No", "Title", "Title Procurement", "No. of Bids", "Contract No", "Estimated Amount", "Agency Name", "PPRA No Publish Date"), show='headings')
tree.heading("PPRA No", text="PPRA No")
tree.heading("Title", text="Title")
tree.heading("Title Procurement", text="Title Procurement")
tree.heading("No. of Bids", text="No. of Bids")
tree.heading("Contract No", text="Contract No")
tree.heading("Estimated Amount", text="Estimated Amount")
tree.heading("Agency Name", text="Agency Name")
tree.heading("PPRA No Publish Date", text="PPRA No Publish Date")

tree.grid(row=12, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Bind the Treeview selection to load the data into the form
tree.bind('<ButtonRelease-1>', load_data_to_form)

# Adjust window size to 95% of screen dimensions
window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window

# Configure column weights
root.grid_rowconfigure(12, weight=1)
root.grid_columnconfigure(1, weight=1)


# Display data on start
display_data()

# Run the main loop
root.mainloop()
