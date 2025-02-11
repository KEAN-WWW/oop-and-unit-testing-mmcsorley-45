from flask import Flask, render_template

# intialize Flask service
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello class CPS3500!'

@app.route("/hi")
def hi():
    return 'This is new section!'
@app.route("/lookup/<username>")
def lookup(username):
    return "You id is: " + str(username)

def display():
    return("<!DOCTYPE html>"
           "<html lang=\"en\">"
           "<head>"
           "<title>Flask Tutorial</title>)"
           "<head>"
           "<body>"
           "<h1>This is the Index page</h1>"
           "</body>"
           "</html>")
@app.route('/template2')
def display_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)