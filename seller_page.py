from logging import*
from logging import root
import tkinter as tk
from tkinter import messagebox
from functions import get_locations_from_db, execute_query, retrieve_current_user
from tkinter import*
import homepage



# Function to insert property data into the database
def insert_property_data(form_data):
    # Retrieve the current logged-in user (session username)
    current_user = retrieve_current_user()

    if current_user is None:
        print("No user is currently logged in.")
        return False  # If no user is logged in, do not proceed

    # Query to insert property data along with the user
    query = """
    INSERT INTO properties (phone_no, property_name, property_type, looking_to, price, bhk, sq_ft, amenities, description, city, area, user)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    amenities_str = ', '.join(form_data['amenities'])

    # Prepare the data for the query
    data = (
        form_data['phone_no'],
        form_data['property_name'],
        form_data['property_type'],
        form_data['looking_to'],
        form_data['price'],
        form_data['bhk'],
        form_data['sq_ft'],
        amenities_str,
        form_data['description'],
        form_data['location'],
        form_data['area'],
        current_user  # Add the current logged-in user here
    )

    # Call execute_query and check if it returns True (success)
    result = execute_query(query, data)

    # Debugging logs to print out the result of query execution
    if result:
        print("Property data inserted successfully.")
        return True  # Success
    else:
        print("Failed to insert property data.")
        return False  # Failure


# Function to update the price slider and its label
# Function to update the price slider and its label
def update_price_slider(selected_option, price_slider, price_slider_label, price_value_label):
    if selected_option == "Sell":
        price_slider_label.config(text="SELL PRICE")
        # Ensure the range goes from 0 to 15 Cr and increments in a way that fits the range
        price_slider.config(troughcolor="#8aa3d1", from_=0, to=150000000, resolution=500000, command=lambda value: update_price_label(value, price_value_label))  # 15 Cr range with no decimal
        update_price_label(price_slider.get(), price_value_label)
    elif selected_option == "Rent":
        price_slider_label.config(text="RENT PRICE")
        price_slider.config(troughcolor="#8aa3d1",from_=0, to=100000, resolution=1000, command=lambda value: update_price_label(value, price_value_label))  # 1 Lakh range
        update_price_label(price_slider.get(), price_value_label)

# Function to update the price label based on the slider value
def update_price_label(value, price_value_label):
    value = int(value)
    if value >= 10000000:
        price_value_label.config(text=f"₹ {value // 10000000} Cr")  # No decimal for Cr
    elif value >= 100000:
        price_value_label.config(text=f"₹ {value // 100000} L")  # No decimal for Lakh
    else:
        price_value_label.config(text=f"₹ {value}")  # For values less than 1 Lakh, display as is

# Function to show the secondary dropdown (area dropdown) based on the location selected
def show_secondary_dropdown(*args, location_var, city_areas, secondary_label, secondary_dropdown, secondary_var):
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

# Function to retrieve form data from the UI
def retrieve_form_data(phone_entry, property_type_var, location_var, secondary_var, property_name_entry, looking_to_var, price_slider, bhk_var, sq_ft_entry, var_lift, var_parking, var_gym, var_furnished, var_public_transport, var_hospital, about_text):
    # Retrieving the data from each widget
    phone_no = phone_entry.get()
    property_type = property_type_var.get()
    location = location_var.get()
    area = secondary_var.get()
    property_name = property_name_entry.get()
    looking_to = looking_to_var.get()
    price = price_slider.get()
    bhk = bhk_var.get()
    sq_ft = sq_ft_entry.get()

    # Validating fields
    if not phone_no.isdigit() or len(phone_no) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
        return

    if not property_name:
        messagebox.showerror("Error", "Please enter a property name.")
        return

    if not location or not area:
        messagebox.showerror("Error", "Please select both location and area.")
        return

    if not looking_to:
        messagebox.showerror("Error", "Please select whether you are looking to sell or rent the property.")
        return

    if price == 0:
        messagebox.showerror("Error", "Please set a price for the property.")
        return

    if not bhk:
        messagebox.showerror("Error", "Please select the number of BHK.")
        return

    if not sq_ft:
        messagebox.showerror("Error", "Please enter the square footage of the property.")
        return

    # Retrieving amenities in a list and converting it into string
    selected_amenities = []
    if var_lift.get():
        selected_amenities.append("Lift")
    if var_parking.get():
        selected_amenities.append("Parking")
    if var_gym.get():
        selected_amenities.append("Gym")
    if var_furnished.get():
        selected_amenities.append("Furnished")
    if var_public_transport.get():
        selected_amenities.append("Public Transport")
    if var_hospital.get():
        selected_amenities.append("Hospital")

    # Property description
    description = about_text.get("1.0", "end-1c")

    # Collecting all the retrieved data as a dictionary
    form_data = {
        "phone_no": phone_no,
        "property_type": property_type,
        "location": location,
        "area": area,
        "property_name": property_name,
        "looking_to": looking_to,
        "price": price,
        "bhk": bhk,
        "sq_ft": sq_ft,
        "amenities": selected_amenities,
        "description": description
    }

    # Insert property data
    success = insert_property_data(form_data)

    if success:
        # If insertion is successful, show a success message
        messagebox.showinfo("Success", "Property data inserted successfully.")
    else:
        # If insertion fails, show an error message
        messagebox.showerror("Error", "Failed to insert property data.")



# Function to set up the seller page UI and its interactions
def seller_page(proot):
    proot.destroy()
    # Retrieve city and areas data from DB
    global city_areas
    city_areas = get_locations_from_db()

    # Set up the main window
    root = tk.Tk()
    background_color = "#8aa3d1"
    root.configure(bg=background_color)
    root.title("Property Form")

    # Main frame to hold everything
    main_frame = tk.Frame(root, bg=background_color)
    main_frame.pack(fill=tk.BOTH, expand=1)

    # Define variable storage for form fields
    property_type_var = tk.StringVar()
    looking_to_var = tk.StringVar()
    bhk_var = tk.StringVar()
    location_var = tk.StringVar()

    # Left frame for property form
    left_frame = tk.Frame(main_frame, bg=background_color)
    left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    tk.Label(left_frame, text="PHONE NUMBER", bg=background_color).grid(row=0, column=0, sticky='w', padx=10, pady=5)
    phone_entry = tk.Entry(left_frame)
    phone_entry.grid(row=0, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    tk.Label(left_frame, text="PROPERTY TYPE", bg=background_color).grid(row=1, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="Independent", variable=property_type_var, value="Independent", bg=background_color).grid(row=1, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Apartment", variable=property_type_var, value="Apartment", bg=background_color).grid(row=1, column=2, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Commercial", variable=property_type_var, value="Commercial", bg=background_color).grid(row=1, column=3, sticky='w', padx=10)

    # Location dropdown
    location_label = tk.Label(left_frame, text="LOCATION", bg=background_color)
    location_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    location_dropdown = tk.OptionMenu(left_frame, location_var, *city_areas.keys())
    location_dropdown.configure(bg=background_color)
    location_dropdown.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    # Secondary dropdown (hidden initially)
    secondary_label = tk.Label(left_frame, text="AREA", bg=background_color)
    secondary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    secondary_label.grid_remove()  # Hide initially
    secondary_var = tk.StringVar()
    secondary_dropdown = tk.OptionMenu(left_frame, secondary_var, "")
    secondary_dropdown.configure(bg=background_color)
    secondary_dropdown.grid(row=3, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
    secondary_dropdown.grid_remove()  # Hide initially

    # Bind the location dropdown to update the area dropdown
    location_var.trace("w", lambda *args: show_secondary_dropdown(*args, location_var=location_var, city_areas=city_areas, secondary_label=secondary_label, secondary_dropdown=secondary_dropdown, secondary_var=secondary_var))

    # Property name entry
    tk.Label(left_frame, text="PROPERTY NAME", bg=background_color).grid(row=4, column=0, sticky='w', padx=10, pady=5)
    property_name_entry = tk.Entry(left_frame)
    property_name_entry.grid(row=4, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    # Looking to sell or rent
    tk.Label(left_frame, text="LOOKING TO", bg=background_color).grid(row=5, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="Sell", variable=looking_to_var, value="Sell", bg=background_color, command=lambda: update_price_slider('Sell', price_slider, price_slider_label, price_value_label)).grid(row=5, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="Rent", variable=looking_to_var, value="Rent", bg=background_color, command=lambda: update_price_slider('Rent', price_slider, price_slider_label, price_value_label)).grid(row=5, column=2, sticky='w', padx=10)

    # Price slider and label
    price_slider_label = tk.Label(left_frame, text="", bg=background_color)
    price_slider_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
    price_slider = tk.Scale(left_frame, from_=0, to=0, resolution=1000, orient="horizontal", bg=background_color)
    price_slider.grid(row=6, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
    price_value_label = tk.Label(left_frame, text="", bg=background_color)
    price_value_label.grid(row=7, column=1, columnspan=3, sticky="w", padx=10, pady=5)
    
    # Default price slider setup
    update_price_slider("Sell", price_slider, price_slider_label, price_value_label)

    # BHK selection
    tk.Label(left_frame, text="BHK", bg=background_color).grid(row=8, column=0, sticky='w', padx=10, pady=5)
    tk.Radiobutton(left_frame, text="1 BHK", variable=bhk_var, value="1 BHK", bg=background_color).grid(row=8, column=1, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="2 BHK", variable=bhk_var, value="2 BHK", bg=background_color).grid(row=8, column=2, sticky='w', padx=10)
    tk.Radiobutton(left_frame, text="3 BHK", variable=bhk_var, value="3 BHK", bg=background_color).grid(row=8, column=3, sticky='w', padx=10)

    # Square footage entry
    tk.Label(left_frame, text="Square Footage", bg=background_color).grid(row=9, column=0, sticky='w', padx=10, pady=5)
    sq_ft_entry = tk.Entry(left_frame)
    sq_ft_entry.grid(row=9, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

    # Amenities selection (checkboxes)
    tk.Label(left_frame, text="Amenities", bg=background_color).grid(row=10, column=0, sticky='w', padx=10, pady=5)
    amenities_frame = tk.Frame(left_frame, bg=background_color)
    amenities_frame.grid(row=11, column=0, columnspan=4, padx=10, pady=5)

    var_lift = tk.BooleanVar()
    var_parking = tk.BooleanVar()
    var_gym = tk.BooleanVar()
    var_furnished = tk.BooleanVar()
    var_public_transport = tk.BooleanVar()
    var_hospital = tk.BooleanVar()

    # Checkbuttons for amenities
    tk.Checkbutton(amenities_frame, text="Lift", variable=var_lift, bg=background_color).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Parking", variable=var_parking, bg=background_color).grid(row=0, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Gym", variable=var_gym, bg=background_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Furnished", variable=var_furnished, bg=background_color).grid(row=1, column=1, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Public Transport", variable=var_public_transport, bg=background_color).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tk.Checkbutton(amenities_frame, text="Hospital", variable=var_hospital, bg=background_color).grid(row=2, column=1, padx=5, pady=5, sticky="w")

    
    
    # Property description text field
    tk.Label(left_frame, text="About the property", bg=background_color).grid(row=12, column=0, sticky="w", padx=10, pady=5)
    about_text = tk.Text(left_frame, height=5, wrap="word", bg=background_color)
    about_text.grid(row=13, column=0, columnspan=4, padx=10, pady=5)

    # Submit button
    submit_button = tk.Button(left_frame, text="Submit", bg="#6a7e98", command=lambda: retrieve_form_data(phone_entry, property_type_var, location_var, secondary_var, property_name_entry, looking_to_var, price_slider, bhk_var, sq_ft_entry, var_lift, var_parking, var_gym, var_furnished, var_public_transport, var_hospital, about_text))
    submit_button.grid(row=14, column=1, columnspan=1, padx=20, pady=20, sticky="e")

	# Back button			
    back_button = tk.Button(left_frame, text="Back", bg="#6a7e98", command=lambda: back_to_home(root))
    back_button.grid(row=14, column=0, columnspan=1, padx=20, pady=20, sticky="w")

    
# Function to navigate back to home page
def back_to_home(seller_page):
    seller_page.destroy()  # Destroy the current window
   
    # Call the function to display the home page
    homepage.show_main_window()
    
    root.mainloop()
     
if __name__ == "__main__":
    seller_page()  # Pass proot as an argument when calling seller_page()
