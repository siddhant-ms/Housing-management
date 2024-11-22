import tkinter as tk
from tkinter import ttk, filedialog


# chatgpt
def add_images():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    for file_path in file_paths:
        img = tk.PhotoImage(file=file_path)
        img = img.subsample(2, 2)  # Resize the image by subsampling
        images.append(img)
    if images:
        display_image(0)  # Display the first image after adding
        prev_button.pack(side=tk.LEFT, padx=10, pady=10)
        next_button.pack(side=tk.RIGHT, padx=10, pady=10)

def display_image(index):
    global current_image_index
    if images:
        current_image_index = index % len(images)
        image_label.configure(image=images[current_image_index])

# Function to go to the next image
def next_image():
    display_image(current_image_index + 1)

# Function to go to the previous image
def prev_image():
    display_image(current_image_index - 1)

##function to show the secondary dropdown based on the location
def show_secondary_dropdown(event):
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
        secondary_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        secondary_dropdown.grid(row=3, column=1, columnspan=3, sticky='ew', padx=10, pady=5)
        secondary_dropdown['values'] = city_areas[selected_city]
        
    else:
        secondary_label.grid_remove()
        secondary_dropdown.grid_remove()

# Create the main window
root = tk.Tk()
background_color = "#8aa3d1"
root.configure(bg=background_color)
root.title("Property Form")
root.geometry("10000x10000")  # Set a default window size

# Create the main frame to contain everything
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Configure rows and columns to be responsive
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

# Variables to hold the values of the options
property_type_var = tk.StringVar()
looking_to_var = tk.StringVar()
bhk_var = tk.StringVar()
location_var = tk.StringVar()

# Create the left frame for the form
left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create the form layout in the left frame
ttk.Label(left_frame, text="NAME").grid(row=0, column=0, sticky='w', padx=10, pady=5)
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=0, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

ttk.Label(left_frame, text="PROPERTY TYPE").grid(row=1, column=0, sticky='w', padx=10, pady=5)
ttk.Radiobutton(left_frame, text="Independent", variable=property_type_var, value="Independent").grid(row=1, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Apartment", variable=property_type_var, value="Apartment").grid(row=1, column=2, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Commercial", variable=property_type_var, value="Commercial").grid(row=1, column=3, sticky='w', padx=10)

# Location dropdown
location_label = tk.Label(left_frame, text="LOCATION")
location_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

location_dropdown = ttk.Combobox(left_frame, textvariable=location_var, state='readonly', style="TCombobox")
location_dropdown['values'] = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Hyderabad", "Ahmedabad", "Jaipur", "Lucknow", "Nagpur", "Visakhapatnam", "Indore", "Coimbatore", "Patna", "Pune"]
location_dropdown.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

# Bind selection event to show_secondary_dropdown function
location_dropdown.bind("<<ComboboxSelected>>", show_secondary_dropdown)

# Secondary dropdown (initially hidden)
secondary_label = tk.Label(left_frame, text="AREA")
secondary_dropdown = ttk.Combobox(left_frame, state='readonly', style="TCombobox")

# Initially hide the secondary dropdown
secondary_label.grid_remove()
secondary_dropdown.grid_remove()

