###Write a function that accepts a sequence of whitespace separated words as a string input, sorts each item alphanumerically 
###and removes any duplicate items, then returns the result as a string. (Stretch goal: Write a test for this function.)

###Suppose the following input is supplied to the program: 'hello world and practice makes perfect and hello world again'
 
###Then, the output should be: 'again and hello makes perfect practice world'

long = "hello world and practice makes perfect and hello world again"
x = long.split()
list1 = list(dict.fromkeys(x))
list1.sort()
string = ' '.join(map(str, list1))
print (string)