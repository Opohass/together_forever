
import requests
adrees="http://10.0.0.220:5000/random"
baseA=adrees="http://10.0.0.220:5000/"
send= baseA+"/2,3,x"

responses=requests.get(send)
print(responses.text)