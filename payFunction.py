hrs = input("Enter Hours: ")
h=float(hrs)
rte = input("Enter Rate: ")
r=float(rte)

def computepay(hr,rt):
    if hr<=40:
        return hr*rt
    else:
        return (40*rt)+((hr-40)*(rt*1.5))
p=computepay(h,r)
print("Pay",p)
