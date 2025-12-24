import numpy
def small_enough(a, limit): 
    arr = numpy.array(a)
    
    result = arr <= limit
    
    if False in result:
        return False
    return True