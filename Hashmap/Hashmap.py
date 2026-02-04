from typing import List 

dictonary = {'a' : 1, 
             'b': 9, 
             'c': 'nebrasaka',
             'd': True
}

dictonary['e'] = 4.5
del dictonary['b']
print(dictonary['c'])

for counter in dictonary:
    print(counter, dictonary[counter])