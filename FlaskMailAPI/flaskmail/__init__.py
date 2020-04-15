# Packages
from flask import Flask

# Initializing the Flask App
app = Flask(__name__)

# Importing Routes
from flaskmail import routes
