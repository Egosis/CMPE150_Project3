actor=input()
listoflists=[]
result=[]
emptylist=[]
file=open("dataset.txt","r")
document=file.read().split("\n")

for i in range (0,len(document)):
    splitted=document[i].split(",")
    actorlist=[]
    toAppend=0
    for j in range(1,4):
        actorlist.append(splitted[j])
        if(actor in splitted[j]):
            toAppend=1 
    if(toAppend==1):
        listoflists.append(actorlist)

for i in range (0,len(listoflists)):
    result=set(result)|set(listoflists[i])
    
emptylist.append(actor)
result=set(result)-set(emptylist)
print (sorted(result))
        
            
file.close()
