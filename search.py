import mysql.connector
from pprint import pprint

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host='localhost',        # Adjust the host if needed
        user='root',             # Your MySQL username
        password='1234',         # Your MySQL password
        database='house_management',
    )

def search_properties(data):
    # Start constructing the SQL query
    base_query = "SELECT * FROM properties WHERE 1=1"
    
    # Dictionary to map filters to actual column names
    filter_mappings = {
        'Amenities': 'amenities',
        'Area': 'area',
        'Budget': 'price',
        'Location': 'city',
        'Looking to': 'looking_to',
        'Property Type': 'property_type'
    }
    
    # Collect filter conditions
    conditions = []
    values = []
    
    # Process each field in the search query
    for key, value in data.items():
        if key == 'Budget' and value > 0:
            conditions.append("price <= %s")  # assuming budget is the max price
            values.append(value)
        elif key == 'Amenities' and value:  # If there are amenities filters
            # Assuming amenities are stored as a comma-separated string (or JSON)
            conditions.append("FIND_IN_SET(%s, amenities) > 0")
            for amenity in value:
                values.append(amenity)
        elif key == 'Area' and value.strip():
            conditions.append("area LIKE %s")
            values.append(f"%{value}%")
        elif key == 'Location' and value.strip():
            conditions.append("city LIKE %s")
            values.append(f"%{value}%")
        elif key == 'Looking to' and value.strip():
            conditions.append("looking_to = %s")
            values.append(value)
        elif key == 'Property Type' and value.strip():
            conditions.append("property_type = %s")
            values.append(value)
    
    # If we have any conditions, add them to the query
    if conditions:
        base_query += " AND " + " AND ".join(conditions)
    
    # Debug: Print out the query and values for validation
    pprint(f"SQL Query: {base_query}")
    pprint(f"Values: {values}")
    
    # Execute the query
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)  # fetch as dictionaries
        cursor.execute(base_query, tuple(values))
        results = cursor.fetchall()
        pprint(results)  # Show results
    except mysql.connector.Error as err:
        pprint(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

