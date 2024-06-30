import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

def projects_update():
    display_projects()
    on_tree_select()
    update_project()
# Function to insert data into Projects table
def insert_project():
    project_title = project_title_entry.get()
    ppra_no = ppra_no_entry.get()
    project_length = project_length_entry.get()
    cost = cost_entry.get()
    project_status = project_status_entry.get()
    project_type = project_type_entry.get()
    completion_date = completion_date_entry.get()
    physical_progress = physical_progress_entry.get()
    financial_progress = financial_progress_entry.get()
    pd_name = pd_name_entry.get()
    pd_email = pd_email_entry.get()

    if not project_title or not ppra_no or not project_length or not cost or not project_status or not project_type or not completion_date or not physical_progress or not financial_progress or not pd_name or not pd_email:
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
        sql_insert_query = """INSERT INTO Projects (project_title, PPRA_no, project_length, cost, project_status, project_type, Completion_Date, Physical_Progress, Financial_Progress, PD_Name, PD_Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (project_title, ppra_no, project_length, cost, project_status, project_type, completion_date, physical_progress, financial_progress, pd_name, pd_email))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_projects()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to search data in Projects table by project_title
def search_project():
    project_title = search_project_title_entry.get()

    if not project_title:
        messagebox.showwarning("Input Error", "Please enter a Project Title to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM Projects WHERE project_title = %s"""
        cursor.execute(sql_search_query, (project_title,))
        result = cursor.fetchone()
        
        if result:
            result_label.config(text=f"Project Title: {result[0]}\nPPRA No: {result[1]}\nProject Length: {result[2]}\nCost: {result[3]}\nProject Status: {result[4]}\nProject Type: {result[5]}\nCompletion Date: {result[6]}\nPhysical Progress: {result[7]}\nFinancial Progress: {result[8]}\nPD Name: {result[9]}\nPD Email: {result[10]}")
        else:
            result_label.config(text="No record found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to delete data from Projects table by project_title
def delete_project():
    project_title = delete_project_title_entry.get()

    if not project_title:
        messagebox.showwarning("Input Error", "Please enter a Project Title to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM Projects WHERE project_title = %s"""
        cursor.execute(sql_delete_query, (project_title,))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given Project Title")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_projects()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to update data in Projects table
def update_project():
    project_title = project_title_entry.get()

    if not project_title:
        messagebox.showwarning("No Item Selected", "Please select a record to update")
        return

    ppra_no = ppra_no_entry.get()
    project_length = project_length_entry.get()
    cost = cost_entry.get()
    project_status = project_status_entry.get()
    project_type = project_type_entry.get()
    completion_date = completion_date_entry.get()
    physical_progress = physical_progress_entry.get()
    financial_progress = financial_progress_entry.get()
    pd_name = pd_name_entry.get()
    pd_email = pd_email_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE Projects SET PPRA_no = %s, project_length = %s, cost = %s, project_status = %s, project_type = %s, Completion_Date = %s, Physical_Progress = %s, Financial_Progress = %s, PD_Name = %s, PD_Email = %s WHERE project_title = %s"""
        cursor.execute(sql_update_query, (ppra_no, project_length, cost, project_status, project_type, completion_date, physical_progress, financial_progress, pd_name, pd_email, project_title))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_projects()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to display data from Projects table in Treeview
def display_projects():
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
        cursor.execute("SELECT * FROM Projects")
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

# Function to select a record from Treeview and populate the form fields
def on_tree_select(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, 'values')

    project_title_entry.delete(0, END)
    project_title_entry.insert(0, values[0])

    ppra_no_entry.delete(0, END)
    ppra_no_entry.insert(0, values[1])

    project_length_entry.delete(0, END)
    project_length_entry.insert(0, values[2])

    cost_entry.delete(0, END)
    cost_entry.insert(0, values[3])

    project_status_entry.delete(0, END)
    project_status_entry.insert(0, values[4])

    project_type_entry.delete(0, END)
    project_type_entry.insert(0, values[5])

    completion_date_entry.delete(0, END)
    completion_date_entry.insert(0, values[6])

    physical_progress_entry.delete(0, END)
    physical_progress_entry.insert(0, values[7])

    financial_progress_entry.delete(0, END)
    financial_progress_entry.insert(0, values[8])

    pd_name_entry.delete(0, END)
    pd_name_entry.insert(0, values[9])

    pd_email_entry.delete(0, END)
    pd_email_entry.insert(0, values[10])

# Create the main window
root = Tk()
root.title("Projects Data Management")
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

# Define widgets
project_title_label = ttk.Label(root, text="Project Title")
project_title_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
project_title_entry = ttk.Entry(root)
project_title_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)

ppra_no_label = ttk.Label(root, text="PPRA No")
ppra_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
ppra_no_entry = ttk.Entry(root)
ppra_no_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

project_length_label = ttk.Label(root, text="Project Length")
project_length_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
project_length_entry = ttk.Entry(root)
project_length_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

cost_label = ttk.Label(root, text="Cost")
cost_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)
cost_entry = ttk.Entry(root)
cost_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=10, sticky=W)

project_status_label = ttk.Label(root, text="Project Status")
project_status_label.grid(row=4, column=0, padx=10, pady=5, sticky=E)
project_status_entry = ttk.Entry(root)
project_status_entry.grid(row=4, column=1, padx=10, pady=5, ipadx=10, sticky=W)

project_type_label = ttk.Label(root, text="Project Type")
project_type_label.grid(row=5, column=0, padx=10, pady=5, sticky=E)
project_type_entry = ttk.Entry(root)
project_type_entry.grid(row=5, column=1, padx=10, pady=5, ipadx=10, sticky=W)

completion_date_label = ttk.Label(root, text="Completion Date (YYYY-MM-DD)")
completion_date_label.grid(row=6, column=0, padx=10, pady=5, sticky=E)
completion_date_entry = ttk.Entry(root)
completion_date_entry.grid(row=6, column=1, padx=10, pady=5, ipadx=10, sticky=W)

physical_progress_label = ttk.Label(root, text="Physical Progress")
physical_progress_label.grid(row=7, column=0, padx=10, pady=5, sticky=E)
physical_progress_entry = ttk.Entry(root)
physical_progress_entry.grid(row=7, column=1, padx=10, pady=5, ipadx=10, sticky=W)

financial_progress_label = ttk.Label(root, text="Financial Progress")
financial_progress_label.grid(row=8, column=0, padx=10, pady=5, sticky=E)
financial_progress_entry = ttk.Entry(root)
financial_progress_entry.grid(row=8, column=1, padx=10, pady=5, ipadx=10, sticky=W)

pd_name_label = ttk.Label(root, text="PD Name")
pd_name_label.grid(row=9, column=0, padx=10, pady=5, sticky=E)
pd_name_entry = ttk.Entry(root)
pd_name_entry.grid(row=9, column=1, padx=10, pady=5, ipadx=10, sticky=W)

pd_email_label = ttk.Label(root, text="PD Email")
pd_email_label.grid(row=10, column=0, padx=10, pady=5, sticky=E)
pd_email_entry = ttk.Entry(root)
pd_email_entry.grid(row=10, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Search by Project Title section
search_frame = Frame(root, bg="#34495e", padx=10, pady=10)
search_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky=W)

search_project_title_label = ttk.Label(search_frame, text="Search Project Title:")
search_project_title_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

search_project_title_entry = ttk.Entry(search_frame)
search_project_title_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = ttk.Button(search_frame, text="Search", command=search_project)
search_button.grid(row=0, column=2, padx=5, pady=5)

result_label = Label(search_frame, text="", padx=10, pady=10, bg="#34495e", fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Delete by Project Title section
delete_frame = Frame(root, bg="#34495e", padx=10, pady=10)
delete_frame.grid(row=2, column=2, rowspan=2, padx=10, pady=5, sticky=W)

delete_project_title_label = ttk.Label(delete_frame, text="Delete Project Title:")
delete_project_title_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

delete_project_title_entry = ttk.Entry(delete_frame)
delete_project_title_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = ttk.Button(delete_frame, text="Delete", command=delete_project)
delete_button.grid(row=0, column=2, padx=5, pady=5)

# Insert button
insert_button = ttk.Button(root, text="Insert Data", command=insert_project)
insert_button.grid(row=11, column=1, padx=10, pady=10)

# Update button
update_button = ttk.Button(root, text="Update Data", command=update_project)
update_button.grid(row=11, column=2, padx=10, pady=10)

# Treeview to display data
tree = ttk.Treeview(root, columns=("project_title", "PPRA_no", "project_length", "cost", "project_status", "project_type", "Completion_Date", "Physical_Progress", "Financial_Progress", "PD_Name", "PD_Email"), show="headings", height=10)
tree.grid(row=12, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)

tree.heading("project_title", text="Project Title")
tree.heading("PPRA_no", text="PPRA No")
tree.heading("project_length", text="Project Length")
tree.heading("cost", text="Cost")
tree.heading("project_status", text="Project Status")
tree.heading("project_type", text="Project Type")
tree.heading("Completion_Date", text="Completion Date")
tree.heading("Physical_Progress", text="Physical Progress")
tree.heading("Financial_Progress", text="Financial Progress")
tree.heading("PD_Name", text="PD Name")
tree.heading("PD_Email", text="PD Email")

tree.bind('<<TreeviewSelect>>', on_tree_select)

window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window

# Configure column weights for Treeview
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Display initial data
display_projects()

# Start the main loop
root.mainloop()