ttk.Label(left_frame, text="PROPERTY NAME").grid(row=4, column=0, sticky='w', padx=10, pady=5)
property_name_entry = ttk.Entry(left_frame)
property_name_entry.grid(row=4, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

ttk.Label(left_frame, text="LOOKING TO").grid(row=5, column=0, sticky='w', padx=10, pady=5)
ttk.Radiobutton(left_frame, text="Sell", variable=looking_to_var, value="Sell").grid(row=5, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="Rent", variable=looking_to_var, value="Rent").grid(row=5, column=2, sticky='w', padx=10)

ttk.Label(left_frame, text="PRICE").grid(row=6, column=0, sticky='w', padx=10, pady=5)
price_entry = ttk.Entry(left_frame)
price_entry.grid(row=6, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

ttk.Label(left_frame, text="BHK").grid(row=7, column=0, sticky='w', padx=10, pady=5)
ttk.Radiobutton(left_frame, text="1 BHK", variable=bhk_var, value="1 BHK").grid(row=7, column=1, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="2 BHK", variable=bhk_var, value="2 BHK").grid(row=7, column=2, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="3 BHK", variable=bhk_var, value="3 BHK").grid(row=7, column=3, sticky='w', padx=10)
ttk.Radiobutton(left_frame, text="4 BHK+", variable=bhk_var, value="4 BHK+").grid(row=7, column=4, sticky='w', padx=10)

ttk.Label(left_frame, text="SQ FT").grid(row=8, column=0, sticky='w', padx=10, pady=5)
sq_ft_entry = ttk.Entry(left_frame)
sq_ft_entry.grid(row=8, column=1, columnspan=3, sticky='ew', padx=10, pady=5)

# Amenities Section
ttk.Label(left_frame, text="Amenities").grid(row=9, column=0, sticky='w', padx=10, pady=5)

# Create a frame to hold checkboxes for amenities
amenities_frame = tk.Frame(left_frame)
amenities_frame.grid(row=10, column=0, columnspan=4, sticky='w', padx=10, pady=5)

# Create each checkbox individually
lift_var = tk.IntVar()
lift_checkbox = tk.Checkbutton(amenities_frame, text="Lift", variable=lift_var)
lift_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

parking_var = tk.IntVar()
parking_checkbox = tk.Checkbutton(amenities_frame, text="Parking", variable=parking_var)
parking_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

gym_var = tk.IntVar()
gym_checkbox = tk.Checkbutton(amenities_frame, text="Gym", variable=gym_var)
gym_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

furnished_var = tk.IntVar()
furnished_checkbox = tk.Checkbutton(amenities_frame, text="Furnished", variable=furnished_var)
furnished_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# New amenities added
public_transport_var = tk.IntVar()
public_transport_checkbox = tk.Checkbutton(amenities_frame, text="Public Transport", variable=public_transport_var)
public_transport_checkbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

hospital_var = tk.IntVar()
hospital_checkbox = tk.Checkbutton(amenities_frame, text="Hospital", variable=hospital_var)
hospital_checkbox.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# About the property section
about_label = tk.Label(left_frame, text="About the property")
about_label.grid(row=11, column=0, sticky='w', padx=10, pady=5)

about_text = tk.Text(left_frame, height=13, wrap='word')
about_text.grid(row=12, column=0, columnspan=4, sticky='ew', padx=10, pady=5)

# Create the right frame for the image handling
right_frame = tk.Frame(main_frame)
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Button to add images
add_image_button = tk.Button(right_frame, text="Add Images", command=add_images)
add_image_button.grid(row=0, column=0, padx=10, pady=10, sticky='n')  # Place at the top

# Frame to display the image
image_display_frame = tk.Frame(right_frame, width=550, height=350, bg='#E0E0E0')
image_display_frame.grid(row=1, column=0, padx=10, pady=10)  # Below the add images button
image_display_frame.pack_propagate(False)  # Prevents resizing with the image

# Label inside the frame to display the images
image_label = tk.Label(image_display_frame, bg='#E0E0E0')  # To blend with the frame
image_label.pack(expand=True)

# Buttons to navigate through images, initially hidden
prev_button = tk.Button(right_frame, text="Previous", command=prev_image)
next_button = tk.Button(right_frame, text="Next", command=next_image)

# Place navigation buttons below the image display frame
prev_button.grid(row=2, column=0, padx=50, pady=10, sticky='w')
next_button.grid(row=2, column=0, padx=50, pady=10, sticky='e')

# List to hold the references to images and the current image index
images = []
current_image_index = 0



# Create the "Submit" button and add it to the right frame using grid
submit_button = tk.Button(right_frame, text="Submit",width=6,font=("bold",15))
submit_button.grid(row=4, column=0, padx=10, pady=50) 


# Start the Tkinter event loop
root.mainloop()
