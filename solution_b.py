
file=open("dataset.txt","r")
document=file.read().split("\n")
mydict={}
actors=[]        


for i in range (0,len(document)):
    splitted=document[i].split(",")
    mydict[splitted[0]]=splitted[1:]
    for j in range(0,3):
        if(mydict[splitted[0]][j] not in actors):
            actors.append(mydict[splitted[0]][j]) 

file.close()             
print (sorted(actors))


