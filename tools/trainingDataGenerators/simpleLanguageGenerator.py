import random

file1 = open("simpleLanguageTrainingData.txt", "w")

line = ""
for i in range(500):
    
    line = ""
    selector =  random.randint(0,7)

    if selector == 0:
        line += "This is a test "
        line += "Test"
    if selector == 1:
        line += "This will be a test "
        line += "Test"
    if selector == 2:
        line += "This might be a test "
        if random.getrandbits(1):
            line += "Test"
        else:
            line += "NoTest"
    if selector == 3:
        line += "This could be a test "
        if random.getrandbits(1):
            line += "Test"
        else:
            line += "NoTest"
    if selector == 4:
        line += "This can be a test "
        if random.getrandbits(1):
            line += "Test"
        else:
            line += "NoTest"
    if selector == 5:
        line += "This is not a test "
        line += "NoTest"
    if selector == 6:
        line += "This will not be a test "
        line += "NoTest"
    if selector == 7:
        line += "This can’t be a test "
        line += "NoTest"
    if selector == 8:
        line += "This will be no test "
        line += "NoTest"
    
    line += "\n"
    file1.write(line)

file1.close()
