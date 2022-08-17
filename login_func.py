import import_export

def signin(name, password):
    data=import_export.pull_data()
    
    if name in data.keys() :
        return data[name] == password
    else :
        return False
        
def signup(name, password):
    data=import_export.pull_data()
    if name in data.keys() :
        print("name already exists")
        return False
    else:
        data[name] = password
        return import_export.push_data(data)