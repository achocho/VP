dec=int(input())
TempBine=[]
ExactBine=[]
bine=[]
OctalBine=[]
while dec>0:
    
 
    if dec%2==0:
        TempBine.append(0)
    else:
        TempBine.append(1)
    dec=dec/2
    dec=int(dec)
for i in range(len(TempBine)-1,-1,-1):
    bine.append(TempBine[i])
ExactBine=bine
OctalBine=bine
length=len(bine)
if length%4!=0:
    TempBine=bine
    bine=[]
    while length%4!=0:
       length+=1
       bine.append(0)
    for i in range(len(TempBine)):
        bine.append(TempBine[i])

hex=[]
tempHex=0
temp=[]
for i in range(len(bine)):
    tempHex=0
    temp.append(bine[i])
    if (i+1)%4==0:
        counter=3
        for i in range(len(temp)):
          
            if temp[i]==1:
                tempHex+=2**counter
            counter-=1
        temp=[]
        if tempHex<10:
           hex.append(tempHex)
        else:
            hex.append(chr(tempHex+55))
length=len(OctalBine)
if length%3!=0:
    TempBine=OctalBine
    OctalBine=[]
    while length%3!=0:
       length+=1
       OctalBine.append(0)
    for i in range(len(TempBine)):
        OctalBine.append(TempBine[i])
oct=[]

tempOct=0
temp=[]
for i in range(len(OctalBine)):
    tempOct=0
    temp.append(OctalBine[i])
    if (i+1)%3==0:
        counter=2
        for i in range(len(temp)):
            
             if temp[i]==1:
                 tempOct+=2**counter
             counter-=1
        temp=[]
        oct.append(tempOct)
print(ExactBine)
print(oct)
print(hex)
       
    

   
