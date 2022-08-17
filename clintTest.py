# echo-client.py
import json
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"save@")
    TestDict=[{"porat":1234,"yohav":1234}
              ]
       
    #split data to 1024 bytes
    sendfile= json.dumps(TestDict).encode('utf-8')
    sendfileSplit= [sendfile[i:i+1000] for i in range(0,len(sendfile),1000)]
    #send files
    for mesage in sendfileSplit:         
        s.send(mesage)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.connect((HOST, PORT))
    s2.send(b"get@")
    dataR = s2.recv(1024)
    print(f"Received {dataR!r}")
