from tkinter import *
from tkinter import ttk, filedialog # Custom widget set
from tkinter import messagebox
import mysql.connector


window = Tk()
window.geometry("400x400")
window.title("Login Screen")
window.configure(background="#333333")

login_label = Label(window, text="Login", font=('boulder', 30, 'bold'), relief=RIDGE, bg='#353935', fg='#ffffff')
login_label.grid(row=0, column=0, columnspan=3, pady=20, sticky=NSEW)

Mframe = Frame(window, bg='#333333')
Mframe.grid(row=1, column=1, padx=20, pady=20, sticky=N)


def login_user():
    username = username_entry.get()
    password = password_entry.get()

    query = "SELECT password FROM users WHERE name = %s;"
    cursor.execute(query, (username,))
    user = cursor.fetchone()        
    if user:
        # If the username is found, check the password
        if user[0] == password:
            messagebox.showinfo("Login Success", "Successfully logged in!")
            MainWindow()  # Proceed to the main page after login
        else:
            messagebox.showerror("Login Error", "Incorrect password!")
    else:
        messagebox.showerror("Login Error", "Username not found!")


# Connect to the database (Ensure this is done before using the cursor)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sujan07kumar",
    database="house_m"
)

if connection.is_connected():
    print("Connected to the database")
    cursor = connection.cursor()  # Initialize the cursor after successful connection
else:
    print("Failed to connect to the database")
    exit()


def signupwindow():
    window.withdraw()
    SUwindow = Toplevel()
    SUwindow.title("Sign up page")
    SUwindow.geometry("400x250")
    SUwindow.configure(bg="#333333")

    def register_user():
        un = username_entry.get()
        mail = email_entry.get()
        phno = phone_entry.get()
        pwd = password_entry.get()

        query = "INSERT INTO users(name, email, phone, password) VALUES(%s, %s, %s, %s);"
        cursor.execute(query, (un, mail, phno, pwd))
        connection.commit()  # Commit the transaction

    def loginpage():
        SUwindow.destroy()  # Closes the sign-up window
        window.deiconify()
        
    signup_title = Label(SUwindow, text="SIGN UP", font=('boulder', 30, 'bold'), relief=RIDGE, bg='#353935', fg='#ffffff')

    username_label = Label(SUwindow, text="Username:", bg='#333333', fg='#ffffff')
    username_entry = Entry(SUwindow)

    email_label = Label(SUwindow, text="Email ID:", bg='#333333', fg='#ffffff')
    email_entry = Entry(SUwindow)

    phone_label = Label(SUwindow, text="Phone Number:", bg='#333333', fg='#ffffff')
    phone_entry = Entry(SUwindow)

    password_label = Label(SUwindow, text="Password:", bg='#333333', fg='#ffffff')
    password_entry = Entry(SUwindow, show="*")
    
    signup_button = Button(SUwindow, text="Create account", bg='#333333', fg='#ffffff', command=loginpage)

    signup_title.grid(row=0, column=0, columnspan=2, pady=5)

    username_label.grid(row=1, column=0, padx=10, pady=5)
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    email_label.grid(row=2, column=0, padx=10, pady=5)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    phone_label.grid(row=3, column=0, padx=10, pady=5)
    phone_entry.grid(row=3, column=1, padx=10, pady=5)
    password_label.grid(row=4, column=0, padx=10, pady=5)
    password_entry.grid(row=4, column=1, padx=10, pady=5)

    signup_button.grid(row=5, columnspan=2, pady=10)

    # Configure column weights to center the widgets
    SUwindow.grid_columnconfigure(0, weight=1)
    SUwindow.grid_columnconfigure(1, weight=1)


