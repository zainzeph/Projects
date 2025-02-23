# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:49:46 2021

@author: zwilliams
"""
import time

infoStore=[10,20,30,40,50,60,70,80]

Positions = ['1',9,10, '1x2',-9,-10, '1x3', 20,21,-22]


Targits = []

print("Input targit 1")
Targit0 = input()
Targits.append(Targit0)
print("Input targit 2")
Targit1 = input()
Targits.append(Targit1)
print("Input targit 3")
Targit2 = input()
Targits.append(Targit2)



start = time.time()

CPosition = []
for I in range(3):       
    var = -1
    for i in Positions:
        var = var + 1
        C = Targits[I]
        if(i == C) :
            re = 0
            while (re < 2) :
                CPosition.append((Positions[var + 1]))
                var = var + 1
                re = re + 1
            
print(CPosition)



C = 0
for i in CPosition:
                Data = CPosition[C]
                if (Data > 0 and i%2==0):
                    Data = Data / infoStore[0]
                if (Data < 0 and i%2==0):
                    Data = Data / infoStore[4]
                    
                if (Data > 0 and i%2==1):
                    Data = Data / infoStore[2]
                if (Data < 0 and i%2==1):
                    Data = Data / infoStore[6]
                C = C + 1
                print(Data)
                
                
Bord = int(input())
A = 500/100
B = Bord/100
C = B / A 

print(A)
print(B)
print(C)

elapsed_time_lc=(time.time()-start)
print(elapsed_time_lc)

