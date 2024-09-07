import tkinter as tk
from tkinter import messagebox
from controller import register_on_db, fetch_all, update, delete, search
from tkinter import *
from tkinter import ttk


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
        search_entry = tk.Entry(self.root)
        search_entry.place(x=400,y=50)
        search_btn = tk.Button(self.root , text="search", command=lambda:self.search_contact(search_entry.get())).place(x=450,y=80)
        save_btn = tk.Button(self.root, text="Save",\
                             command=lambda:self.register_user(name_entry.get(),family_entry.get(),phone_entry.get())).place(x=290,y=140)
        update_btn = Button(self.root, text="Update", command=lambda:self.update_contact\
                            (record[0],name_entry.get(),family_entry.get(),\
                             phone_entry.get())).place(x=200, y= 140)
        delete_btn = Button(self.root, text="Delete", \
                            command=lambda:self.delete_contact(record[0])).place(x=400, y=140)
        refresh_btn = Button(self.root, text="refresh", command=lambda:self.insert_into_tree(tree)).place(x=500, y=140)


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

    def register_user(self, name,family,phone):
        
        if register_on_db(name, family, phone):
            messagebox.showinfo("Success","Contact saved success")
            self.clear_entry()

        else:
            messagebox.showerror("Warning","Data is wrong .. check please")
        

        data = self.fetch_all_contacts()

    def fetch_all_contacts(self):
        return fetch_all()
    
    def insert_into_tree(self, n):
        data = self.fetch_all_contacts()
        self.clear_tree(n)
        self.clear_entry()
        for row in data:
            n.insert("","end",values=(row[0], row[1],row[2],row[3]))

    def clear_tree(self, n):
        for elm in n.get_children():
            n.delete(elm)   
    
    def clear_entry(self):
        name_entry.delete(0, END)
        family_entry.delete(0, END)
        phone_entry.delete(0, END)
  
    def update_contact(self,id,name,family,phone):
        if update (id,name,family,phone):
            self.insert_into_tree(tree)
            messagebox.showinfo("Success","Contact updated success")
        else:
            messagebox.showerror("Warning","Data is wrong .. check please")

    def delete_contact(self,id):
        result = messagebox.askquestion("Delete confirm", "Are you sure?")
        if result == "yes":
            if delete(id):
                messagebox.showinfo("success", "User has been deleted ... ")
            else :
                messagebox.showerror("title", "sth went wrong")
        else:
            pass
                
    def search_contact(self,family):
        data =  search(family)
        self.clear_tree(tree)
        for row in data:
            tree.insert("","end",values=(row[0], row[1],row[2],row[3]))

view= AppView()





