import tkinter as tk
from tkinter import messagebox
from controller import register_on_db, fetch_all, update
from tkinter import *
from tkinter import ttk

id

class AppView:

   
    def __init__(self) :
        self.root = tk.Tk()
        self.root.geometry("850x650")
        self.root.title("MyApp")
        self.second_view()
    
     

    def second_view(self):
        name_lbl = tk.Label(self.root, text="Name:", font=("arial","20","bold"))\
            .place(x=65, y =20)
        global name_entry
        name_entry = tk.Entry(self.root)
        name_entry.place(x=155,y=30)

        family_lbl = tk.Label(self.root, text="Family:", font=("arial","20","bold"))\
            .place(x=55, y =55)
        global family_entry
        family_entry = tk.Entry(self.root)
        family_entry.place(x=155,y=65)
        global phone_entry
        phone_lbl = tk.Label(self.root, text="Phone:", font=("arial","20","bold"))\
            .place(x=55, y =95)
        phone_entry = tk.Entry(self.root)
        phone_entry.place(x=155,y=100)  
        save_btn = tk.Button(self.root, text="Save",\
                             command=lambda:self.register_user(name_entry.get(),family_entry.get(),phone_entry.get())).place(x=290,y=140)
        update_btn = Button(self.root, text="Update", command=lambda:self.update_contact\
                            (record[0],name_entry.get(),family_entry.get(),phone_entry.get())).place(x=200, y= 140)
    

    ##################
        columns= ( "id","name", "family", "phone")
        global tree
        tree = ttk.Treeview(self.root, columns=columns,show="headings")
        tree.place(x=40,y=185)
        
        tree.heading("name", text="Contact_name")
        tree.column("name",anchor=CENTER)
        tree.heading("id", text="Contact_id")
        tree.column("id",anchor=CENTER)
        tree.heading("family", text="family")
        tree.column('family',anchor=CENTER)
        tree.heading("phone",text="phone")
        tree.column("phone",anchor=CENTER)
        self.insert_into_tree(tree)
        tree.bind("<<TreeviewSelect>>", self.item_selected)
        self.root.mainloop()

        

    def item_selected(self, event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            global record
            record = item['values']
            name_entry.delete(0, tk.END)
            name_entry.insert(0, record[1])
            family_entry.delete(0, tk.END)
            family_entry.insert(0, record[2])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, record[3])
            print(record[0])

   
    def register_user(self, name,family,phone):
        self.clear_tree(tree)
        if register_on_db(name, family, phone):
            self.insert_into_tree(tree)
            messagebox.showinfo("Success","Contact saved success")
        else:
            messagebox.showerror("Warning","Data is wrong .. check please")
        

        data = self.fetch_all_contacts()
        for row in data:
            tree.insert("","end",values=(row[0], row[1],row[2]))

    def fetch_all_contacts(self):
        return fetch_all()
    
    def insert_into_tree(self, n):
        data = self.fetch_all_contacts()
        self.clear_tree(n)
        for row in data:
            n.insert("","end",values=(row[0], row[1],row[2],row[3]))

    def clear_tree(self, n):
        for elm in n.get_children():
            n.delete(elm)   
  
    def update_contact(self,id,name,family,phone):
        if update (id,name,family,phone):
            self.insert_into_tree(tree)
            messagebox.showinfo("Success","Contact updated success")
        else:
            messagebox.showerror("Warning","Data is wrong .. check please")


        


view= AppView()





# def item_selected (event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         global student_id
#         student_id=record[4]
#         name.set(record[3])
#         family.set(record[2])
#         phone.set(record[1])
#         address.set(record[0])

# tree.bind("<<TreeviewSelect>>",item_selected)