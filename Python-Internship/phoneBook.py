from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.geometry("800x500")
window.title("Phone-Book")
window.config(bg="#6082B6")

contacts = []

def add_contacts():
    name = name_entry.get().strip()
    phone = phone_entry.get()
    email = email_entry.get()
    if name != "":
        contacts.append((name, phone, email))
        messagebox.showinfo("Save", "Contact Saved Successfully")
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    update_listbox()

def remove_contact():
    selected = contacts_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        update_listbox()
        messagebox.showinfo("Delete", "Contact has been Deleted")

def display_contact():
    for c in contacts:
        messagebox.showinfo("Details", "Name : " + c[0] +
                            '\n' + "Phone : " + c[1] +
                            '\n' + "Email : " + c[2])

def update_listbox():
    contacts_listbox.delete(0, END)
    for c in contacts:
        contacts_listbox.insert(END, c[0])

heading_label = Label(window, text="Phone-Book", font=("Times", 30, "bold underline"), fg="white", bg="#6082B6")
heading_label.place(x=300, y=3)

name_label = Label(window, text="Name:", font=("Arial", 20, "bold"), fg="white", bg="#6082B6")
name_label.place(x=80, y=70)

name_entry = Entry(window, font=("Arial", 17, "italic"), fg="black", bg="#cac1d9")
name_entry.place(x=200, y=70)

phone_label = Label(window, text="Phone:", font=("Arial", 20, "bold"), fg="white", bg="#6082B6")
phone_label.place(x=80, y=120)

phone_entry = Entry(window, font=("Arial", 17, "italic"), fg="black", bg="#cac1d9")
phone_entry.place(x=200, y=120)

email_label = Label(window, text="Email:", font=("Arial", 20, "bold"), fg="white", bg="#6082B6")
email_label.place(x=80, y=170)

email_entry = Entry(window, font=("Arial", 17, "italic"), fg="black", bg="#cac1d9")
email_entry.place(x=200, y=170)

add_button = Button(window, text="Add", font=("Tahoma", 13, "bold"), relief="raised", borderwidth=4, width=18,
                    activeforeground="darkgreen", background="lightgreen", activebackground="green", command=add_contacts)
add_button.place(x=50, y=280)

remove_button = Button(window, text="Remove", font=("Tahoma", 13, "bold"), relief="raised", borderwidth=4, width=18,
                       activeforeground="black", background="red", activebackground="dark red", command=remove_contact)
remove_button.place(x=50, y=330)

display_button = Button(window, text="Display Info", font=("Tahoma", 13, "bold"), relief="raised", borderwidth=4, width=18,
                        activeforeground="white", background="lightblue", activebackground="blue", command=display_contact)
display_button.place(x=50, y=380)

conhead_label = Label(window, text="NAME-BOOK", font=("Times", 20, "bold"), relief="raised", fg="white", bg="#6082B6")
conhead_label.place(x=580, y=180)

contacts_listbox = Listbox(window, font=("Comic Sans MS", 12), width=40)
contacts_listbox.place(x=380, y=230)

window.mainloop()