from tkinter import *
import mysql.connector
from buyer_page import buyer_page
from seller_page import seller_page
from functions import retrieve_current_user  # Import your function

# Function to fetch properties and their prices based on the username
def get_properties(username):
    # Connect to MySQL database (adjust your connection details)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="1234",  # Replace with your MySQL password
        database="house_management"
    )
    cursor = conn.cursor()

    # Query to fetch both property names and their prices for the logged-in user
    cursor.execute("SELECT property_name, price FROM properties WHERE username = %s", (username,))
    properties = cursor.fetchall()  # Fetch all results as a list of tuples

    cursor.close()
    conn.close()

    return properties

def show_main_window():
    root = Tk()
    root.geometry("1000x1000")
    root.title("Home Page")
    root.configure(bg='#353935')

    dropdown_open = False

    def toggle_dropdown():
        nonlocal dropdown_open
        if dropdown_open:
            Back2login.grid_forget()
            Savedprop.grid_forget()
        else:
            Back2login.grid(row=1, column=3)
            Savedprop.grid(row=2, column=3)
        dropdown_open = not dropdown_open

    def proppage():
        username = retrieve_current_user()  # Retrieve current logged-in username

        # If no user is logged in, show an error message
        if not username:
            print("No user is currently logged in.")
            return

        prp = Toplevel(root)
        prp.title("My Properties")
        prp.geometry("600x400")
        prp.configure(bg="#8aa3d1")

        # Get the properties for the logged-in user
        properties = get_properties(username)

        # Display header for My Properties
        Label(prp, text="MY PROPERTIES", bg="gray", fg="white", font=("Arial", 12, "bold"), relief="ridge", padx=5, pady=5).grid(row=0, column=0, columnspan=2, sticky="ew")
        Label(prp, text="Name", bg="#8aa3d1", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5).grid(row=1, column=0, sticky="w", padx=10)
        Label(prp, text="Price", bg="#8aa3d1", fg="black", font=("Arial", 10, "bold"), padx=10, pady=5).grid(row=1, column=1, sticky="w", padx=10)

        
        # Configure grid to ensure it takes the full width
        prp.grid_columnconfigure(0, weight=1)  # Ensure the first column takes up full space
        prp.grid_columnconfigure(1, weight=1)  # Ensure the second column takes up full space

        # Display the list of properties
        if properties:
            for i, (property_name, price) in enumerate(properties):
                # Property name
                property_label = Label(prp, text=property_name, bg="#8aa3d1", fg="black", font=("Arial", 10), padx=10, pady=5)
                property_label.grid(row=i + 2, column=0, sticky="w", padx=10)  # Align name to the left

                # Pricegit add .
                price_label = Label(prp, text=f"₹{price}", bg="#8aa3d1", fg="black", font=("Arial", 10), padx=10, pady=5)
                price_label.grid(row=i + 2, column=1, sticky="w", padx=10)  # Align price to the left

        else:
            Label(prp, text="No properties found.", bg="#8aa3d1", fg="black", font=("Arial", 10), padx=10, pady=5).grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

        prp.mainloop()
    def logout():
        print("Logging out")
        root.destroy()

    def quit_app():
        root.destroy
        print("closing application")

    

    # Home page screen
    homescreen = Label(root, text="HOUSING MANAGEMENT", font=('Arial Black', 30, 'bold'), relief=RIDGE, bg='#333333', fg='#ffffff')
    Buy = Button(root, text="View properties", bg='grey', fg='black', width=20, height=2, command=lambda:buyer_page(root))
    Sell = Button(root, text="Add properties", bg='grey', fg='black', width=20, height=2, command=lambda: seller_page(root))
    exit=Button(root, text="Logout", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=quit_app)
    Back2login = Button(root, text="Logout", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=logout)
    Savedprop = Button(root, text="My properties", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=proppage)
    Menu = Button(root, text="☰", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=toggle_dropdown)

    homescreen.grid(row=1, column=0, columnspan=2, sticky=NS)
    Buy.grid(row=3, column=0)
    Sell.grid(row=3, column=1)
    Menu.grid(row=0, column=3)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(3, weight=1)

    
    root.mainloop()

if __name__ == "__main__":
    show_main_window()

