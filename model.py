import sqlite3


class Connection:
    
    def __init__(self) -> None:
        self.db = sqlite3.connect("my_db.db")
        self.cursor = self.db.cursor()
        
    def register_on_db(self,name,family,phone_number):
       try :
            q = f"insert into contacts (name,family,phone) Values('{name}',\
                '{family}','{phone_number}')"
            self.cursor.execute(q)
            self.db.commit()
            return True
       except : 
           False
    
    def fetch_all(self):
        q = "select * from contacts"
        self.cursor.execute(q)
        return self.cursor.fetchall()
    

    def update(self,id,name,family,phone):
        q = f"update contacts set name = '{name}', family = '{family}', phone = '{phone}' where id = '{id}'"
        self.cursor.execute(q)
        self.db.commit()
        return True

