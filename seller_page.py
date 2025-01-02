import tkinter as tk
import mysql.connector

def seller_page():
    def get_locations_from_db():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="house_management"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT city, area FROM city_areas ORDER BY city, area")
            locations = cursor.fetchall()

            connection.close()

            states = {}
            for state, city in locations:
                if state not in states:
                    states[state] = []
                states[state].append(city)

            return states

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {}

    def show_secondary_dropdown(event):
        selected_state = location_var.get()
        if selected_state in city_areas:
            secondary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
            secondary_dropdown.grid(row=3, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
            secondary_dropdown['values'] = city_areas[selected_state]
        else:
            secondary_label.grid_remove()
            secondary_dropdown.grid_remove()

    def update_price_slider(selected_option):
        if selected_option == "Sell":
            price_slider_label.config(text="SELL PRICE")
            price_slider.config(troughcolor=background_color,from_=1000000, to=500000000, resolution=1000000, command=update_price_label)
            update_price_label(price_slider.get())
        elif selected_option == "Rent":
            price_slider_label.config(text="RENT PRICE")
            price_slider.config(troughcolor=background_color,from_=5000, to=50000, resolution=500, command=update_price_label)
            update_price_label(price_slider.get())

    def update_price_label(value):
        value = int(value)
        if value >= 10000000:
            price_value_label.config(text=f"₹ {value / 10000000} Cr")
        elif value >= 100000:
            price_value_label.config(text=f"₹ {value / 100000} L")
        elif value >= 1000:
            price_value_label.config(text=f"₹ {value / 1000} k")
        else:
            price_value_label.config(text=f"₹ {value}")

    city_areas = get_locations_from_db()

    root = tk.Tk()
    background_color = "#8aa3d1"
    root.configure(bg=background_color)
    root.title("Property Form")

    main_frame = tk.Frame(root, bg=background_color)
    main_frame.pack(fill=tk.BOTH, expand=1)

    property_type_var = tk.StringVar()
    looking_to_var = tk.StringVar()
    bhk_var = tk.StringVar()
    location_var = tk.StringVar()

    left_frame = tk.Frame(main_frame, bg=background_color)
    left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    tk.Label(left_frame, text="NAME", bg=background_color).grid(row=0, column=0, sticky='w', padx=10, pady=5)
    name_entry = tk.Entry(left_frame)
    name_entry.grid(row=0, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    tk.Label(left_frame, text="PROPERTY TYPE", bg=background_color).grid(row=1, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="Independent", variable=property_type_var, value="Independent", bg=background_color).grid(row=1, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Apartment", variable=property_type_var, value="Apartment", bg=background_color).grid(row=1, column=2, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Commercial", variable=property_type_var, value="Commercial", bg=background_color).grid(row=1, column=3, sticky='w', padx=10)

    # Label for Location dropdown
    location_label = tk.Label(left_frame, text="LOCATION", bg=background_color)
    location_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    # Location dropdown with OptionMenu
    location_var = tk.StringVar()
    location_dropdown = tk.OptionMenu(left_frame, location_var, *city_areas.keys())
    location_dropdown.configure(bg=background_color)
    location_dropdown.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    # Label for Area dropdown (secondary dropdown) - hidden initially
    secondary_label = tk.Label(left_frame, text="AREA", bg=background_color)
    secondary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    secondary_label.grid_remove()  # Hide initially

    # Secondary dropdown (area dropdown) - hidden initially
    secondary_var = tk.StringVar()
    secondary_dropdown = tk.OptionMenu(left_frame, secondary_var, "")
    secondary_dropdown.configure(bg=background_color)
    secondary_dropdown.grid(row=3, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
    secondary_dropdown.grid_remove()  # Hide initially

    # Function to update the secondary dropdown based on the location selected
    def show_secondary_dropdown(*args):  # Accepting *args to match the event binding
        selected_location = location_var.get()
        if selected_location in city_areas and city_areas[selected_location]:
            # Show the secondary label and dropdown
            secondary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
            secondary_dropdown.grid(row=3, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
            
            # Update the secondary dropdown with areas based on the selected location
            secondary_dropdown['menu'].delete(0, 'end')  # Clear the old values
            for area in city_areas[selected_location]:
                secondary_dropdown['menu'].add_command(label=area, command=tk._setit(secondary_var, area))
        else:
            # Hide the secondary label and dropdown if no valid location is selected
            secondary_label.grid_remove()
            secondary_dropdown.grid_remove()

    # Bind the location dropdown to the function that updates the secondary dropdown
    location_var.trace("w", show_secondary_dropdown)  # Listen for changes in location_var

    tk.Label(left_frame, text="PROPERTY NAME", bg=background_color).grid(row=4, column=0, sticky='w', padx=10, pady=5)
    property_name_entry = tk.Entry(left_frame)
    property_name_entry.grid(row=4, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    tk.Label(left_frame, text="LOOKING TO", bg=background_color).grid(row=5, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="Sell", variable=looking_to_var, value="Sell", bg=background_color, command=lambda: update_price_slider('Sell')).grid(row=5, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Rent", variable=looking_to_var, value="Rent", bg=background_color, command=lambda: update_price_slider('Rent')).grid(row=5, column=2, sticky='w', padx=10)

    price_slider_label = tk.Label(left_frame, text="", bg=background_color)
    price_slider_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

    price_slider = tk.Scale(left_frame, from_=0, to=0, resolution=1000, orient="horizontal", bg=background_color)
    price_slider.grid(row=6, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    price_value_label = tk.Label(left_frame, text="", bg=background_color)
    price_value_label.grid(row=7, column=1, columnspan=3, sticky="w", padx=10, pady=5)

    update_price_slider("Sell")  # Default to "Sell"

    tk.Label(left_frame, text="BHK", bg=background_color).grid(row=8, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="1 BHK", variable=bhk_var, value="1 BHK", bg=background_color).grid(row=8, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="2 BHK", variable=bhk_var, value="2 BHK", bg=background_color).grid(row=8, column=2, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="3 BHK", variable=bhk_var, value="3 BHK", bg=background_color).grid(row=8, column=3, sticky='w', padx=10)

    tk.Label(left_frame, text="SQ FT", bg=background_color).grid(row=9, column=0, sticky='w', padx=10, pady=5)
    sq_ft_entry = tk.Entry(left_frame)
    sq_ft_entry.grid(row=9, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    tk.Label(left_frame, text="Amenities", bg=background_color).grid(row=10, column=0, sticky='w', padx=10, pady=5)
    amenities_frame = tk.Frame(left_frame, bg=background_color)
    amenities_frame.grid(row=11, column=0, columnspan=4, padx=10, pady=5)

    tk.Checkbutton(amenities_frame, text="Lift", bg=background_color).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Parking", bg=background_color).grid(row=0, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Gym", bg=background_color).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Furnished", bg=background_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Public Transport", bg=background_color).grid(row=1, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Hospital", bg=background_color).grid(row=1, column=2, padx=5, pady=5, sticky="w")

    tk.Label(left_frame, text="Description of the property", bg=background_color).grid(row=12, column=0, sticky='w', padx=10, pady=5)
    about_text = tk.Text(left_frame, height=6, wrap='word')
    about_text.grid(row=13, column=0, columnspan=4, sticky='ew', padx=10, pady=5)

    submit_button = tk.Button(main_frame, text="Submit", width=6, font=("bold", 15), bg=background_color)
    submit_button.grid(row=1, column=0, padx=10, pady=10, sticky="s")

    root.mainloop()

if __name__ == "__main__":
    seller_page()
