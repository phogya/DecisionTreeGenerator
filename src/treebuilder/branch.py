'''
A class that represents a branch in a decision tree.

@author: Peter
'''

class Branch(object):
    '''
    Branch node for decision tree, has one question function that splits children nodes
    '''

    def __init__(self, value, question, children):
        '''
        Branch Constructor
        
        Arguments:
            value - The outcome of the above branch's question that lead to this branch
            question - This branch's question, the questions return values split the children
            children - This branch's children, on for each return value of the question
        '''
        
        self._question = question
        self._children = children
        self._value = value
    
    def __eq__(self, other):
        '''
        Overwrites the equality operator
        
        Arguments:
            other - The other branch to compare to
            
        Returns:
            True if they are equivalent, otherwise False
        '''
        
        if self.question() == other.question() and self.children() == other.children() and self.value() == other.value():
            return True
        return False
            
    def askQuestion(self, strArr):
        '''
        Use this branch's questions on a given string array
        
        Arguments:
            strArr - The string array to use the question on
            
        Returns:
            The return value of the question, should be a string
        '''
        
        return self.question()(strArr)
    
    def value(self):
        '''
        Return this branch's value, the outcome of the above branch's question that lead to
        this branch. This is None if the branch is the root.
        
        Returns:
            The value
        '''
        
        return self._value
        
    def question(self):
        '''
        Returns this branch's question
        
        Return:
            The question
        '''
        
        return self._question
    
    def children(self):
        '''
        Returns the child nodes of this branch
        
        Returns:
            The child nodes
        '''
        
        return self._children
    
    def addChild(self, newChild):
        '''
        Adds a new child node the this branch
        
        Arguments:
            newChild - The child node to add
        '''
        
        self._children.append(newChild)
    
    def type(self):
        '''
        Returns the type of node to differentiate between branchs and leaves
        
        Returns:
            The type 'B' for branch
        '''
        
        return 'B'
        