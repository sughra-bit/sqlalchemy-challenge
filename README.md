# sqlalchemy-challenge

SurfsUp
The SurfsUp directory contains climate_starter.ipynb Jupyter Notebook, the app.py Python script, prcp and frequency1 png and a Resources folder which contains the hawaii.sqlite database, hawaii_measurements.csv and hawaii_stations.csv.

Analyze and Explore the Climate Data
Climate analysis and data exploration was done on the hawaii.sqlite database. The climate.ipynb Jupyter Notebook was created to perform precipitation analysis and station analysis. The app.py Python script was created to design a climate app with a Flask API with 5 routes with JSON lists.

Precipitation Analysis

ORM queries were done to get the date and prcp data for the last 12 months.

Pandas DataFrame was created using the queried data.

precipitation
('2016-08-23', 0.0)
('2016-08-23', 0.15)
('2016-08-23', 0.05)
('2016-08-23', None)
('2016-08-23', 0.02)
('2016-08-23', 1.79)
...	...

A summary statistics table was printed for the precipitation data for the last 12 months.

precipitation
count	2021.000000
mean	0.177279
std	0.461190
min	0.000000
25%	0.000000
50%	0.020000
75%	0.130000
max	6.700000

Station Analysis

All stations and its number of counts were listed in descending order.
[('USC00519281', 2772),
 ('USC00519397', 2724),
 ('USC00513117', 2709),
 ('USC00519523', 2669),
 ('USC00516128', 2612),
 ('USC00514830', 2202),
 ('USC00511918', 1979),
 ('USC00517948', 1372),
 ('USC00518838', 511)]
The minimum, average and maximum temperature data were queried for the most active station.

The last 12 months of temperature observation data for the most active station were queried

tobs
0	77.0
1	77.0
2	80.0
3	80.0
4	75.0
...	...
The results were binned and plotted in histogram using Pandas plot histogram method. image

Design Climate API
A Climate API was created using Flask. The following 5 routes are available routes created using Flask:


/api/v1.0/precipitation (Precipitation)
/api/v1.0/stations (Stations)
/api/v1.0/tobs (TOBS)
/api/v1.0/<start> 
/api/v1.0/<start>/<end>
