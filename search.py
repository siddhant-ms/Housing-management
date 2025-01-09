import mysql.connector
from tkinter import *


def fetch_filter_and_property_data():
    # Establish connection to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='house_management'
    )
    
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to get results as a dictionary
    
    # Queries to fetch data from both filters and properties tables
    filters_query = "SELECT * FROM filters"
    properties_query = "SELECT location, area, property_type, looking_to, price AS budget, amenities FROM properties"
    
    try:
        # Execute filters query
        cursor.execute(filters_query)
        filters_results = cursor.fetchall()  # Fetch all rows from filters table
        
        # Execute properties query
        cursor.execute(properties_query)
        properties_results = cursor.fetchall()  # Fetch all rows from properties table
        
        # Convert the results into dictionaries for filters
        filters_data = []
        for row in filters_results:
            filter_dict = {
                'id': row['id'],
                'location': row['location'],
                'area': row['area'],
                'property_type': row['property_type'],
                'looking_to': row['looking_to'],
                'budget': row['budget'],
                'amenities': row['amenities']
            }
            filters_data.append(filter_dict)
        
        # Convert the results into dictionaries for properties
        properties_data = []
        for row in properties_results:
            property_dict = {
                'location': row['location'],
                'area': row['area'],
                'property_type': row['property_type'],
                'looking_to': row['looking_to'],
                'budget': row['budget'],
                'amenities': row['amenities']
            }
            properties_data.append(property_dict)
        
        # Return both filters and properties data
        return {'filters': filters_data, 'properties': properties_data}
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {'filters': [], 'properties': []}
    
    finally:
        cursor.close()
        connection.close()








def search_win():
    window = Tk()
