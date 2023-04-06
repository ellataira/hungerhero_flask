from flask import Blueprint


# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the 
# blueprint object, not the app object.
views = Blueprint('views', __name__)

# This is a base route
# we simply return a string.  
@views.route('/')
def home():
    return ('<h1>Hello from your web app!!</h1>')

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@views.route('/test')
def tester():
    return "<h1>this is a test!</h1>"