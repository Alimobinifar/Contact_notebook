from model import Connection
conn = Connection()



def register_on_db(name, family, phone):
   
    if conn.register_on_db(name,family,phone):
        return True
    else:
        return False

def fetch_all():
    result = conn.fetch_all()
    if result:
        return result
    else:
        return False

def update(id,name,family,phone):

    if conn.update(id,name,family,phone):
        return True
    else:
        return False