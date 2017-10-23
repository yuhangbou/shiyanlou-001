#! /usr/bin/env python3
import sys

def calculate(salary,dict1):

   def baoxian(y,d):
       number=(float(d['yanglao'])+float(d['yiliao'])+float(d['shiye'])+float(d['gongjijin']))
       if salary<=2193.00:
           number=2193.00*number
       elif salary>=16446.00:
           number=16446.00*number   
       else:
           number=y*number       
       return number
   baoxian=baoxian(salary,dict1)
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
       elif x<=0:
           tax_rate=0.00
       return tax_rate
   rate=calculaterate(x)
   money=salary-baoxian-rate
   return baoxian,rate,money
   print("{0}:{1:.2f}".format(idnum,money))
class makedi(object):
   def __init__(self,name):
       self.name=name
       self.userdate={}
   def set_dict(self,x,y):
       for i in range(len(x)):
           z,w=x[i].strip('\n').split(y)
           self.userdate[z]=w
   def get_dict(self):
       return self.userdate
    

if __name__=='__main__':
    lis=sys.argv[1:]
    cfile=lis[lis.index('-c')+1]
    dfile=lis[lis.index('-d')+1]
    ofile=lis[lis.index('-o')+1]
    try:
        file=open(cfile)
        shehui=file.readlines()
        file.close()
        file=open(dfile)
        worker=file.readlines()
        file.close()
        s=makedi('shehui')
        w=makedi('worker')
        s.set_dict(shehui,'=')
        shehui_dict=s.get_dict()
        w.set_dict(worker,',')
        work_dict=w.get_dict()
        file=open(ofile,'w')
    except:
        print('FileError\n')
    for key,value in work_dict.items():
        sb,rate,salary=calculate(int(value),shehui_dict)
        message=key+','+value+','+'{:.2f}'.format(sb)+','+'{:.2f}'.format(rate)+','+'{:.2f}'.format(salary)+'\n'
        file.write(message)
    file.close()
   

