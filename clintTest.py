#version 17/08/2022 22:33


import json

from socket import socket

from matplotlib.font_manager import json_dump
###online 
import socket
import hashlib
##cinstant 

file_login_name = 'data.json'
##

print("version2.0.0")
###online 
def sendData(data:dict,mesagePost)->str: 
    '''#mesagePost =b"save@sample_file.json@"'''
    try:
        HOST = "127.0.0.1"  # The server's hostname or IP address
        PORT = 65432  # The port used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.send(mesagePost)
            sendfile= json.dumps(data).encode('utf-8')    
            sendfileSplit= [sendfile[i:i+1000] for i in range(0,len(sendfile),1000)]
            #update
            #send files
            for mesage in sendfileSplit:         
                s.sendall(mesage)
            return s.recv(1024) # ok code ==200 false have 401
    except:
        return b"401"
def reciveData(mesagePost)->dict: 
    '''#mesagePost ="get@save@sample_file.json'''
    try:
        HOST = "127.0.0.1"  # The server's hostname or IP address
        PORT = 65432  # The port used by the server
        tempdata=[]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.send(mesagePost)
            while True:
                data = s.recv(1024)
                if data:
                    tempdata.append(data)
                if len(data)<1024:
                    break
            return ((b''.join(tempdata)).decode('utf-8'))
    except:
        return b"401"
            
def chek_login(username:str, password:str)->bool:
    #online
    try:
        mesagePost= b"login@"+file_login_name.encode("utf-8")+b"@"
        hash_username= hashlib.sha256(username.encode()).hexdigest()
        hash_password= hashlib.sha256(password.encode()).hexdigest()
        data={hash_username:hash_password}
        code= StrogeUntily.sendData(data,mesagePost)
        #employe login
        if code == b"202":
            return 202
        #manger login
        elif code == b"203":
            return 203
        elif code ==b"402":
            print("password is incorrect")
            return 402 
        elif code ==b"403":
            print("username is incorrect")
            return 403
        elif code == b"404":
            print("user is login another computer")
            return 404
    except:
        return b"401"
def add_login(username:str, password:str)->None:
    #online
    try:
        mesagePost= b"addUser@"+file_login_name.encode("utf-8")+b"@"
        hash_username= hashlib.sha256(username.encode()).hexdigest()
        hash_password= hashlib.sha256(password.encode()).hexdigest()
        data={hash_username:hash_password}
        return StrogeUntily.sendData(data,mesagePost)
    except:
        return b"401"
def add_login_offline(username:str, password:str)->None:
    hash_username= hashlib.sha256(username.encode()).hexdigest()
    hash_password= hashlib.sha256(password.encode()).hexdigest()
    try:
        file= open(file_login_name,"r")
        data= json.load(file)
    except:
        print("no file we open new one")
        data= {}
    
    data[hash_username]=hash_password
    file =open(file_login_name,"w")
    json.dump(data, file)
    file.close()

    
def chek_login_offline(username:str, password:str)->bool:
    
    hash_username= hashlib.sha256(username.encode()).hexdigest()
    hash_password= hashlib.sha256(password.encode()).hexdigest()
    try:
        file =open(file_login_name,"r")
        loginDict= json.load(file)
    except:
        return False
    if hash_username in loginDict.keys():
        if loginDict[hash_username]==hash_password:
            return True
    return False

    
        
    
        
          
        
        
        