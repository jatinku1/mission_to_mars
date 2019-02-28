from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import scrape_surfing
import scrape_mars

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
#client = PyMongo.MongoClient(conn)

#mongo = PyMongo(app, uri="mongodb://localhost:27017/surfing_app")
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route('/')
def index():
    mars = mongo.db.mars_db.find_all()
    return render_template('index.html', mars=mars)

scraped_data1 = scrape_mars.scrape(scraped_data)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars_db
    mongo.mars_db.insert(scraped_data1)
    mars.update(
        {},
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
