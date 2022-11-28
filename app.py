from flask import Flask

app = Flask(__name__)

# app.run(port=5000)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/czesc")
@app.route("/czesc/<imie>")
def czesc(imie=None):
    return f""" 
    <html>
    <head><title>czesc</title><head>
    <body>
    <h1>CZESC wam i {imie} !</h1>
    </body>    
    </html>
    """
#@app.route("/hej/<imie>")
#def powitanie(imie):
   # return f"Czesc {imie}"

@app.route("/users/<int:id>")

def indentificator_users(id):
    return f"Dane uzytkownika o id: {id}"


