'''
A class that represents a leaf on a decision tree

@author: Peter
'''

class Leaf(object):
    '''
    Leaf node for decision tree
    '''

    def __init__(self, value, outcome, probability):
        '''
        Leaf Constructor
        
        Arguments:
            value - The outcome of the above branch's question that lead to this leaf
            outcome - The determined final outcome of the data line
            probability - The probability of the outcome based on all instances seen in this line of questions
        '''
        
        self._value = value
        self._outcome = outcome
        self._probability = probability
        
    def __eq__(self, other):
        '''
        Overwrites the equality operator
        
        Arguments:
            other - The other leaf to compare to
            
        Returns:
            True if they are equivalent, otherwise False
        '''
        
        if self.outcome() == other.outcome() and self.probability() == other.probability() and self.value() == other.value():
            return True
        return False
    
    def value(self):
        '''
        Return this leaf's value, the outcome of the above branch's question that lead to
        this branch. This is None if this leaf is the root.
        
        Returns:
            The value
        '''
        
        return self._value
    
    def outcome(self):
        '''
        Return this leaf's outcome, the final outcome of the data line determined by the decision tree
        
        Returns:
            The outcome
        '''
        
        return self._outcome
    
    def probability(self):
        '''
        Return this probability of this leaf's outcome based on the number of examples seen in this line of questions
        
        Returns:
            The probability of the outcome
        '''
        
        return self._probability
    
    def type(self):
        '''
        Returns the type of node to differentiate between branchs and leaves
        
        Returns:
            The type 'L' for leaf
        '''
        
        return 'L'