# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################

# find the most recent date in the database
most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Calculate the date 1 year ago from the last data point in the database
first_date = dt.date(2017,8,23) - dt.timedelta(days=365)

session.close()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():

# List all available API routes

    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start date]<br/>"
        f"/api/v1.0/[start date]/[end date]<br/>" )

#####################################################

# Create precipitation route

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    
    """Return the dictionary for last 12 months of precipitation data"""

# query for data and precipitation scores 

 data_prcp = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).filter(Measurement.date>= first_date).all()
    
    
# Creating a dictionary where date is the key and prcp is the value
    prcp_list = []
    
    for date, prcp in data_prcp:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)
        
    
    return jsonify(prcp_list)

###################################################

# Create stations route

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)    
     
    """Return a list of all stations in the database"""

    # Query for all stations from the database
    stations_data = session.query(Station.station).all()

    # open the tuples 
    stations_list = list(np.ravel(stations_data))

    #jsonify list
    return jsonify(stations_list)

###################################################

# Create tempratures route

@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    
    """Return a list of temperatures of the most active station in the last year"""

    # Find the most active station
    tobs_data = session.query(Measurement.station).group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).first()

    most_active_station = tobs_data[0]

    # query to get temperature data for most active station
    temp_data = session.query(Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date>=first_date).all()
    
    # turning query into list
    active_temp_list = list(np.ravel(temp_data))

    # return jsonified list
    return jsonify(active_temp_list)
###################################################

# Create start route
    
@app.route("/api/v1.0/<start>")
def start_temp:

    session = Session(engine)
    
     # take any date and convert to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')

    
    # Make a list to query (the minimum, average and maximum temperature)
    temp_query=session.query[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs).filter(Measurement.date >= date_dt).all()]
    
   
        # Create a list to hold results
    t_list = []
    for result in results:
        r = {}
        r["StartDate"] = start_dt
        r["TMIN"] = result[0]
        r["TAVG"] = result[1]
        r["TMAX"] = result[2]
        t_list.append(r)

    # jsonify the result
    return jsonify(t_list)

##################################################################

# Create end route

@app.route("/api/v1.0/min_max_avg/<start>/<end>")
def start_end(start, end):
    
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average, and the max temperature for a given start and end dates."""

    # take start and end dates and convert to yyyy-mm-dd format for the query
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d')
    end_dt = dt.datetime.strptime(end, "%Y-%m-%d")

    # query data for the start date value
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_dt).filter(Measurement.date <= end_dt)


    # Create a list to hold results
    t_list = []
    for result in results:
        r = {}
        r["StartDate"] = start_dt
        r["EndDate"] = end_dt
        r["TMIN"] = result[0]
        r["TAVG"] = result[1]
        r["TMAX"] = result[2]
        t_list.append(r)

    # jsonify the result
    return jsonify(t_list)

##########################################################
#run the app
if __name__ == "__main__":
    app.run(debug=True)