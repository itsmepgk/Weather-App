
from tkinter import *
import requests
import time

#function to convert wind direction from degrees to cardinal
def windDirConvert(dir):
    print(dir)
    if dir >= 11.25 and dir < 33.75:
        return 'NNE'
    elif dir >= 33.75 and dir < 56.25:
        return 'NE'
    elif dir >= 56.25 and dir < 78.75:
        return 'ENE'
    elif dir >= 78.75 and dir < 101.25:
        return 'E'
    elif dir >= 101.25 and dir < 123.75:
        return 'ESE'
    elif dir >= 123.75 and dir < 146.25:
        return 'SE'
    elif dir >= 146.25 and dir < 168.75:
        return 'SSE'
    elif dir >= 168.75 and dir < 191.25:
        return 'S'
    elif dir >= 191.25 and dir < 213.75:
        return 'SSW'
    elif dir >= 213.75 and dir < 236.25:
        return 'SW'
    elif dir >= 236.25 and dir < 258.75:
        return 'WSW'
    elif dir >= 258.75 and dir < 281.25:
        return 'W'
    elif dir >= 281.25 and dir < 303.75:
        return 'WNW'
    elif dir >= 303.75 and dir < 326.25:
        return 'NW'
    elif dir >= 326.25 and dir < 348.75:
        return 'NNW'
    elif (dir >= 348.75 and dir <= 360) or (dir >= 0 and dir < 11.25):
        return 'N'

#Fucntion that calls the API to fetch the weather data
def getWeatherData(canvas):

    city = cityName.get()
    API = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    #Parsing the JSON output data from the API
    JSONData = requests.get(API).json()
    condition = JSONData['weather'][0]['main']
    temperature = int(JSONData['main']['temp'] - 273.15)
    feelsLike = int(JSONData['main']['feels_like'] - 273.15)
    minTemperature = int(JSONData['main']['temp_min'] - 273.15)
    maxTemperature = int(JSONData['main']['temp_max'] - 273.15)
    visibility = JSONData['visibility']
    humidity = JSONData['main']['humidity']
    windSpeed = ((JSONData['wind']['speed']) * 18) / 5
    windDir = windDirConvert(JSONData['wind']['deg'])
    sunriseTime = time.strftime('%I:%M:%S', time.gmtime(JSONData['sys']['sunrise'] - 21600))
    sunsetTime = time.strftime('%I:%M:%S', time.gmtime(JSONData['sys']['sunset'] - 21600))

    conditionInfo = condition + "\n" + str(temperature) + "°C"
    detailedReport = "\n" + "Feels Like: " + str(feelsLike) + "°C" + "\n" + "Minimum: " + str(minTemperature) + "°C" + "\n" + "Maximum: " + str(maxTemperature) + "°C" + "\n" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Visibility: " + str(visibility) + " m" + "\n" + "Wind: " + windDir + " " + str(round(windSpeed)) + "km/h " + "\n" + "\n" + "Sunrise: " + sunriseTime + "\n" + "Sunset: " + sunsetTime
    conditionLabel.config(text = conditionInfo)
    detailsLabel.config(text = detailedReport)


canvas = Tk()
canvas.geometry("600x600")
canvas.title("Weather")
canvas.config(bg = '#3285a8')
font1 = ("poppins", 15, "bold")
font2 = ("poppins", 36, "bold")

instructionLabel = Label(canvas, font = font1, bg = '#3285a8') 
instructionLabel.config(text = "Enter the city name in the box and press enter")
instructionLabel.pack()
cityName = Entry(canvas, justify = 'center', width = 20, font = font2)
cityName.pack(pady = 20)
cityName.focus()
cityName.bind('<Return>', getWeatherData)

conditionLabel = Label(canvas, font = font2, bg = '#3285a8')
conditionLabel.pack()
detailsLabel = Label(canvas,font = font1, bg = '#3285a8')
detailsLabel.pack()
canvas.mainloop()()
