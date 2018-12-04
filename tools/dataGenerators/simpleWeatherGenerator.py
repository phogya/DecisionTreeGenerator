import random

file1 = open("simpleWeatherData.txt", "w")

line = ""
for i in range(200):
    line = ""
    temperature = random.randint(10,95)
    line+= str(temperature)
    line += " "

    windSpeed = random.randint(0,12)
    line += str(windSpeed)
    line += " "
 

    rain = not random.getrandbits(1)
    if rain:
        line += "Rain "
    else:
        line += "NoRain "

    sun = not random.getrandbits(1)
    if sun and not rain:
        line += "Sunny "
    else:
        line += "NoSun "

    humid = not random.getrandbits(1)
    if humid:
        line += "Humid "
    else:
        line += "NotHumid "
    
    line += "\n"
    file1.write(line)

file1.close()



