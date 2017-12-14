import forecastio
import json
from datetime import datetime

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')



api_key = ""
lat = 51.508530
lng = -0.076132



dt = '2012-10-12 00:30:00'
dateobj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
 
forecast = forecastio.load_forecast(api_key, lat, lng, time=dateobj)


#print json.dumps(forecast.json)


#"currently": {
#    "temperature": 14.02,
#    "dewPoint": 12.93,
#    "precipType": "rain",
#    "cloudCover": 0.71,
#    "summary": "Mostly Cloudy",
#    "apparentTemperature": 14.02,
#    "pressure": 999.17,
#    "windSpeed": 10.79,
#    "visibility": 7.4,
#    "time": 1349998200,
#    "windBearing": 227,
#    "humidity": 0.93,
#    "icon": "partly-cloudy-night"
#  },

#print forecast["currently"]

current=forecast.currently()
#print current.time

#print current.temperature,",",current.dewPoint
#print current.temperature, ',',current.dewPoint,',', current.precipType, ',', current.cloudCover, ',',current.summary, ',',current.apparentTemperature, ',',current.pressure, ',',current.windSpeed, ',',current.visibility, ',',dt, ',',current.windBearing, ',',current.humidity, ',',current.icon


from datetime import date, datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current < end:
        yield current
        current += delta


start = datetime(2012,10,26)
end = datetime(2014,2,28)

print 'temp,dewPoint,precipType,cloudCover,summary,apparentTemp,pressure,windSpeed,visibility,datetime,windBearing,humidity,icon'    
#this unlocks the following interface:
for dt in datetime_range(start, end, {'hours':1}):
    #print dt
#    dateobj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    try:
       forecast = forecastio.load_forecast(api_key, lat, lng, time=dt)
       current=forecast.currently()
       #print json.dumps(forecast.json)
       print current.temperature, ',',current.dewPoint,',', current.precipType, ',', current.cloudCover, ',',current.summary, ',',current.apparentTemperature, ',',current.pressure, ',',current.windSpeed, ',',current.visibility, ',',dt, ',',current.windBearing, ',',current.humidity, ',',current.icon    
       #exit()
    except:
       pass
          
