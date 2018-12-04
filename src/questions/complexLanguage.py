'''
A complex set of functions to determine the language of a string of text. The
language can be English, French, Spanish, German, or Italian

@author: Peter
'''

# Five most common English words
def theQ(line):
    if line == None:
        return ("Contains \"the\"", "Does not contain \"the\"")
    
    if "The" in line or "the" in line:
        return "Contains \"the\""
    else:
        return "Does not contain \"the\""
    
def beQ(line):
    if line == None:
        return ("Contains \"be\"", "Does not contain \"be\"")
    
    if "Be" in line or "be" in line:
        return "Contains \"be\""
    else:
        return "Does not contain \"be\""
    
def toQ(line):
    if line == None:
        return ("Contains \"to\"", "Does not contain \"to\"")
    
    if "To" in line or "to" in line:
        return "Contains \"to\""
    else:
        return "Does not contain \"to\""
    
def ofQ(line):
    if line == None:
        return ("Contains \"of\"", "Does not contain \"of\"")
    
    if "Of" in line or "of" in line:
        return "Contains \"of\""
    else:
        return "Does not contain \"of\""
    
def andQ(line):
    if line == None:
        return ("Contains \"and\"", "Does not contain \"and\"")
    
    if "And" in line or "and" in line:
        return "Contains \"and\""
    else:
        return "Does not contain \"and\""
    
# Five most common Spanish words
def elQ(line):
    if line == None:
        return ("Contains \"el\"", "Does not contain \"el\"")
    
    if "El" in line or "el" in line:
        return "Contains \"el\""
    else:
        return "Does not contain \"el\""
    
def laQ(line):
    if line == None:
        return ("Contains \"la\"", "Does not contain \"la\"")
    
    if "La" in line or "la" in line:
        return "Contains \"la\""
    else:
        return "Does not contain \"la\""
    
def deQ(line):
    if line == None:
        return ("Contains \"de\"", "Does not contain \"de\"")
    
    if "De" in line or "de" in line:
        return "Contains \"de\""
    else:
        return "Does not contain \"de\""
    
def queQ(line):
    if line == None:
        return ("Contains \"que\"", "Does not contain \"que\"")
    
    if "Que" in line or "que" in line:
        return "Contains \"que\""
    else:
        return "Does not contain \"que\""
    
def yQ(line):
    if line == None:
        return ("Contains \"y\"", "Does not contain \"y\"")
    
    if "Y" in line or "y" in line:
        return "Contains \"y\""
    else:
        return "Does not contain \"y\""
    
# Five most common Italian words
def nonQ(line):
    if line == None:
        return ("Contains \"non\"", "Does not contain \"non\"")
    
    if "Non" in line or "non" in line:
        return "Contains \"non\""
    else:
        return "Does not contain \"non\""

def eQ(line):
    if line == None:
        return ("Contains \"e\"", "Does not contain \"e\"")
    
    if "E" in line or "e" in line:
        return "Contains \"e\""
    else:
        return "Does not contain \"e\""
    
def cheQ(line):
    if line == None:
        return ("Contains \"che\"", "Does not contain \"che\"")
    
    if "Che" in line or "che" in line:
        return "Contains \"che\""
    else:
        return "Does not contain \"che\""
    
def diQ(line):
    if line == None:
        return ("Contains \"di\"", "Does not contain \"di\"")
    
    if "Di" in line or "di" in line:
        return "Contains \"di\""
    else:
        return "Does not contain \"di\""
    
def ilQ(line):
    if line == None:
        return ("Contains \"il\"", "Does not contain \"il\"")
    
    if "Il" in line or "il" in line:
        return "Contains \"il\""
    else:
        return "Does not contain \"il\""

# Five most common French words
def leQ(line):
    if line == None:
        return ("Contains \"le\"", "Does not contain \"le\"")
    
    if "Le" in line or "le" in line:
        return "Contains \"le\""
    else:
        return "Does not contain \"le\""
    
def unQ(line):
    if line == None:
        return ("Contains \"un\"", "Does not contain \"un\"")
    
    if "Un" in line or "un" in line:
        return "Contains \"un\""
    else:
        return "Does not contain \"un\""

def àQ(line):
    if line == None:
        return ("Contains \"à\"", "Does not contain \"à\"")
    
    if "À" in line or "à" in line:
        return "Contains \"à\""
    else:
        return "Does not contain \"à\""
    
