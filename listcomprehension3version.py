from math import log


def calcList(v, xs):
    ''' Recieves two inputs(v, xs) from a list. Using list comprehension
        this function manipulates the data to compare it the
        expected results, which is also found in the same list.
        Sample input list
        
       |-TestID-|   |-v-|   |--------xs--------------------|
        (   1,       18,   [-83, 97, 37, 45, -16, -7, 10, 27],

        |---expected result after manipulating list---|
        [443.747, 133.604, 171.2998, 23.0259, 88.9876])'''

    #filters all positive integers into a new list
    filterPositive = filter((lambda x: x>0), xs)

    #With only positive integers left, maps x*log(x) to each element, creating a new list
    mapEquation = list(map(lambda x: x*log(x), filterPositive))

    #formats the data to four decimal places
    fourDecimals = [round(float(x),4) for x in mapEquation]

    #Checks to see if the new x values are greater than the v value
    #If greater, it places elements into our final list
    GreaterThanV = filter((lambda x: x>v), fourDecimals)

    #returns final list
    return list(GreaterThanV)
----------------version 2-----------------------------

    xs = [ x for x in xs if x >0 ]
    xs = [(x*log(x)) for x in xs]
    xs = [round(float(x),4) for x in xs]
    xs = [x for x in xs if x > v]
    return xs       
-------------------version 3------------------------------------


    xs = [x*log(x) for x in xs if (round(float(x),4) > 0)]
    xs = [x for x in xs if x > v]
    return xs       









