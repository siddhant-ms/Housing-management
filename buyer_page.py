import tkinter as tk

from search import search_properties
from pprint import pprint

def buyer_page():
    ## updates the slider label
    def update_budget_label(value):
        value = int(value)
        if value >= 10000000:
            budget_min_label.config(text=f"₹ {value // 10000000} Cr")
        elif value >= 100000:
            budget_min_label.config(text=f"₹ {value // 100000} L")
        elif value >= 1000:
            budget_min_label.config(text=f"₹ {value // 1000} k")
        else:
            budget_min_label.config(text=f"₹ {value}")

    def update_rent_label(value):
        value = int(value)
        if value >= 10000000:
            rent_min_label.config(text=f"₹ {value // 10000000} Cr")
        elif value >= 100000:
            rent_min_label.config(text=f"₹ {value // 100000} L")
        elif value >= 1000:
            rent_min_label.config(text=f"₹ {value // 1000} k")
        else:
            rent_min_label.config(text=f"₹ {value}")

    ## switches between rent and buy slider
    def show_slider():
        if looking_var.get() == "Rent":
            rent_range.config(from_=0, to=100000, resolution=1000)
            rent_min_label.config(text="₹ 0")
            rent_max_label.config(text="₹ 1L")

            rent_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
            rent_range.grid(row=12, column=0, columnspan=2, padx=20, pady=5, sticky="we")
            rent_min_label.grid(row=13, column=0, padx=20, pady=5, sticky="w")
            rent_max_label.grid(row=13, column=1, padx=20, pady=5, sticky="e")

            budget_label.grid_remove()
            budget_range.grid_remove()
            budget_min_label.grid_remove()
            budget_max_label.grid_remove()

        elif looking_var.get() == "Buy":
            budget_range.config(from_=0, to=150000000, resolution=1000000)
            budget_min_label.config(text="₹ 0")
            budget_max_label.config(text="₹ 15 Cr")

            budget_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
            budget_range.grid(row=12, column=0, columnspan=2, padx=20, pady=5, sticky="we")
            budget_min_label.grid(row=13, column=0, padx=20, pady=5, sticky="w")
            budget_max_label.grid(row=13, column=1, padx=20, pady=5, sticky="e")

            rent_label.grid_remove()
            rent_range.grid_remove()
            rent_min_label.grid_remove()
            rent_max_label.grid_remove()

    # Function to show the secondary dropdown based on the location
    def show_secondary_dropdown(*args):
        city_areas = {
            "Mumbai": ["Colaba", "Bandra", "Andheri", "Dadar", "Malad", "Worli", "Thane", "Borivali", "Goregaon", "Santacruz", "Khar", "Vile Parle"],
            "Delhi": ["Connaught Place", "Hauz Khas", "Greater Kailash", "Lajpat Nagar", "Karol Bagh", "Dwarka", "Saket", "Rohini", "Shalimar Bagh", "Chandni Chowk", "Gurgaon"],
            "Bengaluru": ["MG Road", "Marathahalli", "Indiranagar", "Koramangala", "Whitefield", "Jayanagar", "Malleshwaram", "Electronic City", "HSR Layout", "Bellandur", "Rajajinagar", "Yelahanka", "Dodanakundi"],
            "Chennai": ["T Nagar", "Anna Nagar", "Mylapore", "Adyar", "Velachery", "Nungambakkam", "Alwarpet", "Triplicane", "Egmore", "Kotturpuram", "Thiruvanmiyur"],
            "Kolkata": ["Park Street", "Salt Lake City", "Ballygunge", "Behala", "Garia", "Esplanade", "North Kolkata", "Tollygunge", "Bhowanipore"],
            "Hyderabad": ["Banjara Hills", "Jubilee Hills", "Hitech City", "Kukatpally", "Madhapur", "Ameerpet", "Old City (Hyderabad)", "Sanath Nagar", "Shamirpet", "Begumpet"],
            "Pune": ["Koregaon Park", "Kalyani Nagar", "Hinjewadi", "Viman Nagar", "Sadashiv Peth", "Shivaji Nagar", "Bibwewadi", "Sangamwadi", "Hadapsar", "Balewadi"],
            "Ahmedabad": ["Naroda", "Vastrapur", "Maninagar", "Thaltej", "Bopal", "Ellis Bridge", "Navrangpura", "Chandkheda", "Anandnagar", "Shahibaug"],
            "Jaipur": ["C-Scheme", "Malviya Nagar", "Vaishali Nagar", "Mansarovar", "Raja Park", "Jhotwara", "Ajmer Road", "Sanganer", "Shastri Nagar", "Bhankrota", "Pratap Nagar"],
            "Lucknow": ["Hazratganj", "Gomti Nagar", "Alambagh", "Indiranagar", "Mahanagar", "Krishna Nagar", "Kalyanpur", "Chowk"],
            "Nagpur": ["Civil Lines", "Sitabuldi", "Sadar", "Dharampeth", "Ramdaspeth", "Manish Nagar", "Katol Road", "Hingna"],
            "Visakhapatnam": ["Beach Road", "Daba Gardens", "MVP Colony", "Gajuwaka", "Pendurthi", "Kancharapalem", "Kothapeta", "Waltair"],
            "Indore": ["Rajendra Nagar", "Vijay Nagar", "AB Road", "Bhawarkuan", "Malhar Mega Mall", "Ujjain Road", "Rau", "Banganga"],
            "Coimbatore": ["RS Puram", "Gandhipuram", "Peelamedu", "Saravanampatti", "Singanallur", "Race Course", "Vadavalli", "Kalapatti"],
            "Patna": ["Boring Road", "Kankarbagh", "Patliputra", "Gardanibagh", "Rajendra Nagar", "Bailey Road", "Mithapur", "Anisabad"]
        }

        selected_city = location_var.get()
        if selected_city in city_areas:
            secondary_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
            secondary_dropdown.grid(row=1, columnspan=2, column=1, padx=10, pady=5, sticky="ew")
            secondary_dropdown.config(bg=background_color)
            
            # emoves stuff from menu
            menu = secondary_dropdown['menu']
            menu.delete(0, 'end')
            
            # adds new cities
            for area in city_areas[selected_city]:
                menu.add_command(label=area, command=tk._setit(secondary_dropdown_var, area))

            # secondary_dropdown.set('')  # Reset to default (empty selection)
        else:
            secondary_label.grid_remove()
            secondary_dropdown.grid_remove()

        

    # Initialize Tkinter root window
    root = tk.Tk()
    root.title("Property Buying Page")
    root.geometry("")  
    background_color = "#8aa3d1"
    root.configure(bg=background_color)

    # Location dropdown (first dropdown)
    location_label = tk.Label(root, text="Location", bg=background_color)
    location_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    location_var = tk.StringVar()
    location_dropdown = tk.OptionMenu(root, location_var, "Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Nagpur", "Visakhapatnam", "Indore", "Coimbatore", "Patna")
    location_dropdown.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")  # Spanning columns 1 and 2
    location_dropdown.config(bg=background_color)

    # Adjust grid weight to allow stretching
    root.grid_columnconfigure(0, weight=0)  
    root.grid_columnconfigure(1, weight=1)  
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)  

    # Bind selection event to show_secondary_dropdown function
    location_var.trace_add("write", show_secondary_dropdown)

    # Secondary dropdown (hidden initially)
    secondary_label = tk.Label(root, text="Area:", bg=background_color)
    secondary_dropdown_var = tk.StringVar()  
    secondary_dropdown = tk.OptionMenu(root, secondary_dropdown_var, [])  # Starts with an empty list 

    # Initially hide the secondary dropdown
    secondary_label.grid_remove()
    secondary_dropdown.grid_remove()


    ## property type options (radio buttons)
    property_label = tk.Label(root, text="Property type:", bg=background_color)
    property_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    property_type_var = tk.StringVar(value="Independent")
    independent_radio = tk.Radiobutton(root, text="Independent", variable=property_type_var, value="Independent", bg=background_color)
    independent_radio.grid(row=3, column=0, padx=20, pady=2, sticky="w")

    apartment_radio = tk.Radiobutton(root, text="Apartment", variable=property_type_var, value="Apartment", bg=background_color)
    apartment_radio.grid(row=3, column=1, padx=20, pady=2, sticky="w")

    commercial_radio = tk.Radiobutton(root, text="Commercial", variable=property_type_var, value="Commercial", bg=background_color)
    commercial_radio.grid(row=3, column=2, padx=20, pady=2, sticky="w")

    # Looking to? options (radio buttons)
    looking_label = tk.Label(root, text="Looking to?", bg=background_color)
    looking_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    looking_var = tk.StringVar(value="")
    rent_radio = tk.Radiobutton(root, text="Rent", variable=looking_var, value="Rent", command=show_slider, bg=background_color)
    rent_radio.grid(row=7, column=0, padx=20, pady=2, sticky="w")

    buy_radio = tk.Radiobutton(root, text="Buy", variable=looking_var, value="Buy", command=show_slider, bg=background_color)
    buy_radio.grid(row=7, column=1, padx=20, pady=2, sticky="w")

    # Ensure equal spacing between the radio buttons
    root.grid_columnconfigure(0, weight=1, uniform="equal")
    root.grid_columnconfigure(1, weight=1, uniform="equal")
    root.grid_columnconfigure(2, weight=1, uniform="equal")

    # Budget slider (initially hidden)
    budget_label = tk.Label(root, text="Buying Budget:", bg=background_color)
    budget_range = tk.Scale(root, from_=0, to=150000000, orient=tk.HORIZONTAL, resolution=1000000, bg=background_color, troughcolor=background_color, command=update_budget_label)
    budget_min_label = tk.Label(root, text="₹ 0", bg=background_color)
    budget_max_label = tk.Label(root, text="₹ 15 Cr", bg=background_color)
    budget_label.grid_remove()
    budget_range.grid_remove()
    budget_min_label.grid_remove()
    budget_max_label.grid_remove()

    # Rent Budget slider (initially hidden)
    rent_label = tk.Label(root, text="Rent Budget:", bg=background_color)
    rent_range = tk.Scale(root, from_=0, to=10000, orient=tk.HORIZONTAL, resolution=1000, bg=background_color, troughcolor=background_color, command=update_rent_label)
    rent_min_label = tk.Label(root, text="₹ 0", bg=background_color)
    rent_max_label = tk.Label(root, text="₹ 1L", bg=background_color)
    rent_label.grid_remove()
    rent_range.grid_remove()
    rent_min_label.grid_remove()
    rent_max_label.grid_remove()

    # Always visible amenities section with checkboxes
    amenities_label = tk.Label(root, text="Property and locality Amenities:", bg=background_color)
    amenities_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")

    # Frame for checkboxes
    amenities_frame = tk.Frame(root, bg=background_color)
    amenities_frame.grid(row=15, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    # Amenities checkboxes
    amenity_var1 = tk.IntVar()
    amenity_var2 = tk.IntVar()
    amenity_var3 = tk.IntVar()
    amenity_var4 = tk.IntVar()
    amenity_var5 = tk.IntVar()
    amenity_var6 = tk.IntVar()

    lift_checkbox = tk.Checkbutton(amenities_frame, text="Lift", variable=amenity_var1, bg=background_color)
    lift_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    public_transport_checkbox = tk.Checkbutton(amenities_frame, text="Public Transport", variable=amenity_var2, bg=background_color)
    public_transport_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    hospital_checkbox = tk.Checkbutton(amenities_frame, text="Hospital", variable=amenity_var3, bg=background_color)
    hospital_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    furnished_checkbox = tk.Checkbutton(amenities_frame, text="Furnished", variable=amenity_var4, bg=background_color)
    furnished_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    gym_checkbox = tk.Checkbutton(amenities_frame, text="Gym", variable=amenity_var5, bg=background_color)
    gym_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    parking_checkbox = tk.Checkbutton(amenities_frame, text="Parking", variable=amenity_var6, bg=background_color)
    parking_checkbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    def data_dict():
        data = {}
        data['Location']=location_var.get()
        data['Area']=secondary_dropdown_var.get()
        data['Property Type']=property_type_var.get()
        data['Looking to']=looking_var.get()
        if looking_var.get()=='Buy':
            data['Budget']=budget_range.get()
        else:
            data['Budget']=rent_range.get()
        amenities=[]
        if amenity_var1.get()==1:
            amenities.append("Lift")
        if amenity_var2.get()==1:
            amenities.append("Public Transport")
        if amenity_var3.get()==1:
            amenities.append("Hospital")
        if amenity_var4.get()==1:
            amenities.append("Furnished")
        if amenity_var5.get()==1:
            amenities.append("Gym")
        if amenity_var6.get()==1:
            amenities.append("Parking")
        data['Amenities']=amenities


        pprint(data)

        search_properties(data)


    search_button = tk.Button(root, text="Search", bg="#ffffff",command=data_dict)
    search_button.grid(row=16, column=0, columnspan=2, pady=20)

    # Start the main loop
    root.mainloop()

# If the script is run directly, open the page
if __name__ == "__main__":
    buyer_page()
