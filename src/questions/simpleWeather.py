'''
A simple set of functions to determine how the weather is outside

@author: Peter
'''
def temperatureQ(line):
    if line == None:
        return ("Less than 20 degrees", "Between 20 and 40 degrees", "Between 40 and 60 degrees", "Between 60 and 80 degrees", "Over 80 degrees")
    
    temp = int(line[0])
    
    if temp < 20:
        return "Less than 20 degrees"
    elif temp <= 40:
        return "Between 20 and 40 degrees"
    elif temp <= 60:
        return "Between 40 and 60 degrees"
    elif temp <= 80:
        return "Between 60 and 80 degrees"
    else:
        return "Over 80 degrees"
    
def windQ(line):
    if line == None:
        return ("Less than 4 mph", "Between 4 and 8 mph", "Over 8 mph")
    
    wind = int(line[1])
    
    if wind < 4:
        return "Less than 4 mph"
    elif wind <= 8:
        return "Between 4 and 8 mph"
    else:
        return "Over 8 mph"
    
def rainQ(line):
    if line == None:
        return ("Raining", "Not Raining")
    
    rain = line[2]
    
    if rain == "Rain":
        return "Raining"
    else:
        return "Not Raining"
    
def sunQ(line):
    if line == None:
        return ("Sunny", "No sun")
    
    sun = line[3]
    
    if sun == "Sunny":
        return "Sunny"
    else:
        return "No sun"
    
def humidQ(line):
    if line == None:
        return ("High Humidity", "Low Humidity")
    
    humid = line[4]
    
    if humid == "Humid":
        return "High Humidity"
    else:
        return "Low Humidity"