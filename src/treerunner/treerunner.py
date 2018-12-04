'''
Functions for parsing a decision tree created by the treebuilder module and
running it on some data

@author: Peter
'''
from treebuilder.leaf import Leaf
from treebuilder.branch import Branch
from treebuilder.treebuilder import getQuestions, getTreeText
from os import getcwd
from shutil import copy

def runTree(treefile, datafile, outputtype, printbool):
    '''
    Parses given files and options to pass off to other functions and return the
    proper things
    
    Arguments:
        treefile - The file of the tree to use
        datafile - The file of the data to use the tree on
        outputtype - The type of output to write
        printbool - Whether or not the print the output
        
    Returns:
        An error code if it failed somewhere
        The results if printbool is True and outputtype is not print tree
        The tree if outputtype is print tree
        If printbool is false and outputtype is not print tree it returns nothing
    '''
    
    if treefile == "":
        return 105
    if datafile == "" and outputtype != "Print Tree":
        return 106
    if outputtype == "":
        return 107
    
    
    path = getcwd()
    
    try:
        textTree = getTree(path + "/trees/" + treefile)
    except:
        return 205
    
    try:
        questions = getQuestions("questions." + textTree.pop(-1)[0][:-3])
    except:
        return 206
    
    if outputtype != "Print Tree":
        try:
            if ":" in datafile:
                data = getData(datafile)
                dataName = datafile.split("/")[-1]
                copy(datafile, path + "/data/" + dataName)
                
            else:
                data = getData(path + "/data/" + datafile)
                dataName = datafile
        except:
            return 207
    try:
        tree = parseTree(textTree, questions, None, 1)
    except:
        return 302
    
    results = ""
    try:
        if outputtype == "Output Only":
            with open(path + "/results/" + dataName.replace(".txt", "") + "-Results.txt", 'w') as file:
                for line in data:
                    result = str(getResult(tree, line))
                    file.write(result + "\n")
                    results += result + "\n"
            
            if printbool:
                return results
            
        elif outputtype == "Full":
            with open(path + "/results/" + dataName.replace(".txt", "") + "-Results.txt", 'w') as file:
                for line in data:
                    result = str(getResult(tree, line))
                    file.write("Line: " + str(line) + " Result: " + result + "\n")
                    results += "Line: " + str(line) + " Result: " + result + "\n"
                    
            if printbool:
                return results
        
        elif outputtype == "Print Tree":
            return getTreeText(tree)
    except:
        return 208
    
    return

def getResult(tree, line):
    '''
    Uses the given tree on the line to determine it's outcome
    
    Arguments:
        tree - The tree to use
        line - The line to use the tree on
        
    Returns:
        The outcome and probability of the outcome from the tree
    '''
    
    if tree.type() == 'B':
        
        outcome = tree.askQuestion(line)
        
        for child in tree.children():
            if child.value() == outcome:
                return getResult(child, line)
            
    else:
        return (tree.outcome(), tree.probability())

def parseTree(textTree, questions, value, qnum):
    '''
    Takes the text version of the tree from the tree file as well as the questions, as
    an array of functions, to recursively rebuild the tree
    
    Arguments:
        textTree - The text version of the tree from the tree file
        questions - The questions as an array of functions
        value - The outcome of the previous branch that led to this branch/leaf
        qnum - The recursion depth, question number
    
    Returns:
        The tree as a branch node
    '''
    
    if textTree[0][0] == "Output":
        return Leaf(value, textTree[0][1], textTree[0][3])
    
    for question in questions:
        if question.__name__ == textTree[0][2]:
            tree = Branch(value, question , [])
            break
    
    current = 1
    next = 1
    
    while current < len(textTree):
        for i in range (current + 1, len(textTree)):
            if textTree[i][0] == str(qnum):
                next = i
                break
            
        if next == current:
            subtree = textTree[current + 1:len(textTree)]
            next = len(textTree)
        else:
            subtree = textTree[current + 1:next]
            
        tree.addChild(parseTree(subtree, questions, textTree[current][1], qnum + 1))
        current = next
    
    return tree

def getTree(treefile):
    '''
    Gets the text version of the tree from the given file
    
    Arguments:
        treefile - The file to get the tree from
        
    Returns:
        The tree as an array of string arrays
    '''
    
    tree = open(treefile, 'r')
    treeArr = tree.readlines()
    treeArr = [line.rstrip('\n').split("#") for line in treeArr]
    tree.close()
    
    return treeArr

def getData(datafile):
    '''
    Gets the data from the given files
    
    Arguments:
        datafile - The file to get the data from
        
    Returns:
        The data as an array of string arrays
    '''
    
    data = open(datafile, 'r')
    dataArr = data.readlines()
    dataArr = [line.rstrip().split() for line in dataArr]
    data.close()
    
    return dataArr