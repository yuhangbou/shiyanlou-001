#! /usr/bin/env python3
import sys

def calculate(message):
   li=message.split(':')
   try:
       salary=int(li[1])
       idnum=int(li[0])
   except:
       print("Parameter Error")

   def baoxian(y):
       number=y*(0.08+0.02+0.005+0.06)
       return number
   baoxian=baoxian(salary)
   x=salary-baoxian-3500
   def calculaterate(x,tax_rate=0):
        
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
       return tax_rate
   
   money=salary-baoxian-calculaterate(x)
   print("{0}:{1:.2f}".format(idnum,money))
if __name__=='__main__':
    lis=sys.argv[1:]
    for i in lis:
        calculate(i) 
    

