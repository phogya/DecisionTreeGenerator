'''
A complex set of functions to determine how the weather is outside

@author: Peter
'''

# Temperature in celsius
def temperatureQ(line):
    if line == None:
        return ("Temperature < -22C", "-22C <= Temperature < -17C", "-17C <= Temperature < -12C", "-12C <= Temperature < -7C", "-7C <= Temperature < -2C", "-2C <= Temperature < 3C", "3C <= Temperature < 8C", "8C <= Temperature < 13C", "13C <= Temperature < 18C", "18C <= Temperature < 23C", "23C <= Temperature < 28C", "28C <= Temperature < 33C", "33C <= Temperature < 38C", "38C <= Temperature")
    
    temperature = int(line[0])
    
    if temperature < -22:
        return "Temperature < -22C"
    elif -22 <= temperature < -17:
        return "-22C <= Temperature < -17C"
    elif -17 <= temperature < -12:
        return "-17C <= Temperature < -12C"
    elif -12 <= temperature < -7:
        return "-12C <= Temperature < -7C"
    elif -7 <= temperature < -2:
        return "-7C <= Temperature < -2C"
    elif -2 <= temperature < 3:
        return "-2C <= Temperature < 3C"
    elif 3 <= temperature < 8:
        return "3C <= Temperature < 8C"
    elif 8 <= temperature < 13:
        return "8C <= Temperature < 13C"
    elif 13 <= temperature < 18:
        return "13C <= Temperature < 18C"
    elif 18 <= temperature < 23:
        return "18C <= Temperature < 23C"
    elif 23 <= temperature < 28:
        return "23C <= Temperature < 28C"
    elif 28 <= temperature < 33:
        return "28C <= Temperature < 33C"
    elif 33 <= temperature < 38:
        return "33C <= Temperature < 38C"
    else:
        return "38C <= Temperature"
    
# Atmoshperic pressure in millibars
def atmopressureQ(line):
    if line == None:
        return ("Atmospheric Pressure < 900mb", "900mb <= Atmospheric Pressure < 925mb", "925mb <= Atmospheric Pressure < 950mb", "950mb <= Atmospheric Pressure < 975mb", "975mb <= Atmospheric Pressure < 1000mb", "1000mb <= Atmospheric Pressure < 1025mb", "1025mb <= Atmospheric Pressure < 1050mb", "1050mb <= Atmospheric Pressure")
    
    atmoPressure = int(line[1])
    
    if atmoPressure < 900:
        return "Atmospheric Pressure < 900mb"
    elif 900 <= atmoPressure < 925:
        return "900mb <= Atmospheric Pressure < 925mb"
    elif 925 <= atmoPressure < 950:
        return "925mb <= Atmospheric Pressure < 950mb"
    elif 950 <= atmoPressure < 975:
        return "950mb <= Atmospheric Pressure < 975mb"
    elif 975 <= atmoPressure < 1000:
        return "975mb <= Atmospheric Pressure < 1000mb"
    elif 1000 <= atmoPressure < 1025:
        return "1000mb <= Atmospheric Pressure < 1025mb"
    elif 1025 <= atmoPressure < 1050:
        return "1025mb <= Atmospheric Pressure < 1050mb"
    else:
        return "1050mb <= Atmospheric Pressure"
    
# Cardinal and intercardinal
def windDirectionQ(line):
    if line == None:
        return ("N", "S", "E", "W", "NE", "NW", "SE", "SW")
    
    return line[2]

# Speed using Beaufort Scale
def windSpeedQ(line):
    if line == None:
        return ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    
    return line[3]

# Dew Point in Celsius
def dewPointQ(line):
    if line == None:
        return ("Dew Point < -30C", "-30C <= Dew Point < -22C", "-22C <= Dew Point < -14C", "-14C <= Dew Point < -6C", "-6C <= Dew Point < 2C", "2C <= Dew Point < 10C", "10C <= Dew Point < 18C", "18C <= Dew Point < 26C")
    
    dewPoint = int(line[4])
    
    if dewPoint < 30:
        return "Dew Point < -30C"
    elif -30 <= dewPoint < -22:
        return "-30C <= Dew Point < -22C"
    elif -22 <= dewPoint < -14:
        return "-22C <= Dew Point < -14C"
    elif -14 <= dewPoint < -6:
        return "-14C <= Dew Point < -6C"
    elif -6 <= dewPoint < 2:
        return "-6C <= Dew Point < 2C"
    elif 2 <= dewPoint < 10:
        return "2C <= Dew Point < 10C"
    elif 10 <= dewPoint < 18:
        return "10C <= Dew Point < 18C"
    elif 18 <= dewPoint < 26:
        return "18C <= Dew Point < 26C"
    else:
        return "26C <= Dew Point"
    
# Precipitation type
def precipitationTypeQ(line):
    if line == None:
        return ("Drizzle", "Rain", "Sleet", "Snow", "Graupel", "Hail", "None")
    
    return line[5]

