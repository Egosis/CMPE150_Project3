file=open("dataset.txt","r")
document=file.read().split("\n")
films_dict={}
for i in range (0,len(document)):
    films_dict[document[i].split(",")[0]]=document[i].split(",")[1:]
file.close()    
print(films_dict.keys())
