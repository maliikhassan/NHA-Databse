import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

def Power_and_Duties_update():
    display_power_duties()
    load_selected_record()
    update_power_duties()
# Function to insert data into PowerDuties table
def insert_power_duties():
    section = section_entry.get()
    section_allocation = section_allocation_entry.get()
    power_duty_name = power_duty_name_entry.get()
    person_responsible = person_responsible_entry.get()

    if not section or not section_allocation or not power_duty_name or not person_responsible:
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
        sql_insert_query = """INSERT INTO PowerDuties (section, sectionAllocation, power_duty_name, person_Responsible) 
                            VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (section, section_allocation, power_duty_name, person_responsible))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_power_duties()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to display data from PowerDuties table in Treeview
def display_power_duties():
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
        cursor.execute("SELECT * FROM PowerDuties")
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

# Function to search data in PowerDuties table by Section
def search_power_duties():
    section = search_section_entry.get()

    if not section:
        messagebox.showwarning("Input Error", "Please enter a Section to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database' 
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM PowerDuties WHERE section = %s"""
        cursor.execute(sql_search_query, (section,))
        result = cursor.fetchone()

        if result:
            result_label.config(text=f"Section: {result[0]}\nSection Allocation: {result[1]}\nPower Duty Name: {result[2]}\nPerson Responsible: {result[3]}")
        else:
            result_label.config(text="No record found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to delete data from PowerDuties table by Section
def delete_power_duties():
    section = delete_section_entry.get()

    if not section:
        messagebox.showwarning("Input Error", "Please enter a Section to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database' 
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM PowerDuties WHERE section = %s"""
        cursor.execute(sql_delete_query, (section,))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given Section")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_power_duties()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to update data in PowerDuties table
def update_power_duties():
    selected_item = tree.focus()
    values = tree.item(selected_item, "values")

    if not values:
        messagebox.showwarning("No Item Selected", "Please select a record to update")
        return

    section = values[0]
    section_allocation = section_allocation_entry.get()
    power_duty_name = power_duty_name_entry.get()
    person_responsible = person_responsible_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',  
            database='nha_database'  
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE PowerDuties SET sectionAllocation = %s, power_duty_name = %s, person_Responsible = %s WHERE section = %s"""
        cursor.execute(sql_update_query, (section_allocation, power_duty_name, person_responsible, section))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_power_duties()
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
        section_entry.delete(0, END)
        section_entry.insert(0, values[0])

        section_allocation_entry.delete(0, END)
        section_allocation_entry.insert(0, values[1])

        power_duty_name_entry.delete(0, END)
        power_duty_name_entry.insert(0, values[2])

        person_responsible_entry.delete(0, END)
        person_responsible_entry.insert(0, values[3])

# Create the main window
root = Tk()
root.title("Power Duties Data Management")
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
section_label = ttk.Label(root, text="Section")
section_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
section_entry = ttk.Entry(root)
section_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)

section_allocation_label = ttk.Label(root, text="Section Allocation")
section_allocation_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
section_allocation_entry = ttk.Entry(root)
section_allocation_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

power_duty_name_label = ttk.Label(root, text="Power Duty Name")
power_duty_name_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
power_duty_name_entry = ttk.Entry(root)
power_duty_name_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

person_responsible_label = ttk.Label(root, text="Person Responsible")
person_responsible_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)
person_responsible_entry = ttk.Entry(root)
person_responsible_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Create buttons
insert_button = ttk.Button(root, text="Submit", command=insert_power_duties)
insert_button.grid(row=4, column=0, columnspan=2, pady=10)

update_button = ttk.Button(root, text="Update", command=update_power_duties)
update_button.grid(row=4, column=2, columnspan=2, pady=10)

# Create a frame for search and delete functionalities
search_delete_frame = Frame(root, bg="#2c3e50")
search_delete_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Search functionality
search_section_label = ttk.Label(search_delete_frame, text="Search Section")
search_section_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
search_section_entry = ttk.Entry(search_delete_frame)
search_section_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)
search_button = ttk.Button(search_delete_frame, text="Search", command=search_power_duties)
search_button.grid(row=0, column=2, padx=10, pady=5)

result_label = ttk.Label(search_delete_frame, text="", background="#2c3e50", foreground="#ecf0f1")
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Delete functionality
delete_section_label = ttk.Label(search_delete_frame, text="Delete Section")
delete_section_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
delete_section_entry = ttk.Entry(search_delete_frame)
delete_section_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)
delete_button = ttk.Button(search_delete_frame, text="Delete", command=delete_power_duties)
delete_button.grid(row=2, column=2, padx=10, pady=5)

# Create Treeview
columns = ("section", "sectionAllocation", "power_duty_name", "person_Responsible")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("section", text="Section")
tree.heading("sectionAllocation", text="Section Allocation")
tree.heading("power_duty_name", text="Power Duty Name")
tree.heading("person_Responsible", text="Person Responsible")

tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

tree.bind("<<TreeviewSelect>>", load_selected_record)

window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window

# Call display_power_duties to populate the Treeview with data from the database
display_power_duties()

# Run the main loop
root.mainloop()
