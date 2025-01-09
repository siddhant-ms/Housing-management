import mysql.connector

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
    
def execute_query(query, data):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='house_management'
        )
        cursor = connection.cursor()
        
        cursor.execute(query, data)
        connection.commit()  # Commit the transaction
        print("Query executed successfully")
        return True

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

    finally:
        if cursor:
            cursor.close()  # Ensure the cursor is closed if it was created
        if connection:
            connection.close()  # Ensure the connection is closed if it was created

def retrieve_current_user():
# Retrieve the current user from the file
    try:
        with open('current_user.txt', 'r') as file:
            current_user = file.read().strip() 
            return current_user
    except FileNotFoundError:
        return None  # If the file doesn't exist it means no user is logged in, therefore error
    


    