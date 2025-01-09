import mysql.connector
from mysql.connector import errorcode
import random

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

def check_table_exists(cursor, table_name):
    """Check if a table exists in the current database."""
    cursor.execute(f"""
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = '{table_name}'
    """)
    return cursor.fetchone()[0] > 0

def initialize_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="1234", 
            port=3306
        )
        cursor = connection.cursor()
        print("Connected to MySQL server.")

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS house_management")
        print("Database 'house_management' created or already exists.")

        cursor.execute("USE house_management")
        print("Using database 'house_management'.")

        # Check if the users table exists, if not, create it
        if check_table_exists(cursor, 'users'):
            print("Table 'users' already exists.")
        else:
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
            print("Table 'users' created.")

        # Check if the properties table exists, if not, create it
        if check_table_exists(cursor, 'properties'):
            print("Table 'properties' already exists.")
        else:
            create_properties_table_query = """
            CREATE TABLE IF NOT EXISTS properties (
              id INT AUTO_INCREMENT PRIMARY KEY,
                user VARCHAR(255) NOT NULL,
                phone_no BIGINT NOT NULL,  -- Use BIGINT if you want to store phone numbers as numbers
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
            print("Table 'properties' created.")

        # Check if the city_areas table exists, if not, create it
        if check_table_exists(cursor, 'city_areas'):
            print("Table 'city_areas' already exists.")
        else:
            create_city_areas_table_query = """
            CREATE TABLE IF NOT EXISTS city_areas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                area VARCHAR(255) NOT NULL
            )
            """
            cursor.execute(create_city_areas_table_query)
            print("Table 'city_areas' created.")

            # Insert city area data
            for city, areas in city_areas.items():
                for area in areas:
                    insert_query = "INSERT INTO city_areas (city, area) VALUES (%s, %s)"
                    cursor.execute(insert_query, (city, area))

            connection.commit()
            print("City areas data inserted successfully.")

        # Check if the filters table exists, if not, create it
        if check_table_exists(cursor, 'filters'):
            print("Table 'filters' already exists.")
        else:
            create_filters_table_query = """
            CREATE TABLE IF NOT EXISTS filters (
               id INT AUTO_INCREMENT PRIMARY KEY,
                location VARCHAR(255) NOT NULL,
                area VARCHAR(255) NOT NULL,
                property_type VARCHAR(255) NOT NULL,
                looking_to VARCHAR(255) NOT NULL,
                budget DECIMAL(10,2),
                amenities TEXT,
                bhk INT,  -- For the number of BHK rooms
                square_footage DECIMAL(10, 2)
            )
            """
            cursor.execute(create_filters_table_query)
            print("Table 'filters' created.")

        connection.commit()

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




def generate_dummy_data(city_areas, num_records=20):
    property_types = ['Independent', 'Apartment', 'Commercial']
    looking_to = ['Sell', 'Rent']
    bhk_options = ['1 BHK', '2 BHK', '3 BHK']
    amenities = ['Lift', 'Public Transport', 'Hospital', 'Furnished', 'Gym', 'Parking']

    # Generate dummy data
    data = []
    for _ in range(num_records):  # Generate the number of records specified by num_records
        city = random.choice(list(city_areas.keys()))
        area = random.choice(city_areas[city])
        property_type = random.choice(property_types)
        look_to = random.choice(looking_to)
        bhk = random.choice(bhk_options)
        sq_ft = random.randint(500, 5000)  # sq_ft should not exceed 5000
        amenities_str = random.choice(amenities)  # Random single amenity, you can expand it to more if needed

        # Price depending on sell or rent
        if look_to == 'Sell':
            price = random.choice(range(0, 150000001, 500000))  # Sell price ranges from 0 to 150,000,000 (multiples of 500000)
        else:
            price = random.choice(range(0, 100001, 1000))  # Rent price ranges from 0 to 100,000 (multiples of 1000)

        # Generate a 10-digit phone number
        phone_no = ''.join([str(random.randint(0, 9)) for _ in range(10)])

        # Prepare the data
        record = (
            f'User{random.randint(1, 100)}',  # Dummy user name
            phone_no,
            f'Property{random.randint(1, 100)}',  # Dummy property name
            property_type,
            look_to,
            price,
            bhk,
            sq_ft,
            amenities_str,
            f'This is a description of {property_type} property located in {area}, {city}.',  # Dummy description
            city,
            area
        )

        data.append(record)

    return data

def dummy_data(city_areas, num_records=20):
    # Connect to MySQL server
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="1234", 
        port=3306,
        database="house_management"  # Ensure the database is specified here
    )
    cursor = db_connection.cursor()

    # Get dummy data
    data = generate_dummy_data(city_areas, num_records)

    # SQL Insert query
    insert_query = """
    INSERT INTO properties (user, phone_no, property_name, property_type, looking_to, price, bhk, sq_ft, amenities, description, city, area)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Ensure that phone numbers are 10 digits long
    for record in data:
        if len(record[1]) != 10:
            print(f"Phone number {record[1]} is not 10 digits. Skipping insertion for this record.")
            continue

    # Executing the insert queries
    cursor.executemany(insert_query, data)

    # Committing the transaction
    db_connection.commit()

    # Closing the connection
    cursor.close()
    db_connection.close()

    print(f"{num_records} records inserted successfully.")

# Assuming your `city_areas` dictionary is already defined, just pass it to `dummy_data`
dummy_data(city_areas, num_records=50)  # Specify the number of records you want to generate

if __name__ == "__main__":
    initialize_database()
