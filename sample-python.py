from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if this file is the main program
if __name__ == '__main__':
    app.run()

