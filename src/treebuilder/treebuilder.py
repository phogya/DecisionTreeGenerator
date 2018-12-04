'''
Functions for creating, deleting, printing, and writing decision trees built 
from a generic set of functions and some prepared training data

@author: Peter
'''
from importlib import import_module
from math import log
from .leaf import Leaf
from .branch import Branch
from types import FunctionType
from os import getcwd, remove
from shutil import copy
from multiprocessing import Pool

def buildTree(name, examples, questions, tolerance, printbool):
    '''
    Parses given files and hands them off to other functions to process and build the tree
    
    Arguments:
        name - The name of the tree
        examples - the file to get the examples from
        questions - the file to get the questions from
        tolerance - the importance tolerance for tree questions
        printbool - whether or not to print the tree
    
    Returns:
        Error codes if something went wrong
        Nothing if tree is built successfully and printbool is false
        A text version of the tree if built successfully and printbool is true
    '''
    
    if name == "":
        return 101
    if examples == "":
        return 102
    if questions == "":
        return 103
    if tolerance == "":
        return 104
    
    if ":" in examples:
        exBrowse = True
    else:
        exBrowse = False
        
    if ":" in questions:
        qBrowse = True
    else:
        qBrowse = False
    
    path = getcwd()
    try:
        examplesName = examples.split("/")[-1]
        if exBrowse:
            copy(examples, path + "/trainingdata/" + examplesName)
        
        treeExamples = getExamples(path + "/trainingdata/" + examplesName)
    except:
        return 201
    
    try:
        questionsName = questions.split("/")[-1]
        if qBrowse:
            copy(questions, path + "/questions/" + questionsName)
    
        treeQuestions = getQuestions("questions." + questionsName[:-3])
    except:
        return 202
    
    try:
        for question in treeQuestions:
            for outcome in question(None):
                if isinstance(outcome, str):
                    if '\\' in outcome:
                        return 209
    except:
        return 210

    try:
        treeTolerance = float(tolerance)
    except:
        return 203
    
    if treeTolerance <= 0 or treeTolerance >= 1:
        return 203
    
    try:
        tree = decisionTreeLearning(treeExamples, treeQuestions, [], None, treeTolerance)
    except:
        return 301
    
    try:
        writeTree(tree, name, path, questionsName)
    except:
        return 204

    if printbool == True:
        return getTreeText(tree)
    
    return
    
def decisionTreeLearning(examples, questions, parentExamples, value, tolerance):
    '''
    Recursively builds a decision tree from prepared examples and questions
    
    Arguments:
        examples - the remaining examples to build the tree from, with outcomes at the end of every line
        questions - the remaining questions, an array of functions that take an array of strings and return a string
        parentExamples - the previous branche's examples in case there are no examples left at this point, None if first root
        value - the value of this branch from the previous branche's question
        tolerance - the minimum importance value of a question to be included in the tree at a particular point
        
    Returns:
        The root node of a decision tree
    '''
    
    # If there are no examples at this point return the most common outcome of the above branch
    if not examples:
        return makeLeafFromExamples(parentExamples, value)
    
    else:
        i = 1
        examplesAreSame = True
        firstOutcome = examples[0][-1]
        
        for i in range(1, len(examples)):
            if not examples[i][-1]  == firstOutcome:
                examplesAreSame = False
                break
                
        # If all examples have the same outcome return that outcome with 1.0 probability
        if examplesAreSame == True:
            return Leaf(value, firstOutcome, 1.0)
        
        # If there are no more questions return the most common outcome
        elif not questions:
            return makeLeafFromExamples(examples, value)
            
        else:
            # If none of the above conditions are true find the best question and create a branch
            
            bestQuestion = max(questions, key=lambda x: importance(x, examples))
            
            # If the best question is below the tolerance value return the most common outcome
            if importance(bestQuestion, examples) < tolerance:
                return makeLeafFromExamples(examples, value)
            
            outcomes = bestQuestion(None)
            examplesByOutcome = [[] for i in range(len(outcomes))]
            for example in examples:
                examplesByOutcome[outcomes.index(bestQuestion(example))].append(example)  
            
            children = []
            remainingQuestions = [question for question in questions if question != bestQuestion]
            
            # Parallelize children of root, only root children are parallelized as pool creates daemon threads
            # and they cannot spawn more threads, can overwrite pool later to spawn more if wanted
            if value == None:
                argSets = []
                for i in range(len(outcomes)):
                    argSets.append([examplesByOutcome[i], remainingQuestions, examples, outcomes[i], tolerance])
                
                pool = Pool()
                children = pool.map(decisionTreeArgParse, argSets)
            
            # If this isnt the root don't parallelize
            else:
                for i in range(len(outcomes)):
                    children.append(decisionTreeLearning(examplesByOutcome[i], remainingQuestions, examples, outcomes[i], tolerance))
                    
            return Branch(value, bestQuestion, children)

