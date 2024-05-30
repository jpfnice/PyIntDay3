import re


class ParseFloatError(Exception):
    pass 

def parseFloat(inputText):
    """
    parseFloat is a  function ...

    Parameters
    ----------
    inputText : a str
        A string that represent a float value

    Raises
    ------
    ParseFloatError
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.
        
    >>> parseFloat("23.45")
    23.45
    >>> parseFloat("23.")
    23.0
    >>> parseFloat("abc")
    Traceback (most recent call last):
    ...
    ParseFloatError: Bad float format: abc

    """
    reg=re.compile(r"^[+-]?(\d|[1-9]\d*)\.\d*$")
    mo=reg.search(inputText)
    if mo:
        return float(mo[0])+1 # <=> return float(mo.group(0))
    else:
        raise ParseFloatError(f"Bad float format: {inputText}")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=0) 
    

"""
this function parse a string and convert it into a float
...

>>> parseFloat("23.45")
23.45
>>> parseFloat("23.")
23.0
>>> parseFloat("abc")
Traceback (most recent call last):
...
ParseFloatError: Bad float format: abc

"""
    
    