# Amount of rain in mm
def rainAmountQ(line):
    if line == None:
        return ("Rain Amount = 0mm", "0mm < Rain Amount <= 250mm", "250mm < Rain Amount <= 500mm", "500mm < Rain Amount <= 750mm", "750mm < Rain Amount <= 1000mm", "1000mm < Rain Amount <= 1250mm", "1250mm < Rain Amount <= 1500mm", "1500mm < Rain Amount")
    
    rainAmount = int(line[6])
    
    if rainAmount == 0:
        return "Rain Amount = 0mm"
    elif 0 < rainAmount <= 250:
        return "0mm < Rain Amount <= 250mm"
    elif 250 < rainAmount <= 500:
        return "250mm < Rain Amount <= 500mm"
    elif 500 < rainAmount <= 750:
        return "500mm < Rain Amount <= 750mm"
    elif 750 < rainAmount <= 1000:
        return "750mm < Rain Amount <= 1000mm"
    elif 1000 < rainAmount <= 1250:
        return "1000mm < Rain Amount <= 1250mm"
    elif 1250 < rainAmount <= 1500:
        return "1250mm < Rain Amount <= 1500mm"
    else:
        return "1500mm < Rain Amount"
    
# Amount of snow in m
def snowAmountQ(line):
    if line == None:
        return ("Snow Amount = 0.0m", "0.0m < Snow Amount <= 0.5m", "0.5m < Snow Amount <= 1.0m", "1.0m < Snow Amount <= 1.5m", "1.5m < Snow Amount <= 2.0m", "2.0m < Snow Amount <= 2.5m", "2.5m < Snow Amount")
    
    snowAmount = float(line[7])
    
    if snowAmount == 0:
        return "Snow Amount = 0.0m"
    elif 0 < snowAmount <= 0.5:
        return "0.0m < Snow Amount <= 0.5m"
    elif 0.5 < snowAmount <= 1.0:
        return "0.5m < Snow Amount <= 1.0m"
    elif 1.0 < snowAmount <= 1.5:
        return "1.0m < Snow Amount <= 1.5m"
    elif 1.5 < snowAmount <= 2.0:
        return "1.5m < Snow Amount <= 2.0m"
    elif 2.0 < snowAmount <= 2.5:
        return "2.0m < Snow Amount <= 2.5m"
    else:
        return "2.5m < Snow Amount"
    
# Longitude in degress
def longitudeQ(line):
    if line == None:
        return ("-180 <= Longitude < -150", "-150 <= Longitude < -120", "-120 <= Longitude < -90", "-90 <= Longitude < -60", "-60 <= Longitude < -30", "-30 <= Longitude < 0", "0 <= Longitude < 30", "30 <= Longitude < 60", "60 <= Longitude < 90" , "90 <= Longitude < 120", "120 <= Longitude < 150", "150 <= Longitude < 180")
    
    longitude = int(line[8])
    
    if -180 <= longitude < -150:
        return "-180 <= Longitude < -150"
    elif -150 <= longitude < -120:
        return "-150 <= Longitude < -120"
    elif -120 <= longitude < -90:
        return "-120 <= Longitude < -90"
    elif -90 <= longitude < -60:
        return "-90 <= Longitude < -60"
    elif -60 <= longitude < -30:
        return "-60 <= Longitude < -30"
    elif -30 <= longitude < 0:
        return "-30 <= Longitude < 0"
    elif 0 <= longitude < 30:
        return "0 <= Longitude < 30"
    elif 30 <= longitude < 60:
        return "30 <= Longitude < 60"
    elif 60 <= longitude < 90:
        return "60 <= Longitude < 90"
    elif 90 <= longitude < 120:
        return "90 <= Longitude < 120"
    elif 120 <= longitude < 150:
        return "120 <= Longitude < 150"
    else:
        return "150 <= Longitude < 180"
    
# Latitude in degress
def latitudeQ(line):
    if line == None:
        return ("-90 <= Latitude < -75", "-75 <= Latitude < -60", "-60 <= Latitude < -45", "-45 <= Latitude < -30", "-30 <= Latitude < -15", "-15 <= Latitude < 0", "0 <= Latitude < 15", "15 <= Latitude < 30", "30 <= Latitude < 45" , "45 <= Latitude < 60", "60 <= Latitude < 75", "75 <= Latitude < 90")
    
    latitude = int(line[9])
    
    if -90 <= latitude < -75:
        return "-90 <= Latitude < -75"
    elif -75 <= latitude < -60:
        return "-75 <= Latitude < -60"
    elif -60 <= latitude < -45:
        return "-60 <= Latitude < -45"
    elif -45 <= latitude < -30:
        return "-45 <= Latitude < -30"
    elif -30 <= latitude < -15:
        return "-30 <= Latitude < -15"
    elif -15 <= latitude < 0:
        return "-15 <= Latitude < 0"
    elif 0 <= latitude < 15:
        return "0 <= Latitude < 15"
    elif 15 <= latitude < 30:
        return "15 <= Latitude < 30"
    elif 30 <= latitude < 45:
        return "30 <= Latitude < 45"
    elif 45 <= latitude < 60:
        return "45 <= Latitude < 60"
    elif 60 <= latitude < 75:
        return "60 <= Latitude < 75"
    else:
        return "75 <= Latitude < 90"
    