def decisionTreeArgParse(argSet):
    '''
    Helper function for parallelizing root children of decision trees, pool will only take one argument
    so decisionTreeLearning passes it a tuple that gets split up here.
    
    Arguments:
        argSet - A tuple of arguments for decisionTreeLearning
        
    Returns:
        The decision tree after the root
    '''
    
    return decisionTreeLearning(argSet[0], argSet[1], argSet[2], argSet[3], argSet[4])


def mostCommonOutcome(examples):
    '''
    Finds the most common outcome of a given set of examples
    
    Arguments:
        examples - the examples to find the common outcome of
        
    Returns:
        The most common outcome
    '''
    
    outcomes = {}
    for example in examples:
        if example[-1] not in outcomes.keys():
            outcomes[example[-1]] = 1
        else:
            outcomes[example[-1]] += 1
    
    keys = list(outcomes.keys())
    values = list(outcomes.values())
    return keys[values.index(max(values))]

def importance(question, examples):
    '''
    Finds the importance of the given question in sorting the given examples.
    Importance equation and explanation can be found in docs.
    
    Arguments:
        question - the question to find the importance of
        examples - the examples the question will sort
        
    Returns:
        The importance of the question, a number from 0 to 1
    ''' 
    
    exOutcomes = {}
    
    for example in examples:
        if example[-1] not in exOutcomes.keys():
            exOutcomes[example[-1]] = 1
        else:
            exOutcomes[example[-1]] += 1

    exOutcomeProbs = []
    sumExOutcomes = sum(exOutcomes.values())
    
    for exOutcomeValue in exOutcomes.values():
        exOutcomeProbs.append(exOutcomeValue / sumExOutcomes)

    originalEntropy = entropy(exOutcomeProbs)
            
    qOutcomes = {}
    for outcome in question(None):
        qOutcomes[outcome] = {}
    
    for example in examples:
        if example[-1] not in qOutcomes[question(example)].keys():
            qOutcomes[question(example)][example[-1]] = 1
        else:
            qOutcomes[question(example)][example[-1]] += 1
    
    newEntropy = 0
    
    for outcome in qOutcomes.values():
        outcomeProbs = []
        sumOutcomeValues = sum(outcome.values())
        
        for outcomeValue in outcome.values():
            outcomeProbs.append(outcomeValue / sumOutcomeValues)

        newEntropy += ( (sumOutcomeValues / sumExOutcomes ) * entropy(outcomeProbs)) 
        
    return( originalEntropy - newEntropy )

def entropy(probX):
    '''
    Probability entropy equation for use with importance equation, more info in docs.
    Note that this scales the entropy by number of outcomes so it will always return
    between 1 and 0.
    
    Arguments:
        probX - A list of the probabilities of outcomes
        
    Returns:
        The entropy of the given list scaled to be between 0 and 1
    '''
    
    en = 0
    for x in probX:
        if not x == 0:
            en += x * log(x, 2)
    
    try :
        return ( -en / log( len(probX), 2 ))
    except:
        return ( -en )
    
