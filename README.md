# CMPE150_Project3

In this project you will be given a simple dataset of films and actors/actresses. There are 20 films and 3 actors/actresses for each film. Do not forget that the document can change and more films could be added as rows to the dataset file.</br>

Exemple dataset:</br>

Becky,Vera Koonce,Van Reynolds,Carlos Hurley</br>
Captain Underpants: Mega Blissmas,Donald Schoolfield,Robert Black,Anthony Carver</br>
Invasion,Anthony Carver,Van Reynolds,Robert Black</br>

The tasks to do are given below:</br>
</br>
a-) Print the list of films</br>

| Input  | Output          |
| ------ | --------------- |
|  | ['Becky', 'Captain Underpants: Mega Blissmas', 'Invasion']|</br>

b-) Print the list of actors/actresses (No multiple occurences!)</br>


| Input  | Output          |
| ------ | --------------- |
|  | ['Anthony Carver', 'Carlos Hurley', 'Donald Schoolfield', 'Robert Black', 'Van Reynolds', 'Vera Koonce'] |</br>

c-) Take two films' name as a parameter, and give</br>
    - Find the all actors in those movies, which is union A | B</br>
    - Find the common actors in those movies, which is intersection A & B,</br>
    - Find the actors that played in either of the movies but not both, which is symmetric difference A - B</br>
    
    
| Input  |
| ------ | 
| Becky |
|Captain Underpants: Mega Blissmas | 

| Output          |
| --------------- |
|['Anthony Carver', 'Carlos Hurley', 'Robert Black', 'Van Reynolds', 'Vera Koonce']|
|['Van Reynolds']|
|['Anthony Carver', 'Carlos Hurley', 'Robert Black', 'Vera Koonce']|</br>

d-) Given an actors name, find out with whom he/she acted.</br>

| Input  | Output          |
| ------ | --------------- |
| Anthony Carver | ['Donald Schoolfield', 'Robert Black', 'Van Reynolds'] |
