from model import Connection
conn = Connection()



def register_on_db(name, family, phone):
    if name=="" or family=="" or phone == "":
        return False
    else :
        conn.register_on_db(name,family,phone)
        return True


def fetch_all():
    result = conn.fetch_all()
    if result:
        return result
    else:
        return False

def update(id,name,family,phone):
    if name=="" or family=="" or phone == "":
        return False
    else:
       conn.update(id,name,family,phone)
       return True
      
    
def delete(id):
    if conn.delete(id):
        return True
    else:
        return False
    
def search(family):
    result = conn.search(family)
    if result : 
        return result
    else:
        return False