def makeLeafFromExamples(examples, value):
    '''
    Creates a leaf from the given examples
    
    Arguments:
        examples - The examples to find the outcome and probability for this leaf
        value - The outcome of the question branch that leads to this leaf
        
    Returns:
        A leaf with the outcome and probability from the examples and the value
    '''
    
    outcome = mostCommonOutcome(examples)
    numOutcome = 0
    for example in examples:
        if example[-1] == outcome:
            numOutcome += 1
    
    return Leaf(value, outcome, numOutcome / len(examples))
    
def getQuestions(file):
    '''
    Dynamically imports the questions from a given file
    
    Arguments:
        file - The file to pull the questions from
        
    Returns:
        An array of function objects, the questions
    '''
    
    module = import_module(file)
        
    qArr = []
    for a in dir(module):
        if isinstance(getattr(module, a), FunctionType):
            qArr.append(getattr(module, a))
    
    return qArr

def getExamples(file):
    '''
    Gets the examples from the given file
    
    Arguments:
        file - The file to get the examples from
        
    Returns:
        An array of string arrays split by lines then words
    '''
    
    examples = open(file, 'r')
    exArr = examples.readlines()
    exArr = [line.rstrip().split() for line in exArr]
    examples.close()
    
    return exArr

def deleteTree(tree):
    '''
    Deletes a tree file, either from delete button or to clean up after a tree build fail.
    
    Arguments:
        tree - the tree to delete
        
    Returns
        An error code if failed or no return if succeeded
    '''
    
    if tree == "":
        return 105
    
    path = getcwd()
    
    try:
        remove(path + "/trees/" + tree)
    except:
        return 205
    
def writeTreeHelper(tree, output, n=1):
    '''
    Recursive helper function for writeTree
    
    Arguments:
        tree - The tree to write 
        output - An array to append string versions of the tree nodes
        n - The recursion depth
    '''
    
    if tree.type() == 'B':
        output.append("Question" + "#" +  str(n) + "#" + tree.question().__name__ + "\n")
        
        for child in tree.children():
            output.append(str(n) + "#" + str(child.value()) + "\n")
            writeTreeHelper(child, output, n+1)
            
    else:
        output.append("Output#" + str(tree.outcome()) + "#Probability#" + str(tree.probability()) + "\n")

def writeTree(tree, name, path, questions):
    '''
    Writes a given tree to the given path with the given name
    
    Arguments
        tree - The tree to write
        name - The name of the tree
        path - The path to the directory to write the tree in
        questions - The questions file for the tree
    '''
    
    output = []
    writeTreeHelper(tree, output)
    
    with open(path + "/trees/" + name, 'w') as file:
        for line in output:
            file.write(line)
        file.write(questions + "\n")

def printTree(tree, n=1):
    '''
    Prints a given tree to the console
    
    Arguments:
        tree - The tree to print
        n - Recursion depth
    '''
    
    if tree.type() == 'B':
        print(("\t" * (n - 1)) + "Question " + str(n) + " : " + tree.question().__name__)
        
        for child in tree.children():
            print(("\t" * n) + str(n) + " - " + str(child.value()) + " : ")
            printTree(child, n+1)
            
    else:
        print(("\t" * n) + "Output : " + str(tree.outcome()) + ", Probability : " + str(tree.probability()))
        
def getTreeText(tree, n = 1):
    '''
    Gets a readable text version of a tree
    
    Arguments:
        tree - The tree to get the text version of
        n - The recursion depth
        
    Returns:
        An array of strings, a readable version of the tree
    '''
    
    if tree.type() == 'B':
        text = (("\t" * (n - 1)) + "Question " + str(n) + " : " + tree.question().__name__ + "\n")
        
        for child in tree.children():
            text += (("\t" * n) + str(n) + " - " + str(child.value()) + " : " + "\n")
            text += getTreeText(child, n+1)
            
        return text
         
    else:
        return (("\t" * n) + "Output : " + str(tree.outcome()) + ", Probability : " + str(tree.probability()) + "\n")