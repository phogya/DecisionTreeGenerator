import random

file1 = open("simpleWeatherTrainingData.txt", "w")

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

    if temperature <= 30:
        if rain:
            line += "Freezing"
        else:
            line += "Cold"
    elif 30 < temperature <= 40:
        if rain:
            line += "Cold"
        elif windSpeed > 10:
            line += "Cold"
        elif windSpeed > 5 and humid:
            line += "Cold"
        elif windSpeed > 5 and not sun:
            line += "Cold"
        else:
            line += "Warm"
    elif 40 < temperature <= 50:
        if rain:
            line += "Cold"
        elif windSpeed > 10 and humid:
            line += "Cold"
        elif windSpeed > 10 and not sun:
            line += "Cold"
        else:
            line += "Warm"
    elif 50 < temperature <= 60:
        if rain and windSpeed > 10:
            line += "Cold"
        else:
            line += "Warm"
    elif 60 < temperature <= 70:
        if sun and windSpeed < 5:
            line += "Hot"
        else:
            line += "Warm"
    elif 70 < temperature <= 80:
        if windSpeed > 10:
            line += "Warm"
        elif not sun and windSpeed > 5:
            line += "Warm"
        elif rain:
            line += "Warm"
        else:
            line += "Hot"
    else:
        line += "Hot"
    
    line += "\n"
    file1.write(line)

file1.close()



