

# Advanced BMI Calculator with Data Visualization

## 📋 Project Overview
This project is an advanced **Graphical User Interface (GUI)** application developed using Python. It allows users to calculate their Body Mass Index (BMI), categorizes their health status, saves the data to a local database for multiple users, and visualizes historical health trends using graphs.

This application was designed to meet specific advanced requirements including **Data Persistence (SQLite)** and **Data Visualization (Matplotlib)**.

## 🎯 Key Features (Implemented)

This project successfully implements all the advanced challenges:

1.  **User Input Validation:**
    * Validates that inputs are numeric.
    * Prevents zero or negative values for height/weight.
    * Ensures the "User Name" field is not empty before saving.

2.  **Accurate BMI Calculation:**
    * Uses the standard formula: $BMI = Weight(kg) / Height(m)^2$.
    * Results are rounded to 2 decimal places.

3.  **Health Categorization:**
    * **Underweight:** < 18.5
    * **Normal Weight:** 18.5 - 24.9 (Green)
    * **Overweight:** 25 - 29.9 (Orange)
    * **Obese:** 30+ (Red)
    * *Dynamic text coloring implemented based on category.*

4.  **Advanced GUI Design:**
    * Built with **Tkinter**.
    * Clean layout using `LabelFrames` for input grouping.
    * Responsive design that adjusts to window resizing.

5.  **Data Storage (Database):**
    * Uses **SQLite3** for persistent storage.
    * Automatically creates a `bmi_data.db` file.
    * Stores `Name`, `Weight`, `Height`, `BMI`, `Category`, and `Timestamp`.
    * Supports multiple users seamlessly.

6.  **Data Visualization:**
    * Integrated **Matplotlib** to generate trend graphs.
    * Displays a "Date vs. BMI" line graph for the selected user to track progress over time.

7.  **Error Handling:**
    * Graceful handling of database connection errors.
    * `Try-Except` blocks to prevent application crashes on invalid input.

8.  **User Experience (UX):**
    * Clear labels and instructions.
    * Popup message boxes (`MessageBox`) for success notifications and error alerts.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Library:** Tkinter (Built-in)
* **Database:** SQLite3 (Built-in)
* **Visualization:** Matplotlib


## 🚀 How to Use

1.  **Enter User Details:** Input Name, Weight (kg), and Height (m).
2.  **Calculate:** Click **"Calculate & Save"**. The result will appear on the screen, and data will be saved to the database.
3.  **Analyze Trends:** To view a graph of past records, ensure the **User Name** is filled in, then click **"View History & Trends"**.

## 👤 Author

* **Name** - Akansh Jadam
---
*Developed as part of the Python Programming assignments.*
