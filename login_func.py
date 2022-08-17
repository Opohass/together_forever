
import json 

def signin(name, password):
    data={}#yohav func
    
    if name in data.keys() :
        if data[name] == password :
            return True
        else :
            return False
    else :
        return False
        
    