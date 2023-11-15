# sqlalchemy-challenge
## Introduction

The Weather API allows users to access weather data for a particular location. It provides information on precipitation, station details, and temperature observations. The API is built using Flask and SQLAlchemy.

## Technologies Used

- Flask
- SQLAlchemy
- SQLite
- Python

  # Use the SQLAlchemy create_engine() function to connect to your SQLite database.
  ```
  engine = create_engine("sqlite:///hawaii.sqlite")
  ```
  # Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
 ```
Base = automap_base()
Base.prepare(autoload_with=engine)
Measurement = Base.classes.measurement
Station = Base.classes.station
```
# Link Python to the database by creating a SQLAlchemy session.
```
session = Session(engine)
```

## Analysis
# Station Histogram
To analyze and visualize the distribution of temperature observations from the most active weather station, a histogram is created. The following steps can be taken:

-Identify the most active weather station.

-Query the last 12 months of temperature observation data for this station.

-Plot the results as a histogram using Pandas and Matplotlib.
