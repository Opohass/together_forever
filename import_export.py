import json
def pull_data():
    my_dict = {}
    try:
        with open('data.json', "r", encoding='utf-8') as f:
            my_dict = json.load(f)
    except :
        print ("no data found")
            
    return my_dict

def push_data(mydict):
    try:
        with open('data.json', 'w') as f:
            json.dump(mydict,f, indent=4)
        return True
    except:
        print("cant push data")
        return False