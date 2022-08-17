import json
def pull_data():
    my_dict = {}
    try:
        with open('data.json', "r") as f:
            my_dict = json.load(f)
    except :
        print ("no data found")
            
    return my_dict

def push_data(mydict):
    try:
        with open('data.json', 'w') as f:
            json.dumps(f)
        return True
    except:
        return False