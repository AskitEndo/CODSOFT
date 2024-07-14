from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root=root
        self.root.title("To-Do-List")
        self.root.geometry("650x410+300+150")
        self.root.configure(bg="gray")


        self.label = Label(self.root, text="To-Do Planner", font="sans-serif, 26 bold underline italic", width=10, bd=7, bg="purple", fg="white")
        self.label.pack(side="top" , fill=BOTH)

        self.label2 = Label(self.root, text="New Event", font="sans-serif, 18 bold", width=10, bd=7, bg="violet", fg="black")
        self.label2.place(x=10, y=70)

        self.label3 = Label(self.root, text="Events", font="sans-serif, 18 bold", width=10, bd=7, bg="violet", fg="black")
        self.label3.place(x=280, y=70)

        self.main_text  = Listbox(self.root, height=10, bd=5, width=30, font="sans-serif, 14 bold italic" )
        self.main_text.place(x=280, y=120)

        self.text = Text(self.root, bd=5, height=2, width=20, font="ariel, 15 italic")
        self.text.place(x=10, y=120)




        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
        
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt" , "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for  line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()


        self.button = Button(self.root, text="ADD", font="serif, 15", width=20,bd=2, bg="lightgreen", fg="black", command=add)
        self.button.place( x=10, y=200)

        self.button2 = Button(self.root, text="ERASE", font="serif, 15", width=20,bd=2, bg="red", fg="black", command=delete)
        self.button2.place( x=10, y=250)
        



def main():
    root =Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
