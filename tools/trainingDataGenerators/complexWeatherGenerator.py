import random

file1 = open("complexWeatherTrainingData.txt", "w")

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

    stormDanger = 0

    if windSpeed == 12:
        stormDanger += 4
    elif windSpeed == 11:
        stormDanger += 3
    elif windSpeed == 10:
        stormDanger += 2
    elif windSpeed == 9:
        stormDanger += 1

    if rainAmount >= 600:
        stormDanger += 4
    elif rainAmount >= 500:
        stormDanger += 3
    elif rainAmount >= 400:
        stormDanger += 2
    elif rainAmount >= 300:
        stormDanger += 1

    if atmoPressure <= 920:
        stormDanger += 3

    coldDanger = 0

    if temperature <= -20:
        coldDanger += 3
    elif temperature <= -15:
        coldDanger += 2
    elif temperature <= 10:
        coldDanger += 1

    if snowAmount >= 2.0:
        coldDanger += 2
    elif snowAmount >= 1.0:
        coldDanger += 1

    if precipitationType in ("Sleet", "Graupel", "Hail"):
        coldDanger += 1

    pleasantness = 0

    if precipitationType == "Drizzle":
        pleasantness += 1

    if 13 >= temperature < 16:
        pleasantness += 1
    elif 16 >= temperature < 19:
        pleasantness += 2
    elif 19 >= temperature < 24:
        pleasantness += 3
    elif 24 >= temperature < 27:
        pleasantness += 2
    elif 27 >= temperature < 130:
        pleasantness += 1

    if rainAmount == 0:
        pleasantness += 2
    elif rainAmount <= 50:
        pleasantness += 1

    if snowAmount == 0:
        pleasantness += 2
    elif snowAmount <= 0.25:
        pleasantness += 1

    if 0 <= windSpeed <= 2:
        pleasantness += 2
    elif 3 <= windSpeed <=5:
        pleasantness += 1

    # Florida Storm Resist
    if -30 <= latitude <= 30:
        stormDanger -= 1

    # North Cold Resist
    if 40 <= latitude <= 90:
        coldDanger -= 1
    elif -40 >= latitude >= -90:
        coldDanger -= 1

    danger = stormDanger + coldDanger
    netPleasantness = pleasantness - danger

    if danger >= 3:
        line += "Dead"
    elif danger == 2:
        line += "Danger"
    elif 6 < netPleasantness:
        line += "Picnic"
    elif 3 < netPleasantness <= 6:
        line += "Great"
    elif 0 < netPleasantness <= 3:
        line += "Pleasant"
    else:
        line += "Dull"
    
    line += "\n"
    file1.write(line)

file1.close()



