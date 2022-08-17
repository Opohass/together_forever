# echo-server.py
import json
import socket
import hashlib
import ast
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
print ("version2.0.0")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
            tempdata=[]
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if data:
                        tempdata.append(data)
                    if len(data)<1024:
                        break
                
                #tempdata ="code@filename@data
                str_split_data=b''.join(tempdata).decode('utf-8').split('@')
                print(str_split_data[0])
                #send data to clint
                if str_split_data[0]=='addUser':
                    try:
                        file=open(str_split_data[1], 'r')
                        dictlist=json.load(file)
                        file.close()
                    except:
                        print("no login file creat new one")
                        dictlist={}
                    try:
                        #convert str to dict using json and replave 
                        data= str_split_data[2].replace("'","\"")
                        dictData= json.loads(data)
                        flag=True
                    except:
                        flag =False
                    
                    if flag:    
                        dictlist[list(dictData.keys())[0]]=list(dictData.values())[0]#[list(dictData.values())[0],False]
                        file=open(str_split_data[1], 'w')
                        #save file
                        json.dump(dictlist,file)
                        file.close()
                        conn.send(b"200")
                    else:#except:
                        conn.send(b"401")
                elif str_split_data[0]=='login':
                    try:
                        file=open(str_split_data[1], 'r')
                        loginDict=json.load(file)
                        file.close()
                        dictData= ast.literal_eval(str_split_data[2])
                        print(dictData)
                        if list(dictData.keys())[0] in list(loginDict.keys()):
                            if loginDict[list(dictData.keys())[0]][0]==list(dictData.values())[0]:
                                if not (loginDict[list(dictData.keys())[0]][2]):
                                    #test
                                    print(loginDict[list(dictData.keys())[0]][2])
                                    print("sucses")
                                    #
                                    #update login to True
                                    file=open(str_split_data[1], 'w')
                                    loginDict[list(dictData.keys())[0]][2]=True
                                    json.dump(loginDict,file)
                                    file.close()
                                    if loginDict[list(dictData.keys())[0]][1]== "employe":
                                        conn.send(b"202")
                                    elif loginDict[list(dictData.keys())[0]][1]== "mangger":
                                        conn.send(b"203")
                                else:
                                    print("alrdy login")
                                    conn.send(b"404")
                            else:
                                conn.send(b"402")
                        else:
                            conn.send(b"403")
                    except:
                        conn.send(b"401")
        except:           
            conn.close()
           
        
