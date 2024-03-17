import json


with open('objectdata.json', 'r') as objectdata:
    data = json.load(objectdata)
    


def showelement(X1, Y1, X2, Y2, X3, Y3, X4,Y4):
    D1= X1**2+Y1**2
    D2= X2**2+Y2**2
    D3= X3**2+Y3**2
    D4= X4**2+Y4**2
    
    Dlist= [D1,D2,D3,D4]
    Min= Dlist.index(min(Dlist))
    while(Dlist[Min]==0):
        Dlist.pop(Min)
        Min= Dlist.index(min(Dlist))
        
    if (Dlist[Min]==D1):
        return X1,Y1
    if (Dlist[Min]==D2):
        return X2,Y2
    if (Dlist[Min]==D3):
        return X3,Y3
    return X4,Y4

for element in data:
    posX, posY = showelement(element['FirstObjectDistance_X'],element['FirstObjectDistance_Y'],element['SecondObjectDistance_X'],element['SecondObjectDistance_Y'],element['ThirdObjectDistance_X'],element['ThirdObjectDistance_Y'],element['FourthObjectDistance_X'],element['FourthObjectDistance_Y'])
    print(str(int(posX/128))+'  '+str(int(posY/128)))
    

