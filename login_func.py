import import_export
def signin(name, password):
    data=pull_data()
    
    if name in data.keys() :
        if data[name] == password :
            return True
        else :
            return False
    else :
        return False
        
def signup(name, password):
    data=pull_data()
    if name in data.keys() :
        print("name already exists")
        return False
    else:
        push_data({name: password})
        return True