movie1=input()
movie2=input()
movie1list=[]
movie2list=[]
union=[]
intersection=[]
difference=[]
file=open("dataset.txt","r")
document=file.read().split("\n")
actors=[]        
films=[]

for i in range (0,len(document)):
    splitted=document[i].split(",")
    films.append(splitted[0])
    for j in range(1,4):
        if(splitted[j] not in actors):
            actors.append(splitted[j])  
            
for j in range(1,4):
    movie1list.append(document[films.index(movie1)].split(",")[j])    
    movie2list.append(document[films.index(movie2)].split(",")[j])   
    
    
union=set(movie1list)|set(movie2list)
intersection=set(movie1list)&set(movie2list)
difference=set(union)-set(intersection)
print(sorted(union))
print(sorted(intersection))
print(sorted(difference))

file.close()
