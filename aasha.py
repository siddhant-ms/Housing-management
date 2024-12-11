from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Login Page")
window.configure(bg="#ADD8E6")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

login_label = Label(window, text="User Login", font=('Arial', 24, 'bold'), relief=RAISED, bg='#ADD8E6', fg='#2C3E50')
login_label.grid(row=0, column=0, columnspan=3, pady=20, sticky=NSEW)

Mframe = Frame(window, bg='#ADD8E6')
Mframe.grid(row=1, column=0, padx=20, pady=20, sticky=NSEW)

username_label = Label(Mframe, text="Username:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50', relief=FLAT)
username_label.grid(row=0, column=0, pady=10, sticky=E)
username_entry = Entry(Mframe, font=('Arial', 12), relief=SUNKEN, bd=2)
username_entry.grid(row=0, column=1, pady=10)

password_label = Label(Mframe, text="Password:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50', relief=FLAT)
password_label.grid(row=1, column=0, pady=10, sticky=E)
password_entry = Entry(Mframe, font=('Arial', 12), show="*", relief=SUNKEN, bd=2)
password_entry.grid(row=1, column=1, pady=10)

login_button = Button(Mframe, text="Login", font=('Arial', 12), bg='#1ABC9C', fg='white', relief=RAISED, bd=3, width=10)
login_button.grid(row=2, column=0, pady=20)

signup_button = Button(Mframe, text="Sign Up", font=('Arial', 12), bg='#E74C3C', fg='white', relief=RAISED, bd=3, width=10)
signup_button.grid(row=2, column=1, pady=20)

def signup_page():
    signup_window = Toplevel(window)
    signup_window.geometry("500x500")
    signup_window.title("Sign Up Page")
    signup_window.configure(bg="#ADD8E6")

    signup_label = Label(signup_window, text="Create Account", font=('Arial', 20, 'bold'), relief=RAISED, bg='#ADD8E6', fg='#2C3E50')
    signup_label.pack(pady=20)

    Sframe = Frame(signup_window, bg='#ADD8E6')
    Sframe.pack(pady=20)

    username_label_signup = Label(Sframe, text="Username:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50')
    username_label_signup.grid(row=0, column=0, pady=10, sticky=E)
    username_entry_signup = Entry(Sframe, font=('Arial', 12), relief=SUNKEN, bd=2)
    username_entry_signup.grid(row=0, column=1, pady=10)

    email_label = Label(Sframe, text="Email ID:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50')
    email_label.grid(row=1, column=0, pady=10, sticky=E)
    email_entry = Entry(Sframe, font=('Arial', 12), relief=SUNKEN, bd=2)
    email_entry.grid(row=1, column=1, pady=10)

    phone_label = Label(Sframe, text="Phone No.:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50')
    phone_label.grid(row=2, column=0, pady=10, sticky=E)
    phone_entry = Entry(Sframe, font=('Arial', 12), relief=SUNKEN, bd=2)
    phone_entry.grid(row=2, column=1, pady=10)

    password_label_signup = Label(Sframe, text="Password:", font=('Arial', 12), bg='#ADD8E6', fg='#2C3E50')
    password_label_signup.grid(row=3, column=0, pady=10, sticky=E)
    password_entry_signup = Entry(Sframe, font=('Arial', 12), show="*", relief=SUNKEN, bd=2)
    password_entry_signup.grid(row=3, column=1, pady=10)

    signup_button_signup = Button(Sframe, text="Create Account", font=('Arial', 12), bg='#E74C3C', fg='white', relief=RAISED, width=15,
                                  command=lambda: go_back_to_login(signup_window))
    signup_button_signup.grid(row=4, column=0, columnspan=2, pady=20)

def create_home_screen():
    window.withdraw()

    home = Toplevel()
    home.geometry("500x500")
    home.title("Home Screen")
    home.configure(bg="#333333")

    logout_button = Button(home, text="←", font=('Arial', 8), bg='#E74C3C', fg='white', relief=RAISED, bd=3, width=2,
                           command=lambda: go_back_to_login(home))
    logout_button.place(x=5, y=5)

    main_label = Label(home, text="VEHICLE MANAGEMENT", font=('Arial', 18, 'bold'), relief=RIDGE, bg="#333333", fg='#ffffff')
    main_label.pack(pady=20)

    button_frame = Frame(home, bg="#333333")
    button_frame.pack(pady=150)

    buy_button = Button(button_frame, text="BUY", font=('Arial', 12), relief=RAISED, bg="#3498DB", fg="white", width=10)
    buy_button.grid(row=0, column=0, padx=10)

    sell_button = Button(button_frame, text="SELL", font=('Arial', 12), relief=RAISED, bg="#E74C3C", fg="white", width=10)
    sell_button.grid(row=0, column=1, padx=10)

    rent_button = Button(button_frame, text="RENT", font=('Arial', 12), relief=RAISED, bg="#2ECC71", fg="white", width=10)
    rent_button.grid(row=0, column=2, padx=10)

def go_back_to_login(current_window):
    current_window.destroy()
    window.deiconify()

login_button.config(command=create_home_screen)
signup_button.config(command=signup_page)

Mframe.grid_columnconfigure(0, weight=1)
Mframe.grid_columnconfigure(1, weight=2)

window.mainloop()
