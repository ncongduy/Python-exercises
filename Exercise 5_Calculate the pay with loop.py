while True:
    h = raw_input("hours:")
    try:
        hours = float(h)
    except:
        hours = -1
        print "Error, please type positive numeric input"
    if hours>0:
        break

while True:
    r = raw_input("rate:")
    try:
        rate = float(r)
    except:
        rate = -1
        print "Error, please type positive numeric input"
    if rate>0:
        break

if hours<=40:
    pay = hours*rate
elif hours>40:
    pay = 40*rate + (hours-40)*rate*1.5

print pay
        
    
        
    
            
        




        
