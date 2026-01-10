# Advance BMI Calculator
# Developed by: Akansh Jadam
# Internship Task_2 - OIBSIP (Python Programming Internship)
# Date: 8/JAN/2026


import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Calculator")
        self.root.geometry("500x600")

        self.conn = sqlite3.connect('bmi_data.db')
        self.create_table()

        self.create_widgets()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT,
                weight REAL,
                height REAL,
                bmi REAL,
                category TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 11))
        style.configure("TButton", font=("Helvetica", 10, "bold"))

        # Input 
        input_frame = ttk.LabelFrame(self.root, text="New Entry", padding=20)
        input_frame.pack(pady=10, padx=10, fill="x")

        # Name
        ttk.Label(input_frame, text="User Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", pady=5)

        # Weight
        ttk.Label(input_frame, text="Weight (kg):").grid(row=1, column=0, sticky="w", pady=5)
        self.weight_entry = ttk.Entry(input_frame)
        self.weight_entry.grid(row=1, column=1, sticky="ew", pady=5)

        # Height
        ttk.Label(input_frame, text="Height (m):").grid(row=2, column=0, sticky="w", pady=5)
        self.height_entry = ttk.Entry(input_frame)
        self.height_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # Buttons
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Calculate & Save", command=self.calculate_bmi).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="View History & Trends", command=self.view_history).pack(side="left", padx=5)

        # Result Display Area
        self.result_label = ttk.Label(self.root, text="Enter details to see results", font=("Helvetica", 12, "bold"), foreground="blue")
        self.result_label.pack(pady=10)

        # Graph Area (Placeholder)
        self.graph_frame = ttk.Frame(self.root)
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def calculate_bmi(self):
        # 1. User Input Validation
        try:
            name = self.name_entry.get().strip()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if not name:
                messagebox.showerror("Input Error", "Please enter a user name.")
                return
            if height <= 0 or weight <= 0:
                messagebox.showerror("Input Error", "Height and Weight must be positive.")
                return

            # 2. BMI Calculation
            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            # 3. Categorization
            category = ""
            if bmi < 18.5:
                category = "Underweight"
                color = "orange"
            elif 18.5 <= bmi < 24.9:
                category = "Normal Weight"
                color = "green"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"

            # Update Display
            self.result_label.config(text=f"BMI: {bmi} ({category})", foreground=color)

            # 5. Data Storage
            self.save_to_db(name, weight, height, bmi, category)
            messagebox.showinfo("Success", "Record saved successfully!")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

    def save_to_db(self, name, weight, height, bmi, category):
        cursor = self.conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO records (user_name, weight, height, bmi, category, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, weight, height, bmi, category, timestamp))
        self.conn.commit()

    def view_history(self):
        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Required", "Please enter the User Name to view history.")
            return

        # Fetch data
        cursor = self.conn.cursor()
        cursor.execute("SELECT timestamp, bmi FROM records WHERE user_name = ? ORDER BY timestamp", (name,))
        data = cursor.fetchall()

        if not data:
            messagebox.showinfo("No Data", f"No records found for user: {name}")
            return

        # 6. Data Visualization
        dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in data]
        bmis = [row[1] for row in data]

        # Create Matplotlib Figure
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        ax.plot(dates, bmis, marker='o', linestyle='-', color='b')
        ax.set_title(f"BMI Trend for {name}")
        ax.set_xlabel("Date")
        ax.set_ylabel("BMI")
        ax.grid(True)
        
        # Rotate date labels
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
        fig.tight_layout()

        # Embed plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()