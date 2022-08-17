# echo-server.py
import json
import socket
import ast

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
print ("version2.0.0")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
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
            ##
            ##   
            #send data to clint
            
            #login
            if tempdata[0][:4]==b'login@':
                print(tempdata[0][4:])
                print("--------------------------------")
                print(tempdata[0][4:].decode('utf-8'))
                dictD=ast.literal_eval(tempdata[0][4:].decode('utf-8'))
                print("clint want login")
                print("message:",dictD)
                data=  ":".split(tempdata[0::4]) 
                print("just datat",data)
                file= open('data.json', 'r')
                if data[0] in file.keys() :
                    if file[data[0]] == data[1] :
                        return True
                    else :
                        return False
                else :
                    return False
            if tempdata[0][:4]==b'get@':
                print(tempdata[0][4:])
                print("--------------------------------")
                print(tempdata[0][4:].decode('utf-8'))
                dictD=ast.literal_eval(tempdata[0][4:].decode('utf-8'))
                print("clint want dta")
                print(dictD)
                file= open('data.json', 'r')
                data =list(filter(lambda x:x["name"]==dictD["name"],json.load(file)) )[0]
                file.close()
                print(type(json.dumps(data).encode('utf-8')))
                print(f"send message to {json.dumps(data).encode('utf-8')}")
                conn.sendall(json.dumps(data).encode('utf-8'))
            #get data from clint
            elif tempdata[0][:5]==b'save@':
                tempdata[0]=tempdata[0][5:]
                print(tempdata[0])
                print("save data")
                dictData=ast.literal_eval((b''.join(tempdata)).decode('utf-8'))
                #save file 
                file= open('data.json', 'w')
                json.dump(dictData,file)
                file.close()
            else:
                conn.send(b"eror")
            conn.close()
           
        