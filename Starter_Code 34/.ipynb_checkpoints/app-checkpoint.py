# Import the dependencies.
import pandas as pd
import numpy as np  
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session  
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#################################################
# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

#################################################

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes

# Define a route that returns a JSON representation of a query result
@app.route("/")
def welcome():
    return (
        f"Welcome page <br/>"
        f"Routes <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    
    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

if __name__=='__main__':
    app.run()
