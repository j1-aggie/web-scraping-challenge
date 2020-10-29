from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_info = mongo.db.mars_collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_info)

#scrape route
@app.route("/scrape")
def scrape():
  
   
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_collection.update({}, mars_data, upsert=True)
    
    #go back to the home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=5000)