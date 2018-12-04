'''
A simple set of functions to determine whether a string of text is saying it is
a test or not

@author: Peter
'''
def thisQ(line):
    if line == None:
        return ("Contains \"this\"", "Does not contain \"this\"")
    
    if "This" in line or "this" in line:
        return "Contains \"this\""
    else:
        return "Does not contain \"this\""
    
def isQ(line):
    if line == None:
        return ("Contains \"is\"", "Does not contain \"is\"")
    
    if "Is" in line or "is" in line:
        return "Contains \"is\""
    else:
        return "Does not contain \"is\""

def aQ(line):
    if line == None:
        return ("Contains \"a\"", "Does not contain \"a\"")
    
    if "A" in line or "a" in line:
        return "Contains \"a\""
    else:
        return "Does not contain \"a\""
    
def testQ(line):
    if line == None:
        return ("Contains \"test\"", "Does not contain \"test\"")
    
    if "Test" in line or "test" in line:
        return "Contains \"test\""
    else:
        return "Does not contain \"test\""
    
def willQ(line):
    if line == None:
        return ("Contains \"will\"", "Does not contain \"will\"")
    
    if "Will" in line or "will" in line:
        return "Contains \"will\""
    else:
        return "Does not contain \"will\""
    
def beQ(line):
    if line == None:
        return ("Contains \"be\"", "Does not contain \"be\"")
    
    if "Be" in line or "be" in line:
        return "Contains \"be\""
    else:
        return "Does not contain \"be\""
    
def mightQ(line):
    if line == None:
        return ("Contains \"might\"", "Does not contain \"might\"")
    
    if "Might" in line or "might" in line:
        return "Contains \"might\""
    else:
        return "Does not contain \"might\""
    
def couldQ(line):
    if line == None:
        return ("Contains \"could\"", "Does not contain \"could\"")
    
    if "Could" in line or "could" in line:
        return "Contains \"could\""
    else:
        return "Does not contain \"could\""
    
def canQ(line):
    if line == None:
        return ("Contains \"can\"", "Does not contain \"can\"")
    
    if "Can" in line or "can" in line:
        return "Contains \"can\""
    else:
        return "Does not contain \"can\""
    
def notQ(line):
    if line == None:
        return ("Contains \"not\"", "Does not contain \"not\"")
    
    if "Not" in line or "not" in line:
        return "Contains \"not\""
    else:
        return "Does not contain \"not\""
    
def cantQ(line):
    if line == None:
        return ("Contains \"can't\"", "Does not contain \"can't\"")
    
    if "Can't" in line or "can't" in line:
        return "Contains \"can't\""
    else:
        return "Does not contain \"can't\""
    
def noQ(line):
    if line == None:
        return ("Contains \"no\"", "Does not contain \"no\"")
    
    if "No" in line or "No" in line:
        return "Contains \"no\""
    else:
        return "Does not contain \"no\""