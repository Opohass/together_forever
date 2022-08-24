from flask import Flask,render_template,send_from_directory

from random import randint
app= Flask(__name__)



@app.route('/<username>') 
def send_file(username): 
    
    return f"hello {username}"

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/random')
def Myrandom():
    return f"{randint(0,1000)}"

if __name__ == "__main__":
    app.run(host="10.0.0.220")
