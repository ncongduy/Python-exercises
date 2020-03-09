hours = raw_input("hours:")
rate = raw_input("rate:")
if hours<=40:
    pay = float(hours)*float(rate)
    print pay

elif hours>40:
    pay = 40*float(rate)+(float(hours)-40)*float(rate)*1.5
    print pay
    
