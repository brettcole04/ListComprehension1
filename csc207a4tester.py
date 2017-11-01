from csc207a4 import calcList
from csc207a4testData import tests

def closeTo (a, b):
    return abs (a - b) < 0.01

def compareResult (result, expectedResult):
    if not len (result) == len (expectedResult):
        return False
    for i in range (len (result)):
        if not closeTo (result [i], expectedResult [i]):
            return False
    return True

def runTest ():
    passedCases = []
    failedCases = []
    n = len (tests)
    for (testId, v, xs, expectedResult) in tests:
        try:
            result = calcList (v, xs)
            passed = compareResult (result, expectedResult)
            if passed:
                passedCases.append (testId)
            else:
                failedCases.append (testId)
        except:
            failedCases.append (testId)

    score = len (passedCases)
    testScore = score * 0.2
    print ('Passed: %s' % passedCases)
    print ('Failed: %s' % failedCases)
    print ('%d of %d test cases passed. Score = %.2f of 20.00' % (score, n, testScore))

runTest ()
