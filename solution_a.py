file=open("dataset.txt","r")
document=file.read().split("\n")
films=[]
for i in range (0,len(document)):
    films.append(document[i].split(",")[0])
print(sorted(films))
file.close()
