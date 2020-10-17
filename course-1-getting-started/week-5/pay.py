hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
if h <= 40.0:
    gp = h*r
else:
    ot = h-40.0
    gp = (40.0*r)+(ot*(r*1.5))
print(gp)
