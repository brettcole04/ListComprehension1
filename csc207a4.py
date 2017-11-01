#Brett W. Cole
#26 OCT 17
from math import log


def calcList (v, xs):

    ''' Recieves two inputs(v, xs) from a list. Using list comprehension this function manipulates
        the data to compare it the expected results, which is also found in the same list.
                         Sample input list
|-TestID-|   |-v-|   |--------xs--------------------|  |---expected result after manipulating list---|
(   1,       18,   [-83, 97, 37, 45, -16, -7, 10, 27], [443.747, 133.604, 171.2998, 23.0259, 88.9876])'''

    _xs = [x*log(x) for x in xs if (round(float(x),4) > 0)]
    xs = [x for x in _xs if x > v]
    return xs       


            









    

    

