import random

file1 = open("complexWeatherData.txt", "w")

line = ""
for i in range(100000):
    line = ""
    temperature = random.randint(-23, 39)
    line += str(temperature)
    line += " "

    atmoPressure = random.randint(899, 1051)
    line += str(atmoPressure)
    line += " "
 
    windDirection = ("N", "S", "E", "W", "NE", "NW", "SE", "SW")[random.randint(0, 7)]
    line += str(windDirection)
    line += " "
    
    windSpeed = random.randint(0, 12)
    line += str(windSpeed)
    line += " "

    dewPoint = random.randint(-31, 27)
    line += str(dewPoint)
    line += " "

    if dewPoint >= temperature:

        if temperature <= 0:
            precipitationType = ("Sleet", "Snow", "Graupel", "Hail")[random.randint(0, 3)]
        else:
            precipitationType = ("Drizzle", "Rain")[random.randint(0, 1)]

    elif (dewPoint + 5) >= temperature:

        if random.randint(0,3) == 3:
            if temperature <= 0:
                precipitationType = ("Sleet", "Snow", "Graupel", "Hail")[random.randint(0, 3)]
            else:
                precipitationType = ("Drizzle", "Rain")[random.randint(0, 1)]
                
    else:
        precipitationType = None
        
    line += str(precipitationType)
    line += " "

    if precipitationType in ("Drizzle", "Rain"):
        rainAmount = random.randint(1, 1501)
    else:
        rainAmount = 0

    line += str(rainAmount)
    line += " "

    if precipitationType in ("Sleet", "Snow", "Graupel", "Hail"):
        snowAmount = round(random.uniform(0.1,2.5), 1)
    else:
        snowAmount = 0.0
        
    line += str(snowAmount)
    line += " "

    longitude = random.randint(-180, 179)
    line += str(longitude)
    line += " "

    latitude = random.randint(-90,89)
    line += str(latitude)
    line += " "
    
    line += "\n"
    file1.write(line)

file1.close()



