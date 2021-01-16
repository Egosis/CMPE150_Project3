actor=input()
mydict={}
actorlist=[]
result=[]
emptylist=[]
file=open("dataset.txt","r")
document=file.read().split("\n")

for i in range (0,len(document)):
    splitted=document[i].split(",")
    mydict[splitted[0]]=splitted[1:]
    if(actor in  mydict[splitted[0]]):
        actorlist.append(mydict[splitted[0]])
      
for i in range (0,len(actorlist)):
    result=set(result)|set(actorlist[i])


emptylist.append(actor)
result=set(result)-set(emptylist)

file.close()

print (sorted(result))
        
            
