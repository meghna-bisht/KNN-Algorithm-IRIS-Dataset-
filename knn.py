# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:21:23 2018

@author: ACER
"""

import math
import operator
def main():
    k=80
    f=open("iris_train.txt","r")
    f1=f.readlines()
    train=[]
    for x in f1:
        a=x.split(',')
        if(a[4]=='Iris-setosa\n' or a[4]=='Iris-setosa'):
            a[4]=0
        if(a[4]=='Iris-versicolor\n' or a[4]=='Iris-versicolor'):
            a[4]=1
        if(a[4]=='Iris-virginica\n' or a[4]=='Iris-virginica'):
            a[4]=2
        train.append(a)
    f.close()
    
    f=open("iris_test.txt","r")
    f1=f.readlines()
    test=[]
    for x in f1:
        a=x.split(',')
        if(a[4]=='Iris-setosa\n' or a[4]=='Iris-setosa'):
            a[4]=0
        if(a[4]=='Iris-versicolor\n' or a[4]=='Iris-versicolor'):
            a[4]=1
        if(a[4]=='Iris-virginica\n' or a[4]=='Iris-virginica'):
            a[4]=2
        test.append(a)
   
    sum=0
    total=0
    for x in test:
        d=[]
        for y in train:
            t0=(float(x[0])-float(y[0]))*(float(x[0])-float(y[0]))
            t1=(float(x[1])-float(y[1]))*(float(x[1])-float(y[1]))
            t2=(float(x[2])-float(y[2]))*(float(x[2])-float(y[2]))
            t3=(float(x[3])-float(y[3]))*(float(x[3])-float(y[3]))
            t=t0+t1+t2+t3
            
            dis=math.sqrt(t)
            d.append([dis,y[4]])
        z=sorted(d,key=operator.itemgetter(0))
        
        
        #print z
        c0=0
        c1=0
        c2=0
        for i in range(0,k):
            if(z[i][1]==0):
                c0+=1
            elif(z[i][1]==1):
                c1+=1
            elif(z[i][1]==2):
                c2+=1
        print c0,c1,c2
        if(c0>c1):
            if(c0>c2):
                c=0
            else:
                c=2
        else:
            if(c1>c2):
                c=1
            else:
                c=2
        if(c==x[4]):
            sum+=1
        total+=1
    print "Accuracy : " 
    print ((float(sum))/(float(total)))*100
    
if __name__=="__main__":
    main()

