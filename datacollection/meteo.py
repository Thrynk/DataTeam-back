# -*- coding: utf-8 -*-

def recup_meteo(latitude, longitude):
    # Import Meteo model from Django
    import os
    
    # import datetime to get date
    import datetime
    
    # Import requests and Basic auth
    import requests
    from requests.auth import HTTPBasicAuth
    
    # request data from API
    url_base = 'https://api.meteomatics.com/'
    
    date = datetime.datetime.now()
    dateString = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    number_of_days = 7
    number_of_values_per_hour = 1
    
    temperature_parameter = 't_0m:C'
    humidity_parameter = 'relative_humidity_2m:p'
    precipitation_parameter = 'precip_1h:mm'
    
    
    
    url = url_base \
        + dateString \
        + 'P' + str(number_of_days) + 'D:PT' + str(number_of_values_per_hour) + 'H/' \
        + temperature_parameter + ',' + humidity_parameter + ',' + precipitation_parameter + '/' \
        + str(latitude) + ',' + str(longitude) \
        + '/json?model=mix'

    print(url)
        
    
    r = requests.get(url, auth=HTTPBasicAuth('isen_meunier', 'rT2ql81CVUzpS'))
    
    # import json
    #with open('data.json', 'w') as outfile:
    #    json.dump(r.json(), outfile)
        
    data = r.json()

    #print(data)
    
    # temperature
    print(len(data["data"][0]["coordinates"][0]["dates"]))
    # humidity
    print(len(data["data"][1]["coordinates"][0]["dates"]))
    # precipitation
    print(len(data["data"][2]["coordinates"][0]["dates"]))
    
    # create object
    recordsList = []
    for i in range(0, len(data["data"][0]["coordinates"][0]["dates"])):
        recordsList.append( \
                ( \
                        latitude, \
                        longitude, \
                        data["data"][0]["coordinates"][0]["dates"][i]["value"], \
                        data["data"][1]["coordinates"][0]["dates"][i]["value"], \
                        data["data"][2]["coordinates"][0]["dates"][i]["value"], \
                        data["data"][0]["coordinates"][0]["dates"][i]["date"] \
                ) \
        )
        
    BASE_DIR = os.path.abspath('../')
    db_file = os.path.join(BASE_DIR, 'db.sqlite3')
    db_file
    
    import sqlite3
    
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Successfully connected to database")
        
        # create query
        query = """INSERT INTO api_meteo 
            (location_latitude, 
            location_longitude, 
            temperature, 
            humidity, 
            precipitation, 
            date) 
            VALUES(?, ?, ?, ?, ?, ?)"""
        # insert in database
        cursor.executemany(query, recordsList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "records inserted successfully in database")
    except sqlite3.Error as error:
        print(error)
    finally:
        if(sqliteConnection):
            sqliteConnection.close()
            print("database connection closed")
        
if __name__ == "__main__":
    latitude = 50.6
    longitude = 3.06
    recup_meteo(latitude, longitude)