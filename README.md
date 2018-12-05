# Decision Tree Generator

This program builds on the ideas in the Language Decision Tree program. However instead 
of building a tree to determine whether a string of text is in English or Dutch using a 
static set of functions this program builds decision trees from any properly formatted
set of functions data and can be used to determine anything. The functions must be formatted like this:

    def theQ(line):
        if line == None:
            return ("Contains \"the\"", "Does not contain \"the\"")
    
        if "The" in line or "the" in line:
            return "Contains \"the\""
        else:
            return "Does not contain \"the\""

The function must take one argument, an array of strings. It should run some significant test on the array and return some corresponding output as a string. The strings returned will be used when the tree is printed so the more clear they are the easier it will be to analyze the tree later. There should be a special case where None is passed to the function. In this case it should return a tuple of all possible return values. These functions will serve as questions on each line of data to sort them. The training data must be formatted like this:

    The quick brown fox jumps over the lazy dog. English
    Ich bin ein Berliner. German

The training data should contain some string of information with an outcome at the end. These outcomes are what the tree will try to determine on future data that does not have them. For instance when building a tree with this data and the theQ function we defined above it will associate the word "the" with English. So when given non-training data it will be more likely to determine a line is in English if it contains the word "the".

There are several examples given that can further clarify how to create files for the tree to be built from. The functions can be found in the questions folder, the labeled training data can be found in the trainingdata folder, and the unlabeled data can be found in the data folder. Finally none of the function return values and none of the outcome labels at the end of each line of training data may contain a pound # symbol. This symbol is used to store the tree as a pound separated value file. The pound symbol was chosen as commas are very common in written languages and numbers whereas the pound symbol is much more uncommon.

Additionally there is a tolerance value that is used by the tree building algorithm that can be adjusted. This tolerance value must be between 0 and 1, non-inclusive, and will determine the minimum information gain from each function before the algorithm will skip them. This value can significantly mitigate the tendency of overfitting in complex decision trees and should be adjusted according to the amount of functions and the size of the training data set to yield the best tree in a reasonable amount of time. 

More information regarding the use of the UI can be found by clicking on the Help button. The program can be run from the command line by navigating to the src folder and using the command:

    py -3 main.py

with python 3.7 installed.