def MainWindow():
    window.withdraw()  # Hide main login window
    window2 = Toplevel()
    window2.title("Home Page")
    window2.geometry("1000x1000")
    window2.configure(bg='#353935')

    def dropdown():
        Back2login = Button(window2, text="logout", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=return_to_login)
        Savedprop = Button(window2, text="My properties", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=proppage)

        Back2login.grid(row=1, column=3)
        Savedprop.grid(row=2, column=3)


    def proppage():
        # Initialize the main window
        prp = Tk()
        prp.title("My Properties")
        prp.geometry("600x400")  # Adjust the window size as needed
        prp.configure(bg="#8aa3d1")

        # Create the frame for "Added Properties"
        added_frame = Frame(prp, bg="#8aa3d1", width=290, height=400)  # Matches background color of main window
        added_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

        # Label for Added Properties with ridge relief
        added_label = Label(
            added_frame, 
            text="ADDED PROPERTIES", 
            bg="gray", 
            fg="white", 
            font=("Arial", 12, "bold"),
            relief="ridge",
            padx=5,
            pady=5
        )
        added_label.pack(fill="x", pady=5)

        # Create the frame for "Viewed Properties"
        viewed_frame = Frame(prp, bg="#8aa3d1", width=290, height=400)  # Matches background color of main window
        viewed_frame.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="nsew")

        # Label for Viewed Properties with ridge relief
        viewed_label = Label(viewed_frame, text="VIEWED PROPERTIES", bg="gray", fg="white", font=("Arial", 12, "bold"), relief="ridge", padx=5, pady=5)
        viewed_label.pack(fill="x", pady=5)

        # Create the dividing line between frames
        divider_line = Frame(prp, bg="black", width=2, height=400)
        divider_line.grid(row=0, column=1, sticky="ns", padx=5)

        # Configure grid weights to make frames resizable
        prp.grid_columnconfigure(0, weight=1)
        prp.grid_columnconfigure(2, weight=1)
        prp.grid_rowconfigure(0, weight=1)

    def return_to_login():
        window2.withdraw()
        window.deiconify()  # Shows the hidden window again

    def selling_page():
        sellpage = Toplevel()
        sellpage.title("Selling page")
        sellpage.geometry("1000x1000")
        sellpage.configure(bg='#bac2cf')
        gui_frame = Tk.Frame(selling_page)

    def buying_page():
        buypage = Toplevel()
        buypage.title("Buying page")
        buypage.geometry("1000x1000")
        buypage.configure(bg='#bac2cf')

    # Widgets
    homescreen = Label(window2, text="HOUSING MANAGEMENT", font=('Arial Black', 30, 'bold'), relief=RIDGE, bg='#333333', fg='#ffffff')
    Buy = Button(window2, text="View properties", bg='grey', fg='black', width=20, height=2, command=buying_page)
    Sell = Button(window2, text="Add properties", bg='grey', fg='black', width=20, height=2, command=selling_page)
    Menu = Button(window2, text="☰", relief=RAISED, bg='#969997', fg='black', width=10, height=3, command=dropdown)

    homescreen.grid(row=1, column=0, columnspan=2, sticky=NS) 
    Buy.grid(row=3, column=0)
    Sell.grid(row=3, column=1)
    Menu.grid(row=0, column=3)

    # Configuration of grid
    window2.grid_columnconfigure(0, weight=1)
    window2.grid_columnconfigure(1, weight=1)
    window2.grid_rowconfigure(3, weight=1)


# Widgets for the login page
username_label = Label(Mframe, text="Enter username:", bg='#333333', fg='#ffffff')
username_entry = Entry(Mframe)
password_label = Label(Mframe, text="Enter password:", bg='#333333', fg='#ffffff')
password_entry = Entry(Mframe, show="*")
login_button = Button(Mframe, text="Login", bg='grey', fg='black', command=login_user)
signup_button = Button(Mframe, text="Sign up", bg='grey', fg='black', command=signupwindow)

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
signup_button.grid(row=2, column=0, columnspan=1, pady=10, padx=5)
login_button.grid(row=2, column=1, columnspan=1, pady=10, padx=5)

# Grid configuration
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()
