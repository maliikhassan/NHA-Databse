import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

def Toll_Taxes_update():
    display_toll_taxes()
    on_tree_select()
    update_toll_tax()
# Function to insert data into tollTaxes table
def insert_toll_tax():
    sr_no = sr_no_entry.get()
    road_name = road_name_entry.get()
    road_distance = road_distance_entry.get()
    ppra_no = ppra_no_entry.get()
    car = car_entry.get()
    wagon = wagon_entry.get()
    minibus = minibus_entry.get()
    bus = bus_entry.get()
    two_three_axle_truck = two_three_axle_truck_entry.get()
    articulated_truck = articulated_truck_entry.get()

    if not sr_no or not road_name or not road_distance or not ppra_no or not car or not wagon or not minibus or not bus or not two_three_axle_truck or not articulated_truck:
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
        sql_insert_query = """INSERT INTO tollTaxes (srNo, road_name, road_distance, PPRA_no, Car, Wagon, MiniBus, Bus, TwoThreeAxleTruck, articulatedTruck) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (sr_no, road_name, road_distance, ppra_no, car, wagon, minibus, bus, two_three_axle_truck, articulated_truck))
        connection.commit()
        messagebox.showinfo("Success", "Data submitted successfully")
        display_toll_taxes()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to search data in tollTaxes table by srNo
def search_toll_tax():
    sr_no = search_sr_no_entry.get()

    if not sr_no:
        messagebox.showwarning("Input Error", "Please enter an SR No to search")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_search_query = """SELECT * FROM tollTaxes WHERE srNo = %s"""
        cursor.execute(sql_search_query, (sr_no,))
        result = cursor.fetchone()
        
        if result:
            result_label.config(text=f"SR No: {result[0]}\nRoad Name: {result[1]}\nRoad Distance: {result[2]}\nPPRA No: {result[3]}\nCar: {result[4]}\nWagon: {result[5]}\nMiniBus: {result[6]}\nBus: {result[7]}\nTwoThreeAxleTruck: {result[8]}\nArticulated Truck: {result[9]}")
        else:
            result_label.config(text="No record found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to delete data from tollTaxes table by srNo
def delete_toll_tax():
    sr_no = delete_sr_no_entry.get()

    if not sr_no:
        messagebox.showwarning("Input Error", "Please enter an SR No to delete")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM tollTaxes WHERE srNo = %s"""
        cursor.execute(sql_delete_query, (sr_no,))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Info", "No record found with the given SR No")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")
            display_toll_taxes()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to update data in tollTaxes table
def update_toll_tax():
    sr_no = sr_no_entry.get()

    if not sr_no:
        messagebox.showwarning("No Item Selected", "Please select a record to update")
        return

    road_name = road_name_entry.get()
    road_distance = road_distance_entry.get()
    ppra_no = ppra_no_entry.get()
    car = car_entry.get()
    wagon = wagon_entry.get()
    minibus = minibus_entry.get()
    bus = bus_entry.get()
    two_three_axle_truck = two_three_axle_truck_entry.get()
    articulated_truck = articulated_truck_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='eshna 123@',
            database='nha_database'
        )
        cursor = connection.cursor()
        sql_update_query = """UPDATE tollTaxes SET road_name = %s, road_distance = %s, PPRA_no = %s, Car = %s, Wagon = %s, MiniBus = %s, Bus = %s, TwoThreeAxleTruck = %s, articulatedTruck = %s WHERE srNo = %s"""
        cursor.execute(sql_update_query, (road_name, road_distance, ppra_no, car, wagon, minibus, bus, two_three_axle_truck, articulated_truck, sr_no))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully")
        display_toll_taxes()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Function to handle row selection in Treeview
def on_tree_select(event):
    selected_item = tree.selection()[0]
    selected_data = tree.item(selected_item, 'values')
    sr_no_entry.delete(0, END)
    sr_no_entry.insert(0, selected_data[0])
    road_name_entry.delete(0, END)
    road_name_entry.insert(0, selected_data[1])
    road_distance_entry.delete(0, END)
    road_distance_entry.insert(0, selected_data[2])
    ppra_no_entry.delete(0, END)
    ppra_no_entry.insert(0, selected_data[3])
    car_entry.delete(0, END)
    car_entry.insert(0, selected_data[4])
    wagon_entry.delete(0, END)
    wagon_entry.insert(0, selected_data[5])
    minibus_entry.delete(0, END)
    minibus_entry.insert(0, selected_data[6])
    bus_entry.delete(0, END)
    bus_entry.insert(0, selected_data[7])
    two_three_axle_truck_entry.delete(0, END)
    two_three_axle_truck_entry.insert(0, selected_data[8])
    articulated_truck_entry.delete(0, END)
    articulated_truck_entry.insert(0, selected_data[9])

# Function to display data from tollTaxes table in Treeview
def display_toll_taxes():
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
        cursor.execute("SELECT * FROM tollTaxes")
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
root.title("Toll Taxes Data Management")
root.configure(bg="#2c3e50")

# Define styles
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Arial", 12))
style.configure("TButton", background="#2980b9", foreground="white", font=("Arial", 12, "bold"), padding=6)
style.configure("TEntry", font=("Arial", 12), padding=6)
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
style.configure("Treeview", font=("Arial", 12), rowheight=25, background="#ecf0f1", foreground="#2c3e50", fieldbackground="#ecf0f1")

