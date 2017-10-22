#! /usr/bin/env python3
import sys
try:
    salary=int(sys.argv[1])
    
except:
    print("Parameter Error")
x=salary-3500
if x>80000:
    tax_rate=x*0.45-13505
elif 55000<x<=80000:
    tax_rate=x*0.35-5505
elif 35000<x<=55000:
    tax_rate=x*0.30-2755
elif 9000<x<=35000:
    tax_rate=x*0.25-1005
elif 4500<x<=9000:
    tax_rate=x*0.20-555
elif 1500<x<=4500:
    tax_rate=x*0.10-105
elif 0<x<=1500 :
    tax_rate=x*0.03
print("{0:.2f}".format(tax_rate))