def êtreQ(line):
    if line == None:
        return ("Contains \"être\"", "Does not contain \"être\"")
    
    if "Être" in line or "être" in line:
        return "Contains \"être\""
    else:
        return "Does not contain \"être\""
    
def etQ(line):
    if line == None:
        return ("Contains \"et\"", "Does not contain \"et\"")
    
    if "Et" in line or "et" in line:
        return "Contains \"et\""
    else:
        return "Does not contain \"et\""

# Five most common German words
def dasQ(line):
    if line == None:
        return ("Contains \"das\"", "Does not contain \"das\"")
    
    if "Das" in line or "das" in line:
        return "Contains \"das\""
    else:
        return "Does not contain \"das\""
    
def istQ(line):
    if line == None:
        return ("Contains \"ist\"", "Does not contain \"ist\"")
    
    if "Ist" in line or "ist" in line:
        return "Contains \"ist\""
    else:
        return "Does not contain \"ist\""
    
def duQ(line):
    if line == None:
        return ("Contains \"du\"", "Does not contain \"du\"")
    
    if "Du" in line or "du" in line:
        return "Contains \"du\""
    else:
        return "Does not contain \"du\""
    
def ichQ(line):
    if line == None:
        return ("Contains \"ich\"", "Does not contain \"ich\"")
    
    if "Ich" in line or "ich" in line:
        return "Contains \"ich\""
    else:
        return "Does not contain \"ich\""
    
def nichtQ(line):
    if line == None:
        return ("Contains \"nicht\"", "Does not contain \"nicht\"")
    
    if "Nicht" in line or "nicht" in line:
        return "Contains \"nicht\""
    else:
        return "Does not contain \"nicht\""
    
# Non language specific questions
def averageWordLengthQ(line):
    if line == None:
        return ("Less than 3", "3", "4", "5", "6", "7", "8", "More than 8")
    
    wordSum = sum(len(word) for word in line)
    averageWordLength = round(wordSum / len(line))
    
    if averageWordLength < 3:
        return "Less than 3"
    elif averageWordLength > 8:
        return "More than 8"
    else:
        return str(averageWordLength)

# Special character questions    
def ñQ(line):
    if line == None:
        return ("Contains \"ñ\"", "Does not contain \"ñ\"")
    
    for word in line:
        if "Ñ" in word or "ñ" in word:
            return "Contains \"ñ\""
    else:
        return "Does not contain \"ñ\""

# Select acute accented characters: á Á é É í Í ó Ó ú Ú
def acuteAccentQ(line):
    if line == None:
        return ("Contains acute accent", "Does not contain acute accent")
    
    acuteChars = ['á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 'Ú']
    for word in line:
        for char in word:
            if char in acuteChars:
                return "Contains acute accent"
            
    return "Does not contain acute accent"

# Select grave accented characters: à À è È ì Ì ò Ò ù Ù
def graveAccentQ(line):
    if line == None:
        return ("Contains grave accent", "Does not contain grave accent")
    
    graveChars = ['à', 'À', 'è', 'È', 'ì', 'Ì', 'ò', 'Ò', 'ù', 'Ù']
    for word in line:
        for char in word:
            if char in graveChars:
                return "Contains grave accent"
            
    return "Does not contain grave accent"

# Select circumflex accented characters: â Â ê Ê î Î ô Ô û Û
def circumflexAccentQ(line):
    if line == None:
        return ("Contains circumflex accent", "Does not contain circumflex accent")
    
    circumflexChars = ['â', 'Â', 'ê', 'Ê', 'î', 'Î', 'ô', 'Ô', 'û', 'Û']
    for word in line:
        for char in word:
            if char in circumflexChars:
                return "Contains circumflex accent"
            
    return "Does not contain circumflex accent"

# Select diaeresis accented characters: ä Ä ë Ë ï Ï ö Ö ü Ü
def diaeresisAccentQ(line):
    if line == None:
        return ("Contains diaeresis accent", "Does not contain diaeresis accent")
    
    diaeresisChars = ['ä', 'Ä', 'ë', 'Ë', 'ï', 'Ï', 'ö', 'Ö', 'ü', 'Ü']
    for word in line:
        for char in word:
            if char in diaeresisChars:
                return "Contains diaeresis accent"
            
    return "Does not contain diaeresis accent"
