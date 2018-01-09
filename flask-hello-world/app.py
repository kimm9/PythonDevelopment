## Flask Hello World

# import the flask claass from the flask package

from flask import Flask

# create application object

app = Flask(__name__)

# user the decorator pattern to 
# link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string 

def hello_world(): 
	return "YO WHAT IS GOOD, WORLD!"

# start the development server using the run() method

if __name__ == "__main__":
    app.run()