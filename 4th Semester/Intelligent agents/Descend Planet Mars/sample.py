from geopy import geocoders
g = geocoders.GoogleV3(api_key='AIzaSyCS1M21Cz-wJ7PqTD8Lqrf1PmsGbQyllos')

#create an input address string
#you can also build this by reading from an input database and building a string

inputAddress = 'Calle del Universo, 3, Valladolid' 

#do the geocode
location = g.geocode(inputAddress, timeout=10)

#some things you can get from the result
print(location.latitude, location.longitude)
print(location.raw)
print(location.address)