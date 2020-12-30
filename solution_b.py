
file=open("dataset.txt","r")
document=file.read().split("\n")
actors=[]        


for i in range (0,len(document)):
    splitted=document[i].split(",")
    for j in range(1,4):
        if(splitted[j] not in actors):
            actors.append(splitted[j])              
print (sorted(actors))

file.close()

