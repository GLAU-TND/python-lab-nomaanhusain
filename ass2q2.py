try: 
    a = 100
    a = 100 / 0
    print (a)
    b = 'hello'
    c = int(b)
    z = a+b
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
except TypeError:
    print("Attribute exception raised")
except ValueError:
    print("Value exception raised")
else:  
    print ("Success, no error!")