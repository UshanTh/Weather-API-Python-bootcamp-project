import requests
from datetime import datetime

api_key = '8d934250297926b080a7b12654e070e5'
location = input("Enter the City name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("---------------------------")
print ("Weather Stats for - {}  ||  {}".format(location.upper(), date_time))
print ("---------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd, 'kmph')


# create text file
fileName = "Weatherinfo.txt"
accessmode = "w"
myfile = open(fileName, accessmode)
myfile.write("---------------------------\n")
myfile.write("Weather Stats for - {}  ||  {}\n".format(location.upper(), date_time))
myfile.write("---------------------------\n")

myfile.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
myfile.write("Current weather desc  :")
myfile.write(weather_desc+"\n")
myfile.write("Current humidity      :")
myfile.write(str(hmdt) + ' %\n')
myfile.write("Current wind speed    :")
myfile.write(str(wind_spd) + ' kmph')
myfile.close()

