import tkinter as tk
import subprocess

class NhaDatabaseApp:
    def __init__(self, master):
        self.master = master
        master.title("NHA Database Management System")

        # Configure window size and position
        window_width = master.winfo_screenwidth() * 0.99  # 90% of screen width
        window_height = master.winfo_screenheight() * 0.9  # 90% of screen height
        master.geometry(f"{int(window_width)}x{int(window_height)}+{int((master.winfo_screenwidth() - window_width) / 2)}+{int((master.winfo_screenheight() - window_height) / 2)}")  # Centered window

        # Create heading label
        self.label = tk.Label(master, text="NHA Database Management System", font=("Arial", 24))
        self.label.pack(pady=(20, 30))  # Adjusted vertical padding

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        # Create frame for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        # Button color
        button_color = "#2c3e50"  # Dark blue color

        # Create buttons
        buttons = [
            ("Project", "projects.py"),
            ("Tenders", "tenders.py"),
            ("Toll Taxes", "tolltaxes.py"),
            ("Blacklist", "blacklist.py"),
            ("Remarks", "remarks.py"),
            ("Power and Duties", "powerduties.py")
        ]

        for i, (text, file) in enumerate(buttons):
            button = tk.Button(self.button_frame, text=text, width=30, height=5,
                               font=("Arial", 16), bg=button_color, fg="white",
                               command=lambda f=file: self.open_file(f))
            button.grid(row=i // 3, column=i % 3, padx=20, pady=20)  # Use grid layout with 3 columns

    def open_file(self, filename):
        # Open the selected Python file
        try:
            subprocess.Popen(["python", filename], shell=True)
        except Exception as e:
            print(f"Error opening {filename}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NhaDatabaseApp(root)
    root.mainloop()
