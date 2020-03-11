h = raw_input("hours:")
r = raw_input("rate:")
try:
    hours = float(h)
except:
    hours = -1
if hours<=0:
    print "Error, please enter positive numeric input"

try:
    rate = float(r)
except:
    rate = -1
if rate<=0:
    print "Error, please enter positive numeric input"
        
def computepay (hours,rate):
    if hours<=40 and hours>0 and rate>0:
        pay = hours*rate
    elif hours>40 and rate>0:
        pay = 40*rate+(hours-40)*rate*1.5
    else:
        pay = "Please try again"
    return pay

x = computepay(hours,rate)
print x