# Define widgets
sr_no_label = ttk.Label(root, text="SR No")
sr_no_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
sr_no_entry = ttk.Entry(root)
sr_no_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=10, sticky=W)

road_name_label = ttk.Label(root, text="Road Name")
road_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
road_name_entry = ttk.Entry(root)
road_name_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=10, sticky=W)

road_distance_label = ttk.Label(root, text="Road Distance")
road_distance_label.grid(row=2, column=0, padx=10, pady=5, sticky=E)
road_distance_entry = ttk.Entry(root)
road_distance_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=10, sticky=W)

ppra_no_label = ttk.Label(root, text="PPRA No")
ppra_no_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)
ppra_no_entry = ttk.Entry(root)
ppra_no_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=10, sticky=W)

car_label = ttk.Label(root, text="Car")
car_label.grid(row=4, column=0, padx=10, pady=5, sticky=E)
car_entry = ttk.Entry(root)
car_entry.grid(row=4, column=1, padx=10, pady=5, ipadx=10, sticky=W)

wagon_label = ttk.Label(root, text="Wagon")
wagon_label.grid(row=5, column=0, padx=10, pady=5, sticky=E)
wagon_entry = ttk.Entry(root)
wagon_entry.grid(row=5, column=1, padx=10, pady=5, ipadx=10, sticky=W)

minibus_label = ttk.Label(root, text="MiniBus")
minibus_label.grid(row=6, column=0, padx=10, pady=5, sticky=E)
minibus_entry = ttk.Entry(root)
minibus_entry.grid(row=6, column=1, padx=10, pady=5, ipadx=10, sticky=W)

bus_label = ttk.Label(root, text="Bus")
bus_label.grid(row=7, column=0, padx=10, pady=5, sticky=E)
bus_entry = ttk.Entry(root)
bus_entry.grid(row=7, column=1, padx=10, pady=5, ipadx=10, sticky=W)

two_three_axle_truck_label = ttk.Label(root, text="2/3 Axle Truck")
two_three_axle_truck_label.grid(row=8, column=0, padx=10, pady=5, sticky=E)
two_three_axle_truck_entry = ttk.Entry(root)
two_three_axle_truck_entry.grid(row=8, column=1, padx=10, pady=5, ipadx=10, sticky=W)

articulated_truck_label = ttk.Label(root, text="Articulated Truck")
articulated_truck_label.grid(row=9, column=0, padx=10, pady=5, sticky=E)
articulated_truck_entry = ttk.Entry(root)
articulated_truck_entry.grid(row=9, column=1, padx=10, pady=5, ipadx=10, sticky=W)

# Search by SR No section
search_frame = Frame(root, bg="#34495e", padx=10, pady=10)
search_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky=W)

search_sr_no_label = ttk.Label(search_frame, text="Search SR No:")
search_sr_no_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

search_sr_no_entry = ttk.Entry(search_frame)
search_sr_no_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = ttk.Button(search_frame, text="Search", command=search_toll_tax)
search_button.grid(row=0, column=2, padx=5, pady=5)

result_label = Label(search_frame, text="", padx=10, pady=10, bg="#34495e", fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Delete by SR No section
delete_frame = Frame(root, bg="#34495e", padx=10, pady=10)
delete_frame.grid(row=2, column=2, rowspan=2, padx=10, pady=5, sticky=W)

delete_sr_no_label = ttk.Label(delete_frame, text="Delete SR No:")
delete_sr_no_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

delete_sr_no_entry = ttk.Entry(delete_frame)
delete_sr_no_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = ttk.Button(delete_frame, text="Delete", command=delete_toll_tax)
delete_button.grid(row=0, column=2, padx=5, pady=5)

# Insert button
insert_button = ttk.Button(root, text="Insert Data", command=insert_toll_tax)
insert_button.grid(row=10, column=1, padx=10, pady=10)

# Update button
update_button = ttk.Button(root, text="Update Data", command=update_toll_tax)
update_button.grid(row=10, column=2, padx=10, pady=10)

# Treeview to display data
tree = ttk.Treeview(root, columns=("srNo", "road_name", "road_distance", "PPRA_no", "Car", "Wagon", "MiniBus", "Bus", "TwoThreeAxleTruck", "ArticulatedTruck"), show="headings", height=10)
tree.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)

tree.heading("srNo", text="SR No")
tree.heading("road_name", text="Road Name")
tree.heading("road_distance", text="Road Distance")
tree.heading("PPRA_no", text="PPRA No")
tree.heading("Car", text="Car")
tree.heading("Wagon", text="Wagon")
tree.heading("MiniBus", text="MiniBus")
tree.heading("Bus", text="Bus")
tree.heading("TwoThreeAxleTruck", text="2/3 Axle Truck")
tree.heading("ArticulatedTruck", text="Articulated Truck")

tree.bind('<<TreeviewSelect>>', on_tree_select)

window_width = int(root.winfo_screenwidth() * 0.99)
window_height = int(root.winfo_screenheight() * 0.9)
root.geometry(f"{int(window_width)}x{int(window_height)}+{int((root.winfo_screenwidth() - window_width) / 2)}+{int((root.winfo_screenheight() - window_height) / 2)}")  # Centered window
# Configure column weights for Treeview
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Display initial data
display_toll_taxes()

# Start the main loop
root.mainloop()
