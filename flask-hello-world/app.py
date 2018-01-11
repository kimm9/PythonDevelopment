## Flask Hello World

# import the flask claass from the flask package


from flask import Flask

# create application object

app = Flask(__name__)

# user the decorator pattern to 
# link the view function to a url

# Debug Mode/Error Handling
app.config["DEBUG"] = True

# define the view using a function, which returns a string 

@app.route("/")
@app.route("/hello")



def hello_world(): 
  return "Hi World, It's a me a mario"



# return search query on this route 
@app.route("/test/<search_query>")

def search(search_query):
  return search_query

@app.route("/name/<name>")

def index(name):

  if name.lower() == "matthew":
    return "Hello, {}".format(name)
  else:
    return "Not Found", 404


# start the development server using the run() method

if __name__ == "__main__":
    app.run()