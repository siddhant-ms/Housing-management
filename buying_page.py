import tkinter as tk
from tkinter import ttk

# Function to update the budget value label
def update_budget_label(value):
    value = int(value)
    if value >= 10000000:  # 1 crore = 10,00,000
        budget_min_label.config(text=f"{value // 10000000} Cr")  # Convert to crores
    elif value >= 100000:  # 1 lakh = 1,00,000
        budget_min_label.config(text=f"{value // 100000} L")  # Convert to lakhs
    elif value >= 1000:  # 1 thousand = 1,000
        budget_min_label.config(text=f"{value // 1000} k")  # Convert to thousands
    else:
        budget_min_label.config(text=f"{value}")

# Function to update the rent value label
def update_rent_label(value):
    value = int(value)
    if value >= 10000000:  # 1 crore = 10,00,000
        rent_min_label.config(text=f"{value // 10000000} Cr")  # Convert to crores
    elif value >= 100000:  # 1 lakh = 1,00,000
        rent_min_label.config(text=f"{value // 100000} L")  # Convert to lakhs
    elif value >= 1000:  # 1 thousand = 1,000
        rent_min_label.config(text=f"{value // 1000} k")  # Convert to thousands
    else:
        rent_min_label.config(text=f"{value}")

# Function to show the appropriate slider based on the selection
def show_slider():
    if looking_var.get() == "Rent":
        # Show the Rent Budget slider
        rent_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        rent_range.grid(row=12, column=0, columnspan=2, padx=20, pady=5, sticky="we")
        rent_min_label.grid(row=13, column=0, padx=20, pady=5, sticky="w")
        rent_max_label.grid(row=13, column=1, padx=20, pady=5, sticky="e")
        
        # Hide the Buy Budget slider
        budget_label.grid_remove()
        budget_range.grid_remove()
        budget_min_label.grid_remove()
        budget_max_label.grid_remove()
    elif looking_var.get() == "Buy":
        # Show the Buy Budget slider
        budget_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        budget_range.grid(row=9, column=0, columnspan=2, padx=20, pady=5, sticky="we")
        budget_min_label.grid(row=10, column=0, padx=20, pady=5, sticky="w")
        budget_max_label.grid(row=10, column=1, padx=20, pady=5, sticky="e")
        
        # Hide the Rent Budget slider
        rent_label.grid_remove()
        rent_range.grid_remove()
        rent_min_label.grid_remove()
        rent_max_label.grid_remove()

# Initialize the main window
root = tk.Tk()
root.title("Property Buying Page")
background_color = "#8aa3d1"
root.configure(bg=background_color)

# Configure style for ttk widgets to match background color
style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox", background=background_color, fieldbackground=background_color)

# Location dropdown
location_label = tk.Label(root, text="Location", bg=background_color)
location_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

location_var = tk.StringVar()
location_dropdown = ttk.Combobox(root, textvariable=location_var, style="TCombobox")
location_dropdown['values'] = ["Location 1", "Location 2", "Location 3"]  # Replace with actual locations
location_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Property type options (radio buttons)
property_label = tk.Label(root, text="Property type:", bg=background_color)
property_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

property_type_var = tk.StringVar(value="Independent")  # Default selection
independent_radio = tk.Radiobutton(root, text="Independent", variable=property_type_var, value="Independent", bg=background_color)
independent_radio.grid(row=2, column=0, padx=20, pady=2, sticky="w")

apartment_radio = tk.Radiobutton(root, text="Apartment", variable=property_type_var, value="Apartment", bg=background_color)
apartment_radio.grid(row=3, column=0, padx=20, pady=2, sticky="w")

commercial_radio = tk.Radiobutton(root, text="Commercial", variable=property_type_var, value="Commercial", bg=background_color)
commercial_radio.grid(row=4, column=0, padx=20, pady=2, sticky="w")

# Looking to? options (radio buttons)
looking_label = tk.Label(root, text="Looking to?", bg=background_color)
looking_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

looking_var = tk.StringVar(value="")  # No default selection
rent_radio = tk.Radiobutton(root, text="Rent", variable=looking_var, value="Rent", command=show_slider, bg=background_color)
rent_radio.grid(row=6, column=0, padx=20, pady=2, sticky="w")

buy_radio = tk.Radiobutton(root, text="Buy", variable=looking_var, value="Buy", command=show_slider, bg=background_color)
buy_radio.grid(row=7, column=0, padx=20, pady=2, sticky="w")

# Budget slider (initially hidden)
budget_label = tk.Label(root, text="Budget:", bg=background_color)
budget_range = tk.Scale(root, from_=0, to=100000000, orient=tk.HORIZONTAL, resolution=1000000, bg=background_color, troughcolor=background_color, command=update_budget_label)
budget_min_label = tk.Label(root, text="0", bg=background_color)
budget_max_label = tk.Label(root, text="10 Cr", bg=background_color)
budget_label.grid_remove()
budget_range.grid_remove()
budget_min_label.grid_remove()
budget_max_label.grid_remove()

# Rent Budget slider (initially hidden)
rent_label = tk.Label(root, text="Rent Budget:", bg=background_color)
rent_range = tk.Scale(root, from_=0, to=50000, orient=tk.HORIZONTAL, resolution=1000, bg=background_color, troughcolor=background_color, command=update_rent_label)
rent_min_label = tk.Label(root, text="0", bg=background_color)
rent_max_label = tk.Label(root, text="50k", bg=background_color)
rent_label.grid_remove()
rent_range.grid_remove()
rent_min_label.grid_remove()
rent_max_label.grid_remove()

# Search button
search_button = tk.Button(root, text="Search", bg="#ffffff", command=lambda: print("Search initiated"))
search_button.grid(row=14, column=0, columnspan=2, pady=20)

# Start the main loop
root.mainloop()
