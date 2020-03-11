h = raw_input("hours:")
try:
    hours = float(h)
except:
    hours = -1

if hours<=0:
    print "Error, please enter positive numeric input"
elif hours>0:  
    r = raw_input("rate:")
    try:
        rate = float(r)
    except:
        rate = -1

    if rate<=0:
        print "Error, please enter positive numeric input"
    elif rate>0:
        pay = hours*rate
        print pay

        
