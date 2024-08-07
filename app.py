from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("Login Screen")
window.configure(background="#333333")

login_label=Label(window,text="Login",font=('boulder',30,'bold'),relief=RIDGE,bg='#353935',fg='#ffffff')
login_label.grid(row=0,column=0,columnspan=3,pady=20,sticky=NSEW) 


Mframe=Frame(window,bg='#333333')
Mframe.grid(row=1,column=1,padx=20,pady=20,sticky=N) 

def NewWindow():
    window.withdraw()  #gets rid of main window, but its still in background
    window2=Toplevel()
    window2.title("Home Page")
    window2.geometry("1000x1000")
    window2.configure(bg='#353935')

    def dropdown():
        Back2login=Button(window2,text="Back to login",relief=RAISED,bg='#969997',fg='black',width=10,height=3,command= return_to_login)
        Savedprop=Button(window2,text="Saved ♡",relief=RAISED,bg='#969997',fg='black',width=10,height=3,)

        Back2login.grid(row=1,column=3)
        Savedprop.grid(row=2,column=3)



    def return_to_login():
        window2.withdraw()
        window.deiconify() #shows the hidden window again
            
   
    def selling_page():
        sellpage=Toplevel()
        sellpage.title("Selling page")
        sellpage.geometry("1000x1000")
        sellpage.configure(bg='#bac2cf')






    def buying_page():
        buypage=Toplevel()
        buypage.title("Buying page")
        buypage.geometry("1000x1000")
        buypage.configure(bg='#bac2cf')








    #widgets
    homescreen=Label(window2,text="HOUSING MANAGEMENT",font=('Arial Black',30,'bold'),relief=RIDGE,bg='#333333',fg='#ffffff')
    Buy=Button(window2,text="Start buying",bg='grey',fg='black',width=20,height=2,command=buying_page)
    Sell=Button(window2,text="Start selling",bg='grey',fg='black',width=20,height=2,command=selling_page)
    Menu=Button(window2,text="☰",relief=RAISED,bg='#969997',fg='black',width=10,height=3,command=dropdown)

    homescreen.grid(row=1,column=0,columnspan=2,sticky=NS) 
    Buy.grid(row=3,column=0)
    Sell.grid(row=3,column=1)
    Menu.grid(row=0,column=3)


    #configuration of grid
    window2.grid_columnconfigure(0, weight=1)
    window2.grid_columnconfigure(1, weight=1)
    window2.grid_rowconfigure(3, weight=1)
    



#widgets,instead of adding it in the main window, we add in a frame
username_label=Label(Mframe,text="Enter username:",bg='#333333',fg='#ffffff')
username_entry=Entry(Mframe)
password_label=Label(Mframe,text="Enter password:",bg='#333333',fg='#ffffff')
password_entry=Entry(Mframe,show="*")
login_button=Button(Mframe,text="Login", bg='grey', fg='black',command=NewWindow)
# new_window=Button(Mframe,text="Go to home page",bg='grey',fg='black',command=NewWindow)


username_label.grid(row=0,column=0)
username_entry.grid(row=0,column=1)
password_label.grid(row=1,column=0)
password_entry.grid(row=1,column=1)
login_button.grid(row=2,column=0,columnspan=2,pady=10,padx=5)
# new_window.grid(row=3,column=0,columnspan=2,pady=10,padx=5)

#changes the size of the grid, by inc length/breadth of certain grids

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)






window.mainloop()

