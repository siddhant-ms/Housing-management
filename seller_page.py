import tkinter as tk
from tkinter import ttk

def update_property_name_field(*args):
    # Enable property name field only for "Apartment" and "Commercial"
    if property_type_var.get() in ["Apartment", "Commercial"]:
        property_name_entry.config(state='normal')
    else:
        property_name_entry.config(state='disabled')


# Create main window
root = tk.Tk()
root.title("Property Form")
root.configure(bg="#b51919")

# Set window size to fit the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Create main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Create left frame for the form
left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create form elements
ttk.Label(left_frame, text="NAME").grid(row=0, column=0, sticky='w', padx=10, pady=5)
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=0, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

ttk.Label(left_frame, text="PROPERTY TYPE").grid(row=1, column=0, sticky='w', padx=10, pady=5)
property_type_var = tk.StringVar()### stores the type of prop selected
property_type_var.trace("w", update_property_name_field)
ttk.Radiobutton(left_frame, text="Independent", variable=property_type_var, value="Independent").grid(row=1, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Apartment", variable=property_type_var, value="Apartment").grid(row=1, column=2, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Commercial", variable=property_type_var, value="Commercial").grid(row=1, column=3, sticky='w', padx=10)

ttk.Label(left_frame, text="PROPERTY NAME").grid(row=2, column=0, sticky='w', padx=10, pady=5)
property_name_entry = ttk.Entry(left_frame)
property_name_entry.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
property_name_entry.config(state='disabled')  # Initially disabled

ttk.Label(left_frame, text="LOOKING TO").grid(row=3, column=0, sticky='w', padx=10, pady=5)
looking_to_var = tk.StringVar()
ttk.Radiobutton(left_frame, text="Sell", variable=looking_to_var, value="Sell").grid(row=3, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Rent", variable=looking_to_var, value="Rent").grid(row=3, column=2, sticky='w', padx=10)

ttk.Label(left_frame, text="PRICE").grid(row=4, column=0, sticky='w', padx=10, pady=5)
price_entry = ttk.Entry(left_frame)
price_entry.grid(row=4, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

ttk.Label(left_frame, text="BHK").grid(row=5, column=0, sticky='w', padx=10, pady=5)
bhk_var = tk.StringVar()
ttk.Radiobutton(left_frame, text="1 BHK", variable=bhk_var, value="1 BHK").grid(row=5, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="2 BHK", variable=bhk_var, value="2 BHK").grid(row=5, column=2, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="3 BHK", variable=bhk_var, value="3 BHK").grid(row=5, column=3, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="4 BHK+", variable=bhk_var, value="4 BHK+").grid(row=5, column=4, sticky='w', padx=10)

ttk.Label(left_frame, text="SQ FT").grid(row=6, column=0, sticky='w', padx=10, pady=5)
sq_ft_entry = ttk.Entry(left_frame)
sq_ft_entry.grid(row=6, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()



