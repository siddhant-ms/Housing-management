import mysql.connector
from tkinter import *
from tkinter import messagebox


def fetch_filter_and_property_data():
    """Fetch filter and property data from the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='house_management'
        )
        cursor = connection.cursor(dictionary=True)

        # Queries to fetch data
        filters_query = "SELECT * FROM filters ORDER BY id DESC LIMIT 1;"
        properties_query = """
        SELECT user, phone_no, property_name, property_type, looking_to, price, bhk, sq_ft, amenities, city, area 
        FROM properties
        """
        
        cursor.execute(filters_query)
        filters_data = cursor.fetchall()

        cursor.execute(properties_query)
        properties_data = cursor.fetchall()

        return {'filters': filters_data, 'properties': properties_data}
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return {'filters': [], 'properties': []}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def match_filters_with_properties(filters_data: list , properties_data: list):
    """Match properties with filters, ensuring unique results."""
    matched_properties = []
    seen_properties = set()  # To track already-added properties by a unique identifier

    for filter_item in filters_data:
        for property_item in properties_data:
            # Match conditions
            location_match = (
                filter_item['location'].strip().lower() == property_item['city'].strip().lower()
            ) and (
                filter_item['area'].strip().lower() == property_item['area'].strip().lower()
            )
            property_type_match = filter_item['property_type'].strip().lower() == property_item['property_type'].strip().lower()

            # Handle "looking_to" mapping
            looking_to_mapping = {
                'buy': 'sell',
                'rent': 'rent'
            }
            filter_looking_to = filter_item['looking_to'].strip().lower()
            property_looking_to = property_item['looking_to'].strip().lower()
            looking_to_match = looking_to_mapping.get(filter_looking_to) == property_looking_to

            budget_match = property_item['price'] <= filter_item['budget']

            # Amenities match
            filter_amenities = (
                set(item.strip() for item in filter_item['amenities'].split(',')) 
                if filter_item['amenities'] 
                else set()
            )
            property_amenities = (
                set(item.strip() for item in property_item['amenities'].split(',')) 
                if property_item['amenities'] 
                else set()
            )

            print(filter_amenities)
            print()
            print(property_amenities)
            
            amenities_match = not filter_amenities or bool(filter_amenities & property_amenities)

            # Unique identifier for the property (e.g., property name + location)
            property_id = (property_item['property_name'], property_item['city'], property_item['area'])

            # If all conditions match and property is not already added, append it
            if location_match and property_type_match and looking_to_match and budget_match and amenities_match:
                if property_id not in seen_properties:
                    matched_properties.append(property_item)
                    seen_properties.add(property_id)  # Mark property as seen

    return matched_properties




def display_matched_properties(matched_properties):
    """Display matched properties in a new Tkinter window."""
    window = Tk()
    window.title("Matched Properties")
    window.geometry("600x400")
    window.configure(bg="#8aa3d1")

    # Create a frame to hold the text box and scrollbar
    frame = Frame(window,bg="#8aa3d1")
    frame.pack(expand=True, fill=BOTH)

    # Create the text box with wrap set to WORD
    text_box = Text(frame, wrap=WORD,)
    text_box.pack(side=LEFT, expand=True, fill=BOTH)

    # Add scrollbar linked to the text box
    scrollbar = Scrollbar(frame, command=text_box.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_box.config(yscrollcommand=scrollbar.set)

    # Display the matched properties
    if matched_properties:
        for property_item in matched_properties:
            property_details = (
                f"Property Name: {property_item['property_name']}\n"
                f"Location: {property_item['city']}, {property_item['area']}\n"
                f"Property Type: {property_item['property_type']}\n"
                f"Looking To: {property_item['looking_to']}\n"
                f"Price: {property_item['price']}\n"
                f"BHK: {property_item['bhk']}\n"
                f"Square Footage: {property_item['sq_ft']}\n"
                f"Amenities: {property_item['amenities']}\n"
                f"Phone Number: {property_item['phone_no']}\n"
                f"{'-' * 50}\n"
            )
            text_box.insert(END, property_details)
    else:
        text_box.insert(END, "No properties match the given filters.")

    window.mainloop()



def search_win():
    """Main function to search and display matched properties."""
    data = fetch_filter_and_property_data()
    filters_data = data['filters']
    properties_data = data['properties']
    
    matched_properties = match_filters_with_properties(filters_data, properties_data)
    display_matched_properties(matched_properties)


if __name__ == "__main__":
    search_win()
