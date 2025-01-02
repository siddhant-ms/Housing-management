from tkinter import *

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
        prp = Toplevel(root)
        prp.title("My Properties")
        prp.geometry("600x400")
        prp.configure(bg="#8aa3d1")

        added_frame = Frame(prp, bg="#8aa3d1", width=290, height=400)
        added_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

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

        viewed_frame = Frame(prp, bg="#8aa3d1", width=290, height=400)
        viewed_frame.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="nsew")

        viewed_label = Label(
            viewed_frame,
            text="VIEWED PROPERTIES",
            bg="gray",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="ridge",
            padx=5,
            pady=5
        )
        viewed_label.pack(fill="x", pady=5)

        divider_line = Frame(prp, bg="black", width=2, height=400)
        divider_line.grid(row=0, column=1, sticky="ns", padx=5)

        prp.grid_columnconfigure(0, weight=1)
        prp.grid_columnconfigure(2, weight=1)
        prp.grid_rowconfigure(0, weight=1)

    def logout():
        print("Logging out")
        root.destroy()

    homescreen = Label(
        root,
        text="HOUSING MANAGEMENT",
        font=('Arial Black', 30, 'bold'),
        relief=RIDGE,
        bg='#333333',
        fg='#ffffff'
    )
    Buy = Button(root, text="View properties", bg='grey', fg='black', width=20, height=2)
    Sell = Button(root, text="Add properties", bg='grey', fg='black', width=20, height=2)

    Back2login = Button(
        root,
        text="Logout",
        relief=RAISED,
        bg='#969997',
        fg='black',
        width=10,
        height=3,
        command=logout
    )
    Savedprop = Button(
        root,
        text="My properties",
        relief=RAISED,
        bg='#969997',
        fg='black',
        width=10,
        height=3,
        command=proppage
    )

    Menu = Button(
        root,
        text="☰",
        relief=RAISED,
        bg='#969997',
        fg='black',
        width=10,
        height=3,
        command=toggle_dropdown
    )

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
