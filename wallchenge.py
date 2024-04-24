import ctypes
import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import ttk

# Function to set the wallpaper using Windows API
def set_wallpaper(image_path):
    # Convert image to bitmap format and set as wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

# Function to determine if it's currently day or night
def get_time_of_day():
    now = datetime.now()
    current_hour = now.hour
    if 7 <= current_hour < 19:  # Between 7 AM and 7 PM
        return "day"
    else:
        return "night"

# Function to update the label displaying the time of day
def update_wallpaper_label(label):
    # Get the current time of day
    time_of_day = get_time_of_day()
    # Update the label text and color based on whether it's day or night
    label.config(text=time_of_day.capitalize(), foreground="blue" if time_of_day == "day" else "black")
    # Schedule the function to run again after 1 second
    label.after(1000, lambda: update_wallpaper_label(label))

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Wallpaper Changer")
    root.geometry("300x150")
    root.resizable(False, False)

    # Create a frame to hold the UI elements
    frame = ttk.Frame(root)
    frame.pack(pady=10)

    # Create a label to display whether it's day or night
    label = ttk.Label(frame, text="", font=("Helvetica", 20, "bold"))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Update the label to show the current time of day
    update_wallpaper_label(label)

    # Create a label for version information
    version_label = ttk.Label(root, text="Version 1.0")
    version_label.pack(side=tk.BOTTOM, pady=5)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
