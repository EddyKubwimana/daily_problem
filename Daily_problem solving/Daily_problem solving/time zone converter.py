from datetime import datetime
def time_delta(t1, t2):
    form = "%a %d %b %Y %H:%M:%S %z"
    
    t1 = datetime.strptime(t1, form)
    t2 = datetime.strptime(t2, form)
    return (abs((t1-t2).total_seconds()))
    
a ="Sun 10 May 2015 13:54:36 -0700"
b ="Sun 10 May 2015 13:54:36 -0000"
c ="Sat 02 May 2015 19:54:36 +0530"
d="Fri 01 May 2015 13:54:36 -0000"

print(time_delta(a,b))


