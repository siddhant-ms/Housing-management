import mysql.connector
from mysql.connector import errorcode

def initialize_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="1234",  # Replace with your MySQL password
            port=3306
        )
        cursor = connection.cursor()
        print("Connected to MySQL server.")

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS house_management")
        print("Database 'house_management' created or already exists.")

        # Use the created database
        cursor.execute("USE house_management")
        print("Using database 'house_management'.")

        # Create the users table
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(15) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_users_table_query)
        print("Table 'users' created or already exists.")

        # Create the properties table with username instead of user_id
        create_properties_table_query = """
        CREATE TABLE IF NOT EXISTS properties (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            property_name VARCHAR(255) NOT NULL,
            property_type ENUM('Independent','Apartment','Commercial') NOT NULL,
            looking_to ENUM('Sell','Rent') NOT NULL,
            price DECIMAL(15,2) NOT NULL,
            bhk ENUM('1 BHK','2 BHK','3 BHK') NOT NULL,
            sq_ft INT NOT NULL,
            amenities TEXT,
            description TEXT,
            city VARCHAR(255) NOT NULL,
            area VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_properties_table_query)
        print("Table 'properties' created or already exists.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    initialize_database()
