from tkinter import *
from tkinter import messagebox
import mysql.connector
from home import show_main_window

window = Tk()
window.geometry("500x500")
window.title("Login Screen")
window.configure(background="#333333")
login_label = Label(window, text="User Login", font=('Arial', 24, 'bold'), relief=RAISED, bg="#333333")
login_label.grid(row=0, column=0, columnspan=3, pady=20, sticky=NSEW)

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

# Function to get the current user from the file
def get_current_user():
    try:
        with open('current_user.txt', 'r') as file:
            current_user = file.read().strip()  # Read the username from the file
            return current_user
    except FileNotFoundError:
        return None 
# Function to write the current user to a file
def login_user(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    query = "SELECT password FROM users WHERE name = %s;"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        if user[0] == password:
            # Save the current username in a text file
            with open('current_user.txt', 'w') as file:
                file.write(username)  # Save the username when login is successful
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            current_user = get_current_user()
            if current_user:
                print(f"User {current_user} is logged in!")
                connection.close()
            else:
                print("No user is currently logged in.")

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
    Mframe.grid(row=1,column=1,padx=20, pady=20, sticky=N)

    username_label=Label(Mframe,text="Enter username:",bg='#333333',fg='#ffffff')
    username_entry=Entry(Mframe)
    password_label=Label(Mframe,text="Enter password:",bg='#333333',fg='#ffffff')
    password_entry=Entry(Mframe,show="*")
    login_button=Button(Mframe,text="Login", bg='grey', fg='black',command=lambda: login_user(username_entry, password_entry))
    signup_button=Button(Mframe,text="Sign up",bg='grey',fg='black',command=signupwindow)

    username_label.grid(row=0,column=0)
    username_entry.grid(row=0,column=1)
    password_label.grid(row=1,column=0)
    password_entry.grid(row=1,column=1)
    signup_button.grid(row=2,column=0,columnspan=1,pady=10,padx=5)
    login_button.grid(row=2,column=1,columnspan=1,pady=10,padx=5)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)


    window.mainloop()

if __name__ == "__main__":
    # Try reading the current user from the text file
    
    start_login_page()


