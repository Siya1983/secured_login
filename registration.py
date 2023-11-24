import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import messagebox

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.configure(bg="maroon2")


firebase=firebase.FirebaseApplication("https://register-b8169-default-rtdb.firebaseio.com/")

login_password_entry=""
login_username_entry=""
def login(): 
    global login_username_entry
    global login_password_entry
    print("login function")
    username=login_username_entry.get()
    password=login_password_entry.get()
    encrypted_password=hashlib.md5(password.encode())
    hexadecimal_password=encrypted_password.hexdigest()
    get_password=firebase.get("/", username)
    if (get_password != None):
        if (get_password == hexadecimal_password):
            messagebox.showinfo("Info","you have successfully loged in")
        else:
            messagebox.showinfo("Info","please check your password")
    else:
        messagebox.showinfo("Info","You have not registered \n kindly register for the login")
    
    
   
def register(): 
    print("register function")
    username=username_entry.get()
    password= password_entry.get()
    encrypted_password=hashlib.md5(password.encode())
    hex_value1=encrypted_password.hexdigest()  
    print(" MD5 encrypt data : ",hex_value1)
    hex_value_password=firebase.put("/", username,hex_value1)
    messagebox.showinfo("information","successfully registered")
    
def login_window():
    global login_password_entry
    global login_username_entry
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.configure(bg="light green")
    
    
    
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold',bg='dark green')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13',bg='dark green')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13',bg='dark green')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold',bg='dark green', command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    

    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold',bg="maroon3")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13',bg="maroon3")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13',bg="maroon3")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold',bg="maroon3" ,command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold',bg="maroon3" ,  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()