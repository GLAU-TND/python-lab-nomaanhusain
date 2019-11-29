try: 
    a = int(input())
    a = a / 0
    print (a)
    b = 'hello'
    c = int(b)
    z = a+b
    import math
    print(math.exp(a))
    assert a == b
except AssertionError:  
        print ("Assertion Exception Raised.")
except OverflowError:  
        print ("OverFlow Exception Raised.")
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
except TypeError:
    print("Attribute exception raised")
except ValueError:
    print("Value exception raised")
else:  
    print ("Success, no error!")