from tkinter import *
from tkinter import messagebox
import mysql.connector
from home import show_main_window

window = Tk()
window.geometry("500x600")
window.title("Login Screen")
window.configure(background="#333333")

current_user = None  # Global variable to store the current logged-in username

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="house_management"
    )
    if connection.is_connected():
        print("Connected to the database")
        cursor = connection.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

def login_user(username_entry, password_entry):
    global current_user  # Access the global variable

    username = username_entry.get()
    password = password_entry.get()

    query = "SELECT password FROM users WHERE name = %s;"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        if user[0] == password:
            current_user = username  # Store the username in the global variable
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            show_main_window()
            window.quit()
        else:
            messagebox.showerror("Login Error", "Incorrect password!")
    else:
        messagebox.showerror("Login Error", "Username not found!")

def signupwindow():
    window.withdraw()
    SUwindow = Toplevel()
    SUwindow.title("Sign up page")
    SUwindow.geometry("500x500")
    SUwindow.configure(bg="#333333")
    center_window(SUwindow, 500, 500)

    def register_user(username_entry, email_entry, phone_entry, password_entry):
        un = username_entry.get()
        mail = email_entry.get()
        phno = phone_entry.get()
        pwd = password_entry.get()

        # Check if any field is empty
        if not un or not mail or not phno or not pwd:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        try:
            query = "INSERT INTO users(name, email, phone, password) VALUES(%s, %s, %s, %s);"
            cursor.execute(query, (un, mail, phno, pwd))
            connection.commit()
            loginpage()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Failed to create account")

    def loginpage():
        SUwindow.destroy()
        window.deiconify()

    signup_title = Label(SUwindow, text="SIGN UP", font=('Arial Black', 30, 'bold'), relief=RIDGE, bg='#353935', fg='#ffffff')
    signup_title.pack(pady=20)

    username_label = Label(SUwindow, text="Username:", bg='#333333', fg='#ffffff')
    username_label.pack(pady=5)
    username_entry = Entry(SUwindow)
    username_entry.pack(pady=5)

    email_label = Label(SUwindow, text="Email ID:", bg='#333333', fg='#ffffff')
    email_label.pack(pady=5)
    email_entry = Entry(SUwindow)
    email_entry.pack(pady=5)

    phone_label = Label(SUwindow, text="Phone Number:", bg='#333333', fg='#ffffff')
    phone_label.pack(pady=5)
    phone_entry = Entry(SUwindow)
    phone_entry.pack(pady=5)

    password_label = Label(SUwindow, text="Password:", bg='#333333', fg='#ffffff')
    password_label.pack(pady=5)
    password_entry = Entry(SUwindow, show="*")
    password_entry.pack(pady=5)

    signup_button = Button(SUwindow, text="Create account", bg='#333333', fg='#ffffff', command=lambda: register_user(username_entry, email_entry, phone_entry, password_entry))
    signup_button.pack(pady=10)


    back_to_login_button = Button(SUwindow, text="Back to Login", bg='grey', fg='black', command=loginpage)
    back_to_login_button.pack(pady=10)

def start_login_page():
    Mframe = Frame(window, bg='#333333')
    Mframe.pack(padx=20, pady=20, expand=True, fill="both")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    center_window(window, 500, 600)

    login_title = Label(Mframe, text="LOGIN", font=('Arial Black', 30, 'bold'), relief=RIDGE, bg='#353935', fg='#ffffff')
    login_title.pack(pady=20)

    username_label = Label(Mframe, text="Username:", bg='#333333', fg='#ffffff')
    username_label.pack(pady=5)
    username_entry = Entry(Mframe)
    username_entry.pack(pady=5)

    password_label = Label(Mframe, text="Password:", bg='#333333', fg='#ffffff')
    password_label.pack(pady=5)
    password_entry = Entry(Mframe, show="*")
    password_entry.pack(pady=5)

    login_button = Button(Mframe, text="Login", bg='grey', fg='black', command=lambda: login_user(username_entry, password_entry))
    login_button.pack(pady=10)

    signup_button = Button(Mframe, text="Sign up", bg='grey', fg='black', command=signupwindow)
    signup_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    start_login_page()
