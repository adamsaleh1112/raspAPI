from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def default():
    return("Test successful")

@app.route('/login', methods=["GET", "POST"]) # tells API route that the function a POST functon
def login(): # this function is where database would go
    pass

@app.route('/createaccount', methods=["GET", "POST"]) # tells API route that the function a POST functon
def createAccount(): # this function is where database would go
    pass

@app.route('/gui', methods=["GET", "POST"]) # tells API route that the function a POST functon
def gui(): # this function is where database would go
    pass

if __name__ == "__main__":
    app.run()
