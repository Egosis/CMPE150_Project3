movie1, movie2 = input().split(",")
union=[]
intersection=[]
difference=[]

file=open("dataset.txt","r")
document=file.read().split("\n")
actors=[]        
films=[]
mydict={}

for i in range (0,len(document)):
    splitted=document[i].split(",")
    mydict[splitted[0]]=splitted[1:]

union=set(list(mydict[movie1]))|set(list(mydict[movie2]))
intersection=set(list(mydict[movie1]))&set(list(mydict[movie2]))
difference=set(union)-set(intersection)

file.close()

print(sorted(union))
print(sorted(intersection))
print(sorted(difference))


